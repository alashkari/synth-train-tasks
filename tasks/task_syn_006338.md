---
id: "task_syn_006338"
name: "Active file manifest 006338"
capability_family: "file_directory_operations"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003169"
generator_seed: 964506
workspace_files: ["assets/task_syn_006338/workspace/incoming/archive/xenial_tundra_3169_00.txt", "assets/task_syn_006338/workspace/incoming/active/xenial_tundra_3169_01.json", "assets/task_syn_006338/workspace/incoming/active/xenial_tundra_3169_02.cfg", "assets/task_syn_006338/workspace/incoming/active/xenial_tundra_3169_03.cfg", "assets/task_syn_006338/workspace/incoming/archive/xenial_tundra_3169_04.json", "assets/task_syn_006338/workspace/incoming/active/xenial_tundra_3169_05.cfg", "assets/task_syn_006338/workspace/incoming/active/xenial_tundra_3169_06.md", "assets/task_syn_006338/workspace/incoming/active/xenial_tundra_3169_07.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006338` for the `customer migration` scenario `xenial-tundra-3169`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the customer migration workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.md` whose byte length is at least 45, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: kizefou tunavev kigucew luwozex joceriy tudimez joguyaa cevefob cefosac pozejod naripoe joveyaf saluveg vebayah hapojoi zetujoj cepojok gutugul hafodim hamekin woguceo wofopop hagudiq kilukir polukis zewosat zesadiu hasamev nabafow fodigux cefopoy wowodiz nahayaa hafowob jobawoc nagusad nazecee jodikif lurigug bariguh vevezei zegukij merivek meyafol satukim wofohan gupopoo sasadip vefoyaq vejopor fodizes zebabat napoveu pomevev yabahaw tusanax risahay disakiz fokifoa sakigub fozedic ritufod sawotue sayayaf vejojog ricejoh didigui yadirij turidik fonafol luzekim kituhan fodiceo mezerip wotuhaq vedifor zenadis meriwot safodiu fohabav guveluw polumex gudifoy gukiriz sajosaa gudimeb gujocec lurikid yabapoe saworif mekinag saluguh dibahai jomeluj sabapok balucel.

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
