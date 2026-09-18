---
id: "task_syn_007310"
name: "Mini repository maintenance scan 007310"
capability_family: "repository_navigation_software_maintenance"
intended_difficulty_band: 5
grading_type: "automated"
timeout_seconds: 270
base_scenario_id: "scenario_003655"
generator_seed: 1000470
workspace_files: ["assets/task_syn_007310/workspace/repo/config/modules.json", "assets/task_syn_007310/workspace/repo/src/ingest.py", "assets/task_syn_007310/workspace/repo/src/export.py", "assets/task_syn_007310/workspace/repo/src/audit.py", "assets/task_syn_007310/workspace/repo/src/notify.py", "assets/task_syn_007310/workspace/repo/src/cleanup.py", "assets/task_syn_007310/workspace/repo/docs/changelog.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007310` for the `inventory audit` scenario `prairie-juniper-3655`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the mini repository under `repo/`. Create a maintenance report with enabled modules, deprecated modules, TODO markers with their module names, and any enabled module whose source file is missing.

Scenario-specific audit anchors: hatuhae riyamef sapobag nakijoh tupogui naluluj yanawok yakivel kiwokim fofogun zepozeo kibafop kisasaq ririkir tutunas safozet lujoceu zetusav cejosaw wosakix jocecey luwowoz hafojoa kitupob rijofoc luyayad poyajoe ceyajof vebalug riwonah hagudii podiluj zekiluk yajovel vegugum riyagun medijoo meyasap rizesaq popopor kifozes nalufot hazebau foyavev velupow risagux yamebay wocenaz guzepoa bakinab dibadic jocemed hasafoe rihabaf yajowog dizeyah fogujoi dizezej tutupok vedicel merikim tufokin mecemeo vewomep napoceq gurigur gudizes jorisat cekibau popobav megudiw mevemex vecejoy zemesaz tujomea yavemeb zerituc natukid wocevee wohapof hahakig fopofoh rivemei nahafoj nawobak yamefol hahawom luhawon jopozeo woverip baceceq cezerir yazezes tucehat jodibau zemeriv.

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
EXPECTED_OUTPUT = {'result': {'enabled_modules': ['ingest', 'export', 'audit', 'notify', 'cleanup'], 'deprecated_modules': ['cleanup'], 'todo_items': [{'module': 'ingest', 'todo': '7310-0'}, {'module': 'audit', 'todo': '7310-2'}, {'module': 'cleanup', 'todo': '7310-4'}], 'missing_enabled_files': []}, 'evidence': ['repo/config/modules.json', 'repo/src'], 'verification': {'checked_files': 7, 'status': 'pass'}}

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
