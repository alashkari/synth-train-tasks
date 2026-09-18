---
id: "task_syn_001322"
name: "Active file manifest 001322"
capability_family: "file_directory_operations"
intended_difficulty_band: 2
grading_type: "automated"
timeout_seconds: 180
base_scenario_id: "scenario_000661"
generator_seed: 778914
workspace_files: ["assets/task_syn_001322/workspace/incoming/archive/lumen_zenith_0661_00.md", "assets/task_syn_001322/workspace/incoming/active/lumen_zenith_0661_01.md", "assets/task_syn_001322/workspace/incoming/active/lumen_zenith_0661_02.md", "assets/task_syn_001322/workspace/incoming/active/lumen_zenith_0661_03.log", "assets/task_syn_001322/workspace/incoming/archive/lumen_zenith_0661_04.md", "assets/task_syn_001322/workspace/incoming/active/lumen_zenith_0661_05.log", "assets/task_syn_001322/workspace/incoming/active/lumen_zenith_0661_06.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_001322` for the `billing review` scenario `lumen-zenith-0661`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the billing review workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.cfg` whose byte length is at least 38, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: lufowow venayax melukiy yaluvez sajotua namenab lunasac mehawod mezedie nayawof potufog ponadih rikimei fofohaj sanaguk vefosal ponalum tuwoven cepoluo disayap yarihaq mebabar dimepos bawokit pofoguu zefofov medihaw bayayax hawoyay meridiz ceriria jogulub nabacec banawod bagujoe guvefof tukihag dipomeh fogubai vebafoj zeceyak vedijol nalulum luditun vebakio wocefop wojowoq cefodir ripowos meyawot wosadiu zebawov ponamew vehanax luveyay mekizez polugua guhajob zejoguc gubadid tucemee hakipof bahakig metudih mezeyai tudidij digubak joyayal gufovem fosaban nawokio celutup zemeceq dinamer zebatus wovedit jojodiu kivemev gusaluw lucerix woludiy badituz ririlua tuwowob tuhahac jotuzed lurifoe diguvef kilufog fowoyah dijohai rifosaj kikikik cewonal powonam hatulun.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'cfg', 'minimum_bytes': 38, 'selected_files': [], 'active_extension_counts': {'json': 1, 'log': 2, 'md': 2}, 'largest_active_file': {'path': 'incoming/active/lumen_zenith_0661_06.json', 'bytes': 154}}, 'evidence': ['incoming/active/lumen_zenith_0661_01.md', 'incoming/active/lumen_zenith_0661_02.md', 'incoming/active/lumen_zenith_0661_03.log', 'incoming/active/lumen_zenith_0661_05.log'], 'verification': {'checked_files': 7, 'ignored_archive': True, 'status': 'pass'}}

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
