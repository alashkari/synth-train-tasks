---
id: "task_syn_004394"
name: "Active file manifest 004394"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_002197"
generator_seed: 892578
workspace_files: ["assets/task_syn_004394/workspace/incoming/archive/nimbus_delta_2197_00.md", "assets/task_syn_004394/workspace/incoming/active/nimbus_delta_2197_01.json", "assets/task_syn_004394/workspace/incoming/active/nimbus_delta_2197_02.log", "assets/task_syn_004394/workspace/incoming/active/nimbus_delta_2197_03.cfg", "assets/task_syn_004394/workspace/incoming/archive/nimbus_delta_2197_04.cfg", "assets/task_syn_004394/workspace/incoming/active/nimbus_delta_2197_05.txt", "assets/task_syn_004394/workspace/incoming/active/nimbus_delta_2197_06.json", "assets/task_syn_004394/workspace/incoming/active/nimbus_delta_2197_07.json", "assets/task_syn_004394/workspace/incoming/archive/nimbus_delta_2197_08.cfg", "assets/task_syn_004394/workspace/incoming/active/nimbus_delta_2197_09.json", "assets/task_syn_004394/workspace/incoming/active/nimbus_delta_2197_10.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_004394` for the `access cleanup` scenario `nimbus-delta-2197`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: banadia natunab sapowoc venasad fozewoe powovef lutuzeg diyakih harimei gufovej zeveguk metunal yayarim wovekin yajomeo yapopop yapomeq vepoyar rikijos namewot meriveu wodiriv cejonaw guluzex luwoluy menatuz guluhaa luhameb zeguguc melupod diripoe rikivef ririgug dinapoh cenanai fosacej josafok pokizel tuceham kiyafon vejobao kihayap wobafoq hananar wolugus lukimet wonaceu tumediv cezehaw dijowox lukimey sakimez ricemea yamepob tuvepoc gudiced yapolue jonaluf wopojog luworih ribanai fopomej vemesak yalutul savetum gufoban dimeceo woyasap nawowoq rihadir pofogus gupopot hamejou tuhahav guzefow vetumex guzebay sahawoz dimeyaa didimeb yapopoc sariyad hawomee povepof sapojog fodinah gupowoi zeyawoj difoluk ritufol cemepom guzekin bafomeo luhahap nafoguq wogulur.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/nimbus_delta_2197_01.json', 'incoming/active/nimbus_delta_2197_06.json', 'incoming/active/nimbus_delta_2197_07.json', 'incoming/active/nimbus_delta_2197_09.json'], 'active_extension_counts': {'cfg': 1, 'json': 4, 'log': 1, 'txt': 2}, 'largest_active_file': {'path': 'incoming/active/nimbus_delta_2197_10.txt', 'bytes': 197}}, 'evidence': ['incoming/active/nimbus_delta_2197_01.json', 'incoming/active/nimbus_delta_2197_02.log', 'incoming/active/nimbus_delta_2197_03.cfg', 'incoming/active/nimbus_delta_2197_05.txt'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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
