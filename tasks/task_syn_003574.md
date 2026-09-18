---
id: "task_syn_003574"
name: "Context continuation update 003574"
capability_family: "memory_retrieval_context_continuation"
intended_difficulty_band: 4
grading_type: "automated"
timeout_seconds: 240
base_scenario_id: "scenario_001787"
generator_seed: 862238
workspace_files: ["assets/task_syn_003574/workspace/sessions/session_log.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_003574` for the `billing review` scenario `tundra-juniper-1787`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read the session log file or files under `sessions/` and produce a context-continuation update. Separate durable preferences, current state, and stale items.

Scenario-specific audit anchors: celudim verinan jofodio luyacep rijomeq hawohar venajos rituhat gukiceu fogudiv fopopow babakix meceyay jowodiz gukivea zeluyab mewotuc luyarid nagumee merivef sanatug mejofoh jojolui cehadij gusarik cekisal joribam dijohan nakidio luyahap gukipoq poyaver fozeris gukivet ponaveu nameguv guzesaw zesawox basayay tunakiz jomebaa mewoyab fopokic yacerid powokie sajowof tusafog kicemeh yazevei zevewoj cebapok tuceril havelum joluban nafoyao fobavep salufoq zebajor vehazes habacet fofoveu fopotuv tuvehaw hamewox nagumey diribaz wobaria wowonab hagudic mefogud zetumee jorijof tucebag narituh napotui tuyawoj dicekik cemekil tuzetum cesakin fomeluo haguwop savepoq yatuwor cehasas zedirit navehau lujoyav bayapow hahabax fosayay yazeyaz cecelua pobahab cenaric kihagud.

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
EXPECTED_OUTPUT = {'result': {'durable_preferences': ['prefers summaries grouped by ember', 'wants checkpoint files named tundra_juniper_1787_checkpoint'], 'current_state': ['waiting on owner prairie', 'next review covers batch 6'], 'stale_items': []}, 'evidence': ['session_log.md'], 'verification': {'checked_files': 1, 'multi_session': False, 'status': 'pass'}}

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
