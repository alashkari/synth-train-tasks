---
id: "task_syn_006090"
name: "Constraint schedule build 006090"
capability_family: "planning_scheduling_constraint_satisfaction"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003045"
generator_seed: 955330
workspace_files: ["assets/task_syn_006090/workspace/plan/constraints.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006090` for the `release readiness` scenario `delta-willow-3045`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Create a deterministic schedule from `plan/constraints.json`. Process tasks in listed order, honor dependencies, start at the given workday hour, skip tasks with impossible dependencies or non-positive duration, and report finish time.

Scenario-specific audit anchors: hacefog wolujoh kibasai sasayaj najojok pomemel forikim yayakin sayawoo bakilup sagudiq kifotur josaces jonawot riyaluu velusav wotuwow tupomex meluzey riwohaz ceponaa yajowob dijoyac foyalud riwozee zebamef mebajog sakiwoh zebarii jocefoj tusarik jowofol fomenam nahayan dinadio kituwop satuluq cedizer jogugus ceribat fonakiu dipovev zeripow sasanax lunatuy zegubaz yaluwoa dituhab rihaluc dituyad menacee bacebaf wocepog pomeluh cegusai wosadij joverik cenamel wonagum vekiven zeposao kifocep sagutuq yanajor mebajos haguyat cegujou natunav vesabaw tugulux navezey cebakiz gufovea dilusab medimec gujolud mekidie meluluf tulujog sazefoh veworii metuwoj vevefok jokiwol fojojom cebaven lufojoo hanalup natuveq nabajor nakilus vefomet polukiu woguzev yazejow hadihax.

Create `submission/result.json` using this shape:

```json
{
  "result": { ... family-specific deterministic values ... },
  "evidence": ["relative/source/path.ext"],
  "verification": {
    "checked_files": 1,
    "status": "pass"
  }
}
```

Use relative evidence paths from the workspace. Keep lists sorted when the prompt describes a sort order.
Some supplied information is intentionally irrelevant; exclude it from the result.

# Expected Behavior

A correct solution reads the supplied fixtures, performs the requested transformation or analysis, writes `submission/result.json`, cites relevant relative evidence paths, and records deterministic verification details.

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

Capability focus: `planning_scheduling_constraint_satisfaction`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
