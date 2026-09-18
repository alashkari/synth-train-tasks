---
id: "task_syn_004655"
name: "Multi-artifact triage plan 004655"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 5
grading_type: "hybrid"
timeout_seconds: 270
base_scenario_id: "scenario_002328"
generator_seed: 902235
workspace_files: ["assets/task_syn_004655/workspace/triage/tickets.csv", "assets/task_syn_004655/workspace/triage/scoring.json", "assets/task_syn_004655/workspace/triage/events.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_004655` for the `access cleanup` scenario `onyx-brisk-2328`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: kicefob pofosac lubahad vepomee digupof vesagug kiyazeh wohajoi mevepoj jojopok nasazel luposam joriwon hamenao ceyavep rinanaq kisapor dicebas wohagut johahau vecenav dikikiw saditux cekicey cevesaz sanasaa turiveb zedibac gupolud gufosae rihamef sajogug luzeyah tuyakii ceridij mesafok nanakil hajobam nayatun hapokio poyarip lunakiq gudifor gufowos pomehat forijou gupomev fofovew nabazex lufohay mezediz tuvewoa hakifob rizekic fofowod hakimee gurizef gumejog kimefoh nawopoi zeposaj cenasak veharil dimetum cewogun navesao tutufop lupoluq riludir hasaces yabarit lukidiu sapodiv nahawow yavecex rijoriy zenamez cekijoa sajozeb hanazec rigujod cegupoe natusaf melufog rijowoh zeluvei woverij tubaguk guyadil nacegum divemen jomefoo yakisap yabatuq yariyar podikis.

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
EXPECTED_OUTPUT = {'result': {'priority_order': [{'ticket': 'T004655-2', 'owner': 'cam', 'priority_score': 3}, {'ticket': 'T004655-5', 'owner': 'bea', 'priority_score': 3}, {'ticket': 'T004655-1', 'owner': 'bea', 'priority_score': 2}, {'ticket': 'T004655-7', 'owner': 'dev', 'priority_score': 2}, {'ticket': 'T004655-8', 'owner': 'ari', 'priority_score': 2}, {'ticket': 'T004655-3', 'owner': 'dev', 'priority_score': 1}, {'ticket': 'T004655-4', 'owner': 'ari', 'priority_score': 1}, {'ticket': 'T004655-6', 'owner': 'cam', 'priority_score': 1}, {'ticket': 'T004655-0', 'owner': 'ari', 'priority_score': 0}], 'blocked_tickets': ['T004655-0', 'T004655-4', 'T004655-8'], 'malformed_events_skipped': 0}, 'evidence': ['triage/tickets.csv', 'triage/scoring.json', 'triage/events.log'], 'verification': {'checked_files': 3, 'status': 'pass'}}

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
