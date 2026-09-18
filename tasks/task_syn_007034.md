---
id: "task_syn_007034"
name: "Active file manifest 007034"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "hybrid"
timeout_seconds: 240
base_scenario_id: "scenario_003517"
generator_seed: 990258
workspace_files: ["assets/task_syn_007034/workspace/incoming/archive/harbor_cedar_3517_00.log", "assets/task_syn_007034/workspace/incoming/active/harbor_cedar_3517_01.cfg", "assets/task_syn_007034/workspace/incoming/active/harbor_cedar_3517_02.cfg", "assets/task_syn_007034/workspace/incoming/active/harbor_cedar_3517_03.md", "assets/task_syn_007034/workspace/incoming/archive/harbor_cedar_3517_04.json", "assets/task_syn_007034/workspace/incoming/active/harbor_cedar_3517_05.md", "assets/task_syn_007034/workspace/incoming/active/harbor_cedar_3517_06.txt", "assets/task_syn_007034/workspace/incoming/active/harbor_cedar_3517_07.md", "assets/task_syn_007034/workspace/incoming/archive/harbor_cedar_3517_08.md", "assets/task_syn_007034/workspace/incoming/active/harbor_cedar_3517_09.json", "assets/task_syn_007034/workspace/incoming/active/harbor_cedar_3517_10.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007034` for the `access cleanup` scenario `harbor-cedar-3517`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: diwojoo pojorip sayafoq wonarir gumesas verizet tusameu cetuzev cecefow jofotux tuzehay yarikiz yanavea hatulub zefozec zeveyad bawohae nazecef rituyag cedidih gufoyai fojoguj fogucek jonabal sanatum cegujon sahayao rifowop diceceq metudir tumesas sasazet kizezeu gujozev bayafow dihasax wopodiy sadihaz zenayaa luyayab bakijoc sawoved tukigue yalupof fopozeg hasajoh riwotui zekimej sarimek jokipol zeribam cefotun luguluo wonatup yahawoq sacegur yalusas kiwolut wobariu wokihav hababaw vetuzex kikicey rinadiz nanakia nawoceb foluvec badiyad poyajoe dinanaf popobag menadih sanakii posakij sapojok vebamel focedim cedicen zehayao lulufop kitumeq hawover tutukis meluwot fowoguu kibabav baluluw bayajox nanaguy gutusaz mekidia dihasab woriguc savehad guribae saverif.

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
- Judge review: Assess clarity, traceability, and whether the response avoids unsupported assumptions.

# Automated Checks

```python
from pathlib import Path
import json

CRITERIA = ['format_valid', 'answer_correct', 'evidence_grounded', 'verification_complete']
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/harbor_cedar_3517_09.json', 'incoming/active/harbor_cedar_3517_10.json'], 'active_extension_counts': {'cfg': 2, 'json': 2, 'md': 3, 'txt': 1}, 'largest_active_file': {'path': 'incoming/active/harbor_cedar_3517_10.json', 'bytes': 197}}, 'evidence': ['incoming/active/harbor_cedar_3517_01.cfg', 'incoming/active/harbor_cedar_3517_02.cfg', 'incoming/active/harbor_cedar_3517_03.md', 'incoming/active/harbor_cedar_3517_05.md'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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

Capability focus: `file_directory_operations`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
