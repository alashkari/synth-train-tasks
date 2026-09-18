---
id: "task_syn_006265"
name: "Active file manifest 006265"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003133"
generator_seed: 961805
workspace_files: ["assets/task_syn_006265/workspace/incoming/archive/nimbus_glade_3133_00.json", "assets/task_syn_006265/workspace/incoming/active/nimbus_glade_3133_01.cfg", "assets/task_syn_006265/workspace/incoming/active/nimbus_glade_3133_02.json", "assets/task_syn_006265/workspace/incoming/active/nimbus_glade_3133_03.txt", "assets/task_syn_006265/workspace/incoming/archive/nimbus_glade_3133_04.txt", "assets/task_syn_006265/workspace/incoming/active/nimbus_glade_3133_05.md", "assets/task_syn_006265/workspace/incoming/active/nimbus_glade_3133_06.md", "assets/task_syn_006265/workspace/incoming/active/nimbus_glade_3133_07.log", "assets/task_syn_006265/workspace/incoming/archive/nimbus_glade_3133_08.log", "assets/task_syn_006265/workspace/incoming/active/nimbus_glade_3133_09.json", "assets/task_syn_006265/workspace/incoming/archive/distractor_006265.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006265` for the `knowledge-base upkeep` scenario `nimbus-glade-3133`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: hasapoz bakisaa lubalub dijopoc diwogud yatuwoe pomemef menameg diyahah cevegui gujovej tulufok hanapol rifoyam gukiyan barisao meyabap luzemeq menajor lupoves hazesat fodidiu yaluyav vediwow yanakix banafoy wowoluz celumea gunarib tuvevec nanaced yavefoe vefomef cekipog woriguh tubadii vehajoj tubasak yadiwol ceribam povetun fowopoo focedip hahadiq difofor jowonas lumepot mebajou disadiv tujokiw rikilux megudiy metuzez ponaria lukidib kikizec foluced wometue cerikif jodisag gudizeh cefoyai yaguluj yayapok wotuvel cedisam velulun ceforio kiriyap kituluq mehalur nafofos halubat kiriceu cedicev cececew megugux didikiy ceyayaz sarimea gucemeb woguhac gufohad riposae fodicef lucetug womeluh yalupoi guvejoj pomemek jowodil veyasam cenatun luhanao yatuhap woguguq.

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
