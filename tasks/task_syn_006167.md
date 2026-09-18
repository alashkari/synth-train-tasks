---
id: "task_syn_006167"
name: "Multi-artifact triage plan 006167"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003084"
generator_seed: 958179
workspace_files: ["assets/task_syn_006167/workspace/triage/tickets.csv", "assets/task_syn_006167/workspace/triage/scoring.json", "assets/task_syn_006167/workspace/triage/events.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006167` for the `release readiness` scenario `quartz-nimbus-3084`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: saposaf jotupog zewowoh gupokii ridiyaj lulumek wowobal zesagum fovepon luwoguo rigukip dijomeq diguyar posakis wogutut luveriu sanakiv rifoluw halufox lukipoy zebaguz guzeyaa tuyajob wopohac yanagud babapoe risazef lubameg kimekih powomei natumej poveyak tugulul sazekim jojoban hasahao dizecep yadimeq batuyar jojomes hajobat vepoceu sacezev vejoyaw dicekix rifoluy lulupoz kicetua luvejob kibaric nayabad foyapoe mewohaf fojozeg fotumeh fotumei cecekij safohak kigubal gupoham halulun cegusao digupop meyahaq gubakir zewohas tubabat tuzefou natuguv memekiw nafodix wovekiy riyasaz nayagua yafoceb riguguc hadized yayavee yavezef hazelug jovekih bazemei zewokij fosafok cegujol jogufom poyanan vediveo pozedip foveluq guguyar gudiris medirit riveluu disazev fozeyaw.

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

Capability focus: `multi_tool_workflow_orchestration`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
