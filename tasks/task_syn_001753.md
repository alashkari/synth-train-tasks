---
id: "task_syn_001753"
name: "Active file manifest 001753"
capability_family: "file_directory_operations"
intended_difficulty_band: 3
grading_type: "automated"
timeout_seconds: 210
base_scenario_id: "scenario_000877"
generator_seed: 794861
workspace_files: ["assets/task_syn_001753/workspace/incoming/archive/tundra_quartz_0877_00.cfg", "assets/task_syn_001753/workspace/incoming/active/tundra_quartz_0877_01.txt", "assets/task_syn_001753/workspace/incoming/active/tundra_quartz_0877_02.log", "assets/task_syn_001753/workspace/incoming/active/tundra_quartz_0877_03.log", "assets/task_syn_001753/workspace/incoming/archive/tundra_quartz_0877_04.cfg", "assets/task_syn_001753/workspace/incoming/active/tundra_quartz_0877_05.cfg", "assets/task_syn_001753/workspace/incoming/active/tundra_quartz_0877_06.md", "assets/task_syn_001753/workspace/incoming/active/tundra_quartz_0877_07.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_001753` for the `customer migration` scenario `tundra-quartz-0877`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the customer migration workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.md` whose byte length is at least 45, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: ripozel rihapom wolumen yaluzeo jomevep wovefoq vevesar jogubas fotugut sasariu sadivev nakibaw wobasax joyatuy lupotuz cedikia fokisab josadic dibatud dikizee kikivef zewosag sameyah tukijoi zeririj dipoyak gukilul yazebam cejokin memeceo zetuyap vegumeq melurir tufodis yazeyat pomeluu vejotuv saricew luhabax dihavey kimeluz meriria lubajob kiwotuc pokikid jodikie nacejof wopomeg banadih zefogui mekicej wojozek potuhal tuhatum yacetun badirio zeyarip cediluq yabagur dibagus tuyasat gupopou tugukiv gulubaw pobadix zefocey fojoluz fodivea foguzeb luluhac vesasad gupogue jorivef fojoyag jovetuh jowowoi guririj johajok jonagul zericem yasadin mekipoo wojolup fotuceq kihasar zecemes dihahat hatudiu hahabav jodinaw bazerix woyatuy kizediz pofobaa lupofob napozec.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'md', 'minimum_bytes': 45, 'selected_files': ['incoming/active/tundra_quartz_0877_06.md'], 'active_extension_counts': {'cfg': 1, 'json': 1, 'log': 2, 'md': 1, 'txt': 1}, 'largest_active_file': {'path': 'incoming/active/tundra_quartz_0877_07.json', 'bytes': 171}}, 'evidence': ['incoming/active/tundra_quartz_0877_01.txt', 'incoming/active/tundra_quartz_0877_02.log', 'incoming/active/tundra_quartz_0877_03.log', 'incoming/active/tundra_quartz_0877_05.cfg'], 'verification': {'checked_files': 8, 'ignored_archive': True, 'status': 'pass'}}

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
