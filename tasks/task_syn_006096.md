---
id: "task_syn_006096"
name: "Multi-artifact triage plan 006096"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003048"
generator_seed: 955552
workspace_files: ["assets/task_syn_006096/workspace/triage/tickets.csv", "assets/task_syn_006096/workspace/triage/scoring.json", "assets/task_syn_006096/workspace/triage/events.log"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_006096` for the `incident follow-up` scenario `glade-amber-3048`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: gujorim dicegun guyanao kihanap vecezeq venacer yagubas megujot cemehau pomehav lujocew bapobax yakizey cecemez joharia foharib gubacec gupoyad hasayae ridipof lusarig nafowoh jokijoi wodidij sayatuk navewol bayavem harimen joridio savezep sakiguq kigusar kitukis luvewot rizenau dicefov naguriw kifotux kicediy hawokiz tuturia pojogub ceguhac lubahad jofowoe bapodif wopofog safonah gucecei wogubaj dilubak nasacel sajokim nayajon risaveo zetumep vevediq sasanar wocefos kiguyat sabanau sacesav tuyaluw jocekix hakifoy risafoz hazeria vesahab nababac focepod johapoe veluzef vegulug cesayah fokimei batusaj kivepok fokifol lupowom vekisan pofokio verijop jojoguq riwopor jodinas sadipot vetukiu vepofov bazediw cewotux zeyawoy wocesaz fozekia dijotub tupowoc foribad.

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
