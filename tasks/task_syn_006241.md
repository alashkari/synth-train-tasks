---
id: "task_syn_006241"
name: "Active file manifest 006241"
capability_family: "file_directory_operations"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003121"
generator_seed: 960917
workspace_files: ["assets/task_syn_006241/workspace/incoming/archive/brisk_delta_3121_00.log", "assets/task_syn_006241/workspace/incoming/active/brisk_delta_3121_01.cfg", "assets/task_syn_006241/workspace/incoming/active/brisk_delta_3121_02.txt", "assets/task_syn_006241/workspace/incoming/active/brisk_delta_3121_03.log", "assets/task_syn_006241/workspace/incoming/archive/brisk_delta_3121_04.log", "assets/task_syn_006241/workspace/incoming/active/brisk_delta_3121_05.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006241` for the `release readiness` scenario `brisk-delta-3121`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the release readiness workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.log` whose byte length is at least 31, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: fosarib guwohac zeyatud banamee fomejof lufoyag gunanah rikikii hacemej fosajok ponabal zececem hakinan rijoguo diyarip hafodiq lutufor dilukis napogut pokinau kicebav nariwow disavex hakinay meforiz jokicea diveyab cekifoc lujoved hafozee bakisaf meyadig velubah nafomei nafotuj zesabak luyasal jobarim yazeven napojoo kijorip zetuluq ponasar nalujos rivenat mebariu haridiv sazejow lusakix sasacey zerihaz yanalua dikifob kibawoc joyayad mekimee savefof nagumeg babafoh dipomei sababaj cetumek jozesal bacesam nasagun wobaguo verigup yafoyaq pokilur vewohas risavet jofomeu gubatuv mebanaw jovelux powonay wohabaz tupomea gunabab zerifoc basapod povehae lupojof babajog hamebah vebavei hazedij jokibak hazezel hawosam vejogun vetunao didivep pomesaq zenakir wowogus.

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
