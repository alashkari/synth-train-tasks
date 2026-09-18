---
id: "task_syn_007185"
name: "Generate record transformer 007185"
capability_family: "code_generation"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003593"
generator_seed: 995845
workspace_files: ["assets/task_syn_007185/workspace/spec/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007185` for the `policy review` scenario `frost-prairie-3593`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 70. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 90, otherwise `watch`. Sort by code. Write the implementation to `submission/solution.py`.

Scenario-specific code anchors: jodisaj rivehak meyajol gucecem lubakin poyatuo rikimep gusakiq vehagur sakisas cerigut vetuguu banayav vehatuw wogukix dizevey luguzez fokicea jobameb cemedic hadibad guyazee fozepof sazedig nadijoh bayamei menatuj merijok zeharil navewom yawoven mesario ribajop kizejoq jopohar zekifos dikipot kifokiu natucev fobakiw povehax yafovey kizevez guguvea zepoveb tujobac jodirid fogujoe didiluf cezebag bawowoh gusakii jolutuj rifozek fodiyal gumecem vewocen luhaceo dijokip bamepoq dipobar zedikis focelut mecepou tudiyav kidimew foveyax vegusay disatuz sasanaa digunab sayadic wocekid vemelue jotucef fotujog tubanah yaharii kimenaj ritusak luluyal pomerim bacesan gulubao diwogup tumezeq dibahar mepotus balugut pojoluu johaguv fowoluw cejosax cejonay foponaz popovea.

The submitted Python file must use only the standard library and expose the requested public function.
Keep the implementation deterministic and handle malformed records by skipping them when the behavior description implies a numeric conversion.
Ignore files or comments that do not describe the requested function behavior.

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
