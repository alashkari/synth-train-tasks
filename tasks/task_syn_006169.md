---
id: "task_syn_006169"
name: "Active file manifest 006169"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003085"
generator_seed: 958253
workspace_files: ["assets/task_syn_006169/workspace/incoming/archive/ripple_ripple_3085_00.json", "assets/task_syn_006169/workspace/incoming/active/ripple_ripple_3085_01.json", "assets/task_syn_006169/workspace/incoming/active/ripple_ripple_3085_02.cfg", "assets/task_syn_006169/workspace/incoming/active/ripple_ripple_3085_03.txt", "assets/task_syn_006169/workspace/incoming/archive/ripple_ripple_3085_04.md", "assets/task_syn_006169/workspace/incoming/active/ripple_ripple_3085_05.txt", "assets/task_syn_006169/workspace/incoming/active/ripple_ripple_3085_06.log", "assets/task_syn_006169/workspace/incoming/active/ripple_ripple_3085_07.cfg", "assets/task_syn_006169/workspace/incoming/archive/ripple_ripple_3085_08.cfg"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006169` for the `access cleanup` scenario `ripple-ripple-3085`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: kinanah yatuzei pomezej riyakik vewozel kitujom sajohan pozenao cezeyap baribaq dipoyar tuhadis kidiwot vewowou lutukiv kijotuw fobayax yamewoy guririz wotuyaa josakib wofotuc kizehad kisazee zeguwof nadilug disarih hasarii foyawoj jofofok riludil sanayam lumerin rimezeo turikip tucemeq nazejor tunawos pocevet jovetuu pocefov cenaguw dituhax lululuy najoluz lukifoa dinajob gutufoc tuditud zeritue haricef zezeveg jodijoh veluzei salurij ribavek cebabal dikinam nazedin metunao mewosap yasaguq guzegur sajopos pofolut melunau wocehav rivebaw yapoyax gusajoy jotukiz kifojoa mekinab sagusac melujod turitue yacedif luwogug nacedih potufoi kiyacej vemekik sadijol riyaham yajonan fofozeo pozerip fosapoq balufor forimes zehajot zeforiu zewokiv cetuhaw wovepox mesatuy.

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
