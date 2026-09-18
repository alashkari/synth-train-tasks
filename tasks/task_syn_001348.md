---
id: "task_syn_001348"
name: "Structured table normalization 001348"
capability_family: "structured_data_transformation"
intended_difficulty_band: 3
grading_type: "automated"
timeout_seconds: 210
base_scenario_id: "scenario_000674"
generator_seed: 779876
workspace_files: ["assets/task_syn_001348/workspace/tables/source_records.csv", "assets/task_syn_001348/workspace/tables/region_map.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_001348` for the `access cleanup` scenario `yonder-glade-0674`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Transform `tables/source_records.csv` using `tables/region_map.json`. Keep only active rows with `units * unit_cost >= 119`, uppercase each id, map regions to zones, sort by zone then id, and report how many malformed rows were skipped.

Scenario-specific audit anchors: tukiwow bawogux fokibay bacepoz kidiyaa zesabab hawopoc gurifod cedirie hamenaf tucelug lujowoh jofovei lubapoj risavek yafopol powotum kiguhan pokimeo tuwopop tufojoq didihar vevehas riyayat cetukiu tulupov meguhaw zebatux yatukiy hameriz mebawoa narihab jobapoc cepowod riyavee ponayaf luludig kimekih gujozei rihakij nayadik narinal tuhacem bagumen batukio hahabap fobabaq navenar hafomes cedipot cewoveu vepokiv lulusaw bagurix kipobay luveyaz hafotua bacetub hazeric cepokid cefodie lumetuf nazetug tusakih nafovei fovehaj yadiyak dicegul nadijom bapoyan cedisao ripotup mesaceq zemefor fofoces dipofot focetuu dilufov fobayaw mediwox jofotuy rilusaz fopojoa wovemeb zerifoc vewoved nabarie gufowof dihayag kijorih menawoi rikijoj tuwoyak gudisal tuyacem yanazen.

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
Before finishing, verify that the output agrees with the relevant fixture files and record the check in `verification`.

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
EXPECTED_OUTPUT = {'result': {'threshold': 119, 'records': [{'id': 'YON-001', 'zone': 'zone_1', 'total_value': 200}, {'id': 'YON-002', 'zone': 'zone_2', 'total_value': 403}, {'id': 'YON-007', 'zone': 'zone_2', 'total_value': 308}, {'id': 'YON-008', 'zone': 'zone_3', 'total_value': 140}], 'total_value': 1051, 'malformed_rows_skipped': 0}, 'evidence': ['tables/source_records.csv', 'tables/region_map.json'], 'verification': {'checked_files': 2, 'malformed_rows_skipped': 0, 'status': 'pass'}}

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
