#!/usr/bin/env python3
"""Summarize accepted-task distributions."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from _common import accepted_catalog, load_catalog


def summarize(root: Path) -> dict:
    accepted = accepted_catalog(root)
    all_records = load_catalog(root)
    summary = {
        "candidates": len(all_records),
        "accepted": len(accepted),
        "rejected": len(all_records) - len(accepted),
        "rejected_by_reason": Counter(
            reason
            for record in all_records
            if record.get("status") != "accepted"
            for reason in record.get("rejection_reasons", [])
        ),
        "capability_family": Counter(record["capability_family"] for record in accepted),
        "intended_difficulty_band": Counter(str(record["intended_difficulty_band"]) for record in accepted),
        "grading_type": Counter(record["grading_type"] for record in accepted),
        "tool_depth_band": Counter(record.get("tool_depth_band", "unknown") for record in accepted),
        "context_length_band": Counter(record["context_length_band"] for record in accepted),
        "split": Counter(record.get("split", "unknown") for record in accepted),
        "multi_session": sum(1 for record in accepted if record.get("multi_session")),
        "contains_recoverable_failure": sum(
            1 for record in accepted if record.get("contains_recoverable_failure")
        ),
        "requires_verification": sum(1 for record in accepted if record.get("requires_verification")),
        "has_distractor": sum(1 for record in accepted if record.get("has_distractor")),
        "non_english_or_mixed": sum(1 for record in accepted if record.get("non_english_or_mixed")),
        "multiple_files_or_artifacts": sum(
            1 for record in accepted if len(record.get("workspace_files", [])) >= 2
        ),
        "multiple_operations": sum(1 for record in accepted if record.get("dependency_depth", 0) >= 2),
    }
    return {
        key: dict(value) if isinstance(value, Counter) else value
        for key, value in summary.items()
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    summary = summarize(args.root)
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        for key, value in summary.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
