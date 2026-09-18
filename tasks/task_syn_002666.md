---
id: "task_syn_002666"
name: "Active file manifest 002666"
capability_family: "file_directory_operations"
intended_difficulty_band: 1
grading_type: "automated"
timeout_seconds: 150
base_scenario_id: "scenario_001333"
generator_seed: 828642
workspace_files: ["assets/task_syn_002666/workspace/incoming/archive/harbor_zenith_1333_00.txt", "assets/task_syn_002666/workspace/incoming/active/harbor_zenith_1333_01.md", "assets/task_syn_002666/workspace/incoming/active/harbor_zenith_1333_02.cfg", "assets/task_syn_002666/workspace/incoming/active/harbor_zenith_1333_03.txt", "assets/task_syn_002666/workspace/incoming/archive/harbor_zenith_1333_04.log", "assets/task_syn_002666/workspace/incoming/active/harbor_zenith_1333_05.cfg"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_002666` for the `release readiness` scenario `harbor-zenith-1333`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the release readiness workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.log` whose byte length is at least 31, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: jotuwoo kicemep velutuq hakisar satujos fodizet tuceveu tudiriv nazezew wopokix tukinay porizez safogua wosasab pozeyac meyatud sacedie zemenaf vewosag bapofoh bajonai haveguj tujojok jolujol jobajom podizen yakihao sasadip wopotuq guguwor kisakis rifowot nanadiu difoyav tubapow jodipox difojoy ceyahaz lupoyaa luhabab wojowoc posakid hamerie cewojof celuveg luceveh dibazei yatukij wodimek gufokil mefobam wosaven vefosao hayadip baguhaq kihatur tujobas yadigut nazeyau fobajov vekidiw hanalux zenapoy jojojoz nawonaa diyafob luveric gutulud medimee lukiyaf baritug wojoveh vemepoi tuhaluj meguluk veguhal veyajom luhagun ririceo luyayap gunafoq guluyar mebaris riguvet safoceu nabasav poyapow veyarix yakisay cenaluz mesafoa tuceyab mefoluc fonanad vecejoe nakihaf.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'log', 'minimum_bytes': 31, 'selected_files': [], 'active_extension_counts': {'cfg': 2, 'md': 1, 'txt': 1}, 'largest_active_file': {'path': 'incoming/active/harbor_zenith_1333_05.cfg', 'bytes': 142}}, 'evidence': ['incoming/active/harbor_zenith_1333_01.md', 'incoming/active/harbor_zenith_1333_02.cfg', 'incoming/active/harbor_zenith_1333_03.txt', 'incoming/active/harbor_zenith_1333_05.cfg'], 'verification': {'checked_files': 6, 'ignored_archive': True, 'status': 'pass'}}

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
