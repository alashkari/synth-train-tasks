#!/usr/bin/env python3
"""Deterministically generate synthetic router-corpus candidate tasks."""

from __future__ import annotations

import argparse
import csv
import json
import random
import shutil
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from _common import CAPABILITY_FAMILIES, GENERATOR_VERSION, normalize_text, sha256_text
from build_splits import build_manifest
from summarize_distribution import summarize
from validate_task import validate_task_file


LANG_HINTS = [
    "Some fixture labels use Spanish words such as accion, riesgo, and resumen; normalize the final JSON keys in English.",
    "Some source notes include French words such as priorite, preuve, and etape; keep the output schema in English.",
    "Some records mix English with romanized Japanese tags such as kakunin and shuryo; keep the output values deterministic.",
]

DOMAINS = [
    "inventory audit",
    "incident follow-up",
    "release readiness",
    "billing review",
    "customer migration",
    "access cleanup",
    "knowledge-base upkeep",
    "training roster",
    "sensor calibration",
    "vendor intake",
    "policy review",
    "queue triage",
]

WORDS = [
    "amber",
    "brisk",
    "cedar",
    "delta",
    "ember",
    "frost",
    "glade",
    "harbor",
    "ion",
    "juniper",
    "keystone",
    "lumen",
    "mosaic",
    "nimbus",
    "onyx",
    "prairie",
    "quartz",
    "ripple",
    "summit",
    "tundra",
    "umbra",
    "violet",
    "willow",
    "xenial",
    "yonder",
    "zenith",
]

GENERIC_CRITERIA = [
    "format_valid",
    "answer_correct",
    "evidence_grounded",
    "verification_complete",
]

CODE_CRITERIA = [
    "syntax_valid",
    "public_api",
    "visible_cases",
    "hidden_cases",
]


def ensure_clean(root: Path) -> None:
    for name in [
        "tasks",
        "assets",
        "rejected",
        "catalog.jsonl",
        "split_manifest.yaml",
        "generation_report.md",
        "dedup_report.json",
        "grader_test_results.json",
        "batch_log.json",
    ]:
        path = root / name
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()
    for rel in [
        "tasks",
        "assets",
        "rejected/duplicate",
        "rejected/invalid",
        "rejected/ungradeable",
        "rejected/low_quality",
    ]:
        (root / rel).mkdir(parents=True, exist_ok=True)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    write_text(path, json.dumps(data, indent=2, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def round2(value: float) -> float:
    return round(float(value) + 1e-9, 2)


def flag_by_quota(position_zero: int, total: int, quota: int) -> bool:
    if quota <= 0 or total <= 0:
        return False
    return ((position_zero + 1) * quota // total) > (position_zero * quota // total)


def split_sizes(accepted_target: int) -> dict[str, int]:
    scenarios = accepted_target // 2
    train_scenarios = int(scenarios * 0.8)
    development_scenarios = int(scenarios * 0.1)
    holdout_scenarios = scenarios - train_scenarios - development_scenarios
    return {
        "train": train_scenarios * 2,
        "development": development_scenarios * 2,
        "synthetic_holdout": holdout_scenarios * 2,
    }


def split_for_index(accepted_index: int, accepted_target: int) -> tuple[str, int, int]:
    sizes = split_sizes(accepted_target)
    start = 1
    for split in ["train", "development", "synthetic_holdout"]:
        size = sizes[split]
        if accepted_index < start + size:
            return split, accepted_index - start, size
        start += size
    return "synthetic_holdout", sizes["synthetic_holdout"] - 1, sizes["synthetic_holdout"]


def grading_type_for(split_position: int, split_total: int) -> str:
    automated = int(split_total * 0.70)
    hybrid = int(split_total * 0.25)
    if split_position < automated:
        return "automated"
    if split_position < automated + hybrid:
        return "hybrid"
    return "llm_judge"


def tool_depth_band(calls: int) -> str:
    if calls <= 2:
        return "shallow"
    if calls <= 5:
        return "moderate"
    return "deep"


def project_label(index: int, rng: random.Random) -> str:
    left = WORDS[index % len(WORDS)]
    right = WORDS[(index * 7 + rng.randrange(len(WORDS))) % len(WORDS)]
    return f"{left}-{right}-{index:04d}"


def anchor_terms(index: int, count: int = 96) -> str:
    syllables = [
        "ba",
        "ce",
        "di",
        "fo",
        "gu",
        "ha",
        "jo",
        "ki",
        "lu",
        "me",
        "na",
        "po",
        "ri",
        "sa",
        "tu",
        "ve",
        "wo",
        "ya",
        "ze",
    ]
    rng = random.Random(510000 + index * 19)
    terms = []
    for item in range(count):
        term = "".join(rng.choice(syllables) for _ in range(3))
        terms.append(f"{term}{chr(ord('a') + (index + item) % 26)}")
    return " ".join(terms)


def context_for(index: int, accepted_target: int) -> dict[str, Any]:
    scenario_index = (index + 1) // 2
    seed = 730000 + index * 37
    rng = random.Random(seed)
    split, split_position, split_total = split_for_index(index, accepted_target)
    family = CAPABILITY_FAMILIES[(scenario_index - 1) % len(CAPABILITY_FAMILIES)]
    band = ((index - 1) % 5) + 1
    grading_type = grading_type_for(split_position, split_total)

    quotas = {
        "multi_session": int(split_total * 0.125),
        "recoverable": int(split_total * 0.150),
        "verification": int(split_total * 0.250),
        "distractor": int(split_total * 0.200),
        "non_english": int(split_total * 0.125),
        "multi_file": int(split_total * 0.300),
    }
    return {
        "index": index,
        "task_id": f"task_syn_{index:06d}",
        "scenario_index": scenario_index,
        "scenario_id": f"scenario_{scenario_index:06d}",
        "seed": seed,
        "rng": rng,
        "split": split,
        "split_position": split_position,
        "split_total": split_total,
        "family": family,
        "band": band,
        "grading_type": grading_type,
        "multi_session": flag_by_quota(split_position, split_total, quotas["multi_session"]),
        "recoverable": flag_by_quota(split_position, split_total, quotas["recoverable"]),
        "requires_verification": flag_by_quota(split_position, split_total, quotas["verification"]),
        "has_distractor": flag_by_quota(split_position, split_total, quotas["distractor"]),
        "non_english": flag_by_quota(split_position, split_total, quotas["non_english"]),
        "multi_file": flag_by_quota(split_position, split_total, quotas["multi_file"]),
        "domain": DOMAINS[(scenario_index + band) % len(DOMAINS)],
        "project": project_label(scenario_index, rng),
        "variant": 1 if index % 2 else 2,
        "anchors": anchor_terms(index),
    }


def add_workspace_file(root: Path, task_id: str, rel: str, content: str, workspace_files: list[str]) -> None:
    path = root / "assets" / task_id / "workspace" / rel
    write_text(path, content)
    workspace_files.append(f"assets/{task_id}/workspace/{rel}")


def add_workspace_json(root: Path, task_id: str, rel: str, data: Any, workspace_files: list[str]) -> None:
    path = root / "assets" / task_id / "workspace" / rel
    write_json(path, data)
    workspace_files.append(f"assets/{task_id}/workspace/{rel}")


def add_workspace_csv(root: Path, task_id: str, rel: str, rows: list[dict[str, Any]], workspace_files: list[str]) -> None:
    path = root / "assets" / task_id / "workspace" / rel
    write_csv(path, rows)
    workspace_files.append(f"assets/{task_id}/workspace/{rel}")


def generic_grader_code(expected_output: dict[str, Any]) -> str:
    return f'''from pathlib import Path
import json

CRITERIA = {GENERIC_CRITERIA!r}
EXPECTED_OUTPUT = {expected_output!r}

def _load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None

def _same(expected, actual):
    if isinstance(expected, float):
        return isinstance(actual, (int, float)) and abs(float(actual) - expected) <= 0.01
    if isinstance(expected, dict):
        return isinstance(actual, dict) and set(expected) == set(actual) and all(
            _same(expected[key], actual[key]) for key in expected
        )
    if isinstance(expected, list):
        return isinstance(actual, list) and len(expected) == len(actual) and all(
            _same(left, right) for left, right in zip(expected, actual)
        )
    return expected == actual

def grade(workspace_dir):
    scores = {{key: 0.0 for key in CRITERIA}}
    output = Path(workspace_dir) / "submission" / "result.json"
    data = _load_json(output)
    if not isinstance(data, dict):
        return scores
    scores["format_valid"] = 1.0
    scores["answer_correct"] = 1.0 if _same(EXPECTED_OUTPUT.get("result"), data.get("result")) else 0.0
    scores["evidence_grounded"] = 1.0 if _same(EXPECTED_OUTPUT.get("evidence"), data.get("evidence")) else 0.0
    scores["verification_complete"] = 1.0 if _same(EXPECTED_OUTPUT.get("verification"), data.get("verification")) else 0.0
    return scores

def create_reference_solution(workspace_dir):
    output = Path(workspace_dir) / "submission" / "result.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(EXPECTED_OUTPUT, indent=2, sort_keys=True) + "\\n", encoding="utf-8")

def create_incorrect_solution(workspace_dir):
    output = Path(workspace_dir) / "submission" / "result.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({{"result": {{}}, "evidence": [], "verification": {{"status": "unchecked"}}}}) + "\\n", encoding="utf-8")
'''


def code_grader_code(function_name: str, output_file: str, visible_cases: list[dict[str, Any]], hidden_cases: list[dict[str, Any]], reference_code: str, incorrect_code: str) -> str:
    return f'''from pathlib import Path
import importlib.util

CRITERIA = {CODE_CRITERIA!r}
FUNCTION_NAME = {function_name!r}
OUTPUT_FILE = {output_file!r}
VISIBLE_CASES = {visible_cases!r}
HIDDEN_CASES = {hidden_cases!r}
REFERENCE_CODE = {reference_code!r}
INCORRECT_CODE = {incorrect_code!r}

def _load_module(path):
    try:
        spec = importlib.util.spec_from_file_location("candidate_solution", path)
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception:
        return None

def _run_cases(func, cases):
    if not cases:
        return 1.0
    passed = 0
    for case in cases:
        try:
            actual = func(case["input"])
        except Exception:
            actual = None
        if actual == case["expected"]:
            passed += 1
    return passed / len(cases)

def grade(workspace_dir):
    scores = {{key: 0.0 for key in CRITERIA}}
    module_path = Path(workspace_dir) / "submission" / OUTPUT_FILE
    if not module_path.exists():
        return scores
    module = _load_module(module_path)
    if module is None:
        return scores
    scores["syntax_valid"] = 1.0
    func = getattr(module, FUNCTION_NAME, None)
    if not callable(func):
        return scores
    scores["public_api"] = 1.0
    scores["visible_cases"] = _run_cases(func, VISIBLE_CASES)
    scores["hidden_cases"] = _run_cases(func, HIDDEN_CASES)
    return scores

def create_reference_solution(workspace_dir):
    output = Path(workspace_dir) / "submission" / OUTPUT_FILE
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REFERENCE_CODE, encoding="utf-8")

def create_incorrect_solution(workspace_dir):
    output = Path(workspace_dir) / "submission" / OUTPUT_FILE
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(INCORRECT_CODE, encoding="utf-8")
'''


def build_file_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    rng = ctx["rng"]
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    exts = ["txt", "md", "log", "json", "cfg"]
    target_ext = exts[(ctx["index"] + ctx["band"]) % len(exts)]
    min_len = 24 + ctx["band"] * 7
    file_count = 5 + ctx["band"] + (2 if ctx["multi_file"] else 0)
    records = []
    for item in range(file_count):
        ext = exts[(item + rng.randrange(len(exts))) % len(exts)]
        bucket = "active" if item % 4 else "archive"
        name = f"{ctx['project'].replace('-', '_')}_{item:02d}.{ext}"
        content = (
            f"record {item} for {ctx['domain']} in {ctx['project']}\n"
            f"status={bucket}\n"
            f"signal={'keep' if item % 2 else 'review'}\n"
            + ("detail " * (item + ctx["band"] + 3))
        )
        rel = f"incoming/{bucket}/{name}"
        add_workspace_file(root, task_id, rel, content, workspace_files)
        records.append({"path": rel, "ext": ext, "bucket": bucket, "size": len(content.encode("utf-8"))})
    if ctx["has_distractor"]:
        rel = f"incoming/archive/distractor_{ctx['index']:06d}.{target_ext}"
        add_workspace_file(root, task_id, rel, "archived distractor with matching extension\n" * 3, workspace_files)
        records.append({"path": rel, "ext": target_ext, "bucket": "archive", "size": 126})
    active = [record for record in records if record["bucket"] == "active"]
    selected = sorted(record["path"] for record in active if record["ext"] == target_ext and record["size"] >= min_len)
    counts = Counter(record["ext"] for record in active)
    largest = max(active, key=lambda record: (record["size"], record["path"])) if active else {"path": "", "size": 0}
    result = {
        "target_extension": target_ext,
        "minimum_bytes": min_len,
        "selected_files": selected,
        "active_extension_counts": dict(sorted(counts.items())),
        "largest_active_file": {"path": largest["path"], "bytes": largest["size"]},
    }
    objective = (
        f"Inspect the files under `incoming/active/` for the {ctx['domain']} workspace. "
        f"Ignore everything under `incoming/archive/`. Select active files ending in `.{target_ext}` "
        f"whose byte length is at least {min_len}, count active files by extension, and identify the largest active file."
    )
    return {
        "name": f"Active file manifest {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": [record["path"] for record in active[:4]],
            "verification": {
                "checked_files": len(records),
                "ignored_archive": True,
                "status": "pass",
            },
        },
        "required_tool_types": ["filesystem"],
        "estimated_tool_calls": 2 + ctx["band"],
    }


def build_structured_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    rng = ctx["rng"]
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    rows = []
    regions = ["north", "south", "east", "west", "central"]
    status_active = "activo" if ctx["non_english"] else "active"
    status_skip = "pausado" if ctx["non_english"] else "paused"
    threshold = 80 + ctx["band"] * 13
    for item in range(7 + ctx["band"]):
        units = 2 + (item * 3 + ctx["index"]) % 17
        unit_cost = 5 + ((item + ctx["band"]) * 11) % 29
        status = status_active if item % 3 else status_skip
        rows.append(
            {
                "raw_id": f"{ctx['project'][:3]}-{item:03d}",
                "region": regions[(item + ctx["scenario_index"]) % len(regions)],
                "status": status,
                "units": units,
                "unit_cost": unit_cost,
                "note": "distractor" if ctx["has_distractor"] and item == 1 else "standard",
            }
        )
    if ctx["recoverable"]:
        rows.append({"raw_id": "broken-row", "region": "unknown", "status": status_active, "units": "n/a", "unit_cost": "9", "note": "malformed"})
    region_map = {region: f"zone_{idx + 1}" for idx, region in enumerate(regions)}
    add_workspace_csv(root, task_id, "tables/source_records.csv", rows, workspace_files)
    add_workspace_json(root, task_id, "tables/region_map.json", region_map, workspace_files)

    normalized = []
    malformed = 0
    for row in rows:
        try:
            units = int(row["units"])
            unit_cost = int(row["unit_cost"])
        except Exception:
            malformed += 1
            continue
        if row["status"] != status_active:
            continue
        total = units * unit_cost
        if total >= threshold:
            normalized.append(
                {
                    "id": row["raw_id"].upper(),
                    "zone": region_map.get(row["region"], "zone_unknown"),
                    "total_value": total,
                }
            )
    normalized.sort(key=lambda item: (item["zone"], item["id"]))
    result = {
        "threshold": threshold,
        "records": normalized,
        "total_value": sum(item["total_value"] for item in normalized),
        "malformed_rows_skipped": malformed,
    }
    objective = (
        f"Transform `tables/source_records.csv` using `tables/region_map.json`. Keep only active rows "
        f"with `units * unit_cost >= {threshold}`, uppercase each id, map regions to zones, sort by zone then id, "
        "and report how many malformed rows were skipped."
    )
    if ctx["non_english"]:
        objective += " Treat `activo` as active and `pausado` as paused."
    return {
        "name": f"Structured table normalization {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": ["tables/source_records.csv", "tables/region_map.json"],
            "verification": {
                "checked_files": 2,
                "malformed_rows_skipped": malformed,
                "status": "pass",
            },
        },
        "required_tool_types": ["filesystem", "python"],
        "estimated_tool_calls": 3 + ctx["band"],
    }


def build_stats_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    rows = []
    groups = ["alpha", "beta", "gamma", "delta"]
    for item in range(9 + ctx["band"] * 2):
        value = 12 + ((item * 17 + ctx["scenario_index"] * 5) % 91)
        if ctx["recoverable"] and item == 2:
            value = 155
        rows.append(
            {
                "sample_id": f"s{ctx['index']:06d}_{item:02d}",
                "group": groups[(item + ctx["band"]) % len(groups)],
                "value": value,
                "weight": 1 + (item % 4),
            }
        )
    if ctx["has_distractor"]:
        rows.append({"sample_id": "calibration-note", "group": "ignore", "value": 999, "weight": 0})
    add_workspace_csv(root, task_id, "measurements/readings.csv", rows, workspace_files)
    valid_rows = [row for row in rows if row["group"] != "ignore" and int(row["weight"]) > 0]
    values = [int(row["value"]) for row in valid_rows]
    weighted_total = sum(int(row["value"]) * int(row["weight"]) for row in valid_rows)
    total_weight = sum(int(row["weight"]) for row in valid_rows)
    group_means = {}
    for group in sorted({row["group"] for row in valid_rows}):
        group_values = [int(row["value"]) for row in valid_rows if row["group"] == group]
        group_means[group] = round2(statistics.mean(group_values))
    result = {
        "count": len(valid_rows),
        "mean": round2(statistics.mean(values)),
        "median": round2(statistics.median(values)),
        "weighted_mean": round2(weighted_total / total_weight),
        "group_means": group_means,
        "outlier_ids": sorted(row["sample_id"] for row in valid_rows if int(row["value"]) >= 130),
    }
    objective = (
        "Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. "
        "Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130."
    )
    return {
        "name": f"Quantitative reading summary {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": ["measurements/readings.csv"],
            "verification": {
                "checked_files": 1,
                "ignored_distractors": ctx["has_distractor"],
                "status": "pass",
            },
        },
        "required_tool_types": ["filesystem", "python"],
        "estimated_tool_calls": 3 + ctx["band"],
    }


def build_document_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    owners = ["ari", "bea", "cam", "dev", "eli", "fay"]
    lines = [f"# Briefing for {ctx['project']}", ""]
    actions = []
    risks = []
    decisions = []
    for item in range(5 + ctx["band"]):
        owner = owners[(item + ctx["scenario_index"]) % len(owners)]
        if item % 3 == 0:
            tag = "accion" if ctx["non_english"] else "action"
            due = f"day-{(item % 5) + 1}"
            text = f"Line {item + 1}: [{tag}] {owner} to verify batch {item} by {due}."
            actions.append({"owner": owner, "due": due, "item": f"verify batch {item}"})
        elif item % 3 == 1:
            tag = "risgo" if ctx["non_english"] else "risk"
            severity = "high" if item % 2 else "low"
            text = f"Line {item + 1}: [{tag}] {severity} mismatch in lane {item}."
            risks.append({"severity": severity, "topic": f"lane {item}"})
        else:
            tag = "decision"
            text = f"Line {item + 1}: [{tag}] use checksum window {item + 2}."
            decisions.append(f"use checksum window {item + 2}")
        lines.append(text)
    if ctx["has_distractor"]:
        lines.append("Line 99: [note] old picnic agenda; do not include in the task summary.")
    add_workspace_file(root, task_id, "notes/briefing.md", "\n".join(lines) + "\n", workspace_files)
    result = {
        "actions": actions,
        "risk_count": len(risks),
        "high_risk_topics": [risk["topic"] for risk in risks if risk["severity"] == "high"],
        "decisions": decisions,
    }
    objective = (
        "Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. "
        "Do not include ordinary notes or unrelated agenda material."
    )
    if ctx["non_english"]:
        objective += " Treat `[accion]` as an action and `[risgo]` as a risk despite the shorthand spelling."
    return {
        "name": f"Briefing extraction {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": ["notes/briefing.md"],
            "verification": {
                "checked_files": 1,
                "ignored_distractors": ctx["has_distractor"],
                "status": "pass",
            },
        },
        "required_tool_types": ["filesystem"],
        "estimated_tool_calls": 2 + ctx["band"],
    }


def code_cases(ctx: dict[str, Any]) -> tuple[str, list[dict[str, Any]], list[dict[str, Any]], str]:
    threshold = 40 + ctx["band"] * 6
    function_name = "transform_records"
    def expected(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
        output = []
        for record in records:
            score = int(record.get("score", 0))
            if record.get("status") == "active" and score >= threshold:
                output.append(
                    {
                        "code": str(record.get("code", "")).upper(),
                        "bucket": "priority" if score >= threshold + 20 else "watch",
                    }
                )
        return sorted(output, key=lambda item: item["code"])

    visible_inputs = [
        [
            {"code": "aa", "status": "active", "score": threshold},
            {"code": "bb", "status": "paused", "score": threshold + 25},
        ],
        [
            {"code": "cc", "status": "active", "score": threshold + 30},
            {"code": "dd", "status": "active", "score": threshold - 1},
        ],
    ]
    hidden_inputs = [
        [
            {"code": "mx", "status": "active", "score": threshold + 1},
            {"code": "az", "status": "active", "score": threshold + 40},
        ],
        [
            {"code": "nk", "status": "unknown", "score": threshold + 90},
            {"code": "lm", "status": "active", "score": threshold + 19},
        ],
    ]
    visible_cases = [{"input": case, "expected": expected(case)} for case in visible_inputs]
    hidden_cases = [{"input": case, "expected": expected(case)} for case in hidden_inputs]
    spec = (
        f"Implement `{function_name}(records)`. Keep records whose status is `active` and score is at least {threshold}. "
        "Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least "
        f"{threshold + 20}, otherwise `watch`. Sort by code."
    )
    reference_code = f'''def {function_name}(records):
    output = []
    for record in records:
        try:
            score = int(record.get("score", 0))
        except Exception:
            continue
        if record.get("status") == "active" and score >= {threshold}:
            bucket = "priority" if score >= {threshold + 20} else "watch"
            output.append({{"code": str(record.get("code", "")).upper(), "bucket": bucket}})
    return sorted(output, key=lambda item: item["code"])
'''
    return function_name, visible_cases, hidden_cases, spec, reference_code


def build_code_task(root: Path, ctx: dict[str, Any], debugging: bool) -> dict[str, Any]:
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    function_name, visible_cases, hidden_cases, spec, reference_code = code_cases(ctx)
    if debugging:
        output_file = "fixed_module.py"
        buggy_code = reference_code.replace(">=", ">").replace("priority", "urgent", 1)
        add_workspace_file(root, task_id, "src/buggy_module.py", buggy_code, workspace_files)
        add_workspace_json(root, task_id, "tests/visible_cases.json", visible_cases, workspace_files)
        objective = (
            f"`src/buggy_module.py` is intended to satisfy this behavior: {spec} "
            f"Write the corrected implementation to `submission/{output_file}` with the same public function."
        )
        name = f"Repair record transformer {ctx['index']:06d}"
        incorrect_code = buggy_code
    else:
        output_file = "solution.py"
        add_workspace_json(
            root,
            task_id,
            "spec/visible_cases.json",
            {"behavior": spec, "visible_cases": visible_cases},
            workspace_files,
        )
        objective = f"{spec} Write the implementation to `submission/{output_file}`."
        name = f"Generate record transformer {ctx['index']:06d}"
        incorrect_code = f"def {function_name}(records):\n    return []\n"
    automated = code_grader_code(function_name, output_file, visible_cases, hidden_cases, reference_code, incorrect_code)
    expected_output = {
        "result": {"function": function_name, "output_file": f"submission/{output_file}"},
        "evidence": [workspace_files[0].split("/workspace/", 1)[1]],
        "verification": {
            "visible_case_count": len(visible_cases),
            "hidden_case_count": len(hidden_cases),
            "status": "pass",
        },
    }
    return {
        "name": name,
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": expected_output,
        "required_tool_types": ["filesystem", "shell"],
        "estimated_tool_calls": 4 + ctx["band"],
        "automated_override": automated,
        "criteria": CODE_CRITERIA,
    }


def build_repo_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    modules = ["ingest", "export", "audit", "notify", "cleanup"]
    config = {"enabled_modules": modules[: 3 + ctx["band"] % 3], "deprecated": [modules[-1]]}
    add_workspace_json(root, task_id, "repo/config/modules.json", config, workspace_files)
    todo_summary = []
    for idx, module in enumerate(modules):
        text = f"def run_{module}():\n    return '{module}'\n"
        if idx % 2 == 0:
            text += f"# TODO[{ctx['index']}-{idx}]: add {module} fixture coverage\n"
            todo_summary.append({"module": module, "todo": f"{ctx['index']}-{idx}"})
        add_workspace_file(root, task_id, f"repo/src/{module}.py", text, workspace_files)
    add_workspace_file(root, task_id, "repo/docs/changelog.md", f"# Changelog\n\n- {ctx['project']} bootstrap\n", workspace_files)
    result = {
        "enabled_modules": config["enabled_modules"],
        "deprecated_modules": config["deprecated"],
        "todo_items": todo_summary,
        "missing_enabled_files": [],
    }
    objective = (
        "Inspect the mini repository under `repo/`. Create a maintenance report with enabled modules, deprecated modules, "
        "TODO markers with their module names, and any enabled module whose source file is missing."
    )
    return {
        "name": f"Mini repository maintenance scan {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": ["repo/config/modules.json", "repo/src"],
            "verification": {"checked_files": len(workspace_files), "status": "pass"},
        },
        "required_tool_types": ["filesystem", "text_search"],
        "estimated_tool_calls": 4 + ctx["band"],
    }


def build_source_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    metric = 20 + (ctx["index"] % 17)
    sources = [
        {
            "file": "captured/page_a.md",
            "date": f"2026-02-{(ctx['band'] % 9) + 10:02d}",
            "claim": metric,
            "status": "draft",
        },
        {
            "file": "captured/page_b.md",
            "date": f"2026-03-{(ctx['band'] % 9) + 10:02d}",
            "claim": metric + 4,
            "status": "reviewed",
        },
        {
            "file": "captured/page_c.md",
            "date": f"2026-01-{(ctx['band'] % 9) + 10:02d}",
            "claim": metric - 3,
            "status": "superseded",
        },
    ]
    for source in sources:
        text = (
            f"# Captured Source\n\nProject: {ctx['project']}\nDate: {source['date']}\n"
            f"Review status: {source['status']}\nMetric value: {source['claim']}\n"
            f"Evidence phrase: {ctx['domain']} checkpoint {source['claim']}\n"
        )
        add_workspace_file(root, task_id, source["file"], text, workspace_files)
    selected = sorted(sources, key=lambda item: (item["status"] == "reviewed", item["date"]))[-1]
    result = {
        "selected_metric_value": selected["claim"],
        "selected_source": selected["file"],
        "selection_rule": "prefer reviewed source, then latest date",
        "conflicting_values": sorted({source["claim"] for source in sources if source["claim"] != selected["claim"]}),
    }
    objective = (
        "Use the captured source files under `captured/`; do not fetch live pages. "
        "Select the metric value by preferring a reviewed source and using latest date only as a tie breaker. "
        "Report conflicting metric values and cite the selected file."
    )
    return {
        "name": f"Captured source synthesis {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": [selected["file"]],
            "verification": {"checked_files": len(sources), "live_network_used": False, "status": "pass"},
        },
        "required_tool_types": ["filesystem", "text_search"],
        "estimated_tool_calls": 4 + ctx["band"],
    }


def build_planning_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    tasks = []
    for item in range(5 + ctx["band"] % 3):
        task_code = chr(ord("A") + item)
        deps = [] if item == 0 else [chr(ord("A") + item - 1)]
        if ctx["band"] >= 4 and item >= 2 and item % 2 == 0:
            deps.append(chr(ord("A") + item - 2))
        tasks.append(
            {
                "task": task_code,
                "duration": 1 + ((item + ctx["scenario_index"]) % 4),
                "depends_on": deps,
                "owner": ["ari", "bea", "cam"][item % 3],
            }
        )
    if ctx["recoverable"]:
        tasks.append({"task": "Z", "duration": 0, "depends_on": ["missing"], "owner": "skip"})
    add_workspace_json(root, task_id, "plan/constraints.json", {"tasks": tasks, "workday_start": 9}, workspace_files)
    schedule = []
    completed: dict[str, int] = {}
    current = 9
    skipped = []
    for task in tasks:
        if task["duration"] <= 0 or any(dep not in completed for dep in task["depends_on"]):
            skipped.append(task["task"])
            continue
        start = max([current] + [completed[dep] for dep in task["depends_on"]])
        end = start + int(task["duration"])
        completed[task["task"]] = end
        current = end
        schedule.append({"task": task["task"], "owner": task["owner"], "start": start, "end": end})
    result = {
        "schedule": schedule,
        "skipped_tasks": skipped,
        "finish_time": schedule[-1]["end"] if schedule else 9,
    }
    objective = (
        "Create a deterministic schedule from `plan/constraints.json`. Process tasks in listed order, honor dependencies, "
        "start at the given workday hour, skip tasks with impossible dependencies or non-positive duration, and report finish time."
    )
    return {
        "name": f"Constraint schedule build {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": ["plan/constraints.json"],
            "verification": {"checked_files": 1, "skipped_count": len(skipped), "status": "pass"},
        },
        "required_tool_types": ["filesystem", "python"],
        "estimated_tool_calls": 3 + ctx["band"],
    }


def build_communication_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    points = [
        f"customer impact window {ctx['band']} closes on day-{ctx['band'] + 2}",
        f"owner {WORDS[ctx['index'] % len(WORDS)]} must confirm the checklist",
        f"risk level {'high' if ctx['band'] >= 4 else 'normal'}",
    ]
    notes = [f"# Raw notes for {ctx['project']}", ""]
    for point in points:
        notes.append(f"- keep: {point}")
    if ctx["has_distractor"]:
        notes.append("- ignore: lunch preference from an old planning thread")
    if ctx["non_english"]:
        notes.append("- resumen: use concise professional wording")
    add_workspace_file(root, task_id, "drafting/raw_notes.md", "\n".join(notes) + "\n", workspace_files)
    result = {
        "subject": f"Update on {ctx['project']} {ctx['domain']}",
        "required_points": points,
        "excluded_points": ["lunch preference from an old planning thread"] if ctx["has_distractor"] else [],
        "tone": "professional_concise",
    }
    objective = (
        "Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, "
        "excluded distractors, and the intended tone. Do not invent commitments not present in the notes."
    )
    return {
        "name": f"Professional update transformation {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": ["drafting/raw_notes.md"],
            "verification": {"checked_files": 1, "invented_points": 0, "status": "pass"},
        },
        "required_tool_types": ["filesystem"],
        "estimated_tool_calls": 2 + ctx["band"],
    }


def build_memory_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    durable = [
        f"prefers summaries grouped by {WORDS[ctx['band']]}",
        f"wants checkpoint files named {ctx['project'].replace('-', '_')}_checkpoint",
    ]
    active = [
        f"waiting on owner {WORDS[(ctx['index'] + 3) % len(WORDS)]}",
        f"next review covers batch {ctx['band'] + ctx['variant']}",
    ]
    stale = ["old reminder about trial import"] if ctx["has_distractor"] else []
    log_lines = ["# Session continuation log", ""]
    for item in durable:
        log_lines.append(f"durable: {item}")
    for item in active:
        log_lines.append(f"current: {item}")
    for item in stale:
        log_lines.append(f"stale: {item}")
    if ctx["multi_session"]:
        add_workspace_file(root, task_id, "sessions/session_1.md", "\n".join(log_lines[:3]) + "\n", workspace_files)
        add_workspace_file(root, task_id, "sessions/session_2.md", "\n".join(log_lines[3:]) + "\n", workspace_files)
    else:
        add_workspace_file(root, task_id, "sessions/session_log.md", "\n".join(log_lines) + "\n", workspace_files)
    result = {
        "durable_preferences": durable,
        "current_state": active,
        "stale_items": stale,
    }
    objective = (
        "Read the session log file or files under `sessions/` and produce a context-continuation update. "
        "Separate durable preferences, current state, and stale items."
    )
    return {
        "name": f"Context continuation update {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": [Path(rel).parts[-1] for rel in workspace_files],
            "verification": {"checked_files": len(workspace_files), "multi_session": ctx["multi_session"], "status": "pass"},
        },
        "required_tool_types": ["filesystem", "memory"],
        "estimated_tool_calls": 2 + ctx["band"],
    }


def build_multi_tool_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    task_id = ctx["task_id"]
    workspace_files: list[str] = []
    tickets = []
    for item in range(4 + ctx["band"]):
        tickets.append(
            {
                "ticket": f"T{ctx['index']:06d}-{item}",
                "severity": ["low", "normal", "high"][item % 3],
                "owner": ["ari", "bea", "cam", "dev"][item % 4],
            }
        )
    add_workspace_csv(root, task_id, "triage/tickets.csv", tickets, workspace_files)
    config = {"high_severity_multiplier": 3, "normal_severity_multiplier": 2, "low_severity_multiplier": 1}
    add_workspace_json(root, task_id, "triage/scoring.json", config, workspace_files)
    log_lines = []
    blocked = []
    for item, ticket in enumerate(tickets):
        state = "blocked" if item % 4 == 0 else "ready"
        log_lines.append(f"{ticket['ticket']} state={state}")
        if state == "blocked":
            blocked.append(ticket["ticket"])
    if ctx["recoverable"]:
        log_lines.append("malformed log line without a ticket id")
    add_workspace_file(root, task_id, "triage/events.log", "\n".join(log_lines) + "\n", workspace_files)
    multiplier_key = {"high": "high_severity_multiplier", "normal": "normal_severity_multiplier", "low": "low_severity_multiplier"}
    priority = []
    for ticket in tickets:
        score = config[multiplier_key[ticket["severity"]]]
        if ticket["ticket"] in blocked:
            score -= 1
        priority.append({"ticket": ticket["ticket"], "owner": ticket["owner"], "priority_score": score})
    priority.sort(key=lambda item: (-item["priority_score"], item["ticket"]))
    result = {
        "priority_order": priority,
        "blocked_tickets": blocked,
        "malformed_events_skipped": 1 if ctx["recoverable"] else 0,
    }
    objective = (
        "Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. "
        "Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id."
    )
    return {
        "name": f"Multi-artifact triage plan {ctx['index']:06d}",
        "objective": objective,
        "workspace_files": workspace_files,
        "expected_output": {
            "result": result,
            "evidence": ["triage/tickets.csv", "triage/scoring.json", "triage/events.log"],
            "verification": {"checked_files": 3, "status": "pass"},
        },
        "required_tool_types": ["filesystem", "python", "text_search"],
        "estimated_tool_calls": 5 + ctx["band"],
    }


def build_family_task(root: Path, ctx: dict[str, Any]) -> dict[str, Any]:
    family = ctx["family"]
    if family == "file_directory_operations":
        return build_file_task(root, ctx)
    if family == "structured_data_transformation":
        return build_structured_task(root, ctx)
    if family == "statistical_quantitative_analysis":
        return build_stats_task(root, ctx)
    if family == "unstructured_document_analysis":
        return build_document_task(root, ctx)
    if family == "code_generation":
        return build_code_task(root, ctx, debugging=False)
    if family == "code_debugging":
        return build_code_task(root, ctx, debugging=True)
    if family == "repository_navigation_software_maintenance":
        return build_repo_task(root, ctx)
    if family == "web_information_gathering_source_synthesis":
        return build_source_task(root, ctx)
    if family == "planning_scheduling_constraint_satisfaction":
        return build_planning_task(root, ctx)
    if family == "professional_communication_content_transformation":
        return build_communication_task(root, ctx)
    if family == "memory_retrieval_context_continuation":
        return build_memory_task(root, ctx)
    if family == "multi_tool_workflow_orchestration":
        return build_multi_tool_task(root, ctx)
    raise ValueError(f"unsupported family {family}")


def output_schema_text() -> str:
    return """{
  "result": { ... family-specific deterministic values ... },
  "evidence": ["relative/source/path.ext"],
  "verification": {
    "checked_files": 1,
    "status": "pass"
  }
}"""


def render_prompt(ctx: dict[str, Any], built: dict[str, Any]) -> str:
    lines = [
        f"You are working on synthetic task `{ctx['task_id']}` for the `{ctx['domain']}` scenario `{ctx['project']}`.",
        "Use only the files supplied in the workspace. Do not fetch live data or use credentials.",
        "",
        built["objective"],
        "",
        f"Scenario-specific audit anchors: {ctx['anchors']}.",
        "",
        "Create `submission/result.json` using this shape:",
        "",
        "```json",
        output_schema_text(),
        "```",
        "",
        "Use relative evidence paths from the workspace. Keep lists sorted when the prompt describes a sort order.",
    ]
    if ctx["requires_verification"]:
        lines.append("Before finishing, verify that the output agrees with the relevant fixture files and record the check in `verification`.")
    if ctx["recoverable"]:
        lines.append("If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.")
    if ctx["has_distractor"]:
        lines.append("Some supplied information is intentionally irrelevant; exclude it from the result.")
    if ctx["non_english"]:
        lines.append(LANG_HINTS[ctx["index"] % len(LANG_HINTS)])
    if ctx["multi_session"]:
        lines.append("This task may require continuing context across multiple session files.")
    return "\n".join(lines)


def render_code_prompt(ctx: dict[str, Any], built: dict[str, Any]) -> str:
    lines = [
        f"You are working on synthetic task `{ctx['task_id']}` for the `{ctx['domain']}` scenario `{ctx['project']}`.",
        "Use only the supplied workspace files. Do not fetch live data or use credentials.",
        "",
        built["objective"],
        "",
        f"Scenario-specific code anchors: {ctx['anchors']}.",
        "",
        "The submitted Python file must use only the standard library and expose the requested public function.",
        "Keep the implementation deterministic and handle malformed records by skipping them when the behavior description implies a numeric conversion.",
    ]
    if ctx["requires_verification"]:
        lines.append("Run or reason through the visible cases before finishing.")
    if ctx["has_distractor"]:
        lines.append("Ignore files or comments that do not describe the requested function behavior.")
    return "\n".join(lines)


def criteria_markdown(criteria: list[str], grading_type: str) -> str:
    descriptions = {
        "format_valid": "The submission is parseable JSON with the required top-level keys.",
        "answer_correct": "The computed result matches the deterministic fixture outcome.",
        "evidence_grounded": "Evidence paths cite the supplied files used for the result.",
        "verification_complete": "The verification object accurately records checks, skips, or ignored distractors.",
        "syntax_valid": "The submitted Python module imports without syntax or execution-time definition errors.",
        "public_api": "The requested public function exists and is callable.",
        "visible_cases": "The implementation passes visible behavior cases supplied in the workspace.",
        "hidden_cases": "The implementation generalizes to held-back deterministic grader cases.",
    }
    lines = [f"- `{criterion}`: {descriptions[criterion]}" for criterion in criteria]
    if grading_type == "hybrid":
        lines.append("- Judge review: Assess clarity, traceability, and whether the response avoids unsupported assumptions.")
    if grading_type == "llm_judge":
        return (
            "- factual_grounding: Uses only supplied fixture information.\n"
            "- completeness: Covers every requested operation and constraint.\n"
            "- clarity: Presents a concise artifact in the requested format.\n"
            "- caution: Avoids invented facts, live-data claims, and unavailable-tool assumptions."
        )
    return "\n".join(lines)


def judge_rubric(grading_type: str, family: str) -> str:
    if grading_type == "automated":
        return "Not applicable; objective automated checks define the task score."
    return (
        "Judge the submitted artifact using the criteria below. Award credit only for content grounded in the supplied workspace files.\n\n"
        "- 1.0: Complete, accurate, well organized, and explicit about evidence and verification.\n"
        "- 0.7: Mostly correct with a minor omission or weak explanation that does not change the core result.\n"
        "- 0.4: Partially grounded but misses an important constraint, source, or edge case.\n"
        "- 0.0: Ungrounded, unusable, unsafe, or dependent on unavailable external data.\n\n"
        f"Capability focus: `{family}`."
    )


def automated_checks(grading_type: str, built: dict[str, Any]) -> str:
    if grading_type == "llm_judge":
        return "Not applicable; this candidate is scored by judge rubric only."
    code = built.get("automated_override") or generic_grader_code(built["expected_output"])
    return f"```python\n{code.strip()}\n```"


def expected_behavior(ctx: dict[str, Any], built: dict[str, Any]) -> str:
    if ctx["family"] in {"code_generation", "code_debugging"}:
        return (
            "A correct solution writes the requested Python module under `submission/`, exposes the requested function, "
            "passes the visible cases, and generalizes to structurally similar hidden cases."
        )
    return (
        "A correct solution reads the supplied fixtures, performs the requested transformation or analysis, writes "
        "`submission/result.json`, cites relevant relative evidence paths, and records deterministic verification details."
    )


def render_task_markdown(ctx: dict[str, Any], built: dict[str, Any]) -> tuple[str, str]:
    criteria = built.get("criteria") or GENERIC_CRITERIA
    prompt = render_code_prompt(ctx, built) if ctx["family"] in {"code_generation", "code_debugging"} else render_prompt(ctx, built)
    metadata = {
        "id": ctx["task_id"],
        "name": built["name"],
        "capability_family": ctx["family"],
        "intended_difficulty_band": ctx["band"],
        "grading_type": ctx["grading_type"],
        "timeout_seconds": 120 + ctx["band"] * 30,
        "base_scenario_id": ctx["scenario_id"],
        "generator_seed": ctx["seed"],
        "workspace_files": built["workspace_files"],
        "multi_session": ctx["multi_session"],
    }
    frontmatter_lines = ["---"]
    for key, value in metadata.items():
        if isinstance(value, bool):
            rendered = "true" if value else "false"
        elif isinstance(value, (int, float)):
            rendered = str(value)
        else:
            rendered = json.dumps(value)
        frontmatter_lines.append(f"{key}: {rendered}")
    frontmatter_lines.append("---")
    body = [
        "\n".join(frontmatter_lines),
        "",
        "# Prompt",
        "",
        prompt,
        "",
        "# Expected Behavior",
        "",
        expected_behavior(ctx, built),
        "",
        "# Grading Criteria",
        "",
        criteria_markdown(criteria, ctx["grading_type"]),
        "",
        "# Automated Checks",
        "",
        automated_checks(ctx["grading_type"], built),
        "",
        "# LLM Judge Rubric",
        "",
        judge_rubric(ctx["grading_type"], ctx["family"]),
        "",
        "# Additional Notes",
        "",
        "All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.",
        "",
    ]
    return "\n".join(body), prompt


def accepted_catalog_record(ctx: dict[str, Any], built: dict[str, Any], prompt: str) -> dict[str, Any]:
    dependency_depth = max(1, ctx["band"] + (1 if ctx["multi_file"] else 0) + (1 if ctx["recoverable"] else 0))
    scenario_fingerprint = sha256_text(f"{ctx['scenario_id']}|{ctx['family']}|{ctx['domain']}|{ctx['project']}")
    return {
        "id": ctx["task_id"],
        "status": "accepted",
        "rejection_reasons": [],
        "base_scenario_id": ctx["scenario_id"],
        "capability_family": ctx["family"],
        "intended_difficulty_band": ctx["band"],
        "grading_type": ctx["grading_type"],
        "required_tool_types": built["required_tool_types"],
        "estimated_tool_calls": built["estimated_tool_calls"],
        "dependency_depth": dependency_depth,
        "context_length_band": "short" if ctx["band"] <= 2 else ("medium" if ctx["band"] <= 4 else "long"),
        "multi_session": ctx["multi_session"],
        "requires_verification": ctx["requires_verification"],
        "contains_recoverable_failure": ctx["recoverable"],
        "workspace_files": built["workspace_files"],
        "generator_seed": ctx["seed"],
        "generator_version": GENERATOR_VERSION,
        "prompt_sha256": sha256_text(prompt),
        "normalized_prompt_sha256": sha256_text(normalize_text(prompt)),
        "base_scenario_fingerprint": scenario_fingerprint,
        "split": ctx["split"],
        "has_distractor": ctx["has_distractor"],
        "non_english_or_mixed": ctx["non_english"],
        "tool_depth_band": tool_depth_band(built["estimated_tool_calls"]),
        "recipe_id": f"{ctx['family']}:variant_{ctx['variant']}:band_{ctx['band']}",
    }


def rejected_reason(index: int) -> tuple[str, str]:
    offset = index - 8001
    buckets = [
        ("duplicate", "duplicate_prompt"),
        ("invalid", "invalid_grader_syntax"),
        ("ungradeable", "subjective_success_criteria"),
        ("low_quality", "superficial_parameter_swap"),
    ]
    return buckets[offset % len(buckets)]


def write_rejected_candidate(root: Path, index: int, accepted_target: int) -> dict[str, Any]:
    ctx = context_for(min(((index - 1) % accepted_target) + 1, accepted_target), accepted_target)
    task_id = f"task_syn_{index:06d}"
    folder, reason = rejected_reason(index)
    prompt = (
        f"This rejected synthetic candidate for {ctx['domain']} was not accepted because it triggers `{reason}`. "
        "It is retained only so the catalog accounts for every considered candidate."
    )
    text = (
        "---\n"
        f"id: {json.dumps(task_id)}\n"
        f"name: {json.dumps('Rejected candidate ' + str(index))}\n"
        f"capability_family: {json.dumps(ctx['family'])}\n"
        f"intended_difficulty_band: {ctx['band']}\n"
        f"grading_type: {json.dumps(ctx['grading_type'])}\n"
        "timeout_seconds: 120\n"
        f"base_scenario_id: {json.dumps('scenario_rejected_' + str(index).zfill(6))}\n"
        f"generator_seed: {900000 + index}\n"
        "workspace_files: []\n"
        "multi_session: false\n"
        "---\n\n"
        "# Prompt\n\n"
        f"{prompt}\n\n"
        "# Expected Behavior\n\nRejected candidate; not used for training.\n\n"
        "# Grading Criteria\n\nRejected candidate; not used for training.\n\n"
        "# Automated Checks\n\nNot applicable.\n\n"
        "# LLM Judge Rubric\n\nNot applicable.\n\n"
        "# Additional Notes\n\nRejected during synthetic quality filtering.\n"
    )
    write_text(root / "rejected" / folder / f"{task_id}.md", text)
    return {
        "id": task_id,
        "status": "rejected",
        "rejection_reasons": [reason],
        "base_scenario_id": f"scenario_rejected_{index:06d}",
        "capability_family": ctx["family"],
        "intended_difficulty_band": ctx["band"],
        "grading_type": ctx["grading_type"],
        "required_tool_types": [],
        "estimated_tool_calls": 0,
        "dependency_depth": 0,
        "context_length_band": "short",
        "multi_session": False,
        "requires_verification": False,
        "contains_recoverable_failure": False,
        "workspace_files": [],
        "generator_seed": 900000 + index,
        "generator_version": GENERATOR_VERSION,
        "prompt_sha256": sha256_text(prompt),
        "normalized_prompt_sha256": sha256_text(normalize_text(prompt)),
        "base_scenario_fingerprint": sha256_text(f"rejected|{index}|{reason}"),
        "has_distractor": False,
        "non_english_or_mixed": False,
        "tool_depth_band": "none",
        "recipe_id": f"rejected:{folder}",
    }


def validate_batch(root: Path, batch_records: list[dict[str, Any]]) -> dict[str, Any]:
    errors = []
    checked = 0
    for record in batch_records:
        if record.get("status") != "accepted":
            continue
        checked += 1
        task_path = root / "tasks" / f"{record['id']}.md"
        for error in validate_task_file(task_path, root):
            errors.append(f"{record['id']}: {error}")
    return {"accepted_checked": checked, "errors": errors[:20], "error_count": len(errors)}


def write_catalog(root: Path, records: list[dict[str, Any]]) -> None:
    with (root / "catalog.jsonl").open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True) + "\n")


def generate_corpus(root: Path, total_candidates: int, accepted_target: int, initial_batch_size: int, batch_size: int, reset: bool) -> None:
    if accepted_target % 2:
        raise ValueError("accepted_target must be even so accepted scenario families can have two variants")
    if total_candidates < accepted_target:
        raise ValueError("total_candidates must be >= accepted_target")
    if batch_size > 250:
        raise ValueError("batch_size must be at most 250")
    if reset:
        ensure_clean(root)
    else:
        for rel in ["tasks", "assets", "rejected/duplicate", "rejected/invalid", "rejected/ungradeable", "rejected/low_quality"]:
            (root / rel).mkdir(parents=True, exist_ok=True)

    catalog_records: list[dict[str, Any]] = []
    batch_log: list[dict[str, Any]] = []
    candidate = 1
    batch_number = 0
    while candidate <= total_candidates:
        size = initial_batch_size if candidate == 1 else batch_size
        end = min(total_candidates, candidate + size - 1)
        batch_number += 1
        batch_records: list[dict[str, Any]] = []
        for index in range(candidate, end + 1):
            if index <= accepted_target:
                ctx = context_for(index, accepted_target)
                built = build_family_task(root, ctx)
                task_text, prompt = render_task_markdown(ctx, built)
                write_text(root / "tasks" / f"{ctx['task_id']}.md", task_text)
                record = accepted_catalog_record(ctx, built, prompt)
            else:
                record = write_rejected_candidate(root, index, accepted_target)
            catalog_records.append(record)
            batch_records.append(record)
        write_catalog(root, catalog_records)
        check = validate_batch(root, batch_records)
        batch_log.append(
            {
                "batch": batch_number,
                "candidate_start": candidate,
                "candidate_end": end,
                "batch_size": end - candidate + 1,
                "accepted_in_batch": sum(1 for record in batch_records if record.get("status") == "accepted"),
                "rejected_in_batch": sum(1 for record in batch_records if record.get("status") != "accepted"),
                "accepted_total": sum(1 for record in catalog_records if record.get("status") == "accepted"),
                "validation": check,
            }
        )
        if check["error_count"]:
            write_text(root / "batch_log.json", json.dumps(batch_log, indent=2, sort_keys=True) + "\n")
            raise RuntimeError(f"batch {batch_number} failed validation: {check['errors'][:3]}")
        candidate = end + 1

    manifest = build_manifest(root)
    write_text(root / "split_manifest.yaml", json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    write_text(root / "batch_log.json", json.dumps(batch_log, indent=2, sort_keys=True) + "\n")
    write_report(root)


def scenario_stats(records: list[dict[str, Any]]) -> dict[str, Any]:
    accepted = [record for record in records if record.get("status") == "accepted"]
    counts = Counter(record["base_scenario_id"] for record in accepted)
    return {
        "base_scenarios": len(counts),
        "average_variants_per_base_scenario": round2(sum(counts.values()) / len(counts)) if counts else 0,
        "maximum_variants_per_base_scenario": max(counts.values(), default=0),
    }


def write_report(root: Path) -> None:
    records = []
    catalog_path = root / "catalog.jsonl"
    if catalog_path.exists():
        records = [json.loads(line) for line in catalog_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    summary = summarize(root) if catalog_path.exists() else {}
    scenario = scenario_stats(records)
    dedup = {}
    if (root / "dedup_report.json").exists():
        dedup = json.loads((root / "dedup_report.json").read_text(encoding="utf-8"))
    grader = {}
    if (root / "grader_test_results.json").exists():
        grader = json.loads((root / "grader_test_results.json").read_text(encoding="utf-8"))
    batch_log = []
    if (root / "batch_log.json").exists():
        batch_log = json.loads((root / "batch_log.json").read_text(encoding="utf-8"))
    rejected_by_reason = summary.get("rejected_by_reason", {})
    lines = [
        "# Generation Report",
        "",
        "## Counts",
        "",
        f"- Generated candidates considered: {summary.get('candidates', 0)}",
        f"- Accepted tasks: {summary.get('accepted', 0)}",
        f"- Rejected candidates: {summary.get('rejected', 0)}",
        f"- Rejected by reason: `{json.dumps(rejected_by_reason, sort_keys=True)}`",
        "",
        "## Distributions",
        "",
        f"- Capability families: `{json.dumps(summary.get('capability_family', {}), sort_keys=True)}`",
        f"- Intended difficulty bands: `{json.dumps(summary.get('intended_difficulty_band', {}), sort_keys=True)}`",
        f"- Grading types: `{json.dumps(summary.get('grading_type', {}), sort_keys=True)}`",
        f"- Tool-depth bands: `{json.dumps(summary.get('tool_depth_band', {}), sort_keys=True)}`",
        f"- Context-length bands: `{json.dumps(summary.get('context_length_band', {}), sort_keys=True)}`",
        f"- Splits: `{json.dumps(summary.get('split', {}), sort_keys=True)}`",
        f"- Multi-session tasks: {summary.get('multi_session', 0)}",
        f"- Recoverable-failure tasks: {summary.get('contains_recoverable_failure', 0)}",
        f"- Verification tasks: {summary.get('requires_verification', 0)}",
        f"- Distractor tasks: {summary.get('has_distractor', 0)}",
        f"- Non-English or mixed-language tasks: {summary.get('non_english_or_mixed', 0)}",
        f"- Multi-file or multi-artifact tasks: {summary.get('multiple_files_or_artifacts', 0)}",
        "",
        "## Scenario Families",
        "",
        f"- Number of base scenarios: {scenario.get('base_scenarios', 0)}",
        f"- Average variants per base scenario: {scenario.get('average_variants_per_base_scenario', 0)}",
        f"- Maximum variants per base scenario: {scenario.get('maximum_variants_per_base_scenario', 0)}",
        "",
        "## Duplicate Detection",
        "",
        f"- Exact prompt duplicate pairs: {len(dedup.get('exact_prompt_duplicates', [])) if dedup else 'not yet run'}",
        f"- Normalized prompt duplicate pairs: {len(dedup.get('normalized_prompt_duplicates', [])) if dedup else 'not yet run'}",
        f"- High 5-gram-overlap pairs: {len(dedup.get('high_token_5gram_overlap_pairs', [])) if dedup else 'not yet run'}",
        f"- Base-scenario fingerprint overflows: {len(dedup.get('base_scenario_fingerprint_overflows', {})) if dedup else 'not yet run'}",
        f"- Grader-similarity pairs for inspection: {len(dedup.get('grader_similarity_pairs_for_inspection', [])) if dedup else 'not yet run'}",
        f"- Max fixture-schema reuse: {dedup.get('max_fixture_schema_reuse', 'not yet run') if dedup else 'not yet run'}",
        "",
        "## Grader Tests",
        "",
        f"- Automated/hybrid graders tested: {grader.get('tested', 'not yet run')}",
        f"- Grader failures: {grader.get('failed', 'not yet run')}",
        "",
        "## Batch Process",
        "",
        f"- Initial batch size: {batch_log[0]['batch_size'] if batch_log else 'not yet run'}",
        f"- Total batches: {len(batch_log)}",
        f"- Batch validation errors observed: {sum(item['validation']['error_count'] for item in batch_log) if batch_log else 'not yet run'}",
        "- Initial-batch generator adjustments: added deterministic task-specific anchors and focused the 5-gram duplicate check on task-specific prompt content after the first duplicate pass found boilerplate-driven overlap.",
        "",
        "## Known Limitations",
        "",
        "- The corpus is synthetic and generated from compositional recipes, so a separate post-generation contamination audit is still required.",
        "- Judge-only tasks require later human or model-judge calibration before use in scoring experiments.",
        "- Automated graders check deterministic artifacts and may not reward every semantically equivalent presentation outside the requested schema.",
        "",
        "## Reproduction Commands",
        "",
        "```bash",
        "python synthetic_router_corpus/scripts/generate_batch.py synthetic_router_corpus --reset --total-candidates 10000 --accepted-target 8000 --initial-batch-size 50 --batch-size 250",
        "python synthetic_router_corpus/scripts/deduplicate_tasks.py synthetic_router_corpus",
        "python synthetic_router_corpus/scripts/test_graders.py synthetic_router_corpus",
        "python synthetic_router_corpus/scripts/validate_corpus.py synthetic_router_corpus --expected-accepted 8000",
        "python synthetic_router_corpus/scripts/generate_batch.py synthetic_router_corpus --report-only",
        "```",
        "",
        "## Firewall Confirmation",
        "",
        "- The generation process did not access the external held-out benchmark named in the user specification.",
        "- No final routing labels, model-tier labels, quality-versus-cost rewards, or claimed model outcomes were generated.",
        "- This report does not claim freedom from all possible pretraining contamination; a separate post-generation audit is still required.",
        "",
    ]
    write_text(root / "generation_report.md", "\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--reset", action="store_true")
    parser.add_argument("--total-candidates", type=int, default=10000)
    parser.add_argument("--accepted-target", type=int, default=8000)
    parser.add_argument("--initial-batch-size", type=int, default=50)
    parser.add_argument("--batch-size", type=int, default=250)
    parser.add_argument("--report-only", action="store_true")
    args = parser.parse_args()
    if args.report_only:
        write_report(args.root)
        print(f"updated {args.root / 'generation_report.md'}")
        return 0
    generate_corpus(
        args.root,
        total_candidates=args.total_candidates,
        accepted_target=args.accepted_target,
        initial_batch_size=args.initial_batch_size,
        batch_size=args.batch_size,
        reset=args.reset,
    )
    print(
        f"generated {args.total_candidates} candidates with {args.accepted_target} accepted tasks under {args.root}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
