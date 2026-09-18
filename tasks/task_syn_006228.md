---
id: "task_syn_006228"
name: "Repair record transformer 006228"
capability_family: "code_debugging"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003114"
generator_seed: 960436
workspace_files: ["assets/task_syn_006228/workspace/src/buggy_module.py", "assets/task_syn_006228/workspace/tests/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006228` for the `vendor intake` scenario `umbra-juniper-3114`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

`src/buggy_module.py` is intended to satisfy this behavior: Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 58. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 78, otherwise `watch`. Sort by code. Write the corrected implementation to `submission/fixed_module.py` with the same public function.

Scenario-specific code anchors: kicepoo digucep veribaq guhagur vepopos fodibat sadidiu kipohav cehazew cebagux fowocey cepohaz hasalua zeharib vejomec luwojod tuyatue mebavef pojorig mebaceh rikizei rikiluj vevebak nayazel tudikim rizezen popodio disapop tusahaq jonapor jokices bazekit mepohau verijov mejovew gubakix samepoy narifoz yalubaa mejomeb haluzec vefogud hayakie tuhapof gunadig satujoh jojofoi yakipoj fopotuk lupogul zepofom poyahan poyayao vecevep kibaluq yawozer wohayas mezerit metuzeu bawofov pokikiw kicehax cetupoy kigumez luluzea zerijob lukibac didihad jovehae yagubaf bafofog vebaceh wotuvei ditusaj sapozek fobafol hagupom rimepon bavemeo johabap vehaceq bacenar nawosas jojolut sahaceu worimev luricew lukihax kihaluy nabaluz fonabaa joditub nafocec rijokid tulucee focemef.

The submitted Python file must use only the standard library and expose the requested public function.
Keep the implementation deterministic and handle malformed records by skipping them when the behavior description implies a numeric conversion.
Run or reason through the visible cases before finishing.

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
