---
id: "task_syn_007947"
name: "Structured table normalization 007947"
capability_family: "structured_data_transformation"
intended_difficulty_band: 2
grading_type: "hybrid"
timeout_seconds: 180
base_scenario_id: "scenario_003974"
generator_seed: 1024039
workspace_files: ["assets/task_syn_007947/workspace/tables/source_records.csv", "assets/task_syn_007947/workspace/tables/region_map.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007947` for the `customer migration` scenario `willow-lumen-3974`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Transform `tables/source_records.csv` using `tables/region_map.json`. Keep only active rows with `units * unit_cost >= 106`, uppercase each id, map regions to zones, sort by zone then id, and report how many malformed rows were skipped.

Scenario-specific audit anchors: vewozer nanadis fohatut jojoceu potufov zekikiw disajox celuguy ceworiz gunanaa kimezeb ceceyac johazed venadie fowoguf forimeg cekihah merikii ribapoj sagupok halulul dilukim ditutun safopoo lusacep jotupoq dikizer meguves dinarit dikiluu vefohav lulufow foyatux ricetuy yabajoz dilukia ribafob gumekic wopopod cebague vehacef dibasag yawohah wodisai cevesaj vedihak nazezel nanabam tuvehan worisao najorip jonabaq jocejor cekisas gufotut wopopou jofopov vezekiw meyasax tufobay hatupoz wovecea tujorib fogucec rizedid rivehae tunajof podidig babazeh yakirii nanasaj hazemek pojozel hariyam worihan hahapoo wotukip badituq poyacer foluhas sakizet nagunau jofowov zedituw hahafox ceceriy nawohaz veguzea meforib cejopoc merisad babakie joyajof zenawog fojoyah pozekii.

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
- Judge review: Assess clarity, traceability, and whether the response avoids unsupported assumptions.

# Automated Checks

```python
from pathlib import Path
import json

CRITERIA = ['format_valid', 'answer_correct', 'evidence_grounded', 'verification_complete']
EXPECTED_OUTPUT = {'result': {'threshold': 106, 'records': [{'id': 'WIL-001', 'zone': 'zone_1', 'total_value': 117}, {'id': 'WIL-002', 'zone': 'zone_2', 'total_value': 320}, {'id': 'WIL-007', 'zone': 'zone_2', 'total_value': 238}, {'id': 'WIL-008', 'zone': 'zone_3', 'total_value': 476}, {'id': 'WIL-005', 'zone': 'zone_5', 'total_value': 192}], 'total_value': 1343, 'malformed_rows_skipped': 1}, 'evidence': ['tables/source_records.csv', 'tables/region_map.json'], 'verification': {'checked_files': 2, 'malformed_rows_skipped': 1, 'status': 'pass'}}

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

Judge the submitted artifact using the criteria below. Award credit only for content grounded in the supplied workspace files.

- 1.0: Complete, accurate, well organized, and explicit about evidence and verification.
- 0.7: Mostly correct with a minor omission or weak explanation that does not change the core result.
- 0.4: Partially grounded but misses an important constraint, source, or edge case.
- 0.0: Ungrounded, unusable, unsafe, or dependent on unavailable external data.

Capability focus: `structured_data_transformation`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
