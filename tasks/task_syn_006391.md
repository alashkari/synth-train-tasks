---
id: "task_syn_006391"
name: "Briefing extraction 006391"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003196"
generator_seed: 966467
workspace_files: ["assets/task_syn_006391/workspace/notes/briefing.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006391` for the `access cleanup` scenario `yonder-delta-3196`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material.

Scenario-specific audit anchors: zehahav kilupow yaguhax zedijoy diyavez hakinaa kikinab sakijoc woyawod yakibae batuzef vemelug sasajoh gutupoi hasavej tumenak bagugul tumejom ridigun worinao hacezep luluzeq tukikir banagus zemeyat saluluu fohamev sajofow cetuhax zebacey yahatuz ditunaa narigub vejovec melumed napolue kifohaf velunag vetujoh poribai wodikij mewocek pomecel kikitum nadicen woyaguo tuvebap bamezeq nasamer tukives wodimet lutuhau mesaluv cehajow basapox foluhay savesaz fogunaa mekidib wotubac bawojod gujomee wokicef basakig ponahah riyamei fodijoj jozerik fonamel fovejom guzefon tuyayao lunabap naguceq gutumer yaposas wotuhat vecezeu hafocev jonapow powosax kinasay sarimez mebadia luyagub dijokic jotuyad kipodie cefopof riluhag wowoguh wozesai kiworij zesaguk fokitul lumezem.

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

Capability focus: `unstructured_document_analysis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
