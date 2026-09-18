---
id: "task_syn_007970"
name: "Active file manifest 007970"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003985"
generator_seed: 1024890
workspace_files: ["assets/task_syn_007970/workspace/incoming/archive/harbor_xenial_3985_00.txt", "assets/task_syn_007970/workspace/incoming/active/harbor_xenial_3985_01.cfg", "assets/task_syn_007970/workspace/incoming/active/harbor_xenial_3985_02.json", "assets/task_syn_007970/workspace/incoming/active/harbor_xenial_3985_03.log", "assets/task_syn_007970/workspace/incoming/archive/harbor_xenial_3985_04.txt", "assets/task_syn_007970/workspace/incoming/active/harbor_xenial_3985_05.log", "assets/task_syn_007970/workspace/incoming/active/harbor_xenial_3985_06.cfg", "assets/task_syn_007970/workspace/incoming/active/harbor_xenial_3985_07.cfg", "assets/task_syn_007970/workspace/incoming/archive/harbor_xenial_3985_08.md", "assets/task_syn_007970/workspace/incoming/active/harbor_xenial_3985_09.md", "assets/task_syn_007970/workspace/incoming/active/harbor_xenial_3985_10.md", "assets/task_syn_007970/workspace/incoming/active/harbor_xenial_3985_11.json", "assets/task_syn_007970/workspace/incoming/archive/distractor_007970.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007970` for the `knowledge-base upkeep` scenario `harbor-xenial-3985`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: tujoguo jonadip podipoq kizeyar rihajos zejovet tujohau wojojov fokiwow meharix rihayay tulufoz tuwozea dipodib jorifoc luzenad lurikie vetupof guwotug ricepoh dilukii diwoluj fotuyak sakilul diyaham gujoban vejobao kigugup nawowoq josahar kiceces wowogut yavemeu tuwoguv tuzeyaw yanafox nariwoy natupoz gukipoa cekinab fohayac tupoved wofozee cebaluf jofosag mefoyah poyafoi mebapoj guvehak cevecel fohatum dihamen lusafoo banajop kihaguq nalukir mekidis vececet cejofou didiguv jojodiw tukifox didiriy haribaz rikikia kifokib yawoyac ricesad memepoe wokicef cegunag cehafoh luvejoi rijohaj nabaluk meharil disavem tuporin mevenao dididip tubanaq mewocer porives pogubat banapou wozecev hayayaw zezewox lujotuy pofopoz kipolua kimelub lusapoc bazefod basazee pojorif.

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

Capability focus: `file_directory_operations`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
