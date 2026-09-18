---
id: "task_syn_002161"
name: "Active file manifest 002161"
capability_family: "file_directory_operations"
intended_difficulty_band: 1
grading_type: "automated"
timeout_seconds: 150
base_scenario_id: "scenario_001081"
generator_seed: 809957
workspace_files: ["assets/task_syn_002161/workspace/incoming/archive/prairie_umbra_1081_00.txt", "assets/task_syn_002161/workspace/incoming/active/prairie_umbra_1081_01.log", "assets/task_syn_002161/workspace/incoming/active/prairie_umbra_1081_02.json", "assets/task_syn_002161/workspace/incoming/active/prairie_umbra_1081_03.json", "assets/task_syn_002161/workspace/incoming/archive/prairie_umbra_1081_04.txt", "assets/task_syn_002161/workspace/incoming/active/prairie_umbra_1081_05.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_002161` for the `release readiness` scenario `prairie-umbra-1081`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the release readiness workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.log` whose byte length is at least 31, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: harijod wotutue guhawof gudimeg disadih zehawoi pokifoj fomezek ririlul salurim guvefon tusafoo sajonap yafofoq mekigur wosakis vewocet gurijou gukijov wozezew riwocex naveguy kilumez zezehaa vecerib napodic dikibad sajocee cedipof sadikig vehaceh meyasai jobakij sakizek gulupol bagupom zefozen tuzejoo tugusap cerinaq rigumer lucefos dilugut posapou kihadiv kikiguw bagupox luwokiy yajonaz popojoa vezejob lumeyac yalufod kizefoe fokicef kirifog hazetuh fofopoi wocezej bakibak fozedil mebanam fozesan baguwoo vecefop jomeceq foyajor worisas halucet jobaluu yatuyav zesavew cedivex cewoguy tusafoz luzehaa naridib melutuc jozegud wozecee hajodif vemeceg tutunah cekikii wocetuj digufok vezewol popowom najodin woluceo divefop yapohaq zebadir mebanas zedirit kiriluu.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'log', 'minimum_bytes': 31, 'selected_files': ['incoming/active/prairie_umbra_1081_01.log', 'incoming/active/prairie_umbra_1081_05.log'], 'active_extension_counts': {'json': 2, 'log': 2}, 'largest_active_file': {'path': 'incoming/active/prairie_umbra_1081_05.log', 'bytes': 142}}, 'evidence': ['incoming/active/prairie_umbra_1081_01.log', 'incoming/active/prairie_umbra_1081_02.json', 'incoming/active/prairie_umbra_1081_03.json', 'incoming/active/prairie_umbra_1081_05.log'], 'verification': {'checked_files': 6, 'ignored_archive': True, 'status': 'pass'}}

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
