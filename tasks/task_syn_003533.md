---
id: "task_syn_003533"
name: "Quantitative reading summary 003533"
capability_family: "statistical_quantitative_analysis"
intended_difficulty_band: 3
grading_type: "automated"
timeout_seconds: 210
base_scenario_id: "scenario_001767"
generator_seed: 860721
workspace_files: ["assets/task_syn_003533/workspace/measurements/readings.csv"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_003533` for the `knowledge-base upkeep` scenario `zenith-ripple-1767`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130.

Scenario-specific audit anchors: dijosax yamekiy barivez jowozea kifowob sawohac sawokid mejohae sariwof mepowog cezekih dipowoi jowoyaj yavehak lukitul jobacem tubapon fobaguo lusalup rirituq lutuhar havefos potuzet luposau hajowov kiposaw natuyax tujowoy tuyamez kiyafoa fogurib kitumec guwowod fovevee sazehaf hahalug haceyah hafodii kiwomej nawosak mecewol havetum foposan lubazeo bahawop jofonaq joposar tuzebas jobavet diwowou fokizev tuyajow salupox rigusay vezenaz fopovea potuveb jodikic dituyad rinague luwohaf veridig baguyah hamegui yanaguj salunak lupoyal satudim guverin zemezeo risalup lukisaq tuwobar pozeris tujomet tudihau menacev wotubaw luhadix kigutuy salujoz cenawoa hahameb guzefoc tunalud ludicee guwodif mekirig lufohah nasarii diyabaj saverik gutuyal havesam cemeven wofohao.

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

# Automated Checks

```python
from pathlib import Path
import json

CRITERIA = ['format_valid', 'answer_correct', 'evidence_grounded', 'verification_complete']
EXPECTED_OUTPUT = {'result': {'count': 15, 'mean': 54.07, 'median': 54.0, 'weighted_mean': 54.31, 'group_means': {'alpha': 48.0, 'beta': 65.0, 'delta': 53.75, 'gamma': 48.0}, 'outlier_ids': []}, 'evidence': ['measurements/readings.csv'], 'verification': {'checked_files': 1, 'ignored_distractors': False, 'status': 'pass'}}

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
