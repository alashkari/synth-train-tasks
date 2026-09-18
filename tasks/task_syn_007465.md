---
id: "task_syn_007465"
name: "Active file manifest 007465"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "automated"
timeout_seconds: 270
base_scenario_id: "scenario_003733"
generator_seed: 1006205
workspace_files: ["assets/task_syn_007465/workspace/incoming/archive/prairie_onyx_3733_00.cfg", "assets/task_syn_007465/workspace/incoming/active/prairie_onyx_3733_01.json", "assets/task_syn_007465/workspace/incoming/active/prairie_onyx_3733_02.json", "assets/task_syn_007465/workspace/incoming/active/prairie_onyx_3733_03.cfg", "assets/task_syn_007465/workspace/incoming/archive/prairie_onyx_3733_04.cfg", "assets/task_syn_007465/workspace/incoming/active/prairie_onyx_3733_05.cfg", "assets/task_syn_007465/workspace/incoming/active/prairie_onyx_3733_06.cfg", "assets/task_syn_007465/workspace/incoming/active/prairie_onyx_3733_07.json", "assets/task_syn_007465/workspace/incoming/archive/prairie_onyx_3733_08.json", "assets/task_syn_007465/workspace/incoming/active/prairie_onyx_3733_09.json", "assets/task_syn_007465/workspace/incoming/archive/distractor_007465.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007465` for the `knowledge-base upkeep` scenario `prairie-onyx-3733`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: tutuved zepokie saluzef yatujog gumerih tuwohai tugubaj woyavek wopokil dihasam kimeban gukiyao hapokip mecehaq tuluver vewobas kiluvet tubazeu luludiv jomemew wojobax luzejoy samefoz cemekia zevewob mebapoc ricemed risajoe guvehaf fojodig rizerih ditujoi fobaguj jofotuk cewolul sazefom worilun lunabao bakimep melujoq poyapor jowodis hanavet vepopou cezesav zerikiw cetucex hapoluy vesamez lumepoa tufoveb jovecec kijosad bayague riguluf poguhag cepohah womerii mefopoj sayajok sazesal mefotum joveven rikibao yawocep zetuzeq tuhaver pomepos cetujot gumewou zehaguv bahamew vejowox jovefoy jomeyaz meveyaa pojomeb luharic kimedid najogue tuzesaf posalug satufoh meditui vesatuj meveluk guritul dipotum wosacen yacetuo wosavep saveluq havelur rizejos halujot yavepou.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'txt', 'minimum_bytes': 59, 'selected_files': [], 'active_extension_counts': {'cfg': 3, 'json': 4}, 'largest_active_file': {'path': 'incoming/active/prairie_onyx_3733_09.json', 'bytes': 201}}, 'evidence': ['incoming/active/prairie_onyx_3733_01.json', 'incoming/active/prairie_onyx_3733_02.json', 'incoming/active/prairie_onyx_3733_03.cfg', 'incoming/active/prairie_onyx_3733_05.cfg'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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
