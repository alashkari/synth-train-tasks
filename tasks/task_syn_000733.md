---
id: "task_syn_000733"
name: "Mini repository maintenance scan 000733"
capability_family: "repository_navigation_software_maintenance"
intended_difficulty_band: 3
grading_type: "automated"
timeout_seconds: 210
base_scenario_id: "scenario_000367"
generator_seed: 757121
workspace_files: ["assets/task_syn_000733/workspace/repo/config/modules.json", "assets/task_syn_000733/workspace/repo/src/ingest.py", "assets/task_syn_000733/workspace/repo/src/export.py", "assets/task_syn_000733/workspace/repo/src/audit.py", "assets/task_syn_000733/workspace/repo/src/notify.py", "assets/task_syn_000733/workspace/repo/src/cleanup.py", "assets/task_syn_000733/workspace/repo/docs/changelog.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_000733` for the `policy review` scenario `delta-umbra-0367`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the mini repository under `repo/`. Create a maintenance report with enabled modules, deprecated modules, TODO markers with their module names, and any enabled module whose source file is missing.

Scenario-specific audit anchors: yapoyaf zetunag joluwoh yagudii dirikij nacenak johacel mefokim zehapon sariceo cewolup rizehaq bavetur wowohas cevegut ditumeu megumev wohawow tudinax saluguy posasaz rididia folubab baveyac fodisad gupojoe gujotuf dimelug vehajoh jofotui mesanaj guyapok fobafol lucebam rivegun zewofoo hahapop navezeq mepofor riwoces mefoyat barikiu lululuv nanabaw sayakix kiporiy yafozez diceria jowopob yayavec tuceced woripoe bazekif savetug foluguh fopovei nafobaj hatunak forihal vepolum cedipon cepoguo rijohap kiceguq yayakir sarigus nacevet digubau mezevev wokinaw foyazex hakiluy fosafoz nazevea hayajob diwopoc ceyagud popomee lunayaf naluhag dimeveh yavepoi sayarij cepowok podihal velugum nakimen cehaceo wodikip hadinaq zevesar dizenas mebatut sajoceu woguhav josapow.

Create `submission/result.json` using this shape:

```json
{
  "result": { ... family-specific deterministic values ... },
  "evidence": ["relative/source/path.ext"],
  "verification": {
    "checked_files": 1,
    "status": "pass"
  }
}
```

Use relative evidence paths from the workspace. Keep lists sorted when the prompt describes a sort order.

# Expected Behavior

A correct solution reads the supplied fixtures, performs the requested transformation or analysis, writes `submission/result.json`, cites relevant relative evidence paths, and records deterministic verification details.

# Grading Criteria

- `format_valid`: The submission is parseable JSON with the required top-level keys.
- `answer_correct`: The computed result matches the deterministic fixture outcome.
- `evidence_grounded`: Evidence paths cite the supplied files used for the result.
- `verification_complete`: The verification object accurately records checks, skips, or ignored distractors.

# Automated Checks

```python
from pathlib import Path
import json

CRITERIA = ['format_valid', 'answer_correct', 'evidence_grounded', 'verification_complete']
EXPECTED_OUTPUT = {'result': {'enabled_modules': ['ingest', 'export', 'audit'], 'deprecated_modules': ['cleanup'], 'todo_items': [{'module': 'ingest', 'todo': '733-0'}, {'module': 'audit', 'todo': '733-2'}, {'module': 'cleanup', 'todo': '733-4'}], 'missing_enabled_files': []}, 'evidence': ['repo/config/modules.json', 'repo/src'], 'verification': {'checked_files': 7, 'status': 'pass'}}

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
    scores = {key: 0.0 for key in CRITERIA}
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
    output.write_text(json.dumps(EXPECTED_OUTPUT, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def create_incorrect_solution(workspace_dir):
    output = Path(workspace_dir) / "submission" / "result.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"result": {}, "evidence": [], "verification": {"status": "unchecked"}}) + "\n", encoding="utf-8")
```

# LLM Judge Rubric

Not applicable; objective automated checks define the task score.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
