---
id: "task_syn_006369"
name: "Generate record transformer 006369"
capability_family: "code_generation"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003185"
generator_seed: 965653
workspace_files: ["assets/task_syn_006369/workspace/spec/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006369` for the `vendor intake` scenario `nimbus-violet-3185`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 64. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 84, otherwise `watch`. Sort by code. Write the implementation to `submission/solution.py`.

Scenario-specific code anchors: fopoguz foyayaa rivehab foyadic diririd riyakie zehacef pocezeg jowoyah diyazei hajotuj foriyak yalumel yanacem guwodin yanaveo disatup ludikiq ceribar guzelus diditut cediwou rizeyav lurituw joporix yapojoy safohaz cecelua jogufob nadiguc pojopod rizebae wosadif dikibag baposah habayai yavecej difovek tudihal cehaham turidin cerisao fokilup hayaveq sapover yabakis tufogut bayabau dicewov kipojow wopopox rimejoy naguguz jokicea cetuzeb balumec cewonad najogue riyawof namegug batuluh vesanai sapodij tutumek rikiyal foyawom hajohan wojoluo rifoyap vezehaq fobarir jobadis kiforit habariu potudiv tunafow sapotux sahasay popobaz wojokia wokinab cepozec zemenad jomezee rijosaf bafokig samedih nabasai zekikij jovecek wonamel vepogum vefokin luhario pocerip zerinaq.

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
