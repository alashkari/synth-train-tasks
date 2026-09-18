---
id: "task_syn_006129"
name: "Generate record transformer 006129"
capability_family: "code_generation"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003065"
generator_seed: 956773
workspace_files: ["assets/task_syn_006129/workspace/spec/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006129` for the `vendor intake` scenario `xenial-xenial-3065`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 64. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 84, otherwise `watch`. Sort by code. Write the implementation to `submission/solution.py`.

Scenario-specific code anchors: vemebat yawoluu menapov hamecew luyabax guwodiy mejoriz hajofoa tumelub cenakic vedimed narifoe cekipof jobatug risakih tubapoi rinarij yaluvek dijobal badiyam jogulun nanabao wojokip nalupoq cerilur vepogus wopozet venapou kiwotuv bamejow halufox bagudiy pofoguz yasalua cezeveb lusabac ritujod safodie gulurif luhawog bafokih jonafoi tuzecej vecekik fozecel ritusam batudin jozeyao guyavep vediluq zebayar hasaces gufolut zezeyau saforiv mepocew sacetux vesasay lufonaz kifomea womepob tupocec nakigud lukiyae vedivef gufogug cebawoh zebalui zevezej lutunak hahakil mekizem kiponan didijoo pofoyap zeridiq napotur saponas rikivet yameluu vehapov mececew guwopox lupopoy sapohaz wobafoa zevelub cesaluc guyarid zehazee woluluf veluveg lukiyah mepoyai yagubaj verisak.

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
