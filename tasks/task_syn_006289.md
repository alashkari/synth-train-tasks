---
id: "task_syn_006289"
name: "Active file manifest 006289"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003145"
generator_seed: 962693
workspace_files: ["assets/task_syn_006289/workspace/incoming/archive/zenith_delta_3145_00.cfg", "assets/task_syn_006289/workspace/incoming/active/zenith_delta_3145_01.log", "assets/task_syn_006289/workspace/incoming/active/zenith_delta_3145_02.cfg", "assets/task_syn_006289/workspace/incoming/active/zenith_delta_3145_03.md", "assets/task_syn_006289/workspace/incoming/archive/zenith_delta_3145_04.md", "assets/task_syn_006289/workspace/incoming/active/zenith_delta_3145_05.txt", "assets/task_syn_006289/workspace/incoming/active/zenith_delta_3145_06.md", "assets/task_syn_006289/workspace/incoming/active/zenith_delta_3145_07.txt", "assets/task_syn_006289/workspace/incoming/archive/zenith_delta_3145_08.cfg"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006289` for the `access cleanup` scenario `zenith-delta-3145`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: kiwobax sahazey guveriz sazegua tuhameb dijodic hamenad lutukie powopof tuluzeg foyasah bavetui lufovej dikicek poyahal habasam guyapon jokipoo woyazep narizeq wotucer yarices bamejot habatuu yacejov zesanaw poworix wobawoy diluriz guwoyaa salumeb guzefoc yazedid baluvee nasasaf fomehag yajosah zehakii sapowoj satumek bahawol haluvem rimefon womehao nayavep ponabaq meriwor sahalus kijowot yarinau tufoyav dicetuw tudipox fokituy riyafoz fomeyaa pogurib merimec najodid sakigue zemebaf yasatug zeyadih zesasai tumeguj fopojok hajoril cejotum mewokin tuceyao divevep disabaq cehagur zehajos velujot hazefou kikiguv poluguw gusakix hafosay cebazez sawomea vevelub rinaguc ludived nacedie fomemef dibapog bahaveh pogucei potuhaj tusaluk mecepol vefosam zepoban mesario.

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
