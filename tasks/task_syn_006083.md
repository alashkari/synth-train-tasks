---
id: "task_syn_006083"
name: "Repair record transformer 006083"
capability_family: "code_debugging"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003042"
generator_seed: 955071
workspace_files: ["assets/task_syn_006083/workspace/src/buggy_module.py", "assets/task_syn_006083/workspace/tests/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006083` for the `vendor intake` scenario `amber-willow-3042`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

`src/buggy_module.py` is intended to satisfy this behavior: Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 58. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 78, otherwise `watch`. Sort by code. Write the corrected implementation to `submission/fixed_module.py` with the same public function.

Scenario-specific code anchors: tuzeluz ceyatua vezefob sasamec tumerid napovee rihavef diwosag gusahah focejoi gukiguj jotupok zetufol fonawom gunarin tuvejoo fohanap jowojoq gucesar guturis luyabat pojoyau kiyariv vepobaw cerilux saveyay yanahaz joforia kigulub sajotuc sabakid wofosae dihapof tuyagug hadijoh meguvei podijoj sayacek lujopol rifosam vewoyan nayafoo tugukip rikiyaq jonayar yajogus popovet sabaguu poyazev podipow zetulux ludidiy cehawoz vetujoa celupob bamewoc zevemed kisague jodidif sarijog venajoh bazegui yamehaj riwofok cefolul sagugum jovepon hajopoo mejozep sayapoq nakisar dihazes balupot rikiwou sayadiv cepowow fopodix savemey fokibaz hasaria lucehab nameguc jowojod yamemee josamef diwohag nagupoh bawonai dicehaj baluhak zenasal riwoyam sanaven wohanao rilurip sayajoq.

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
