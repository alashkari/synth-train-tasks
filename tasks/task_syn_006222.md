---
id: "task_syn_006222"
name: "Quantitative reading summary 006222"
capability_family: "statistical_quantitative_analysis"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003111"
generator_seed: 960214
workspace_files: ["assets/task_syn_006222/workspace/measurements/readings.csv"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006222` for the `access cleanup` scenario `ripple-delta-3111`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130.

Scenario-specific audit anchors: vebazei naveluj zefobak mepofol woharim lujofon jojofoo yavejop gujowoq focemer tulubas vediwot lufoluu satuyav guhaguw rinatux vebajoy sabadiz tutuwoa yakipob pobatuc najotud sagunae tufocef tutuzeg mebasah hahapoi sacedij vemenak badiril barijom tutuyan zesabao potuwop sagutuq lubabar yamejos fodirit cepoluu zesahav womeguw cepomex jonatuy dikicez vezebaa zewotub guwozec yatuzed ponamee pojohaf merizeg baludih rimecei wotufoj yanapok wocemel hayagum pobagun yabatuo vetulup jotufoq jojonar jonaces kibayat porifou fowosav vefowow tudibax rinariy ribakiz vemegua nafoyab sazezec tugurid celunae vehamef sayazeg cewonah kihanai kikiyaj poyanak rizetul mesajom kikigun nasaguo zebafop diceguq dimerir zelukis zekihat fobahau bafodiv zejosaw rinabax jovekiy tuhamez.

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

Capability focus: `statistical_quantitative_analysis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
