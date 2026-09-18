---
id: "task_syn_006168"
name: "Multi-artifact triage plan 006168"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003084"
generator_seed: 958216
workspace_files: ["assets/task_syn_006168/workspace/triage/tickets.csv", "assets/task_syn_006168/workspace/triage/scoring.json", "assets/task_syn_006168/workspace/triage/events.log"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_006168` for the `billing review` scenario `quartz-glade-3084`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: wofojog yapoguh kifonai josavej diceluk hatumel joyatum memedin nazekio yayafop fosaceq zehalur savebas popogut zeveceu guvesav jodiyaw zememex kihakiy kijopoz yamevea bacezeb vekivec celulud fozelue pojowof ripoyag rijopoh naricei jojoguj najopok zerisal zeworim narikin bapoceo kipolup gucesaq joveyar veyazes tujohat meguguu kiworiv zeluzew kisalux wonapoy basakiz rimenaa sazegub guyajoc halurid fojovee gubaluf yarinag cekiguh kihajoi yakimej hakifok jopovel gumeham foyaven bavenao sakihap posabaq tujobar zenalus yavecet hapopou sapoluv lugusaw riwotux kifohay diluvez pokihaa mecehab wokiluc potufod fowozee pobaluf lupoyag gugukih ceyacei ludimej gunakik medidil cemewom dijosan luyaceo vekidip sacezeq wocefor bakizes yakigut wodiguu ririfov pomejow rijokix.

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
Before finishing, verify that the output agrees with the relevant fixture files and record the check in `verification`.
Some fixture labels use Spanish words such as accion, riesgo, and resumen; normalize the final JSON keys in English.
This task may require continuing context across multiple session files.

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
