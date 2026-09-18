---
id: "task_syn_002292"
name: "Repair record transformer 002292"
capability_family: "code_debugging"
intended_difficulty_band: 2
grading_type: "automated"
timeout_seconds: 180
base_scenario_id: "scenario_001146"
generator_seed: 814804
workspace_files: ["assets/task_syn_002292/workspace/src/buggy_module.py", "assets/task_syn_002292/workspace/tests/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_002292` for the `sensor calibration` scenario `cedar-ion-1146`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

`src/buggy_module.py` is intended to satisfy this behavior: Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 52. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 72, otherwise `watch`. Sort by code. Write the corrected implementation to `submission/fixed_module.py` with the same public function.

Scenario-specific code anchors: ripogue fovecef kitukig baporih kitusai menacej vetuguk fotuzel lufobam wolusan bapobao cedicep hawonaq zevefor nabahas wopotut venaceu riveyav pozediw havebax sakituy balupoz yabadia hafoyab saguwoc zedijod bakitue foriluf nayasag diludih kihatui joturij foricek bamejol gudidim hatumen luzefoo divelup bazeveq disadir poworis menadit kibameu poyariv kirinaw zeluzex lunajoy ricevez rivelua sagurib haceluc kiripod veyafoe safozef jotufog kiceluh lulusai baluzej luzevek pogutul gudivem cesajon guhajoo luwocep woguguq zezeyar naripos zepotut cefohau poceyav tucefow diyayax meluyay fobakiz disaria hanaveb wocecec bajokid cevezee mebabaf nawotug zenanah hacewoi kipodij samerik zenayal vefoham cediyan jowoguo jolukip guporiq bafonar yatukis luzejot kigujou popohav.

The submitted Python file must use only the standard library and expose the requested public function.
Keep the implementation deterministic and handle malformed records by skipping them when the behavior description implies a numeric conversion.
Run or reason through the visible cases before finishing.

# Expected Behavior

A correct solution writes the requested Python module under `submission/`, exposes the requested function, passes the visible cases, and generalizes to structurally similar hidden cases.

# Grading Criteria

- `syntax_valid`: The submitted Python module imports without syntax or execution-time definition errors.
- `public_api`: The requested public function exists and is callable.
- `visible_cases`: The implementation passes visible behavior cases supplied in the workspace.
- `hidden_cases`: The implementation generalizes to held-back deterministic grader cases.

# Automated Checks

```python
from pathlib import Path
import importlib.util

CRITERIA = ['syntax_valid', 'public_api', 'visible_cases', 'hidden_cases']
FUNCTION_NAME = 'transform_records'
OUTPUT_FILE = 'fixed_module.py'
VISIBLE_CASES = [{'input': [{'code': 'aa', 'status': 'active', 'score': 52}, {'code': 'bb', 'status': 'paused', 'score': 77}], 'expected': [{'code': 'AA', 'bucket': 'watch'}]}, {'input': [{'code': 'cc', 'status': 'active', 'score': 82}, {'code': 'dd', 'status': 'active', 'score': 51}], 'expected': [{'code': 'CC', 'bucket': 'priority'}]}]
HIDDEN_CASES = [{'input': [{'code': 'mx', 'status': 'active', 'score': 53}, {'code': 'az', 'status': 'active', 'score': 92}], 'expected': [{'code': 'AZ', 'bucket': 'priority'}, {'code': 'MX', 'bucket': 'watch'}]}, {'input': [{'code': 'nk', 'status': 'unknown', 'score': 142}, {'code': 'lm', 'status': 'active', 'score': 71}], 'expected': [{'code': 'LM', 'bucket': 'watch'}]}]
REFERENCE_CODE = 'def transform_records(records):\n    output = []\n    for record in records:\n        try:\n            score = int(record.get("score", 0))\n        except Exception:\n            continue\n        if record.get("status") == "active" and score >= 52:\n            bucket = "priority" if score >= 72 else "watch"\n            output.append({"code": str(record.get("code", "")).upper(), "bucket": bucket})\n    return sorted(output, key=lambda item: item["code"])\n'
INCORRECT_CODE = 'def transform_records(records):\n    output = []\n    for record in records:\n        try:\n            score = int(record.get("score", 0))\n        except Exception:\n            continue\n        if record.get("status") == "active" and score > 52:\n            bucket = "urgent" if score > 72 else "watch"\n            output.append({"code": str(record.get("code", "")).upper(), "bucket": bucket})\n    return sorted(output, key=lambda item: item["code"])\n'

def _load_module(path):
    try:
        spec = importlib.util.spec_from_file_location("candidate_solution", path)
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception:
        return None

def _run_cases(func, cases):
    if not cases:
        return 1.0
    passed = 0
    for case in cases:
        try:
            actual = func(case["input"])
        except Exception:
            actual = None
        if actual == case["expected"]:
            passed += 1
    return passed / len(cases)

def grade(workspace_dir):
    scores = {key: 0.0 for key in CRITERIA}
    module_path = Path(workspace_dir) / "submission" / OUTPUT_FILE
    if not module_path.exists():
        return scores
    module = _load_module(module_path)
    if module is None:
        return scores
    scores["syntax_valid"] = 1.0
    func = getattr(module, FUNCTION_NAME, None)
    if not callable(func):
        return scores
    scores["public_api"] = 1.0
    scores["visible_cases"] = _run_cases(func, VISIBLE_CASES)
    scores["hidden_cases"] = _run_cases(func, HIDDEN_CASES)
    return scores

def create_reference_solution(workspace_dir):
    output = Path(workspace_dir) / "submission" / OUTPUT_FILE
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REFERENCE_CODE, encoding="utf-8")

def create_incorrect_solution(workspace_dir):
    output = Path(workspace_dir) / "submission" / OUTPUT_FILE
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(INCORRECT_CODE, encoding="utf-8")
```

# LLM Judge Rubric

Not applicable; objective automated checks define the task score.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
