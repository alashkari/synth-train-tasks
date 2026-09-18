---
id: "task_syn_001944"
name: "Multi-artifact triage plan 001944"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_000972"
generator_seed: 801928
workspace_files: ["assets/task_syn_001944/workspace/triage/tickets.csv", "assets/task_syn_001944/workspace/triage/scoring.json", "assets/task_syn_001944/workspace/triage/events.log"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_001944` for the `customer migration` scenario `keystone-brisk-0972`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: sagupou dibasav woyanaw fotuyax zeguvey saluwoz zefosaa gutuhab cesazec fosafod lusadie cefowof yarijog baporih ricegui nadivej fomewok pobatul dirikim difodin basameo bavepop kimeyaq popokir vejojos lujotut pofoguu pohahav tudivew tuyagux gusacey cerimez fovetua gulugub ririzec joyadid bawokie dimehaf yalunag luwosah kirinai luripoj veluyak folucel yamevem wofonan ripohao zebayap joluriq jopozer fopogus mepocet guhafou tumesav fowotuw woceyax risadiy gukijoz mefodia yagulub turikic jonadid mejolue nafocef luyameg tubanah celudii powosaj podibak hanaril zeguvem bagucen tupokio jokidip veyayaq lupobar gudizes riririt wodiwou rituwov dipofow haribax wotujoy lusasaz mejolua gugutub zecedic gucejod poworie gufoyaf nariyag rivejoh cejovei rifofoj foveguk kidinal.

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
EXPECTED_OUTPUT = {'result': {'priority_order': [{'ticket': 'T001944-2', 'owner': 'cam', 'priority_score': 3}, {'ticket': 'T001944-5', 'owner': 'bea', 'priority_score': 3}, {'ticket': 'T001944-1', 'owner': 'bea', 'priority_score': 2}, {'ticket': 'T001944-7', 'owner': 'dev', 'priority_score': 2}, {'ticket': 'T001944-3', 'owner': 'dev', 'priority_score': 1}, {'ticket': 'T001944-4', 'owner': 'ari', 'priority_score': 1}, {'ticket': 'T001944-6', 'owner': 'cam', 'priority_score': 1}, {'ticket': 'T001944-0', 'owner': 'ari', 'priority_score': 0}], 'blocked_tickets': ['T001944-0', 'T001944-4'], 'malformed_events_skipped': 0}, 'evidence': ['triage/tickets.csv', 'triage/scoring.json', 'triage/events.log'], 'verification': {'checked_files': 3, 'status': 'pass'}}

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
