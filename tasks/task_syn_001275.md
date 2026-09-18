---
id: "task_syn_001275"
name: "Structured table normalization 001275"
capability_family: "structured_data_transformation"
intended_difficulty_band: 5
grading_type: "automated"
timeout_seconds: 270
base_scenario_id: "scenario_000638"
generator_seed: 777175
workspace_files: ["assets/task_syn_001275/workspace/tables/source_records.csv", "assets/task_syn_001275/workspace/tables/region_map.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_001275` for the `training roster` scenario `onyx-xenial-0638`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Transform `tables/source_records.csv` using `tables/region_map.json`. Keep only active rows with `units * unit_cost >= 145`, uppercase each id, map regions to zones, sort by zone then id, and report how many malformed rows were skipped.

Scenario-specific audit anchors: nariveb fotuwoc rizebad zevewoe zenadif luvekig cejosah divetui yatuvej mevefok mebatul wogugum dijonan wogumeo womecep vekiguq fowowor meworis ridihat gutuveu lulufov gudipow luguyax poyavey tusacez jozekia tunameb kisatuc rijofod yamepoe nawozef foyabag luwoceh cebacei safobaj diwoyak gukipol hamegum tukiyan rihario tutuzep luhafoq joyamer dijolus gudifot wobasau tucenav zetucew yafosax vepoguy dibapoz podikia joposab cepodic lurilud yapopoe bakizef ludikig dihakih namevei pometuj wodiluk nahayal yalusam dicezen mezeceo nafopop fonazeq sanatur sakinas vesacet pomeyau veceyav wohaluw zesatux zejovey jowohaz dinazea dikisab guzeluc jofokid ribamee kijodif yahanag fokiluh haritui lufoguj hazetuk nacecel megucem tuyagun lutuzeo sarivep najokiq cemeyar yakiwos.

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
Some supplied information is intentionally irrelevant; exclude it from the result.

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
EXPECTED_OUTPUT = {'result': {'threshold': 145, 'records': [{'id': 'ONY-002', 'zone': 'zone_1', 'total_value': 192}, {'id': 'ONY-008', 'zone': 'zone_2', 'total_value': 288}, {'id': 'ONY-004', 'zone': 'zone_3', 'total_value': 238}, {'id': 'ONY-005', 'zone': 'zone_4', 'total_value': 476}, {'id': 'ONY-010', 'zone': 'zone_4', 'total_value': 375}], 'total_value': 1569, 'malformed_rows_skipped': 0}, 'evidence': ['tables/source_records.csv', 'tables/region_map.json'], 'verification': {'checked_files': 2, 'malformed_rows_skipped': 0, 'status': 'pass'}}

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
