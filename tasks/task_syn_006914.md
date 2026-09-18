---
id: "task_syn_006914"
name: "Active file manifest 006914"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_003457"
generator_seed: 985818
workspace_files: ["assets/task_syn_006914/workspace/incoming/archive/zenith_summit_3457_00.log", "assets/task_syn_006914/workspace/incoming/active/zenith_summit_3457_01.cfg", "assets/task_syn_006914/workspace/incoming/active/zenith_summit_3457_02.md", "assets/task_syn_006914/workspace/incoming/active/zenith_summit_3457_03.log", "assets/task_syn_006914/workspace/incoming/archive/zenith_summit_3457_04.json", "assets/task_syn_006914/workspace/incoming/active/zenith_summit_3457_05.log", "assets/task_syn_006914/workspace/incoming/active/zenith_summit_3457_06.json", "assets/task_syn_006914/workspace/incoming/active/zenith_summit_3457_07.cfg", "assets/task_syn_006914/workspace/incoming/archive/zenith_summit_3457_08.cfg", "assets/task_syn_006914/workspace/incoming/active/zenith_summit_3457_09.json", "assets/task_syn_006914/workspace/incoming/active/zenith_summit_3457_10.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006914` for the `access cleanup` scenario `zenith-summit-3457`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: cekidiy kizediz yasamea hawojob luvetuc jonanad womeyae venaluf bapobag sanahah sarigui fohakij riwozek guyakil disalum sasacen sarinao mezevep halufoq pobalur cecedis dicerit cekiyau samepov tusasaw lumelux lukiluy hazetuz rinakia bavelub zeyaluc dizehad pokitue guhajof bapodig kigudih safozei mewozej cevehak foluwol kiritum cejojon gumeveo johatup cekifoq vecepor mebadis josavet posapou yayapov fohaguw narikix sabamey lugusaz pozenaa dipolub hapokic vegukid menanae fogurif podihag riguceh fofozei vehadij gurituk babavel yasakim sadinan lutusao dihazep tutujoq cebarir hariyas zevewot natupou havesav gumebaw kiwosax vecenay lucesaz medidia wolusab badiric dibarid yapocee dibamef wosakig kiriyah yayarii wosajoj vepopok wokidil yaribam zemeven poriguo luzewop.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'json', 'minimum_bytes': 52, 'selected_files': ['incoming/active/zenith_summit_3457_06.json', 'incoming/active/zenith_summit_3457_09.json'], 'active_extension_counts': {'cfg': 2, 'json': 2, 'log': 3, 'md': 1}, 'largest_active_file': {'path': 'incoming/active/zenith_summit_3457_10.log', 'bytes': 198}}, 'evidence': ['incoming/active/zenith_summit_3457_01.cfg', 'incoming/active/zenith_summit_3457_02.md', 'incoming/active/zenith_summit_3457_03.log', 'incoming/active/zenith_summit_3457_05.log'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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
