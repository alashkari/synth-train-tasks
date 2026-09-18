---
id: "task_syn_006314"
name: "Active file manifest 006314"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003157"
generator_seed: 963618
workspace_files: ["assets/task_syn_006314/workspace/incoming/archive/lumen_summit_3157_00.md", "assets/task_syn_006314/workspace/incoming/active/lumen_summit_3157_01.json", "assets/task_syn_006314/workspace/incoming/active/lumen_summit_3157_02.cfg", "assets/task_syn_006314/workspace/incoming/active/lumen_summit_3157_03.txt", "assets/task_syn_006314/workspace/incoming/archive/lumen_summit_3157_04.json", "assets/task_syn_006314/workspace/incoming/active/lumen_summit_3157_05.json", "assets/task_syn_006314/workspace/incoming/active/lumen_summit_3157_06.txt", "assets/task_syn_006314/workspace/incoming/active/lumen_summit_3157_07.log", "assets/task_syn_006314/workspace/incoming/archive/lumen_summit_3157_08.cfg", "assets/task_syn_006314/workspace/incoming/active/lumen_summit_3157_09.txt", "assets/task_syn_006314/workspace/incoming/active/lumen_summit_3157_10.cfg"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006314` for the `access cleanup` scenario `lumen-summit-3157`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: rivetuw mekikix fopowoy gujobaz cetuwoa zekibab rivevec pogujod zejocee meluguf mejogug woguwoh tulurii mehafoj gufojok fojovel pozedim kimelun bawonao nawokip gunaveq vehazer narilus vehayat nagumeu zejocev tubafow mewoyax dikisay johaguz porigua yawobab vezeric hazerid vehanae gukicef wozefog zedibah popoyai posasaj dibasak fonawol zesatum sadiban gulujoo kitusap saribaq wobawor guluces kivelut cenaveu zepoluv mejoyaw memefox wosafoy cesaguz fofopoa pokizeb riposac lujobad megukie hadiyaf tuwosag banakih lujozei hanakij bakimek nacefol womepom guritun yawoguo riwodip dirihaq vemekir yaporis jogutut ditudiu fodiwov lupokiw veyabax dipozey guhadiz gukipoa bajodib naveguc poyahad zeditue jocerif mezekig joluhah ceponai ritubaj gukibak nadimel bacekim veluban.

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
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.

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
