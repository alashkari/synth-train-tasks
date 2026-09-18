---
id: "task_syn_002570"
name: "Active file manifest 002570"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "automated"
timeout_seconds: 270
base_scenario_id: "scenario_001285"
generator_seed: 825090
workspace_files: ["assets/task_syn_002570/workspace/incoming/archive/lumen_ripple_1285_00.json", "assets/task_syn_002570/workspace/incoming/active/lumen_ripple_1285_01.log", "assets/task_syn_002570/workspace/incoming/active/lumen_ripple_1285_02.cfg", "assets/task_syn_002570/workspace/incoming/active/lumen_ripple_1285_03.txt", "assets/task_syn_002570/workspace/incoming/archive/lumen_ripple_1285_04.txt", "assets/task_syn_002570/workspace/incoming/active/lumen_ripple_1285_05.md", "assets/task_syn_002570/workspace/incoming/active/lumen_ripple_1285_06.md", "assets/task_syn_002570/workspace/incoming/active/lumen_ripple_1285_07.json", "assets/task_syn_002570/workspace/incoming/archive/lumen_ripple_1285_08.txt", "assets/task_syn_002570/workspace/incoming/active/lumen_ripple_1285_09.md", "assets/task_syn_002570/workspace/incoming/active/lumen_ripple_1285_10.json", "assets/task_syn_002570/workspace/incoming/active/lumen_ripple_1285_11.cfg", "assets/task_syn_002570/workspace/incoming/archive/distractor_002570.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_002570` for the `knowledge-base upkeep` scenario `lumen-ripple-1285`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: lutucew basasax dirihay gufonaz guwogua sabarib guriluc memezed polunae sabasaf zebazeg hanaveh sadirii menatuj mekidik pofowol tutukim vevetun yaceveo yahayap nabariq velukir vecelus mehawot najoyau tuvehav nasavew jofofox lusabay tunafoz mefotua lujoveb zemewoc joguyad diyawoe vewodif meribag rijobah pokimei fomekij fonasak memeyal nadisam turiven ridikio sapohap banaveq lupozer wolulus wokimet nahaluu jobasav kivediw wovebax kidisay wovepoz habajoa vejohab hawovec zeposad zedirie guyatuf gukikig nasawoh worijoi sacebaj nakirik tuwobal vecemem diyagun wotunao rimeyap pogupoq difosar luyapos hadilut yavesau dibapov turimew nahagux bagukiy wonatuz potunaa fovesab bagumec diturid basabae gusasaf veritug navetuh mebakii bahahaj zemecek mebadil pojorim wozepon.

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
Some supplied information is intentionally irrelevant; exclude it from the result.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'txt', 'minimum_bytes': 59, 'selected_files': ['incoming/active/lumen_ripple_1285_03.txt'], 'active_extension_counts': {'cfg': 2, 'json': 2, 'log': 1, 'md': 3, 'txt': 1}, 'largest_active_file': {'path': 'incoming/active/lumen_ripple_1285_11.cfg', 'bytes': 216}}, 'evidence': ['incoming/active/lumen_ripple_1285_01.log', 'incoming/active/lumen_ripple_1285_02.cfg', 'incoming/active/lumen_ripple_1285_03.txt', 'incoming/active/lumen_ripple_1285_05.md'], 'verification': {'checked_files': 13, 'ignored_archive': True, 'status': 'pass'}}

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
