---
id: "task_syn_007161"
name: "Generate record transformer 007161"
capability_family: "code_generation"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003581"
generator_seed: 994957
workspace_files: ["assets/task_syn_007161/workspace/spec/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007161` for the `knowledge-base upkeep` scenario `tundra-brisk-3581`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 46. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 66, otherwise `watch`. Sort by code. Write the implementation to `submission/solution.py`.

Scenario-specific code anchors: yahadil diyanam hacedin zeripoo naguzep rikiveq fosanar gubaves jomelut gutukiu zecejov vepotuw wovecex velusay natutuz vezemea poluveb yaluyac poluved wopofoe mehayaf lupopog lufoguh hacedii kiwodij joyamek kituhal hazerim pozekin folujoo rimefop jonawoq yagufor saguces diditut cebaveu turipov dibajow jowosax gufobay mesasaz pojokia tubaceb yaguyac didiyad fofotue nadivef ritumeg wojosah dipohai poporij vewoyak dibacel posanam zejocen sasario zehamep saguluq batujor zehames kirizet mewomeu nalupov barivew gujorix kiluzey cekiguz celunaa nakijob lutusac wodihad diworie riripof yadipog fobadih ripomei jowonaj hariwok foyajol luvezem ceveban pohasao ditugup lusahaq jogujor wowowos sadizet lubayau mezevev didicew diyanax hasapoy mekiguz woyatua tusameb gunabac.

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
