---
id: "task_syn_002241"
name: "Generate record transformer 002241"
capability_family: "code_generation"
intended_difficulty_band: 1
grading_type: "automated"
timeout_seconds: 150
base_scenario_id: "scenario_001121"
generator_seed: 812917
workspace_files: ["assets/task_syn_002241/workspace/spec/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_002241` for the `knowledge-base upkeep` scenario `delta-amber-1121`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 46. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 66, otherwise `watch`. Sort by code. Write the implementation to `submission/solution.py`.

Scenario-specific code anchors: lulucef josaveg ditufoh kitucei wozemej bavemek luhafol hasanam nabarin fofokio diyafop sajoriq jolugur bajojos kibakit fozewou dicekiv rifoguw pofopox riyapoy hariwoz cemeyaa hasanab yavekic nabajod jokizee wofokif lurilug ripowoh fotucei pozepoj fozejok zelujol gulufom mejozen naluveo fozevep bakidiq veluhar nayatus mesasat riyadiu hajobav guyasaw wowotux ripovey guyabaz natutua hamezeb nadikic jozezed pozesae dibajof vecewog turikih tukibai wotuyaj lucebak habakil kihalum tutufon ricezeo woyavep sawonaq yanajor sajomes pojozet badipou rilumev banasaw tudikix ribabay batuyaz bawojoa jogusab fojokic fonagud wofopoe zenakif jotunag kikijoh sadivei pojoyaj veyayak hadibal fogupom jolulun banahao vemewop jozeceq gulunar vefojos gucetut pojosau badimev forimew.

The submitted Python file must use only the standard library and expose the requested public function.
Keep the implementation deterministic and handle malformed records by skipping them when the behavior description implies a numeric conversion.

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
OUTPUT_FILE = 'solution.py'
VISIBLE_CASES = [{'input': [{'code': 'aa', 'status': 'active', 'score': 46}, {'code': 'bb', 'status': 'paused', 'score': 71}], 'expected': [{'code': 'AA', 'bucket': 'watch'}]}, {'input': [{'code': 'cc', 'status': 'active', 'score': 76}, {'code': 'dd', 'status': 'active', 'score': 45}], 'expected': [{'code': 'CC', 'bucket': 'priority'}]}]
HIDDEN_CASES = [{'input': [{'code': 'mx', 'status': 'active', 'score': 47}, {'code': 'az', 'status': 'active', 'score': 86}], 'expected': [{'code': 'AZ', 'bucket': 'priority'}, {'code': 'MX', 'bucket': 'watch'}]}, {'input': [{'code': 'nk', 'status': 'unknown', 'score': 136}, {'code': 'lm', 'status': 'active', 'score': 65}], 'expected': [{'code': 'LM', 'bucket': 'watch'}]}]
REFERENCE_CODE = 'def transform_records(records):\n    output = []\n    for record in records:\n        try:\n            score = int(record.get("score", 0))\n        except Exception:\n            continue\n        if record.get("status") == "active" and score >= 46:\n            bucket = "priority" if score >= 66 else "watch"\n            output.append({"code": str(record.get("code", "")).upper(), "bucket": bucket})\n    return sorted(output, key=lambda item: item["code"])\n'
INCORRECT_CODE = 'def transform_records(records):\n    return []\n'

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
