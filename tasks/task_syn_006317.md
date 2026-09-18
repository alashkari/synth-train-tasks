---
id: "task_syn_006317"
name: "Quantitative reading summary 006317"
capability_family: "statistical_quantitative_analysis"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003159"
generator_seed: 963729
workspace_files: ["assets/task_syn_006317/workspace/measurements/readings.csv"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006317` for the `access cleanup` scenario `nimbus-nimbus-3159`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130.

Scenario-specific audit anchors: zebavez jogulua wotupob ditudic yavekid cekifoe basapof hadiwog jopokih kigusai riridij hadinak didisal sasagum ririzen jokijoo woricep woriceq memedir tumeves yaluhat zenazeu dijomev mepoguw nadimex focefoy sawowoz posamea zeyayab gucefoc bacewod vepohae sajomef mehadig ripojoh nadimei safodij kipodik fobasal cegudim hahatun rinaluo luyadip tusadiq hagubar hatubas sacevet nanatuu gufopov habacew dilurix barizey rihaguz hamekia dinalub sanayac fopojod jorimee luwobaf yadizeg nawosah gusayai lutudij fowozek yabasal fovegum yadinan lukiguo diluhap kimediq hafosar memeris forimet cemefou savediv foporiw porivex cehaluy lumevez mesagua hafolub meceyac dimehad jowopoe yabasaf hapoveg medijoh dikinai kiwovej zetutuk zegudil rigunam kicesan nakifoo sadiwop tunatuq.

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
