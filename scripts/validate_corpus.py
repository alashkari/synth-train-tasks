#!/usr/bin/env python3
"""Validate the complete synthetic router corpus."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from _common import (
    CAPABILITY_FAMILIES,
    accepted_catalog,
    contains_forbidden_benchmark_reference,
    contains_routing_label_field,
    load_catalog,
    normalize_text,
    relative_task_path,
    sha256_text,
)
from validate_task import validate_task_file


def _percent(count: int, total: int) -> float:
    return 100.0 * count / total if total else 0.0


def _check_range(errors: list[str], label: str, count: int, total: int, low: float, high: float) -> None:
    value = _percent(count, total)
    if value < low or value > high:
        errors.append(f"{label} is {value:.2f}% ({count}/{total}), expected {low:.1f}%..{high:.1f}%")


def _load_split_manifest(root: Path) -> dict:
    path = root / "split_manifest.yaml"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def validate_corpus(root: Path, expected_accepted: int | None = None, relaxed: bool = False) -> list[str]:
    errors: list[str] = []
    catalog = load_catalog(root)
    accepted = [record for record in catalog if record.get("status") == "accepted"]
    accepted_count = len(accepted)

    if expected_accepted is not None and accepted_count != expected_accepted:
        errors.append(f"accepted task count {accepted_count} != expected {expected_accepted}")
    if not relaxed and accepted_count < 8000:
        errors.append(f"accepted task count {accepted_count} is below 8000")
    if not relaxed and len(catalog) < 10000:
        errors.append(f"candidate count {len(catalog)} is below 10000")

    ids = [record.get("id") for record in catalog]
    duplicate_ids = [task_id for task_id, count in Counter(ids).items() if count > 1]
    if duplicate_ids:
        errors.append(f"duplicate catalog ids: {duplicate_ids[:10]}")

    prompt_hashes: dict[str, str] = {}
    normalized_hashes: dict[str, str] = {}
    scenario_to_split: dict[str, str] = {}
    scenario_fingerprint_counts: Counter[str] = Counter()
    split_counts: Counter[str] = Counter()
    split_family_counts: dict[str, Counter[str]] = defaultdict(Counter)
    split_band_counts: dict[str, Counter[int]] = defaultdict(Counter)

    for record in accepted:
        if contains_routing_label_field(record):
            errors.append(f"{record.get('id')}: catalog contains a routing-label field")
        if contains_forbidden_benchmark_reference(json.dumps(record, sort_keys=True)):
            errors.append(f"{record.get('id')}: catalog contains forbidden benchmark reference")
        task_path = relative_task_path(root, record["id"])
        if not task_path.exists():
            errors.append(f"missing accepted task file: {task_path}")
            continue
        task_errors = validate_task_file(task_path, root)
        errors.extend(f"{record['id']}: {error}" for error in task_errors)

        text = task_path.read_text(encoding="utf-8")
        if contains_forbidden_benchmark_reference(text):
            errors.append(f"{record['id']}: task text contains forbidden benchmark reference")
        if "routing_label" in text or "final_routing" in text or "ground_truth_route" in text:
            errors.append(f"{record['id']}: task text contains explicit routing-label token")

        prompt = text.split("# Prompt", 1)[1].split("# Expected Behavior", 1)[0].strip()
        prompt_hash = sha256_text(prompt)
        normalized_hash = sha256_text(normalize_text(prompt))
        if prompt_hash in prompt_hashes:
            errors.append(f"exact prompt duplicate: {prompt_hashes[prompt_hash]} and {record['id']}")
        prompt_hashes[prompt_hash] = record["id"]
        if normalized_hash in normalized_hashes:
            errors.append(f"normalized prompt duplicate: {normalized_hashes[normalized_hash]} and {record['id']}")
        normalized_hashes[normalized_hash] = record["id"]

        scenario_id = record["base_scenario_id"]
        split = record.get("split")
        if scenario_id in scenario_to_split and scenario_to_split[scenario_id] != split:
            errors.append(f"base scenario {scenario_id} crosses splits")
        scenario_to_split[scenario_id] = split
        scenario_fingerprint_counts[record.get("base_scenario_fingerprint", "")] += 1
        split_counts[split] += 1
        split_family_counts[split][record["capability_family"]] += 1
        split_band_counts[split][record["intended_difficulty_band"]] += 1

        for rel_path in record.get("workspace_files", []):
            if not (root / rel_path).exists():
                errors.append(f"{record['id']}: missing catalog workspace asset {rel_path}")

    overfull_fingerprints = {
        fingerprint: count for fingerprint, count in scenario_fingerprint_counts.items() if count > 3
    }
    if overfull_fingerprints:
        errors.append(f"base-scenario fingerprint overflows: {list(overfull_fingerprints.items())[:10]}")

    manifest = _load_split_manifest(root)
    if manifest:
        manifest_ids = set()
        for split, payload in manifest.get("splits", {}).items():
            manifest_ids.update(payload.get("task_ids", []))
            if payload.get("task_count") != split_counts.get(split, 0):
                errors.append(f"split manifest count mismatch for {split}")
        accepted_ids = {record["id"] for record in accepted}
        if manifest_ids != accepted_ids:
            errors.append("split manifest task ids do not match accepted task ids")
    elif not relaxed:
        errors.append("missing split_manifest.yaml")

    if not relaxed and accepted_count:
        family_counts = Counter(record["capability_family"] for record in accepted)
        band_counts = Counter(record["intended_difficulty_band"] for record in accepted)
        grading_counts = Counter(record["grading_type"] for record in accepted)

        for family in CAPABILITY_FAMILIES:
            _check_range(errors, f"family {family}", family_counts[family], accepted_count, 7.0, 10.0)
        for band in [1, 2, 3, 4, 5]:
            _check_range(errors, f"difficulty band {band}", band_counts[band], accepted_count, 18.0, 22.0)
        _check_range(errors, "automated grading", grading_counts["automated"], accepted_count, 68.0, 72.0)
        _check_range(errors, "hybrid grading", grading_counts["hybrid"], accepted_count, 23.0, 27.0)
        _check_range(errors, "judge-only grading", grading_counts["llm_judge"], accepted_count, 0.0, 5.0)
        _check_range(errors, "multi-session tasks", sum(1 for r in accepted if r.get("multi_session")), accepted_count, 10.0, 15.0)
        _check_range(
            errors,
            "recoverable-failure tasks",
            sum(1 for r in accepted if r.get("contains_recoverable_failure")),
            accepted_count,
            10.0,
            20.0,
        )
        if _percent(sum(1 for r in accepted if r.get("requires_verification")), accepted_count) < 15.0:
            errors.append("requires_verification is below 15%")
        if _percent(sum(1 for r in accepted if r.get("has_distractor")), accepted_count) < 15.0:
            errors.append("has_distractor is below 15%")
        if _percent(sum(1 for r in accepted if r.get("non_english_or_mixed")), accepted_count) < 10.0:
            errors.append("non_english_or_mixed is below 10%")
        if _percent(sum(1 for r in accepted if len(r.get("workspace_files", [])) >= 2), accepted_count) < 25.0:
            errors.append("multiple-file/artifact tasks are below 25%")
        if _percent(sum(1 for r in accepted if r.get("dependency_depth", 0) >= 2), accepted_count) < 30.0:
            errors.append("multiple-operation tasks are below 30%")

        expected_splits = {
            "train": int(accepted_count * 0.8),
            "development": int(accepted_count * 0.1),
            "synthetic_holdout": accepted_count - int(accepted_count * 0.8) - int(accepted_count * 0.1),
        }
        for split, expected in expected_splits.items():
            if split_counts[split] != expected:
                errors.append(f"split {split} has {split_counts[split]} tasks, expected {expected}")
            split_total = split_counts[split]
            if split_total:
                for family in CAPABILITY_FAMILIES:
                    _check_range(
                        errors,
                        f"split {split} family {family}",
                        split_family_counts[split][family],
                        split_total,
                        7.0,
                        10.0,
                    )
                for band in [1, 2, 3, 4, 5]:
                    _check_range(
                        errors,
                        f"split {split} difficulty band {band}",
                        split_band_counts[split][band],
                        split_total,
                        18.0,
                        22.0,
                    )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--expected-accepted", type=int, default=None)
    parser.add_argument("--relaxed", action="store_true")
    args = parser.parse_args()
    errors = validate_corpus(args.root, args.expected_accepted, args.relaxed)
    if errors:
        for error in errors[:200]:
            print(error)
        if len(errors) > 200:
            print(f"... {len(errors) - 200} additional errors")
        return 1
    print("OK corpus validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
