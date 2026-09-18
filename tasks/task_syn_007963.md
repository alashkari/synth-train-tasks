---
id: "task_syn_007963"
name: "Professional update transformation 007963"
capability_family: "professional_communication_content_transformation"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003982"
generator_seed: 1024631
workspace_files: ["assets/task_syn_007963/workspace/drafting/raw_notes.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007963` for the `incident follow-up` scenario `ember-brisk-3982`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, excluded distractors, and the intended tone. Do not invent commitments not present in the notes.

Scenario-specific audit anchors: navenah nabatui kibatuj gutuluk fohayal bapogum kijotun sajoluo zeguvep tubapoq tujohar kibabas metudit kizediu hawoyav navefow popodix posatuy jomebaz yadivea tujoveb fofojoc guguwod jopokie jotutuf yanasag nahafoh hafonai forinaj vesahak woworil bahanam bagufon nacedio luyamep menakiq tutunar rifomes kikibat jokiyau kisatuv namekiw vedimex tulufoy bavezez vedikia memefob bacevec cerinad dicevee gujopof hakigug lutufoh kivesai ripodij havefok wozejol woludim veriban hadibao jorijop tutunaq dirinar nayayas luyalut rimepou sajohav gudisaw luwozex bamepoy kiripoz dihasaa dikipob veceyac fokihad yazejoe diyaguf diwomeg cesafoh nazewoi baguyaj fopocek mejokil ridicem zehatun vemeguo fozebap hafoyaq rifomer merijos cevepot meribau kituguv hadiluw tufodix jowokiy.

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

Capability focus: `professional_communication_content_transformation`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
