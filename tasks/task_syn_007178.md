---
id: "task_syn_007178"
name: "Active file manifest 007178"
capability_family: "file_directory_operations"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003589"
generator_seed: 995586
workspace_files: ["assets/task_syn_007178/workspace/incoming/archive/brisk_amber_3589_00.json", "assets/task_syn_007178/workspace/incoming/active/brisk_amber_3589_01.cfg", "assets/task_syn_007178/workspace/incoming/active/brisk_amber_3589_02.md", "assets/task_syn_007178/workspace/incoming/active/brisk_amber_3589_03.txt", "assets/task_syn_007178/workspace/incoming/archive/brisk_amber_3589_04.txt", "assets/task_syn_007178/workspace/incoming/active/brisk_amber_3589_05.log", "assets/task_syn_007178/workspace/incoming/active/brisk_amber_3589_06.txt", "assets/task_syn_007178/workspace/incoming/active/brisk_amber_3589_07.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007178` for the `customer migration` scenario `brisk-amber-3589`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the customer migration workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.md` whose byte length is at least 45, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: naguluc mecefod josawoe difotuf vetumeg nakisah luritui fohabaj kigupok bajocel cegubam zekijon tuzefoo dirisap kibawoq tuzesar forilus yatuwot meveveu basariv forimew haribax wonayay fogufoz veceria yalukib kibafoc cefojod zefojoe hawopof vetuzeg kidikih jojohai najokij yazevek risavel pogumem yabanan cerifoo cehawop vezehaq vebamer sazehas jolulut johajou cefofov haveluw jocecex popoguy ribayaz jotusaa savehab vecehac meverid porihae dirizef gukinag worifoh ripomei ridiwoj rigusak ceguvel habasam hafocen didihao zekihap yarinaq rimecer gupoces baludit nadizeu batuzev jovediw vecejox nayavey yatuyaz lukiyaa fojojob turisac nahadid baporie zecesaf lupopog bacemeh jonasai mesajoj kiyahak sazehal lupoham cerisan foyaguo natujop mevesaq zezezer lunanas vekibat.

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

- factual_grounding: Uses only supplied fixture information.
- completeness: Covers every requested operation and constraint.
- clarity: Presents a concise artifact in the requested format.
- caution: Avoids invented facts, live-data claims, and unavailable-tool assumptions.

# Automated Checks

Not applicable; this candidate is scored by judge rubric only.

# LLM Judge Rubric

Judge the submitted artifact using the criteria below. Award credit only for content grounded in the supplied workspace files.

- 1.0: Complete, accurate, well organized, and explicit about evidence and verification.
- 0.7: Mostly correct with a minor omission or weak explanation that does not change the core result.
- 0.4: Partially grounded but misses an important constraint, source, or edge case.
- 0.0: Ungrounded, unusable, unsafe, or dependent on unavailable external data.

Capability focus: `file_directory_operations`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
