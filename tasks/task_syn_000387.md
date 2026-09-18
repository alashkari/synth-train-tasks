---
id: "task_syn_000387"
name: "Structured table normalization 000387"
capability_family: "structured_data_transformation"
intended_difficulty_band: 2
grading_type: "automated"
timeout_seconds: 180
base_scenario_id: "scenario_000194"
generator_seed: 744319
workspace_files: ["assets/task_syn_000387/workspace/tables/source_records.csv", "assets/task_syn_000387/workspace/tables/region_map.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_000387` for the `customer migration` scenario `mosaic-brisk-0194`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Transform `tables/source_records.csv` using `tables/region_map.json`. Keep only active rows with `units * unit_cost >= 106`, uppercase each id, map regions to zones, sort by zone then id, and report how many malformed rows were skipped.

Scenario-specific audit anchors: bacepox dinasay wobadiz mekibaa guzeveb tuzefoc fozekid cefoyae bamehaf riyanag zenazeh sapofoi sapopoj wosajok gurimel mejofom gumekin cetumeo vehavep pozehaq jozeyar haceris mehalut baguyau nazeguv najoguw zeyajox nakiluy wozenaz fogufoa tucenab ludihac veharid zekibae hayacef lucegug jofoveh tucejoi mebapoj jocepok rigunal tumecem nayatun jotutuo ceribap woyajoq gucesar bamegus vezekit rituveu mekisav zejozew fosabax hajobay pogumez wowomea disajob tuzeluc wozeced disamee nadibaf nayaveg pomesah vehadii vemehaj lutufok gugutul rijobam tulufon potumeo vegurip nagumeq dikijor kikitus hacelut bajoyau difopov saluzew basadix jovetuy lutuhaz ricecea baritub yadiguc risafod forikie pocejof luzeceg polupoh yalufoi ludizej celukik savepol yayacem mepoven lufoluo.

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
EXPECTED_OUTPUT = {'result': {'threshold': 106, 'records': [{'id': 'MOS-001', 'zone': 'zone_1', 'total_value': 162}, {'id': 'MOS-008', 'zone': 'zone_3', 'total_value': 140}, {'id': 'MOS-004', 'zone': 'zone_4', 'total_value': 130}, {'id': 'MOS-005', 'zone': 'zone_5', 'total_value': 312}], 'total_value': 744, 'malformed_rows_skipped': 1}, 'evidence': ['tables/source_records.csv', 'tables/region_map.json'], 'verification': {'checked_files': 2, 'malformed_rows_skipped': 1, 'status': 'pass'}}

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
