---
id: "task_syn_006321"
name: "Generate record transformer 006321"
capability_family: "code_generation"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003161"
generator_seed: 963877
workspace_files: ["assets/task_syn_006321/workspace/spec/visible_cases.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006321` for the `knowledge-base upkeep` scenario `prairie-quartz-3161`.
Use only the supplied workspace files. Do not fetch live data or use credentials.

Implement `transform_records(records)`. Keep records whose status is `active` and score is at least 46. Return dictionaries with uppercase `code` and `bucket`, where bucket is `priority` when the score is at least 66, otherwise `watch`. Sort by code. Write the implementation to `submission/solution.py`.

Scenario-specific code anchors: navedid hamegue tusarif naririg fodinah guyarii worifoj rimenak tufopol kikidim joluyan zesapoo melusap lutujoq guvecer tuhalus wojonat nadinau saguyav foveguw diyasax verikiy hawokiz jogusaa jonanab jotukic kinamed hamepoe yaceluf kidisag kiyanah baguhai veyacej lukiyak hawodil rinanam jogukin pobanao hadirip jobazeq luzepor ririlus ridikit yaturiu sazevev wozeluw lusakix menamey kivesaz zezedia yadirib hajobac zetumed metudie gunapof foyaceg cediwoh namegui vehazej zebaguk kiwovel vesarim jokiwon zewojoo luyadip fozeceq rijorir nadidis cecesat pohaceu luyaluv hawohaw folulux pobariy folukiz womefoa tuwomeb bacenac nasalud veforie powodif cejoveg woyabah lucepoi zenapoj nacecek kiwokil zekicem riyaban guzepoo yanagup potukiq yayalur tuzeris rihalut zetuzeu.

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
