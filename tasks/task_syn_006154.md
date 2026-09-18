---
id: "task_syn_006154"
name: "Generate record transformer 006154"
capability_family: "code_generation"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003077"
generator_seed: 957698
workspace_files: ["assets/task_syn_006154/workspace/spec/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006154` for the `vendor intake` scenario `juniper-harbor-3077`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 64. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 84, otherwise `watch`. Sort by code. Write the implementation to `submission/solution.py`.

Scenario-specific code anchors: cekiris porimet namefou medisav mediyaw vebazex lurifoy tulupoz guvemea kivekib meforic poluved bayanae sarikif pobajog kicesah focelui folutuj lusabak menaril ditunam hahacen kilutuo bameyap rituguq gupoyar rigumes cejowot nazeguu poluriv mezecew bazezex pocetuy fojomez megudia hafobab bametuc wozesad pokitue guzehaf mesadig yatunah hafozei zemecej kiwopok zepokil sawoyam vekipon wowozeo yawobap melukiq halukir gucebas luyapot veyadiu kiwovev rikipow gucedix nasayay vegumez gusafoa kitulub lubatuc difogud cevecee narituf nakijog tucejoh sazesai dihazej ritukik cekicel porijom medigun mejohao vefodip navepoq nabalur memetus hatucet verituu dicepov yatuyaw zedizex fobaguy bacewoz bayacea fokinab yaveric bafomed kipopoe ponahaf fodilug gugusah bavenai vediguj.

The submitted Python file must use only the standard library and expose the requested public function.
Keep the implementation deterministic and handle malformed records by skipping them when the behavior description implies a numeric conversion.

# Expected Behavior

A correct solution writes the requested Python module under `submission/`, exposes the requested function, passes the visible cases, and generalizes to structurally similar hidden cases.

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

Capability focus: `code_generation`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
