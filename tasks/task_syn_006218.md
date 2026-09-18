---
id: "task_syn_006218"
name: "Active file manifest 006218"
capability_family: "file_directory_operations"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003109"
generator_seed: 960066
workspace_files: ["assets/task_syn_006218/workspace/incoming/archive/prairie_onyx_3109_00.txt", "assets/task_syn_006218/workspace/incoming/active/prairie_onyx_3109_01.json", "assets/task_syn_006218/workspace/incoming/active/prairie_onyx_3109_02.cfg", "assets/task_syn_006218/workspace/incoming/active/prairie_onyx_3109_03.json", "assets/task_syn_006218/workspace/incoming/archive/prairie_onyx_3109_04.json", "assets/task_syn_006218/workspace/incoming/active/prairie_onyx_3109_05.json", "assets/task_syn_006218/workspace/incoming/active/prairie_onyx_3109_06.cfg", "assets/task_syn_006218/workspace/incoming/active/prairie_onyx_3109_07.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006218` for the `customer migration` scenario `prairie-onyx-3109`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the customer migration workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.md` whose byte length is at least 45, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: zeritue difoguf yapolug lumewoh digumei foriyaj venacek joyakil bagufom hakicen poveveo saluwop yawoluq fovekir jovetus bayapot bafoguu vemecev sazeriw woluyax tucesay lusapoz nahagua difonab tunabac ridigud lupocee kidirif medirig ricesah fojohai barituj gutuluk lucelul guyasam bazerin meyaluo tugugup zepobaq johayar pojopos luzezet gukisau nabariv salupow salukix hadinay joyamez wozetua nadimeb posavec kilumed luhavee zegujof jorinag namenah zejocei tuyabaj dibahak lukiril pofowom cesacen kijoceo hafomep wonazeq tudilur fomesas diridit cenameu yafonav nanazew baguvex bawoluy zelupoz pomenaa zewomeb pokinac sadiced habafoe vevewof tuyadig polubah kivenai vemezej povetuk gujokil sabatum sagurin popoguo kidikip fobatuq ludiyar yasalus tutuyat nazeveu wokifov.

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
