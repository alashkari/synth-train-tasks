#!/usr/bin/env python3
"""Execute automated grader snippets against empty, incorrect, and valid workspaces."""

from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

from _common import (
    accepted_catalog,
    bounded_scores,
    extract_python_code,
    read_task,
    relative_task_path,
)


def copy_workspace_files(root: Path, record: dict[str, Any], destination: Path) -> None:
    for rel in record.get("workspace_files", []):
        source = root / rel
        parts = Path(rel).parts
        if "workspace" in parts:
            index = parts.index("workspace")
            target_rel = Path(*parts[index + 1 :])
        else:
            target_rel = Path(source.name)
        target = destination / target_rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def load_grader(root: Path, task_id: str) -> dict[str, Any]:
    metadata, sections, _body, _text = read_task(relative_task_path(root, task_id))
    code = extract_python_code(sections.get("Automated Checks", ""))
    namespace: dict[str, Any] = {}
    exec(compile(code, f"<grader:{task_id}>", "exec"), namespace)
    return namespace


def run_case(namespace: dict[str, Any], workspace: Path) -> dict[str, float]:
    scores = namespace["grade"](str(workspace))
    if not bounded_scores(scores):
        raise AssertionError(f"malformed score mapping: {scores!r}")
    return dict(scores)


def test_record(root: Path, record: dict[str, Any]) -> dict[str, Any]:
    task_id = record["id"]
    namespace = load_grader(root, task_id)
    if not callable(namespace.get("grade")):
        raise AssertionError("missing grade function")

    result: dict[str, Any] = {"id": task_id, "cases": {}}
    with tempfile.TemporaryDirectory() as tmp:
        scores = run_case(namespace, Path(tmp))
        result["cases"]["empty"] = scores

    with tempfile.TemporaryDirectory() as tmp:
        workspace = Path(tmp)
        copy_workspace_files(root, record, workspace)
        maker = namespace.get("create_incorrect_solution")
        if callable(maker):
            maker(str(workspace))
        else:
            (workspace / "submission").mkdir(exist_ok=True)
            (workspace / "submission" / "result.json").write_text('{"incorrect": true}\n', encoding="utf-8")
        scores = run_case(namespace, workspace)
        result["cases"]["incorrect"] = scores

    with tempfile.TemporaryDirectory() as tmp:
        workspace = Path(tmp)
        copy_workspace_files(root, record, workspace)
        maker = namespace.get("create_reference_solution")
        if not callable(maker):
            raise AssertionError("missing create_reference_solution helper")
        maker(str(workspace))
        scores = run_case(namespace, workspace)
        result["cases"]["reference"] = scores
        if any(value < 0.999 for value in scores.values()):
            raise AssertionError(f"reference solution did not receive full score: {scores!r}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    records = [
        record
        for record in accepted_catalog(args.root)
        if record.get("grading_type") in {"automated", "hybrid"}
    ]
    if args.limit is not None:
        records = records[: args.limit]

    failures: list[dict[str, str]] = []
    tested = 0
    for record in records:
        try:
            test_record(args.root, record)
            tested += 1
        except Exception as exc:
            failures.append({"id": record.get("id", "unknown"), "error": str(exc)})

    summary = {"tested": tested, "failed": len(failures), "failures": failures[:50]}
    (args.root / "grader_test_results.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
