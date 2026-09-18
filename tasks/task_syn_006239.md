---
id: "task_syn_006239"
name: "Multi-artifact triage plan 006239"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003120"
generator_seed: 960843
workspace_files: ["assets/task_syn_006239/workspace/triage/tickets.csv", "assets/task_syn_006239/workspace/triage/scoring.json", "assets/task_syn_006239/workspace/triage/events.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006239` for the `customer migration` scenario `amber-keystone-3120`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: sawofoz zeveyaa dikiceb rimeyac bazegud dikihae guveluf fohagug vezenah zewonai kidikij halukik didibal haribam vekifon diluluo kihabap harituq safover gumeris wotunat tufoveu hadipov zenafow wobajox safojoy sasajoz guhabaa zetubab namenac nacerid sapowoe saluvef safotug yalukih fozebai sakinaj hafoguk dibapol kikijom sapojon kijorio guharip risaveq pohajor jonames lusadit fohajou riyadiv jonavew vezejox kiririy fofonaz jozeria cevepob vewoyac yacebad vejobae cesamef pofojog sawosah bawokii tugucej nadicek yatuzel vemekim gumejon yawojoo lupobap digupoq jowotur luyadis wobatut yazesau sadivev tukiyaw riyazex dicebay gukisaz hahapoa guguzeb woyakic hayaved yaripoe kihayaf satuyag cehajoh megumei naluguj vejovek cewovel wozebam luvesan nazemeo pofodip tuguceq.

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

Capability focus: `multi_tool_workflow_orchestration`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
