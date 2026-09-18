#!/usr/bin/env python3
"""Build a scenario-family split manifest from catalog.jsonl."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from _common import accepted_catalog


def build_manifest(root: Path) -> dict:
    split_scenarios: dict[str, dict[str, set[str] | list[str]]] = {
        "train": {"scenario_ids": set(), "task_ids": []},
        "development": {"scenario_ids": set(), "task_ids": []},
        "synthetic_holdout": {"scenario_ids": set(), "task_ids": []},
    }
    scenario_to_split: dict[str, str] = {}
    for record in accepted_catalog(root):
        split = record.get("split")
        scenario_id = record.get("base_scenario_id")
        task_id = record.get("id")
        if split not in split_scenarios:
            raise ValueError(f"invalid split {split!r} for {task_id}")
        if scenario_id in scenario_to_split and scenario_to_split[scenario_id] != split:
            raise ValueError(f"scenario {scenario_id} crosses splits")
        scenario_to_split[scenario_id] = split
        split_scenarios[split]["scenario_ids"].add(scenario_id)
        split_scenarios[split]["task_ids"].append(task_id)

    manifest = {
        "split_policy": "scenario_family",
        "splits": {},
    }
    for split, payload in split_scenarios.items():
        scenario_ids = sorted(payload["scenario_ids"])
        task_ids = sorted(payload["task_ids"])
        manifest["splits"][split] = {
            "scenario_count": len(scenario_ids),
            "task_count": len(task_ids),
            "scenario_ids": scenario_ids,
            "task_ids": task_ids,
        }
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    manifest = build_manifest(args.root)
    output_path = args.root / "split_manifest.yaml"
    output_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
