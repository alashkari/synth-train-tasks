---
id: "task_syn_007993"
name: "Active file manifest 007993"
capability_family: "file_directory_operations"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003997"
generator_seed: 1025741
workspace_files: ["assets/task_syn_007993/workspace/incoming/archive/tundra_delta_3997_00.cfg", "assets/task_syn_007993/workspace/incoming/active/tundra_delta_3997_01.json", "assets/task_syn_007993/workspace/incoming/active/tundra_delta_3997_02.log", "assets/task_syn_007993/workspace/incoming/active/tundra_delta_3997_03.log", "assets/task_syn_007993/workspace/incoming/archive/tundra_delta_3997_04.txt", "assets/task_syn_007993/workspace/incoming/active/tundra_delta_3997_05.log", "assets/task_syn_007993/workspace/incoming/active/tundra_delta_3997_06.txt", "assets/task_syn_007993/workspace/incoming/active/tundra_delta_3997_07.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007993` for the `customer migration` scenario `tundra-delta-3997`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the customer migration workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.md` whose byte length is at least 45, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: yadicel pobajom kijowon nafowoo vejofop jowodiq jowosar riyasas wonayat tusasau lukinav zejobaw popotux vedipoy joriguz kikiwoa babagub vewosac saguyad rididie jotuvef vebagug difozeh vehacei wojotuj lusanak yavefol gubafom bajotun kiguhao cemewop batuyaq nacelur sasasas zedimet rihameu jonawov cehafow nabacex pozejoy jotukiz diluvea gujolub yasaric bawogud posavee pofoluf gufosag jodidih zewohai ponadij lupoluk yadiyal tubamem pometun medihao yasapop yapohaq naritur riwomes badicet baluhau rihazev luzejow sahasax zesariy dijoriz potugua mepopob bazedic jojodid diyapoe tubayaf mewomeg kinahah kivewoi halunaj yafohak didibal gukizem kizecen tunaveo rizeyap kimenaq hajotur naluzes nagudit jomeriu foripov satuhaw bamehax dihahay gumediz kiyasaa saceveb jolucec.

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
