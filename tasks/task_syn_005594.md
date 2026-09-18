---
id: "task_syn_005594"
name: "Active file manifest 005594"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "hybrid"
timeout_seconds: 240
base_scenario_id: "scenario_002797"
generator_seed: 936978
workspace_files: ["assets/task_syn_005594/workspace/incoming/archive/prairie_violet_2797_00.txt", "assets/task_syn_005594/workspace/incoming/active/prairie_violet_2797_01.json", "assets/task_syn_005594/workspace/incoming/active/prairie_violet_2797_02.txt", "assets/task_syn_005594/workspace/incoming/active/prairie_violet_2797_03.md", "assets/task_syn_005594/workspace/incoming/archive/prairie_violet_2797_04.txt", "assets/task_syn_005594/workspace/incoming/active/prairie_violet_2797_05.txt", "assets/task_syn_005594/workspace/incoming/active/prairie_violet_2797_06.json", "assets/task_syn_005594/workspace/incoming/active/prairie_violet_2797_07.log", "assets/task_syn_005594/workspace/incoming/archive/prairie_violet_2797_08.md", "assets/task_syn_005594/workspace/incoming/active/prairie_violet_2797_09.txt", "assets/task_syn_005594/workspace/incoming/active/prairie_violet_2797_10.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_005594` for the `access cleanup` scenario `prairie-violet-2797`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: dilunae vewozef vesawog polumeh wobapoi lupowoj tuhanak lurisal zebabam tupolun metutuo kiluhap ceririq bafotur hahazes tulumet luhariu lucekiv luvesaw wodigux babamey mebajoz zeyadia vebaveb zekisac tuhatud sasacee vedijof lugumeg tuludih kisanai badituj velukik fosasal zedivem jofomen tuwodio zetulup nariguq sazegur bazesas gutulut meluhau cebazev joluguw yanabax nayasay mebapoz rivetua wogulub luluric zejolud josahae vememef fozetug zeriluh zesagui posawoj zekijok tupodil lulugum sazeyan ricehao josagup tuzejoq tubasar pocejos tunahat didituu bapoguv yazekiw divepox tuyapoy fonasaz zetumea wogulub fopotuc mevegud melusae haluvef cemeceg sazebah wopopoi dirijoj luwopok vegutul turijom foyarin ripowoo luvewop dizeluq yaditur jorihas dijocet mekiveu lumehav.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/prairie_violet_2797_01.json', 'incoming/active/prairie_violet_2797_06.json', 'incoming/active/prairie_violet_2797_10.json'], 'active_extension_counts': {'json': 3, 'log': 1, 'md': 1, 'txt': 3}, 'largest_active_file': {'path': 'incoming/active/prairie_violet_2797_10.json', 'bytes': 199}}, 'evidence': ['incoming/active/prairie_violet_2797_01.json', 'incoming/active/prairie_violet_2797_02.txt', 'incoming/active/prairie_violet_2797_03.md', 'incoming/active/prairie_violet_2797_05.txt'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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
