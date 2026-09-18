#!/usr/bin/env python3
"""Validate one synthetic router-corpus task file."""

from __future__ import annotations

import argparse
import ast
import tempfile
from pathlib import Path
from typing import Any

from _common import (
    CAPABILITY_FAMILIES,
    GRADING_TYPES,
    REQUIRED_FRONTMATTER,
    REQUIRED_SECTIONS,
    bounded_scores,
    check_grader_ast,
    contains_forbidden_benchmark_reference,
    contains_routing_label_field,
    extract_criterion_names,
    extract_list_constant,
    extract_python_code,
    read_task,
)


def _execute_grader_empty_workspace(code: str) -> tuple[dict[str, float] | None, str | None]:
    namespace: dict[str, Any] = {}
    try:
        exec(compile(code, "<grader>", "exec"), namespace)
    except Exception as exc:
        return None, f"grader import/definition failed: {exc}"
    grade = namespace.get("grade")
    if not callable(grade):
        return None, "grader grade function is not callable"
    try:
        with tempfile.TemporaryDirectory() as tmp:
            scores = grade(tmp)
    except Exception as exc:
        return None, f"grader crashed on empty workspace: {exc}"
    if not bounded_scores(scores):
        return None, f"grader returned unbounded or malformed scores: {scores!r}"
    return dict(scores), None


def validate_task_file(path: Path, root: Path | None = None) -> list[str]:
    errors: list[str] = []
    root = root or path.parents[1]
    try:
        metadata, sections, _body, text = read_task(path)
    except Exception as exc:
        return [f"{path}: {exc}"]

    for key in REQUIRED_FRONTMATTER:
        if key not in metadata:
            errors.append(f"missing required frontmatter key: {key}")
    if contains_routing_label_field(metadata):
        errors.append("frontmatter contains a routing-label field")

    task_id = metadata.get("id")
    if not isinstance(task_id, str) or not task_id.startswith("task_syn_"):
        errors.append("invalid task id")
    elif path.name != f"{task_id}.md":
        errors.append(f"filename does not match id {task_id}")

    if metadata.get("capability_family") not in CAPABILITY_FAMILIES:
        errors.append(f"invalid capability family: {metadata.get('capability_family')}")
    if metadata.get("grading_type") not in GRADING_TYPES:
        errors.append(f"invalid grading type: {metadata.get('grading_type')}")
    if metadata.get("intended_difficulty_band") not in {1, 2, 3, 4, 5}:
        errors.append("intended_difficulty_band must be 1..5")
    timeout = metadata.get("timeout_seconds")
    if not isinstance(timeout, int) or timeout < 30 or timeout > 1800:
        errors.append("timeout_seconds must be an integer between 30 and 1800")
    if not isinstance(metadata.get("multi_session"), bool):
        errors.append("multi_session must be boolean")
    workspace_files = metadata.get("workspace_files")
    if not isinstance(workspace_files, list):
        errors.append("workspace_files must be a list")
    else:
        for rel_path in workspace_files:
            if not isinstance(rel_path, str):
                errors.append("workspace_files entries must be strings")
                continue
            if Path(rel_path).is_absolute() or ".." in Path(rel_path).parts:
                errors.append(f"workspace file path is not safe relative path: {rel_path}")
            elif not (root / rel_path).exists():
                errors.append(f"workspace asset does not exist: {rel_path}")

    for section in REQUIRED_SECTIONS:
        if section not in sections:
            errors.append(f"missing required section: {section}")
    if not sections.get("Prompt", "").strip():
        errors.append("prompt section is empty")
    if contains_forbidden_benchmark_reference(text):
        errors.append("task contains a forbidden benchmark reference")
    if "routing_label" in text or "final_routing" in text or "ground_truth_route" in text:
        errors.append("task contains an explicit routing-label token")

    grading_type = metadata.get("grading_type")
    code = extract_python_code(sections.get("Automated Checks", ""))
    criteria = extract_criterion_names(sections.get("Grading Criteria", ""))

    if grading_type in {"automated", "hybrid"}:
        if not code:
            errors.append("automated or hybrid task is missing a Python grader code block")
        else:
            errors.extend(check_grader_ast(code))
            try:
                tree = ast.parse(code)
                code_criteria = extract_list_constant(tree, "CRITERIA")
            except SyntaxError:
                code_criteria = None
            if not criteria:
                errors.append("automated or hybrid task has no named grading criteria")
            if code_criteria is None:
                errors.append("grader must define CRITERIA as a list of score keys")
            elif sorted(criteria) != sorted(code_criteria):
                errors.append(
                    f"grading criteria names {criteria!r} do not match grader keys {code_criteria!r}"
                )
            scores, exec_error = _execute_grader_empty_workspace(code)
            if exec_error:
                errors.append(exec_error)
            elif code_criteria and sorted(scores or {}) != sorted(code_criteria):
                errors.append("grader score keys do not match CRITERIA on empty workspace")
    elif grading_type == "llm_judge":
        rubric = sections.get("LLM Judge Rubric", "")
        if not rubric or "not applicable" in rubric.lower():
            errors.append("llm_judge task must include an applicable judge rubric")
        if code:
            errors.append("llm_judge-only task must not include an automated grader code block")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task_file", type=Path)
    parser.add_argument("--root", type=Path, default=None)
    args = parser.parse_args()
    errors = validate_task_file(args.task_file, args.root)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"OK {args.task_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
