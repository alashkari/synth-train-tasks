---
id: "task_syn_006337"
name: "Active file manifest 006337"
capability_family: "file_directory_operations"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003169"
generator_seed: 964469
workspace_files: ["assets/task_syn_006337/workspace/incoming/archive/xenial_glade_3169_00.log", "assets/task_syn_006337/workspace/incoming/active/xenial_glade_3169_01.log", "assets/task_syn_006337/workspace/incoming/active/xenial_glade_3169_02.cfg", "assets/task_syn_006337/workspace/incoming/active/xenial_glade_3169_03.json", "assets/task_syn_006337/workspace/incoming/archive/xenial_glade_3169_04.md", "assets/task_syn_006337/workspace/incoming/active/xenial_glade_3169_05.json", "assets/task_syn_006337/workspace/incoming/active/xenial_glade_3169_06.md", "assets/task_syn_006337/workspace/incoming/active/xenial_glade_3169_07.md", "assets/task_syn_006337/workspace/incoming/archive/xenial_glade_3169_08.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006337` for the `billing review` scenario `xenial-glade-3169`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the billing review workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.cfg` whose byte length is at least 38, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: cefomet nariveu harijov zefobaw hakibax lusasay hadibaz posatua ditukib fofozec mesapod lupogue fohaluf pomenag rifodih hasamei safonaj dicevek tuvezel zenafom luluhan tukihao jokitup guzebaq riluyar posajos gunasat wohajou cejowov hapomew lutulux velubay potukiz zezemea pozeveb foluwoc tunazed povehae foguhaf havejog yazezeh hagudii bapovej zetujok lupolul hazeham wobanan tujonao turikip vekizeq hacebar cejokis tuhapot mewobau vezewov mebajow cedilux potufoy jonatuz fobahaa lusakib memewoc fomeced cefovee lugufof ripowog wozeceh naditui tugumej josahak fobaril popopom bavelun hametuo fonagup cebakiq jovepor tumenas habapot yapozeu turijov hanaluw jobakix nabavey fodikiz vetupoa rigukib lukivec cehagud ririyae mesanaf tubafog sariwoh sarinai hadikij fowohak.

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
