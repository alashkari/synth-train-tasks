---
id: "task_syn_006769"
name: "Active file manifest 006769"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_003385"
generator_seed: 980453
workspace_files: ["assets/task_syn_006769/workspace/incoming/archive/frost_ripple_3385_00.json", "assets/task_syn_006769/workspace/incoming/active/frost_ripple_3385_01.cfg", "assets/task_syn_006769/workspace/incoming/active/frost_ripple_3385_02.txt", "assets/task_syn_006769/workspace/incoming/active/frost_ripple_3385_03.md", "assets/task_syn_006769/workspace/incoming/archive/frost_ripple_3385_04.txt", "assets/task_syn_006769/workspace/incoming/active/frost_ripple_3385_05.txt", "assets/task_syn_006769/workspace/incoming/active/frost_ripple_3385_06.log", "assets/task_syn_006769/workspace/incoming/active/frost_ripple_3385_07.json", "assets/task_syn_006769/workspace/incoming/archive/frost_ripple_3385_08.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006769` for the `access cleanup` scenario `frost-ripple-3385`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: poridij dihadik zegudil basafom zemekin hahaceo guwopop gucehaq zetudir posalus risawot veposau naposav cemeluw luzefox dikimey hayanaz meyamea wojojob haluyac medilud luvezee sapowof luwohag zeriwoh fonavei gucezej tutuhak havevel bavesam sadidin hadiwoo luwofop meturiq wotuyar nasatus wogudit dilutuu tutudiv cetukiw zedirix cevefoy gukinaz yazesaa luriveb vejodic vemenad ponakie wokizef cesayag celuveh lusajoi havefoj zezecek kidilul hatuvem yafokin veguzeo woluvep hawozeq bapodir bamewos tuludit kiceluu metupov ceyavew mezesax nasasay sadifoz nalukia natuyab cerihac wocebad tuceyae yayanaf yapotug kihatuh cefofoi joyafoj hatupok ricefol kihasam bavepon vefopoo gusanap yabaveq woluwor foyazes nafobat woluhau naricev diyazew balupox meyazey yaguzez wodilua.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/frost_ripple_3385_07.json'], 'active_extension_counts': {'cfg': 1, 'json': 1, 'log': 1, 'md': 1, 'txt': 2}, 'largest_active_file': {'path': 'incoming/active/frost_ripple_3385_07.json', 'bytes': 173}}, 'evidence': ['incoming/active/frost_ripple_3385_01.cfg', 'incoming/active/frost_ripple_3385_02.txt', 'incoming/active/frost_ripple_3385_03.md', 'incoming/active/frost_ripple_3385_05.txt'], 'verification': {'checked_files': 9, 'ignored_archive': True, 'status': 'pass'}}

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
