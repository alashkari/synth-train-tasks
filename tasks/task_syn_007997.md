---
id: "task_syn_007997"
name: "Quantitative reading summary 007997"
capability_family: "statistical_quantitative_analysis"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003999"
generator_seed: 1025889
workspace_files: ["assets/task_syn_007997/workspace/measurements/readings.csv"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007997` for the `access cleanup` scenario `violet-ember-3999`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130.

Scenario-specific audit anchors: nawojop naworiq sapoyar vejodis vevegut cegusau vesaluv hapokiw pomehax wohasay sasacez tutucea medisab cetuwoc yaluzed cebasae diyanaf yafojog nawonah zepohai kibanaj tubabak cegufol hayamem kisalun safomeo jomedip riguzeq vepofor nasawos didisat jobakiu naveriv riririw guzehax guhapoy yafoluz pomelua vejomeb difopoc cerived namebae bahafof pokiveg nasaceh fonapoi kikimej cehayak gumenal naribam yazedin sasaveo vewohap tuzezeq jocetur lupowos mecegut pobajou gumeluv natufow guhamex zeveguy hakimez lucekia sacegub sapoguc jomeyad rilurie havejof pofodig ceporih gucetui nananaj didiyak cekibal jodizem yayahan fokirio rijoyap banahaq babayar kinabas memewot wodipou mewowov difowow fowosax zediguy nayawoz veyanaa dihalub kivezec nahazed ceyamee tucewof guluceg.

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
