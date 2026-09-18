---
id: "task_syn_002690"
name: "Active file manifest 002690"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "automated"
timeout_seconds: 270
base_scenario_id: "scenario_001345"
generator_seed: 829530
workspace_files: ["assets/task_syn_002690/workspace/incoming/archive/tundra_onyx_1345_00.cfg", "assets/task_syn_002690/workspace/incoming/active/tundra_onyx_1345_01.md", "assets/task_syn_002690/workspace/incoming/active/tundra_onyx_1345_02.json", "assets/task_syn_002690/workspace/incoming/active/tundra_onyx_1345_03.md", "assets/task_syn_002690/workspace/incoming/archive/tundra_onyx_1345_04.md", "assets/task_syn_002690/workspace/incoming/active/tundra_onyx_1345_05.txt", "assets/task_syn_002690/workspace/incoming/active/tundra_onyx_1345_06.log", "assets/task_syn_002690/workspace/incoming/active/tundra_onyx_1345_07.txt", "assets/task_syn_002690/workspace/incoming/archive/tundra_onyx_1345_08.cfg", "assets/task_syn_002690/workspace/incoming/active/tundra_onyx_1345_09.json", "assets/task_syn_002690/workspace/incoming/active/tundra_onyx_1345_10.md", "assets/task_syn_002690/workspace/incoming/active/tundra_onyx_1345_11.log", "assets/task_syn_002690/workspace/incoming/archive/distractor_002690.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_002690` for the `knowledge-base upkeep` scenario `tundra-onyx-1345`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: luguvem sasajon dimemeo cememep jodimeq vezecer nadibas kikirit sazediu pozemev wofoguw kiwofox nacediy zedidiz fowolua wovemeb mejotuc yabalud zenague zeyakif zeyazeg pozezeh savemei ceyajoj ludibak pogupol dihayam yacejon tujohao wocerip navenaq guwobar sakihas disavet riwomeu yawokiv yarisaw wobavex nanazey luriyaz zeditua jowoveb fohawoc povenad kicelue lupokif fodisag jojowoh kizemei zecebaj gunafok yaluril poguyam gujosan dirihao mecejop yayaveq mehajor cedipos gupogut kiposau fojojov jocevew hasanax luriyay sakiriz sadipoa narikib yacepoc jomepod jolunae zeluluf jorizeg dikiluh luhawoi gupotuj bavecek kitubal zebakim cevenan tudipoo folupop luguyaq fodiver yajofos merigut wohatuu risatuv jonadiw cecebax nasasay vebabaz wocesaa tutuyab zedicec luverid.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'txt', 'minimum_bytes': 59, 'selected_files': ['incoming/active/tundra_onyx_1345_05.txt', 'incoming/active/tundra_onyx_1345_07.txt'], 'active_extension_counts': {'json': 2, 'log': 2, 'md': 3, 'txt': 2}, 'largest_active_file': {'path': 'incoming/active/tundra_onyx_1345_11.log', 'bytes': 215}}, 'evidence': ['incoming/active/tundra_onyx_1345_01.md', 'incoming/active/tundra_onyx_1345_02.json', 'incoming/active/tundra_onyx_1345_03.md', 'incoming/active/tundra_onyx_1345_05.txt'], 'verification': {'checked_files': 13, 'ignored_archive': True, 'status': 'pass'}}

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
