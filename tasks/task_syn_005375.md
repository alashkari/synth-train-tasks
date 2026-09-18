---
id: "task_syn_005375"
name: "Multi-artifact triage plan 005375"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 5
grading_type: "hybrid"
timeout_seconds: 270
base_scenario_id: "scenario_002688"
generator_seed: 928875
workspace_files: ["assets/task_syn_005375/workspace/triage/tickets.csv", "assets/task_syn_005375/workspace/triage/scoring.json", "assets/task_syn_005375/workspace/triage/events.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_005375` for the `access cleanup` scenario `keystone-violet-2688`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: yafobat merijou porivev kitudiw luhanax hacejoy hazeguz josajoa kiluveb sazesac megusad vebasae cekihaf ridizeg yayahah gutunai fosabaj tufowok yaguvel mepopom lukirin tujomeo jowovep bacekiq mecelur balunas mecekit zeluveu tugubav kivehaw tulubax bagusay kiforiz kihakia fodipob kijoguc samerid tudinae bazevef saludig johayah babafoi tukipoj fozewok tuwotul dimejom celucen dikituo hatukip vezeyaq kibagur zezemes hacetut tupopou bafobav gufojow kitujox basadiy nazehaz tuyasaa zelubab namekic tujofod potulue joluguf pozetug fogupoh mepomei habapoj megupok kivefol wowodim sasapon havesao haforip rizekiq pozefor pozeris havemet woyabau wowonav zeyanaw ricejox hasafoy pojoyaz hanazea yabapob fomemec bamedid difohae tufoluf zenatug zeguyah kigunai wokisaj cebadik.

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
- Judge review: Assess clarity, traceability, and whether the response avoids unsupported assumptions.

# Automated Checks

```python
from pathlib import Path
import json

CRITERIA = ['format_valid', 'answer_correct', 'evidence_grounded', 'verification_complete']
EXPECTED_OUTPUT = {'result': {'priority_order': [{'ticket': 'T005375-2', 'owner': 'cam', 'priority_score': 3}, {'ticket': 'T005375-5', 'owner': 'bea', 'priority_score': 3}, {'ticket': 'T005375-1', 'owner': 'bea', 'priority_score': 2}, {'ticket': 'T005375-7', 'owner': 'dev', 'priority_score': 2}, {'ticket': 'T005375-8', 'owner': 'ari', 'priority_score': 2}, {'ticket': 'T005375-3', 'owner': 'dev', 'priority_score': 1}, {'ticket': 'T005375-4', 'owner': 'ari', 'priority_score': 1}, {'ticket': 'T005375-6', 'owner': 'cam', 'priority_score': 1}, {'ticket': 'T005375-0', 'owner': 'ari', 'priority_score': 0}], 'blocked_tickets': ['T005375-0', 'T005375-4', 'T005375-8'], 'malformed_events_skipped': 0}, 'evidence': ['triage/tickets.csv', 'triage/scoring.json', 'triage/events.log'], 'verification': {'checked_files': 3, 'status': 'pass'}}

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

Capability focus: `multi_tool_workflow_orchestration`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
