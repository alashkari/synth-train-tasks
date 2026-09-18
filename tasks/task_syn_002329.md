---
id: "task_syn_002329"
name: "Active file manifest 002329"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_001165"
generator_seed: 816173
workspace_files: ["assets/task_syn_002329/workspace/incoming/archive/violet_nimbus_1165_00.json", "assets/task_syn_002329/workspace/incoming/active/violet_nimbus_1165_01.txt", "assets/task_syn_002329/workspace/incoming/active/violet_nimbus_1165_02.md", "assets/task_syn_002329/workspace/incoming/active/violet_nimbus_1165_03.json", "assets/task_syn_002329/workspace/incoming/archive/violet_nimbus_1165_04.json", "assets/task_syn_002329/workspace/incoming/active/violet_nimbus_1165_05.cfg", "assets/task_syn_002329/workspace/incoming/active/violet_nimbus_1165_06.md", "assets/task_syn_002329/workspace/incoming/active/violet_nimbus_1165_07.md", "assets/task_syn_002329/workspace/incoming/archive/violet_nimbus_1165_08.cfg"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_002329` for the `access cleanup` scenario `violet-nimbus-1165`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: difomep cehanaq woyanar wonawos cebahat baluhau tusatuv mefoguw fohagux gufotuy wopotuz bayawoa kivefob tujozec rigurid kidipoe megudif dimesag zezemeh sagusai harikij pomeguk rijocel gunagum tulukin hazeveo vetukip zeluceq cezezer haworis bamevet kimewou hawoguv wodiriw guhatux gudiwoy havejoz tufokia joyagub gufofoc powopod fomefoe vecejof cenadig sagumeh lubasai hasakij fofonak gujodil kilumem cefogun bakihao mebagup savefoq cewofor tutumes tulurit jodipou yatubav pobayaw posamex zepobay haveluz wolufoa hahabab pofocec badiced vekiyae zezedif foguwog sacetuh fobagui yakijoj poluhak hapolul zeyanam venajon posaveo cerikip lutuyaq kikirir cehawos rilukit yamekiu zemevev yafotuw meyalux kiguyay popomez sazehaa gutuveb hazesac nazegud joguzee tulurif fodizeg.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/violet_nimbus_1165_03.json'], 'active_extension_counts': {'cfg': 1, 'json': 1, 'md': 3, 'txt': 1}, 'largest_active_file': {'path': 'incoming/active/violet_nimbus_1165_07.md', 'bytes': 174}}, 'evidence': ['incoming/active/violet_nimbus_1165_01.txt', 'incoming/active/violet_nimbus_1165_02.md', 'incoming/active/violet_nimbus_1165_03.json', 'incoming/active/violet_nimbus_1165_05.cfg'], 'verification': {'checked_files': 9, 'ignored_archive': True, 'status': 'pass'}}

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
