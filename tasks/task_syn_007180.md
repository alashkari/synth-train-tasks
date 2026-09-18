---
id: "task_syn_007180"
name: "Structured table normalization 007180"
capability_family: "structured_data_transformation"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003590"
generator_seed: 995660
workspace_files: ["assets/task_syn_007180/workspace/tables/source_records.csv", "assets/task_syn_007180/workspace/tables/region_map.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007180` for the `training roster` scenario `cedar-amber-3590`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Transform `tables/source_records.csv` using `tables/region_map.json`. Keep only active rows with `units * unit_cost >= 145`, uppercase each id, map regions to zones, sort by zone then id, and report how many malformed rows were skipped.

Scenario-specific audit anchors: poyawoe diturif kibagug guyazeh hamejoi pozekij guririk sasavel pozefom zepomen yaguhao nahasap kihayaq lugucer gucedis cedirit kibanau gululuv wofoyaw kiyajox napovey metufoz safodia cebahab kidiguc bafodid tupohae vesavef yahagug satunah lutucei basanaj kipomek hafoyal vecefom fopotun tufotuo kihapop pofoguq woditur zevefos yafosat ripowou jovehav metuguw yapotux bazebay lutuguz wometua riluzeb ceturic cecesad lupofoe tugucef kitubag pobahah merinai samejoj satukik lubasal vedibam focehan bayameo nanamep dilumeq luvedir sakihas luguhat vepoguu pozebav kirizew guhakix riyanay jotuyaz hafogua pohakib melubac disapod ripotue rivenaf jonabag banadih nalufoi vejoyaj folukik kiharil verisam vebajon velunao digurip fozefoq vewomer safomes rizerit nawojou tubahav.

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
Before finishing, verify that the output agrees with the relevant fixture files and record the check in `verification`.
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.
Some supplied information is intentionally irrelevant; exclude it from the result.

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

Capability focus: `structured_data_transformation`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
