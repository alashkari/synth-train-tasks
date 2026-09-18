---
id: "task_syn_006193"
name: "Active file manifest 006193"
capability_family: "file_directory_operations"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003097"
generator_seed: 959141
workspace_files: ["assets/task_syn_006193/workspace/incoming/archive/delta_delta_3097_00.cfg", "assets/task_syn_006193/workspace/incoming/active/delta_delta_3097_01.md", "assets/task_syn_006193/workspace/incoming/active/delta_delta_3097_02.log", "assets/task_syn_006193/workspace/incoming/active/delta_delta_3097_03.log", "assets/task_syn_006193/workspace/incoming/archive/delta_delta_3097_04.txt", "assets/task_syn_006193/workspace/incoming/active/delta_delta_3097_05.txt", "assets/task_syn_006193/workspace/incoming/active/delta_delta_3097_06.txt", "assets/task_syn_006193/workspace/incoming/active/delta_delta_3097_07.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006193` for the `customer migration` scenario `delta-delta-3097`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the customer migration workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.md` whose byte length is at least 45, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: dipowof baponag cebabah poturii naluguj nafosak veceril vevetum yavenan batumeo hahafop jotujoq rijobar gurinas zekiyat vefohau mecebav joceyaw wosavex kifobay jozeriz vekivea woluceb porizec jorifod tucebae riceguf nakifog vetuzeh tuyakii lubajoj cevetuk tujokil melukim tupowon jobario bavepop wonariq kiyapor velupos dizecet foturiu cesayav poyakiw rizenax tuvehay dihaguz wocecea posapob wosanac gujoved tuyalue nadinaf haluzeg ribatuh veluwoi vevenaj yanakik fowowol tuyakim podidin sametuo yaturip lukikiq guhalur hahajos bawowot joyatuu hanayav luyanaw wowodix yazeriy veyawoz nacejoa bawoyab yayabac saceved woririe nahayaf menagug cemekih nasadii hanasaj yayanak gulugul ririham medijon bahawoo bazelup cekihaq cecerir velubas hajohat vehadiu saceluv jogucew.

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
