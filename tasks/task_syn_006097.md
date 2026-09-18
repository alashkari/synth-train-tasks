---
id: "task_syn_006097"
name: "Active file manifest 006097"
capability_family: "file_directory_operations"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003049"
generator_seed: 955589
workspace_files: ["assets/task_syn_006097/workspace/incoming/archive/harbor_quartz_3049_00.json", "assets/task_syn_006097/workspace/incoming/active/harbor_quartz_3049_01.json", "assets/task_syn_006097/workspace/incoming/active/harbor_quartz_3049_02.log", "assets/task_syn_006097/workspace/incoming/active/harbor_quartz_3049_03.md", "assets/task_syn_006097/workspace/incoming/archive/harbor_quartz_3049_04.json", "assets/task_syn_006097/workspace/incoming/active/harbor_quartz_3049_05.json", "assets/task_syn_006097/workspace/incoming/active/harbor_quartz_3049_06.cfg", "assets/task_syn_006097/workspace/incoming/active/harbor_quartz_3049_07.json", "assets/task_syn_006097/workspace/incoming/archive/harbor_quartz_3049_08.cfg"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006097` for the `billing review` scenario `harbor-quartz-3049`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the billing review workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.cfg` whose byte length is at least 38, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: rifojon guhayao sahavep yaguguq zedirir luvegus rinatut joguceu riwovev wosatuw wocesax joyatuy zeyanaz nagufoa zeluyab diyahac pokidid balunae bawokif cecetug jobafoh luwozei lukizej jobayak rizefol guriwom fogulun sacetuo vetuvep yazeriq tukinar sayanas bahajot ririmeu veyabav pocecew hazezex yaluluy tuwoluz gurizea cehafob lunadic guluyad dinajoe tupoyaf kizegug cezewoh yadilui hadijoj mevedik fojobal yacekim hahalun najomeo verikip meriyaq yalujor fofokis jojobat josapou guriyav vepojow podinax dibabay wocevez joluzea yatusab vevesac difotud tuvesae lupodif potudig ribajoh fokivei vepohaj zepojok jodisal mekirim wogufon halufoo pobalup meveluq zebayar dinasas hapowot forifou barifov tubariw halumex kimediy tutuluz difosaa rilunab nanajoc womefod nafobae.

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
