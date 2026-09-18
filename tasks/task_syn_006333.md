---
id: "task_syn_006333"
name: "Context continuation update 006333"
capability_family: "memory_retrieval_context_continuation"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003167"
generator_seed: 964321
workspace_files: ["assets/task_syn_006333/workspace/sessions/session_log.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006333` for the `release readiness` scenario `violet-brisk-3167`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read the session log file or files under `sessions/` and produce a context-continuation update. Separate durable preferences, current state, and stale items.

Scenario-specific audit anchors: folujop meguhaq yalukir bavedis naguyat cesameu venaluv podizew powovex verisay guhamez gubazea mecewob guvekic yacehad kikiwoe kirihaf ribafog zewowoh kitumei zelunaj ririkik gupojol dicegum hahalun zenasao vevelup nameveq tubawor luturis tuyafot hazesau jowokiv tuluhaw gusafox badituy kifocez sabakia diripob cemejoc mevekid rijoyae mezebaf vewodig wofoyah yatumei baguwoj celusak tubahal guhadim wosarin ceyadio tujokip wovekiq yajomer wolugus pozepot mewokiu venajov wocehaw joriwox nagujoy jokipoz pozeria basaveb difopoc hakikid rizevee sahavef bakikig wocerih cehabai kivehaj tumehak wozegul ribawom dijotun popotuo joritup haluveq lumemer sadijos kiyafot hahaveu kigumev safocew sagukix zeveyay woluwoz lufolua kisatub vesasac povefod tukibae zeyafof sahazeg.

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
