---
id: "task_syn_004370"
name: "Active file manifest 004370"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "automated"
timeout_seconds: 270
base_scenario_id: "scenario_002185"
generator_seed: 891690
workspace_files: ["assets/task_syn_004370/workspace/incoming/archive/brisk_violet_2185_00.log", "assets/task_syn_004370/workspace/incoming/active/brisk_violet_2185_01.txt", "assets/task_syn_004370/workspace/incoming/active/brisk_violet_2185_02.log", "assets/task_syn_004370/workspace/incoming/active/brisk_violet_2185_03.log", "assets/task_syn_004370/workspace/incoming/archive/brisk_violet_2185_04.log", "assets/task_syn_004370/workspace/incoming/active/brisk_violet_2185_05.cfg", "assets/task_syn_004370/workspace/incoming/active/brisk_violet_2185_06.cfg", "assets/task_syn_004370/workspace/incoming/active/brisk_violet_2185_07.json", "assets/task_syn_004370/workspace/incoming/archive/brisk_violet_2185_08.log", "assets/task_syn_004370/workspace/incoming/active/brisk_violet_2185_09.txt", "assets/task_syn_004370/workspace/incoming/active/brisk_violet_2185_10.md", "assets/task_syn_004370/workspace/incoming/active/brisk_violet_2185_11.log", "assets/task_syn_004370/workspace/incoming/archive/distractor_004370.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_004370` for the `knowledge-base upkeep` scenario `brisk-violet-2185`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: cejonac diveved mehazee womepof nabasag naceveh sanamei jopovej guyavek luyajol vedisam cefopon rikiguo tuworip pokiguq vebarir potufos nadihat savebau vesajov diwojow nasarix wokiguy kibayaz bajozea luhabab vevepoc verimed hayadie popofof tutubag ceceluh tusajoi badifoj mehaluk lupovel kiguwom cevegun luwofoo porivep turimeq guzedir yapowos zenabat joludiu meluvev zeyajow mevemex mesadiy sagutuz yapowoa vezewob pocefoc sacenad dihajoe joyazef kidigug lunayah luvenai sawobaj lugubak dijohal ritucem vetucen badiveo rimeyap guzeluq lurihar pofosas pobanat hafojou zefohav cefocew nadidix lujobay ditudiz pokinaa jocezeb ditubac fosaced fohafoe rinanaf yaripog cetukih zericei gupowoj fofofok zehazel mehajom vewozen kirisao worinap yavetuq worisar kivelus didifot.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'txt', 'minimum_bytes': 59, 'selected_files': ['incoming/active/brisk_violet_2185_01.txt', 'incoming/active/brisk_violet_2185_09.txt'], 'active_extension_counts': {'cfg': 2, 'json': 1, 'log': 3, 'md': 1, 'txt': 2}, 'largest_active_file': {'path': 'incoming/active/brisk_violet_2185_11.log', 'bytes': 216}}, 'evidence': ['incoming/active/brisk_violet_2185_01.txt', 'incoming/active/brisk_violet_2185_02.log', 'incoming/active/brisk_violet_2185_03.log', 'incoming/active/brisk_violet_2185_05.cfg'], 'verification': {'checked_files': 13, 'ignored_archive': True, 'status': 'pass'}}

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
