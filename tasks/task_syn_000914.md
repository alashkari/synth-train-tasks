---
id: "task_syn_000914"
name: "Active file manifest 000914"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_000457"
generator_seed: 763818
workspace_files: ["assets/task_syn_000914/workspace/incoming/archive/prairie_ion_0457_00.json", "assets/task_syn_000914/workspace/incoming/active/prairie_ion_0457_01.cfg", "assets/task_syn_000914/workspace/incoming/active/prairie_ion_0457_02.json", "assets/task_syn_000914/workspace/incoming/active/prairie_ion_0457_03.cfg", "assets/task_syn_000914/workspace/incoming/archive/prairie_ion_0457_04.md", "assets/task_syn_000914/workspace/incoming/active/prairie_ion_0457_05.txt", "assets/task_syn_000914/workspace/incoming/active/prairie_ion_0457_06.md", "assets/task_syn_000914/workspace/incoming/active/prairie_ion_0457_07.cfg", "assets/task_syn_000914/workspace/incoming/archive/prairie_ion_0457_08.txt", "assets/task_syn_000914/workspace/incoming/active/prairie_ion_0457_09.txt", "assets/task_syn_000914/workspace/incoming/active/prairie_ion_0457_10.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_000914` for the `access cleanup` scenario `prairie-ion-0457`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: foyadie kizecef diponag fofodih zelusai rinabaj gudijok tuyapol lutuwom hayapon kibakio megupop nafoyaq risapor woporis cepodit didimeu wocevev babanaw zewoyax riwobay yavekiz bavemea rifosab guzedic kimezed pogusae medicef fonanag kimeveh guhadii sadifoj woyawok babawol gucerim hajoyan meceluo tuzegup baceveq potucer sazeces pogudit kiyadiu kitunav kiwokiw guzeyax fovewoy rifowoz zenabaa hazezeb zeceric nagulud lufomee vegupof potumeg diyazeh fonapoi povesaj mezedik cewogul pogugum meyakin vemehao rimeyap difonaq dihanar wokiyas pohavet safokiu zeyamev cemejow dirivex veyamey cejomez rilukia hatuceb tujohac mecebad hagulue cememef vehaceg baponah jonabai yatufoj nahabak dijonal bawosam nadihan yacepoo zejorip zeveveq wozeyar bacekis nanapot jovepou mevecev.

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
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/prairie_ion_0457_02.json'], 'active_extension_counts': {'cfg': 3, 'json': 1, 'md': 1, 'txt': 3}, 'largest_active_file': {'path': 'incoming/active/prairie_ion_0457_10.txt', 'bytes': 196}}, 'evidence': ['incoming/active/prairie_ion_0457_01.cfg', 'incoming/active/prairie_ion_0457_02.json', 'incoming/active/prairie_ion_0457_03.cfg', 'incoming/active/prairie_ion_0457_05.txt'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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
