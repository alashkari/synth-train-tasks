---
id: "task_syn_002714"
name: "Active file manifest 002714"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_001357"
generator_seed: 830418
workspace_files: ["assets/task_syn_002714/workspace/incoming/archive/frost_ember_1357_00.md", "assets/task_syn_002714/workspace/incoming/active/frost_ember_1357_01.txt", "assets/task_syn_002714/workspace/incoming/active/frost_ember_1357_02.json", "assets/task_syn_002714/workspace/incoming/active/frost_ember_1357_03.json", "assets/task_syn_002714/workspace/incoming/archive/frost_ember_1357_04.md", "assets/task_syn_002714/workspace/incoming/active/frost_ember_1357_05.json", "assets/task_syn_002714/workspace/incoming/active/frost_ember_1357_06.txt", "assets/task_syn_002714/workspace/incoming/active/frost_ember_1357_07.md", "assets/task_syn_002714/workspace/incoming/archive/frost_ember_1357_08.md", "assets/task_syn_002714/workspace/incoming/active/frost_ember_1357_09.json", "assets/task_syn_002714/workspace/incoming/active/frost_ember_1357_10.cfg"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_002714` for the `access cleanup` scenario `frost-ember-1357`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: vegudik divekil kidimem wosadin powoguo gudicep riyahaq rijopor sarifos vekidit diluluu sanavev zevejow gujorix mezecey tuzediz yahahaa foturib zevecec kiyawod fobatue zevehaf sajolug menapoh lusanai tumebaj zejodik menacel cediham mezegun kicenao kihamep bazetuq fovenar wobakis yabasat luyaveu vejokiv vemeyaw fopolux woveyay kibayaz vehagua vedisab bahadic risazed hawopoe zejoluf hazeceg digudih kihanai difocej navenak yacebal pobalum wowosan diponao tuyatup jojojoq dikisar vewofos batukit fovebau kikimev luwonaw lumevex cesasay cezefoz luyajoa bamedib vefojoc yafojod jolulue kihanaf dipopog rimewoh wopoyai hamedij tuyavek luluyal kiharim tuluzen bakikio hanafop nakizeq sajodir sazejos mejorit hajoceu badizev tukijow fopowox yafowoy pogupoz yapovea ceridib.

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
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/frost_ember_1357_02.json', 'incoming/active/frost_ember_1357_03.json', 'incoming/active/frost_ember_1357_05.json', 'incoming/active/frost_ember_1357_09.json'], 'active_extension_counts': {'cfg': 1, 'json': 4, 'md': 1, 'txt': 2}, 'largest_active_file': {'path': 'incoming/active/frost_ember_1357_10.cfg', 'bytes': 196}}, 'evidence': ['incoming/active/frost_ember_1357_01.txt', 'incoming/active/frost_ember_1357_02.json', 'incoming/active/frost_ember_1357_03.json', 'incoming/active/frost_ember_1357_05.json'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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
