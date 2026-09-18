---
id: "task_syn_006121"
name: "Active file manifest 006121"
capability_family: "file_directory_operations"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003061"
generator_seed: 956477
workspace_files: ["assets/task_syn_006121/workspace/incoming/archive/tundra_mosaic_3061_00.json", "assets/task_syn_006121/workspace/incoming/active/tundra_mosaic_3061_01.cfg", "assets/task_syn_006121/workspace/incoming/active/tundra_mosaic_3061_02.json", "assets/task_syn_006121/workspace/incoming/active/tundra_mosaic_3061_03.txt", "assets/task_syn_006121/workspace/incoming/archive/tundra_mosaic_3061_04.json", "assets/task_syn_006121/workspace/incoming/active/tundra_mosaic_3061_05.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006121` for the `release readiness` scenario `tundra-mosaic-3061`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the release readiness workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.log` whose byte length is at least 31, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: sarimel menazem basawon zepomeo bacebap womekiq gucever samenas meyalut nadipou risaluv cesadiw wobagux vemeyay tufopoz badivea disarib hafovec cewopod kizevee lunarif safolug pocewoh zerizei jocekij mevevek kibalul zesatum dibalun hajowoo jomedip sakiveq cetukir yanapos guhakit zeyaluu jowotuv bawovew zewopox kizekiy hasavez gukifoa dizejob gurisac kifodid sahalue difokif jopopog badihah diwogui rikipoj tuyajok fomesal tuhabam riwodin luceyao sahakip cegufoq pohasar wowotus povebat hapoguu fokituv diluguw poripox hakimey bajoyaz tuluvea podikib folunac sacemed vehamee mejosaf nafojog ceyazeh cesabai wojokij menarik ceyalul vepolum ririyan natuceo yatuyap luyabaq wodiver lupolus guwotut pobaguu joluriv ricezew wotubax wodikiy dihahaz mesalua cesaceb dikiwoc.

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
