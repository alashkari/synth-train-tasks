---
id: "task_syn_006025"
name: "Active file manifest 006025"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "hybrid"
timeout_seconds: 270
base_scenario_id: "scenario_003013"
generator_seed: 952925
workspace_files: ["assets/task_syn_006025/workspace/incoming/archive/xenial_harbor_3013_00.txt", "assets/task_syn_006025/workspace/incoming/active/xenial_harbor_3013_01.log", "assets/task_syn_006025/workspace/incoming/active/xenial_harbor_3013_02.txt", "assets/task_syn_006025/workspace/incoming/active/xenial_harbor_3013_03.md", "assets/task_syn_006025/workspace/incoming/archive/xenial_harbor_3013_04.cfg", "assets/task_syn_006025/workspace/incoming/active/xenial_harbor_3013_05.txt", "assets/task_syn_006025/workspace/incoming/active/xenial_harbor_3013_06.cfg", "assets/task_syn_006025/workspace/incoming/active/xenial_harbor_3013_07.log", "assets/task_syn_006025/workspace/incoming/archive/xenial_harbor_3013_08.txt", "assets/task_syn_006025/workspace/incoming/active/xenial_harbor_3013_09.log", "assets/task_syn_006025/workspace/incoming/archive/distractor_006025.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006025` for the `knowledge-base upkeep` scenario `xenial-harbor-3013`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: dilucet yadikiu ceyaguv jojoluw metutux kiwosay wopofoz fomesaa lumeveb hanahac baritud wovecee menajof mewopog poyabah wowopoi ceporij yadidik tutugul hawotum divedin rikipoo zenavep yamehaq luyadir sacedis rivetut dibadiu jocewov tutupow kidizex bazebay lulucez dilubaa wosasab rituzec cezenad ricepoe tumefof medikig yabafoh jomevei wogucej tujoguk najojol yawowom zelutun zecemeo cevebap cerinaq yaguhar nakisas vehasat yakifou memeluv wozefow gupoyax memepoy gufonaz yayalua potusab fojofoc nakifod wonakie rinatuf bawogug zerizeh zebanai hapobaj diwoyak vepomel kirisam sadijon tujoluo wojofop dikiriq mecepor jodifos zepoyat poceceu nafocev mezewow gudikix yamebay nagujoz sazekia zemesab kicehac bayabad sayazee cekibaf zebafog rifonah dizetui joludij jonadik.

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
EXPECTED_OUTPUT = {'result': {'target_extension': 'txt', 'minimum_bytes': 59, 'selected_files': ['incoming/active/xenial_harbor_3013_02.txt', 'incoming/active/xenial_harbor_3013_05.txt'], 'active_extension_counts': {'cfg': 1, 'log': 3, 'md': 1, 'txt': 2}, 'largest_active_file': {'path': 'incoming/active/xenial_harbor_3013_09.log', 'bytes': 202}}, 'evidence': ['incoming/active/xenial_harbor_3013_01.log', 'incoming/active/xenial_harbor_3013_02.txt', 'incoming/active/xenial_harbor_3013_03.md', 'incoming/active/xenial_harbor_3013_05.txt'], 'verification': {'checked_files': 11, 'ignored_archive': True, 'status': 'pass'}}

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
