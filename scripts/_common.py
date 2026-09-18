#!/usr/bin/env python3
"""Shared helpers for the synthetic router corpus scripts."""

from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path
from typing import Any


GENERATOR_VERSION = "1.0"

CAPABILITY_FAMILIES = [
    "file_directory_operations",
    "structured_data_transformation",
    "statistical_quantitative_analysis",
    "unstructured_document_analysis",
    "code_generation",
    "code_debugging",
    "repository_navigation_software_maintenance",
    "web_information_gathering_source_synthesis",
    "planning_scheduling_constraint_satisfaction",
    "professional_communication_content_transformation",
    "memory_retrieval_context_continuation",
    "multi_tool_workflow_orchestration",
]

GRADING_TYPES = {"automated", "hybrid", "llm_judge"}

REQUIRED_FRONTMATTER = [
    "id",
    "name",
    "capability_family",
    "intended_difficulty_band",
    "grading_type",
    "timeout_seconds",
    "base_scenario_id",
    "generator_seed",
    "workspace_files",
    "multi_session",
]

REQUIRED_SECTIONS = [
    "Prompt",
    "Expected Behavior",
    "Grading Criteria",
    "Automated Checks",
    "LLM Judge Rubric",
    "Additional Notes",
]

ALLOWED_GRADER_IMPORTS = {
    "ast",
    "collections",
    "csv",
    "datetime",
    "decimal",
    "difflib",
    "fnmatch",
    "fractions",
    "hashlib",
    "html",
    "importlib",
    "io",
    "itertools",
    "json",
    "math",
    "operator",
    "os",
    "pathlib",
    "re",
    "statistics",
    "string",
    "textwrap",
    "unicodedata",
    "xml",
}

FORBIDDEN_IMPORTS = {
    "asyncio",
    "ftplib",
    "http",
    "imaplib",
    "poplib",
    "requests",
    "shutil",
    "smtplib",
    "socket",
    "subprocess",
    "telnetlib",
    "urllib",
    "webbrowser",
}

FORBIDDEN_CALL_NAMES = {
    "urlopen",
    "urlretrieve",
    "request",
    "connect",
    "socket",
    "Popen",
    "run",
    "system",
}

ROUTING_LABEL_KEYS = {
    "routing_label",
    "route_label",
    "final_routing_label",
    "final_route",
    "model_tier",
    "target_tier",
    "ground_truth_route",
    "ground_truth_label",
    "optimal_route",
}

# Construct the held-out benchmark name without storing it contiguously in the
# generated corpus files.
FORBIDDEN_BENCHMARK_TERMS = ["Pinch" + "Bench"]


class TaskParseError(ValueError):
    pass


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_text(text: str) -> str:
    lowered = text.lower()
    lowered = re.sub(r"\b\d+(?:\.\d+)?\b", "<num>", lowered)
    lowered = re.sub(r"[^a-z0-9_<>\s]+", " ", lowered)
    return re.sub(r"\s+", " ", lowered).strip()


def token_ngrams(text: str, n: int = 5) -> set[tuple[str, ...]]:
    tokens = normalize_text(text).split()
    if len(tokens) < n:
        return set()
    return {tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)}


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value == "":
        return ""
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() == "null":
        return None
    if value.startswith("[") or value.startswith("{"):
        return ast.literal_eval(value)
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return ast.literal_eval(value)
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?\d+\.\d+", value):
        return float(value)
    return value


def parse_frontmatter_block(block: str) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    current_key: str | None = None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            metadata.setdefault(current_key, []).append(parse_scalar(line[4:]))
            continue
        if ":" not in line:
            raise TaskParseError(f"invalid frontmatter line: {line!r}")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        current_key = key
        if raw_value == "":
            metadata[key] = []
        else:
            metadata[key] = parse_scalar(raw_value)
    return metadata


def parse_task_text(text: str) -> tuple[dict[str, Any], dict[str, str], str]:
    if not text.startswith("---\n"):
        raise TaskParseError("missing YAML frontmatter opening delimiter")
    try:
        _, frontmatter, body = text.split("---", 2)
    except ValueError as exc:
        raise TaskParseError("missing YAML frontmatter closing delimiter") from exc
    metadata = parse_frontmatter_block(frontmatter)
    sections: dict[str, str] = {}
    matches = list(re.finditer(r"^# ([^\n#]+)\n", body, flags=re.MULTILINE))
    for index, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections[title] = body[start:end].strip()
    return metadata, sections, body


def read_task(path: Path) -> tuple[dict[str, Any], dict[str, str], str, str]:
    text = path.read_text(encoding="utf-8")
    metadata, sections, body = parse_task_text(text)
    return metadata, sections, body, text


def extract_python_code(section_text: str) -> str:
    match = re.search(r"```python\n(.*?)\n```", section_text, flags=re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_criterion_names(section_text: str) -> list[str]:
    names: list[str] = []
    for line in section_text.splitlines():
        stripped = line.strip()
        match = re.match(r"[-*]\s+`?([a-zA-Z0-9_]+)`?\s*:", stripped)
        if match:
            names.append(match.group(1))
    return names


def extract_list_constant(tree: ast.AST, constant_name: str) -> list[str] | None:
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == constant_name:
                    try:
                        value = ast.literal_eval(node.value)
                    except Exception:
                        return None
                    if isinstance(value, (list, tuple)) and all(
                        isinstance(item, str) for item in value
                    ):
                        return list(value)
    return None


def check_grader_ast(code: str) -> list[str]:
    errors: list[str] = []
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        return [f"grader syntax error: {exc}"]

    has_grade = any(isinstance(node, ast.FunctionDef) and node.name == "grade" for node in tree.body)
    if not has_grade:
        errors.append("grader does not define grade(workspace_dir)")

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports = []
            if isinstance(node, ast.Import):
                imports = [alias.name.split(".")[0] for alias in node.names]
            elif node.module:
                imports = [node.module.split(".")[0]]
            for imported in imports:
                if imported in FORBIDDEN_IMPORTS:
                    errors.append(f"forbidden grader import: {imported}")
                elif imported not in ALLOWED_GRADER_IMPORTS:
                    errors.append(f"unsupported grader import: {imported}")
        if isinstance(node, ast.Call):
            func = node.func
            name = ""
            if isinstance(func, ast.Name):
                name = func.id
            elif isinstance(func, ast.Attribute):
                name = func.attr
            if name in FORBIDDEN_CALL_NAMES:
                errors.append(f"forbidden grader call: {name}")
    return errors


def load_catalog(root: Path) -> list[dict[str, Any]]:
    catalog_path = root / "catalog.jsonl"
    if not catalog_path.exists():
        return []
    records = []
    for line_number, line in enumerate(catalog_path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON in catalog line {line_number}: {exc}") from exc
    return records


def accepted_catalog(root: Path) -> list[dict[str, Any]]:
    return [record for record in load_catalog(root) if record.get("status") == "accepted"]


def relative_task_path(root: Path, task_id: str) -> Path:
    return root / "tasks" / f"{task_id}.md"


def bounded_scores(scores: Any) -> bool:
    if not isinstance(scores, dict) or not scores:
        return False
    for key, value in scores.items():
        if not isinstance(key, str):
            return False
        if not isinstance(value, (int, float)):
            return False
        if value < 0.0 or value > 1.0:
            return False
    return True


def contains_forbidden_benchmark_reference(text: str) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in FORBIDDEN_BENCHMARK_TERMS)


def contains_routing_label_field(mapping: dict[str, Any]) -> bool:
    return any(str(key).lower() in ROUTING_LABEL_KEYS for key in mapping)
