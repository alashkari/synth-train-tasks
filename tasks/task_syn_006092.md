---
id: "task_syn_006092"
name: "Professional update transformation 006092"
capability_family: "professional_communication_content_transformation"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003046"
generator_seed: 955404
workspace_files: ["assets/task_syn_006092/workspace/drafting/raw_notes.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006092` for the `inventory audit` scenario `ember-prairie-3046`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, excluded distractors, and the intended tone. Do not invent commitments not present in the notes.

Scenario-specific audit anchors: kikitui dibaluj wotuluk forifol lubajom povelun sakibao sagudip polutuq bababar zenakis cebamet yavewou fonacev jodizew tucerix dimevey tutukiz vefohaa luwobab fofohac fosanad tuyamee wosayaf wocesag joyawoh foyabai wopovej sayajok menadil medidim turirin dikiwoo fojopop sakihaq yakiwor potufos mepohat tudikiu vebaluv jocetuw veceyax naturiy tuwomez rilumea fobaveb sariyac guzehad gugunae dicerif jomepog baceceh metuzei zeyafoj fosapok vepomel havemem guwokin tujosao lurilup sacekiq tukilur satunas hasarit luriguu mecewov fokiguw tuhahax kimecey pocediz hanawoa josayab poyaric gufofod wolujoe hawowof hasarig hafowoh yamerii dicezej havejok joturil celugum lupoven cesaveo nasavep guguhaq cepodir ribahas gusalut metupou tuwoyav nanahaw vefomex hagukiy dizeriz.

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
Before finishing, verify that the output agrees with the relevant fixture files and record the check in `verification`.

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

Capability focus: `professional_communication_content_transformation`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
