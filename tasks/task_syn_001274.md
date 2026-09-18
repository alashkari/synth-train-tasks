---
id: "task_syn_001274"
name: "Active file manifest 001274"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_000637"
generator_seed: 777138
workspace_files: ["assets/task_syn_001274/workspace/incoming/archive/nimbus_juniper_0637_00.cfg", "assets/task_syn_001274/workspace/incoming/active/nimbus_juniper_0637_01.json", "assets/task_syn_001274/workspace/incoming/active/nimbus_juniper_0637_02.txt", "assets/task_syn_001274/workspace/incoming/active/nimbus_juniper_0637_03.log", "assets/task_syn_001274/workspace/incoming/archive/nimbus_juniper_0637_04.cfg", "assets/task_syn_001274/workspace/incoming/active/nimbus_juniper_0637_05.txt", "assets/task_syn_001274/workspace/incoming/active/nimbus_juniper_0637_06.json", "assets/task_syn_001274/workspace/incoming/active/nimbus_juniper_0637_07.txt", "assets/task_syn_001274/workspace/incoming/archive/nimbus_juniper_0637_08.md", "assets/task_syn_001274/workspace/incoming/active/nimbus_juniper_0637_09.txt", "assets/task_syn_001274/workspace/incoming/active/nimbus_juniper_0637_10.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_001274` for the `access cleanup` scenario `nimbus-juniper-0637`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: zesakia ridisab zecenac bahaced yalujoe nayakif nakitug mesahah bahamei ceyabaj fodirik naluzel riridim veyagun fogutuo sagufop luwotuq gugumer veyames ricebat vefoveu meriwov baridiw tukiwox lupotuy jopovez jorinaa vezegub fotuyac cefonad saripoe pohatuf pocegug mepoluh wofokii disapoj jodirik saluril mekiham zevemen risaceo bacebap hakikiq jorinar rivehas tubahat powotuu nagukiv haguwow fozeyax mefozey hajoguz guvecea yavenab rikimec riyawod lunayae tuguhaf kilufog babameh ribazei tuluguj dizerik saguyal woyapom ludikin napokio nazevep kibasaq yaceyar fokidis ritujot jobariu wogudiv jocebaw digumex menanay hafotuz yasapoa haceceb vezetuc nazemed yafohae mefojof jocehag jonajoh yamesai cehaluj wopofok wonamel cepovem kiluban yakihao melupop jomeceq havepor.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/nimbus_juniper_0637_01.json', 'incoming/active/nimbus_juniper_0637_06.json'], 'active_extension_counts': {'json': 2, 'log': 1, 'md': 1, 'txt': 4}, 'largest_active_file': {'path': 'incoming/active/nimbus_juniper_0637_10.md', 'bytes': 199}}, 'evidence': ['incoming/active/nimbus_juniper_0637_01.json', 'incoming/active/nimbus_juniper_0637_02.txt', 'incoming/active/nimbus_juniper_0637_03.log', 'incoming/active/nimbus_juniper_0637_05.txt'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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
