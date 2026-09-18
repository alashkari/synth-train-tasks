---
id: "task_syn_006367"
name: "Briefing extraction 006367"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003184"
generator_seed: 965579
workspace_files: ["assets/task_syn_006367/workspace/notes/briefing.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006367` for the `knowledge-base upkeep` scenario `mosaic-mosaic-3184`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material.

Scenario-specific audit anchors: zesapox bagukiy bakijoz hamemea bayahab fonahac rifomed jowonae celuluf foririg vesadih luzemei dirituj tufoluk ririwol jozekim zezehan yalufoo popoyap baforiq sagunar vebakis fofopot joveveu kitukiv diponaw cerilux gumesay tucekiz fowozea nabawob joluwoc pokigud guhapoe ribasaf badibag nawojoh pohatui celuvej jobabak vehadil tubanam kikirin vediceo cevejop fodiyaq turicer hapowos kiyadit kidiyau yafofov nayapow hajokix vekijoy fonabaz gululua bamepob tunatuc navepod zenajoe guvehaf zezekig hapozeh hapogui tucefoj luguguk hakidil lubazem ceyadin vehapoo bawolup balunaq tuhajor joluyas tufosat yadiyau jopohav vemeluw foturix sakipoy hafopoz metunaa nayaveb kibajoc mehafod jocekie fozedif meguwog jozedih cezemei rivetuj hakizek riwojol fosacem jolupon sarituo.

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

Capability focus: `unstructured_document_analysis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
