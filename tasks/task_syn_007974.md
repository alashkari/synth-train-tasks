---
id: "task_syn_007974"
name: "Quantitative reading summary 007974"
capability_family: "statistical_quantitative_analysis"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003987"
generator_seed: 1025038
workspace_files: ["assets/task_syn_007974/workspace/measurements/readings.csv"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007974` for the `training roster` scenario `juniper-delta-3987`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130.

Scenario-specific audit anchors: diyajos popotut hafoguu savewov divesaw sahapox foyapoy zenaluz hatuhaa kiforib womesac ririsad fosahae foluvef mewofog haluguh fotului guwodij ridibak tupogul zefofom jonajon samebao hawosap jobajoq foceyar sasaves tuverit bakiluu rijopov fokijow tuwopox vehasay mepoyaz vepohaa rizetub turikic vezenad fosajoe dijovef vefobag riwoguh cericei yaguvej bawoyak nanadil meharim sanazen mehadio yaturip tumezeq luwomer venaris zesawot yakisau nazetuv havekiw kizedix navehay zegubaz jokinaa lujoveb tunafoc tudived cezejoe zesasaf hawoveg yafotuh lupocei sacemej yarifok fosaril fokikim nawowon hanameo megubap nayasaq cezelur kibames guhafot megusau sametuv ricecew nazetux mevepoy rijotuz forinaa bacenab johahac verimed jocecee wonanaf zebadig gubasah medilui rifofoj.

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
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.

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
