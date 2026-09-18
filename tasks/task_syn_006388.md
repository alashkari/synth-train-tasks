---
id: "task_syn_006388"
name: "Structured table normalization 006388"
capability_family: "structured_data_transformation"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003194"
generator_seed: 966356
workspace_files: ["assets/task_syn_006388/workspace/tables/source_records.csv", "assets/task_syn_006388/workspace/tables/region_map.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006388` for the `access cleanup` scenario `willow-ion-3194`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Transform `tables/source_records.csv` using `tables/region_map.json`. Keep only active rows with `units * unit_cost >= 119`, uppercase each id, map regions to zones, sort by zone then id, and report how many malformed rows were skipped.

Scenario-specific audit anchors: nafohas joditut hariveu nayahav mesanaw hayavex gutuwoy cetuzez vezehaa sayazeb mefokic vesayad salufoe nawomef diyalug luyajoh pobatui difofoj rikihak fotuvel hapoham povenan zeyaveo tuditup kituceq sabayar wocejos tuhapot foyaveu digutuv guceriw pokicex ribabay cevekiz pomelua sacefob zeluyac kinarid verinae safotuf cehaceg jodifoh luzehai didikij tubaluk johapol gudibam ceriban zevezeo yadigup nasazeq tusasar yajobas bazesat jomeceu yafotuv mebamew yazefox dituvey wocecez cerigua gubajob mejohac fojolud veguzee cewoyaf jopokig guhaguh riyamei vezerij mesafok cezetul riwomem cepomen dizeveo veyanap diwojoq foharir kiwofos cebamet kiworiu guzesav pojosaw veluwox ceyaluy gunawoz kikiria yapoceb zepotuc woguzed wojosae meharif wozelug wowomeh najovei yasarij.

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
