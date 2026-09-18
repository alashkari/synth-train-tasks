---
id: "task_syn_003362"
name: "Active file manifest 003362"
capability_family: "file_directory_operations"
intended_difficulty_band: 2
grading_type: "automated"
timeout_seconds: 180
base_scenario_id: "scenario_001681"
generator_seed: 854394
workspace_files: ["assets/task_syn_003362/workspace/incoming/archive/ripple_delta_1681_00.cfg", "assets/task_syn_003362/workspace/incoming/active/ripple_delta_1681_01.txt", "assets/task_syn_003362/workspace/incoming/active/ripple_delta_1681_02.txt", "assets/task_syn_003362/workspace/incoming/active/ripple_delta_1681_03.log", "assets/task_syn_003362/workspace/incoming/archive/ripple_delta_1681_04.log", "assets/task_syn_003362/workspace/incoming/active/ripple_delta_1681_05.md", "assets/task_syn_003362/workspace/incoming/active/ripple_delta_1681_06.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_003362` for the `billing review` scenario `ripple-delta-1681`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the billing review workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.cfg` whose byte length is at least 38, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: savevei bajorij sasajok nacecel gugujom veyapon nakiguo cevewop gubadiq jocever cedihas jozelut vepoluu tutucev baguluw posawox gugubay guyavez pofopoa jojohab zevenac navetud cejohae dipowof luyayag fonaveh hawoyai dilukij sayacek sapotul kipomem yaluban yatusao hatudip ceyaveq baguwor polutus meludit vebatuu hajowov wozecew yavepox nacefoy fobadiz zeyamea tukibab kimecec kinagud kicehae satusaf wobayag rivebah kikijoi tumevej hakiguk yajojol kicejom cetutun gupopoo vefojop cesafoq babafor venabas zeyarit pobayau fozecev tubaluw vedikix fohazey gusanaz vevewoa yafoyab bagutuc yagunad ponabae josayaf bacejog jovesah potunai veposaj ceguluk kilunal dihaham popokin namejoo savedip yagumeq risanar diluces gunarit hajoceu wohafov hahapow foriwox zeribay tuhacez.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'cfg', 'minimum_bytes': 38, 'selected_files': [], 'active_extension_counts': {'log': 1, 'md': 2, 'txt': 2}, 'largest_active_file': {'path': 'incoming/active/ripple_delta_1681_06.md', 'bytes': 154}}, 'evidence': ['incoming/active/ripple_delta_1681_01.txt', 'incoming/active/ripple_delta_1681_02.txt', 'incoming/active/ripple_delta_1681_03.log', 'incoming/active/ripple_delta_1681_05.md'], 'verification': {'checked_files': 7, 'ignored_archive': True, 'status': 'pass'}}

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
