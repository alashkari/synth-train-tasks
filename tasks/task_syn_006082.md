---
id: "task_syn_006082"
name: "Generate record transformer 006082"
capability_family: "code_generation"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003041"
generator_seed: 955034
workspace_files: ["assets/task_syn_006082/workspace/spec/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006082` for the `training roster` scenario `zenith-ripple-3041`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 52. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 72, otherwise `watch`. Sort by code. Write the implementation to `submission/solution.py`.

Scenario-specific code anchors: foguyay dimehaz dikinaa povejob sameyac yanagud gucelue diluyaf risaceg yapohah sarisai sajojoj tuhahak vebatul kiyalum poyajon cecezeo gubabap mejojoq zemejor tunames ribakit hawoveu tuluyav joluyaw nabavex dibapoy jowobaz cejodia wojogub yawofoc sananad sariwoe jofofof cesameg foyaluh fomerii wolukij vepowok foriyal yavefom polutun nasaceo wotulup dibazeq woposar sanabas yawonat meceluu veguyav kisahaw kibazex yacezey bajodiz tufonaa folujob cevenac lulumed kiverie dipotuf cenawog hanakih tuworii poyacej fofotuk sametul zetuzem fodirin fodipoo balusap focediq fohatur kitusas sakivet tufonau wojosav yayatuw yayatux woridiy zezesaz mekidia yagupob dizebac ridiyad yameyae tuyaluf cewolug vesameh kihapoi zepoyaj wopocek natulul zevenam wodiban dijosao diluzep.

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
