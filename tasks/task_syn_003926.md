---
id: "task_syn_003926"
name: "Mini repository maintenance scan 003926"
capability_family: "repository_navigation_software_maintenance"
intended_difficulty_band: 1
grading_type: "automated"
timeout_seconds: 150
base_scenario_id: "scenario_001963"
generator_seed: 875262
workspace_files: ["assets/task_syn_003926/workspace/repo/config/modules.json", "assets/task_syn_003926/workspace/repo/src/ingest.py", "assets/task_syn_003926/workspace/repo/src/export.py", "assets/task_syn_003926/workspace/repo/src/audit.py", "assets/task_syn_003926/workspace/repo/src/notify.py", "assets/task_syn_003926/workspace/repo/src/cleanup.py", "assets/task_syn_003926/workspace/repo/docs/changelog.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_003926` for the `sensor calibration` scenario `nimbus-yonder-1963`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the mini repository under `repo/`. Create a maintenance report with enabled modules, deprecated modules, TODO markers with their module names, and any enabled module whose source file is missing.

Scenario-specific audit anchors: hacelua fohaceb fovemec jonabad yaririe lulucef bagumeg cepotuh woharii nahadij yazefok nagugul difolum vegudin yalukio risadip ceyaceq metucer naveris tuvelut meluyau mevepov tucetuw hadirix rivebay riwosaz posajoa yawomeb banadic wobasad poporie luyadif bazekig yafopoh hamezei pojovej gutubak tuzenal yawodim gurisan hasaceo mebahap dinameq yatukir pohajos pohasat nanafou pobajov vefodiw tululux joluyay yanadiz tumekia gulufob bacetuc fofosad tusague dimewof zewowog metutuh tutuyai kigujoj zezebak rizegul zeriwom hapojon jozejoo nasavep fozeveq lunadir sahanas yagufot najohau kiripov kihazew yayapox luzeluy wokiwoz tupomea tujojob fonafoc pocetud fovedie nakiyaf zesakig luguhah tuyavei yazenaj hapohak diyajol guluzem zecenan meyaguo ponajop kivemeq wojover.

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
EXPECTED_OUTPUT = {'result': {'enabled_modules': ['ingest', 'export', 'audit', 'notify'], 'deprecated_modules': ['cleanup'], 'todo_items': [{'module': 'ingest', 'todo': '3926-0'}, {'module': 'audit', 'todo': '3926-2'}, {'module': 'cleanup', 'todo': '3926-4'}], 'missing_enabled_files': []}, 'evidence': ['repo/config/modules.json', 'repo/src'], 'verification': {'checked_files': 7, 'status': 'pass'}}

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
