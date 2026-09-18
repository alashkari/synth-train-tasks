---
id: "task_syn_007989"
name: "Context continuation update 007989"
capability_family: "memory_retrieval_context_continuation"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003995"
generator_seed: 1025593
workspace_files: ["assets/task_syn_007989/workspace/sessions/session_log.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007989` for the `billing review` scenario `ripple-yonder-3995`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read the session log file or files under `sessions/` and produce a context-continuation update. Separate durable preferences, current state, and stale items.

Scenario-specific audit anchors: baluzeh meyavei pobabaj ririzek hatunal wofodim menafon woriguo focezep vefodiq cefodir focegus hajogut batukiu hakibav satuhaw vevezex nafokiy kirisaz mesaria pozepob sapofoc dijotud sawomee nazeyaf diponag dibapoh vetusai vejozej ririkik saguzel tukigum diluhan woyameo hawohap rizeguq gusamer cevesas nacenat yapozeu cetupov dirinaw nayamex cehajoy gukivez worikia lunakib rilutuc zedijod pokigue yahavef worihag zevepoh mejojoi lubahaj pomehak yabazel nazebam havezen yavehao cemejop jomehaq ririwor fofoyas pobafot kigutuu jotucev yabanaw mehasax gubapoy bapobaz nakizea tutuveb zenatuc tudihad rilurie zegufof yapofog wosaceh ritusai womeluj kirikik ricedil venasam ceritun vetubao vehagup cezebaq worizer sayahas kibadit yagudiu havepov tudikiw hanabax poyatuy.

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

Capability focus: `memory_retrieval_context_continuation`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
