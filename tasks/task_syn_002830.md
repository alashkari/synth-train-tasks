---
id: "task_syn_002830"
name: "Context continuation update 002830"
capability_family: "memory_retrieval_context_continuation"
intended_difficulty_band: 5
grading_type: "automated"
timeout_seconds: 270
base_scenario_id: "scenario_001415"
generator_seed: 834710
workspace_files: ["assets/task_syn_002830/workspace/sessions/session_log.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_002830` for the `customer migration` scenario `lumen-zenith-1415`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read the session log file or files under `sessions/` and produce a context-continuation update. Separate durable preferences, current state, and stale items.

Scenario-specific audit anchors: dizesaw yalutux lujotuy tumediz sasakia mevepob dibafoc yanaved luhadie tudinaf cezegug mevemeh bahanai vetuwoj tudituk mehahal cemerim nazeban pokibao powonap dikituq fodisar tulujos sarisat kihayau fowozev merimew bamefox vejozey meveluz dididia yanatub lujobac jonawod hayakie yahaluf ludimeg yasayah vetutui rijopoj polufok wofonal jokiyam rigudin yadijoo ponahap yabatuq mepozer kihazes zeluhat dituhau riyavev polubaw najohax gugucey lusavez yabaria lujoyab cecezec nayakid hayacee kigupof savefog zeluzeh sayalui jomekij jokimek zememel jovesam rilupon rifoluo kivegup kibakiq vezekir savejos disamet harihau nameriv vebaguw diluwox habanay yaguluz luguhaa tunameb yadiwoc yadilud ricelue megumef wokiwog yabarih jopodii veluguj vehanak focejol wovetum jorinan.

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
EXPECTED_OUTPUT = {'result': {'durable_preferences': ['prefers summaries grouped by frost', 'wants checkpoint files named lumen_zenith_1415_checkpoint'], 'current_state': ['waiting on owner zenith', 'next review covers batch 7'], 'stale_items': ['old reminder about trial import']}, 'evidence': ['session_log.md'], 'verification': {'checked_files': 1, 'multi_session': False, 'status': 'pass'}}

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
