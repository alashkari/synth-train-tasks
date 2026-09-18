#!/usr/bin/env python3
"""Duplicate checks for the accepted synthetic corpus."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from _common import (
    accepted_catalog,
    extract_python_code,
    normalize_text,
    read_task,
    relative_task_path,
    sha256_text,
    token_ngrams,
)


def _jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


def _task_specific_prompt(prompt: str) -> str:
    without_blocks = []
    in_block = False
    for line in prompt.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_block = not in_block
            continue
        if in_block:
            continue
        lowered = stripped.lower()
        if not stripped:
            continue
        if lowered.startswith("you are working on synthetic task"):
            continue
        if lowered.startswith("use only"):
            continue
        if lowered.startswith("do not fetch"):
            continue
        if lowered.startswith("create `submission/result.json`"):
            continue
        if lowered.startswith("use relative evidence paths"):
            continue
        if lowered.startswith("the submitted python file"):
            continue
        if lowered.startswith("keep the implementation deterministic"):
            continue
        without_blocks.append(stripped)
    return "\n".join(without_blocks)


def _fixture_schema(root: Path, record: dict) -> str:
    pieces = []
    for rel in record.get("workspace_files", []):
        path = root / rel
        suffix = path.suffix.lower()
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            text = ""
        descriptor = suffix
        if suffix == ".csv":
            descriptor += ":" + (text.splitlines()[0] if text.splitlines() else "")
        elif suffix == ".json":
            try:
                data = json.loads(text)
                if isinstance(data, dict):
                    descriptor += ":" + ",".join(sorted(data.keys())[:12])
                elif isinstance(data, list) and data and isinstance(data[0], dict):
                    descriptor += ":list:" + ",".join(sorted(data[0].keys())[:12])
                else:
                    descriptor += ":" + type(data).__name__
            except Exception:
                descriptor += ":malformed"
        elif suffix in {".md", ".txt"}:
            heads = [line[:40] for line in text.splitlines() if line.startswith("#") or ":" in line]
            descriptor += ":" + "|".join(heads[:6])
        pieces.append(descriptor)
    return sha256_text("||".join(pieces))


def deduplicate(root: Path, max_pairs: int = 100) -> dict:
    records = accepted_catalog(root)
    prompts: dict[str, str] = {}
    normalized_prompts: dict[str, str] = {}
    prompt_ngrams: dict[str, set[tuple[str, ...]]] = {}
    grader_ngrams: dict[str, set[tuple[str, ...]]] = {}
    fixture_schemas: Counter[str] = Counter()
    base_fingerprints: Counter[str] = Counter()

    for record in records:
        task_id = record["id"]
        _metadata, sections, _body, _text = read_task(relative_task_path(root, task_id))
        prompt = sections.get("Prompt", "")
        prompts[task_id] = prompt
        normalized_prompts[task_id] = normalize_text(prompt)
        prompt_ngrams[task_id] = token_ngrams(_task_specific_prompt(prompt), 5)
        if record.get("grading_type") in {"automated", "hybrid"}:
            code = extract_python_code(sections.get("Automated Checks", ""))
            grader_ngrams[task_id] = token_ngrams(code, 7)
        fixture_schemas[_fixture_schema(root, record)] += 1
        base_fingerprints[record.get("base_scenario_fingerprint", "")] += 1

    exact_seen: dict[str, str] = {}
    normalized_seen: dict[str, str] = {}
    exact_duplicates = []
    normalized_duplicates = []
    for task_id, prompt in prompts.items():
        prompt_hash = sha256_text(prompt)
        normalized_hash = sha256_text(normalized_prompts[task_id])
        if prompt_hash in exact_seen:
            exact_duplicates.append([exact_seen[prompt_hash], task_id])
        exact_seen[prompt_hash] = task_id
        if normalized_hash in normalized_seen:
            normalized_duplicates.append([normalized_seen[normalized_hash], task_id])
        normalized_seen[normalized_hash] = task_id

    inverted: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for task_id, ngrams in prompt_ngrams.items():
        for ngram in ngrams:
            inverted[ngram].append(task_id)

    pair_counts: Counter[tuple[str, str]] = Counter()
    for task_ids in inverted.values():
        if len(task_ids) > 20:
            continue
        ordered = sorted(task_ids)
        for index, left in enumerate(ordered):
            for right in ordered[index + 1 :]:
                pair_counts[(left, right)] += 1

    high_ngram_pairs = []
    for (left, right), _count in pair_counts.most_common():
        score = _jaccard(prompt_ngrams[left], prompt_ngrams[right])
        if score > 0.35:
            high_ngram_pairs.append({"left": left, "right": right, "jaccard": round(score, 4)})
            if len(high_ngram_pairs) >= max_pairs:
                break

    grader_pairs = []
    grader_items = list(grader_ngrams.items())
    grader_inverted: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for task_id, ngrams in grader_items:
        for ngram in ngrams:
            grader_inverted[ngram].append(task_id)
    grader_pair_counts: Counter[tuple[str, str]] = Counter()
    for task_ids in grader_inverted.values():
        if len(task_ids) > 25:
            continue
        ordered = sorted(task_ids)
        for index, left in enumerate(ordered):
            for right in ordered[index + 1 :]:
                grader_pair_counts[(left, right)] += 1
    for (left, right), _count in grader_pair_counts.most_common():
        score = _jaccard(grader_ngrams[left], grader_ngrams[right])
        if score > 0.85:
            grader_pairs.append({"left": left, "right": right, "similarity": round(score, 4)})
            if len(grader_pairs) >= max_pairs:
                break

    report = {
        "accepted_tasks": len(records),
        "exact_prompt_duplicates": exact_duplicates,
        "normalized_prompt_duplicates": normalized_duplicates,
        "high_token_5gram_overlap_pairs": high_ngram_pairs,
        "grader_similarity_pairs_for_inspection": grader_pairs,
        "base_scenario_fingerprint_overflows": {
            key: count for key, count in base_fingerprints.items() if count > 3
        },
        "fixture_schema_groups_over_3": sum(1 for count in fixture_schemas.values() if count > 3),
        "max_fixture_schema_reuse": max(fixture_schemas.values(), default=0),
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--max-pairs", type=int, default=100)
    args = parser.parse_args()
    report = deduplicate(args.root, args.max_pairs)
    output_path = args.root / "dedup_report.json"
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    hard_fail = (
        report["exact_prompt_duplicates"]
        or report["normalized_prompt_duplicates"]
        or report["high_token_5gram_overlap_pairs"]
        or report["base_scenario_fingerprint_overflows"]
    )
    return 1 if hard_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
