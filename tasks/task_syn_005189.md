---
id: "task_syn_005189"
name: "Quantitative reading summary 005189"
capability_family: "statistical_quantitative_analysis"
intended_difficulty_band: 4
grading_type: "hybrid"
timeout_seconds: 240
base_scenario_id: "scenario_002595"
generator_seed: 921993
workspace_files: ["assets/task_syn_005189/workspace/measurements/readings.csv"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_005189` for the `training roster` scenario `violet-keystone-2595`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130.

Scenario-specific audit anchors: riririp fonadiq sapotur difokis digunat kiluveu tuluhav nanacew lunawox sajoluy hagudiz fozenaa bakibab mekinac naveced bafopoe woworif gumeveg gufowoh kiyacei zesayaj diriguk kiwozel rivebam yasakin wokirio nakipop sajoveq podifor vevelus dikisat sapotuu cenajov gubamew bazegux venanay satukiz jopovea gukibab vedidic tuwofod ludirie mefobaf navewog jojonah bahayai woyahaj narijok hacejol poyarim tukiban diveceo poponap kiveyaq cebakir ludisas yapogut wolumeu kijoguv kilucew luvezex riluguy medikiz yanaria basajob fotuyac sasadid fovesae hamejof jocegug poluveh joyagui wojonaj sarituk zenapol tukizem lutugun jozetuo turitup wopozeq lugusar fodives joforit ceyawou diceriv wogufow gurimex mepopoy yajoyaz wokizea vemesab rituric badiyad tuvefoe gutuyaf zeworig.

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
EXPECTED_OUTPUT = {'result': {'count': 17, 'mean': 56.47, 'median': 59.0, 'weighted_mean': 57.83, 'group_means': {'alpha': 55.4, 'beta': 47.5, 'delta': 58.75, 'gamma': 64.5}, 'outlier_ids': []}, 'evidence': ['measurements/readings.csv'], 'verification': {'checked_files': 1, 'ignored_distractors': False, 'status': 'pass'}}

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

Capability focus: `statistical_quantitative_analysis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
