---
id: "task_syn_006215"
name: "Multi-artifact triage plan 006215"
capability_family: "multi_tool_workflow_orchestration"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003108"
generator_seed: 959955
workspace_files: ["assets/task_syn_006215/workspace/triage/tickets.csv", "assets/task_syn_006215/workspace/triage/scoring.json", "assets/task_syn_006215/workspace/triage/events.log"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006215` for the `access cleanup` scenario `onyx-ripple-3108`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Combine `triage/tickets.csv`, `triage/scoring.json`, and `triage/events.log` into a priority plan. Apply severity multipliers, subtract one point for blocked tickets, skip malformed event lines, and sort by score descending then ticket id.

Scenario-specific audit anchors: sadibab gudiguc lumefod venanae folusaf mecerig womeguh kiludii guhabaj kiporik fokinal wolukim rikiyan nafokio cehapop veveluq foyalur kiguces poyajot vemepou zefocev disatuw womedix yaguzey poripoz menajoa basasab hafocec fopodid merizee pohavef badidig wowozeh joguhai saluwoj mevefok rihayal cewonam fojocen lusatuo nabarip meveyaq fogusar woturis cefosat pokimeu guguluv vejosaw guyatux nahadiy jorimez bacehaa bamezeb yavedic hapozed sayajoe potucef menarig rijoceh yakihai satuguj jobakik cebafol yabalum luzemen rihahao jobacep yamefoq ceyawor hababas zejocet tuhahau zenanav zezeriw vejorix mediriy vedijoz fosalua vemetub tusatuc podized kihamee yajomef zegunag nadiyah vetuzei zewokij napovek mekihal cesasam povefon zekinao wotuzep rikijoq ceyagur batupos.

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
Some supplied information is intentionally irrelevant; exclude it from the result.

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
