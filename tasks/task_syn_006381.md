---
id: "task_syn_006381"
name: "Context continuation update 006381"
capability_family: "memory_retrieval_context_continuation"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003191"
generator_seed: 966097
workspace_files: ["assets/task_syn_006381/workspace/sessions/session_log.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006381` for the `inventory audit` scenario `tundra-cedar-3191`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read the session log file or files under `sessions/` and produce a context-continuation update. Separate durable preferences, current state, and stale items.

Scenario-specific audit anchors: lujojol wozegum yahatun guhanao zebazep dituwoq fovenar mezetus veluhat posafou foguriv woludiw guyagux kilupoy bagufoz safowoa tufonab vemejoc jobadid wobasae dirisaf wogumeg riwohah nafodii kikibaj habanak focelul sabaham sacewon fozenao hajorip cetunaq luzetur sahasas kiludit hazebau wowofov cetumew megumex bakituy wosazez mepoyaa foditub bapocec gurisad mebadie poluluf bakisag meyarih guverii hawodij diwohak luribal kibajom yatuyan gugujoo yabahap podituq bayamer tupoves zeguvet gunahau kidijov wokimew womenax fokiwoy najodiz mezeria sadiveb tuguguc bagupod vehacee yafosaf wozelug vebapoh hawovei joyaguj riwojok podibal dibazem johapon lusameo sawodip baguzeq pomegur tumesas natufot guwoluu badiluv wohariw zezesax fowovey luceguz rimetua natuwob luriyac.

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
