---
id: "task_syn_007995"
name: "Structured table normalization 007995"
capability_family: "structured_data_transformation"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003998"
generator_seed: 1025815
workspace_files: ["assets/task_syn_007995/workspace/tables/source_records.csv", "assets/task_syn_007995/workspace/tables/region_map.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007995` for the `training roster` scenario `umbra-brisk-3998`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Transform `tables/source_records.csv` using `tables/region_map.json`. Keep only active rows with `units * unit_cost >= 145`, uppercase each id, map regions to zones, sort by zone then id, and report how many malformed rows were skipped.

Scenario-specific audit anchors: cesayan verijoo woguhap vemeriq dihajor riguwos mewokit wonameu wowosav cegudiw cenajox ceforiy jokipoz forilua ludiceb namekic banamed yahapoe sasatuf jojoveg rifosah zekibai tufoluj wonaguk ceyagul vewotum guluhan poluwoo divefop yameveq meharir kimebas halutut hawotuu rijobav najonaw cefogux fosatuy zehahaz kiwosaa bawopob rilufoc meguced tufosae poyayaf guwobag tuceceh sawodii ripopoj nasajok pomenal nahalum nazetun wotubao sakisap tuyadiq kitugur kikimes kitufot vehayau yabapov vehapow lujowox joluvey menaluz sayadia sapofob ritujoc harinad turiwoe mehapof hamefog povedih tudilui veyapoj kicepok haritul womevem nasatun dijozeo womecep joveveq yalujor rinabas cemewot polukiu natutuv zevetuw diwowox guhacey vehahaz vezeyaa melunab hagupoc rijomed vedigue.

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
