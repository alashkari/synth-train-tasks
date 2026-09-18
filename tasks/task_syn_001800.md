---
id: "task_syn_001800"
name: "Multi-artifact triage plan 001800"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 5
grading_type: "automated"
timeout_seconds: 270
base_scenario_id: "scenario_000900"
generator_seed: 796600
workspace_files: ["assets/task_syn_001800/workspace/triage/tickets.csv", "assets/task_syn_001800/workspace/triage/scoring.json", "assets/task_syn_001800/workspace/triage/events.log"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_001800` for the `access cleanup` scenario `quartz-amber-0900`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: kigurig fosakih dipobai riverij kisarik foyapol bayavem cetuzen diverio lupomep yatufoq gubayar sayagus tuponat samezeu hanabav powonaw cewopox haluzey lupovez fonanaa cesazeb pomedic havedid tugusae fojohaf luhagug gucemeh zegunai rifosaj kinabak veposal diposam vebajon cenajoo bazelup sabaluq hasajor medijos yahanat ririluu mekivev wopotuw joluhax lumesay didituz zezefoa fonawob dihazec dibapod zezelue hawoyaf vehameg wohadih vejopoi mecetuj luzevek dirijol dibavem mesakin nawojoo sanavep nakijoq guriver yaluyas zepogut zebanau tusamev hasajow wofozex kicenay tujoguz batufoa focewob dinamec foturid nadizee dijovef guceyag dikiluh barivei zelufoj wowocek pozedil podirim jozerin vepotuo zezesap tufokiq kimesar rikifos hajowot gunahau gusapov vegupow sapoyax.

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
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.
Some supplied information is intentionally irrelevant; exclude it from the result.
Some fixture labels use Spanish words such as accion, riesgo, and resumen; normalize the final JSON keys in English.
This task may require continuing context across multiple session files.

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
EXPECTED_OUTPUT = {'result': {'priority_order': [{'ticket': 'T001800-2', 'owner': 'cam', 'priority_score': 3}, {'ticket': 'T001800-5', 'owner': 'bea', 'priority_score': 3}, {'ticket': 'T001800-1', 'owner': 'bea', 'priority_score': 2}, {'ticket': 'T001800-7', 'owner': 'dev', 'priority_score': 2}, {'ticket': 'T001800-8', 'owner': 'ari', 'priority_score': 2}, {'ticket': 'T001800-3', 'owner': 'dev', 'priority_score': 1}, {'ticket': 'T001800-4', 'owner': 'ari', 'priority_score': 1}, {'ticket': 'T001800-6', 'owner': 'cam', 'priority_score': 1}, {'ticket': 'T001800-0', 'owner': 'ari', 'priority_score': 0}], 'blocked_tickets': ['T001800-0', 'T001800-4', 'T001800-8'], 'malformed_events_skipped': 1}, 'evidence': ['triage/tickets.csv', 'triage/scoring.json', 'triage/events.log'], 'verification': {'checked_files': 3, 'status': 'pass'}}

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
