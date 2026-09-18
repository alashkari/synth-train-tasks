---
id: "task_syn_006275"
name: "Repair record transformer 006275"
capability_family: "code_debugging"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003138"
generator_seed: 962175
workspace_files: ["assets/task_syn_006275/workspace/src/buggy_module.py", "assets/task_syn_006275/workspace/tests/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006275` for the `queue triage` scenario `summit-xenial-3138`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

`src/buggy_module.py` is intended to satisfy this behavior: Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 70. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 90, otherwise `watch`. Sort by code. Write the corrected implementation to `submission/fixed_module.py` with the same public function.

Scenario-specific code anchors: mesaguj lulutuk bafodil fokicem woyaven rigujoo hajosap foyajoq gujover hakinas yabasat kidikiu verizev sajokiw tutupox verijoy dikiyaz medipoa vefozeb nafoluc cedived bahatue zebapof bavejog rihameh wokipoi jocehaj podikik wogufol gurivem dihafon tulufoo jojoyap rijowoq wobagur sarihas guluvet vepodiu tudiriv fosajow dizewox satuhay vedizez rimecea podiwob mehanac jozebad pozejoe bapoluf joriveg babanah posadii luvenaj ritufok banadil hapogum tubafon diridio batudip lurihaq basatur zeposas yayabat sacetuu sajokiv tusayaw gubatux tutubay cefowoz pocetua fopoveb zegumec zekijod naguwoe zecepof gunakig guvemeh mekitui luyayaj naluguk lujohal fovepom woyacen hahadio turiwop hayahaq naluyar poguris jotupot kigumeu sadiguv ritutuw bawotux basabay wojotuz wojopoa.

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

Capability focus: `code_debugging`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
