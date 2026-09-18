---
id: "task_syn_006142"
name: "Context continuation update 006142"
capability_family: "memory_retrieval_context_continuation"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003071"
generator_seed: 957254
workspace_files: ["assets/task_syn_006142/workspace/sessions/session_log.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006142` for the `incident follow-up` scenario `delta-yonder-3071`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read the session log file or files under `sessions/` and produce a context-continuation update. Separate durable preferences, current state, and stale items.

Scenario-specific audit anchors: tucemeg poyayah banahai jogumej kiririk vevegul wobarim kihawon haririo luwohap dikisaq dibacer dituces jorigut guyatuu wozesav zeluwow jojonax dituguy zediluz jomekia lukibab ceyajoc bameced vejozee johayaf nasapog zejoyah tusafoi jorivej tuvecek tufowol pozevem sazedin zezeguo zeharip lutuluq wofoyar jojoris kisahat lujokiu guhahav jodibaw mezedix megucey yanavez bazemea luposab tucefoc dihazed zericee bahasaf habapog tuvenah divekii jonazej didirik sasacel mepoham sarilun yabapoo jorijop hacezeq hahaver yazekis cekiwot wovefou nazeyav bafosaw zenajox luhanay rijocez zegumea dikirib gunacec dibahad dizezee tuhayaf bayagug hajohah polurii vemecej hadiluk dituvel nacemem yarilun hadirio bahakip kicetuq nakinar ribames kicevet dihaveu cehahav yabavew difolux.

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
