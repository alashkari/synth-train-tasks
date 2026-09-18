---
id: "task_syn_006383"
name: "Multi-artifact triage plan 006383"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003192"
generator_seed: 966171
workspace_files: ["assets/task_syn_006383/workspace/triage/tickets.csv", "assets/task_syn_006383/workspace/triage/scoring.json", "assets/task_syn_006383/workspace/triage/events.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006383` for the `billing review` scenario `umbra-frost-3192`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: pomeven kiluyao jomelup wobayaq meforir luyaves lugukit pozeveu zepoluv batuhaw cetunax tuluvey powopoz vejobaa fojofob dikipoc ceguved kihacee mewocef batudig wozefoh celului kilujoj nakidik yahahal badirim gusafon rigukio wohagup riririq luzedir kikidis gululut cenahau mecewov bawowow gujodix dibariy powoluz zepodia lufozeb baharic nanafod powobae pobapof podipog womeluh sahawoi foguvej hamefok hayavel bakijom zeyakin rihadio mevefop sawoveq zevenar zevegus cewocet sakiguu vemediv jokiguw bagugux potumey najocez yacecea jorikib johaluc josamed sanayae gutubaf namelug sasasah bazehai jorituj zehanak powoyal tukimem kibafon josafoo wojobap mekiyaq bamever wohagus yaluzet yanasau wotuguv kifobaw pokimex tuwoluy hasayaz fotuzea fovehab johanac bavegud luyavee.

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
