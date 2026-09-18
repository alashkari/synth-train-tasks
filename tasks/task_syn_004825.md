---
id: "task_syn_004825"
name: "Active file manifest 004825"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "hybrid"
timeout_seconds: 270
base_scenario_id: "scenario_002413"
generator_seed: 908525
workspace_files: ["assets/task_syn_004825/workspace/incoming/archive/violet_keystone_2413_00.log", "assets/task_syn_004825/workspace/incoming/active/violet_keystone_2413_01.md", "assets/task_syn_004825/workspace/incoming/active/violet_keystone_2413_02.json", "assets/task_syn_004825/workspace/incoming/active/violet_keystone_2413_03.cfg", "assets/task_syn_004825/workspace/incoming/archive/violet_keystone_2413_04.log", "assets/task_syn_004825/workspace/incoming/active/violet_keystone_2413_05.txt", "assets/task_syn_004825/workspace/incoming/active/violet_keystone_2413_06.log", "assets/task_syn_004825/workspace/incoming/active/violet_keystone_2413_07.txt", "assets/task_syn_004825/workspace/incoming/archive/violet_keystone_2413_08.txt", "assets/task_syn_004825/workspace/incoming/active/violet_keystone_2413_09.txt", "assets/task_syn_004825/workspace/incoming/archive/distractor_004825.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_004825` for the `knowledge-base upkeep` scenario `violet-keystone-2413`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: gumefop wotuguq powowor rifofos yabawot wobameu meyatuv yariguw fozegux kidipoy zemenaz zedibaa bakiyab dicefoc lurized turinae gupofof mesalug kikikih wotubai vezebaj kidivek cenadil tujopom dilugun gunakio rigusap sazefoq sarizer jodimes dihatut batujou cemekiv yagubaw jokicex luzekiy fokicez rifojoa wosafob fopozec saponad hayavee nagukif bayawog nanakih dihawoi dibarij namefok nacehal nayajom rikikin bayaveo zepogup gubayaq difodir batugus zeribat rifowou wogufov lubasaw rivekix rihaluy zezecez dilufoa lucemeb mesaguc bafotud nawomee lufofof jolutug gubazeh bagukii nasasaj yakikik hajolul guyabam pokifon hazesao vesamep vepojoq guveyar wozefos wowotut gufokiu risariv kijotuw kitusax tudijoy sapobaz bamecea wonasab kihasac saririd rikitue kijohaf ribanag.

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
- Judge review: Assess clarity, traceability, and whether the response avoids unsupported assumptions.

# Automated Checks

```python
from pathlib import Path
import json

CRITERIA = ['format_valid', 'answer_correct', 'evidence_grounded', 'verification_complete']
EXPECTED_OUTPUT = {'result': {'target_extension': 'txt', 'minimum_bytes': 59, 'selected_files': ['incoming/active/violet_keystone_2413_05.txt', 'incoming/active/violet_keystone_2413_07.txt', 'incoming/active/violet_keystone_2413_09.txt'], 'active_extension_counts': {'cfg': 1, 'json': 1, 'log': 1, 'md': 1, 'txt': 3}, 'largest_active_file': {'path': 'incoming/active/violet_keystone_2413_09.txt', 'bytes': 204}}, 'evidence': ['incoming/active/violet_keystone_2413_01.md', 'incoming/active/violet_keystone_2413_02.json', 'incoming/active/violet_keystone_2413_03.cfg', 'incoming/active/violet_keystone_2413_05.txt'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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
