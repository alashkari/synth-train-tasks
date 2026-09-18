---
id: "task_syn_007249"
name: "Active file manifest 007249"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_003625"
generator_seed: 998213
workspace_files: ["assets/task_syn_007249/workspace/incoming/archive/lumen_lumen_3625_00.cfg", "assets/task_syn_007249/workspace/incoming/active/lumen_lumen_3625_01.log", "assets/task_syn_007249/workspace/incoming/active/lumen_lumen_3625_02.log", "assets/task_syn_007249/workspace/incoming/active/lumen_lumen_3625_03.log", "assets/task_syn_007249/workspace/incoming/archive/lumen_lumen_3625_04.md", "assets/task_syn_007249/workspace/incoming/active/lumen_lumen_3625_05.json", "assets/task_syn_007249/workspace/incoming/active/lumen_lumen_3625_06.cfg", "assets/task_syn_007249/workspace/incoming/active/lumen_lumen_3625_07.md", "assets/task_syn_007249/workspace/incoming/archive/lumen_lumen_3625_08.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007249` for the `access cleanup` scenario `lumen-lumen-3625`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: saguluv sadiwow pocejox didinay dirimez joporia tuhawob dicewoc nawozed bariyae lunamef zefowog cepojoh lukizei rihazej veworik focevel jorigum yalulun tufofoo fosahap kisatuq wojoyar diyagus tuwosat zetudiu kisawov worihaw salulux zebaguy kifodiz zekiyaa zemewob nakibac zeyamed foritue yajoguf wocedig rilunah zehatui mekinaj vezesak lugucel bavepom kicefon tuzedio mezewop harinaq mekimer ceyatus yakipot lujohau lupobav pobaguw dinapox lubasay saluriz kipodia lufofob yabavec batubad nasacee rifoyaf yapoyag ceriyah bajomei foriluj sasapok gusakil memekim yarikin hasameo kinasap cefopoq wotutur jonahas lurihat joveguu sazejov fogunaw saforix cediluy womeyaz mefokia zefoceb diyawoc zeworid lucesae worinaf tubaceg zegukih kifomei riwosaj kiyajok cekivel hakiwom.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/lumen_lumen_3625_05.json'], 'active_extension_counts': {'cfg': 1, 'json': 1, 'log': 3, 'md': 1}, 'largest_active_file': {'path': 'incoming/active/lumen_lumen_3625_07.md', 'bytes': 172}}, 'evidence': ['incoming/active/lumen_lumen_3625_01.log', 'incoming/active/lumen_lumen_3625_02.log', 'incoming/active/lumen_lumen_3625_03.log', 'incoming/active/lumen_lumen_3625_05.json'], 'verification': {'checked_files': 9, 'ignored_archive': True, 'status': 'pass'}}

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
