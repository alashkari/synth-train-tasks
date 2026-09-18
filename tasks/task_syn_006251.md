---
id: "task_syn_006251"
name: "Repair record transformer 006251"
capability_family: "code_debugging"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003126"
generator_seed: 961287
workspace_files: ["assets/task_syn_006251/workspace/src/buggy_module.py", "assets/task_syn_006251/workspace/tests/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006251` for the `training roster` scenario `glade-lumen-3126`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

`src/buggy_module.py` is intended to satisfy this behavior: Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 46. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 66, otherwise `watch`. Sort by code. Write the corrected implementation to `submission/fixed_module.py` with the same public function.

Scenario-specific code anchors: womecel safokim wojonan vebadio poluyap tuguluq poyazer haluces hahayat rigujou metujov nazeyaw fobayax wosawoy zediriz wosalua kifowob celubac vecewod guriyae dipofof zediwog rihakih jobasai sapohaj havezek kihalul zesapom vebanan satuveo pohapop naceceq tufokir zedilus fomewot dizeceu melufov wotuwow nazewox kiluguy jolufoz hacedia tuwoceb sapopoc pomekid yayarie guzejof gusajog ceguveh luriwoi gumedij gunadik rikijol lutupom yarilun fobazeo nagurip fozebaq pobacer jocegus kicenat wokiyau foguluv zefofow kituyax foluzey navehaz woguvea zeceyab mepovec nabazed mesafoe yanaguf ditukig tubameh haluwoi wopotuj guyayak joluzel vebatum riwoban nayafoo hadifop gujomeq jozepor vekilus vevewot wojohau yapovev veyazew yalumex yalunay didifoz tudipoa lubaveb harikic.

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

Capability focus: `code_debugging`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
