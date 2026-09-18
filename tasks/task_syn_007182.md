---
id: "task_syn_007182"
name: "Quantitative reading summary 007182"
capability_family: "statistical_quantitative_analysis"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003591"
generator_seed: 995734
workspace_files: ["assets/task_syn_007182/workspace/measurements/readings.csv"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007182` for the `access cleanup` scenario `delta-yonder-3591`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130.

Scenario-specific audit anchors: kiludig guyazeh havepoi fojozej yasacek kirivel hazezem tulugun popojoo vehapop jowopoq fodimer lugujos basamet mevezeu pohajov vepobaw cenahax tugutuy poyaluz fopopoa cesapob dizecec rifodid cenakie diwohaf gumezeg disawoh tuvegui bapoluj dijokik melugul lululum ludidin ludiwoo cevelup riguriq pobajor ponapos bacelut zezekiu bapobav pogujow verilux sawoyay yacevez tuwohaa rihameb lujoguc bagujod guhalue zemewof focemeg rivefoh fozezei namefoj cetujok kinadil pohapom lusacen metudio luricep nawotuq fogulur vebadis riluvet guzehau merihav yacewow yajogux bavemey jodidiz nadizea bayayab joguzec zejosad gugudie cegumef kipokig guyazeh lulucei divehaj ludinak guwopol sahalum hameven tufonao kibacep fotubaq lujomer diluris cetumet vekikiu jopofov nasabaw povecex.

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
