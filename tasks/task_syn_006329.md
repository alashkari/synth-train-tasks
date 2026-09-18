---
id: "task_syn_006329"
name: "Constraint schedule build 006329"
capability_family: "planning_scheduling_constraint_satisfaction"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003165"
generator_seed: 964173
workspace_files: ["assets/task_syn_006329/workspace/plan/constraints.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006329` for the `incident follow-up` scenario `tundra-juniper-3165`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Create a deterministic schedule from `plan/constraints.json`. Process tasks in listed order, honor dependencies, start at the given workday hour, skip tasks with impossible dependencies or non-positive duration, and report finish time.

Scenario-specific audit anchors: zesapol luvefom kifonan povedio ceguyap foceyaq guwocer dirizes bahafot womeyau najokiv hakinaw guzecex guwozey wonacez sarinaa lukipob cefofoc lubarid tuhapoe ripokif kilugug tulusah sadizei pobakij cedihak dijodil nazenam tutucen risawoo ceyarip pobafoq gukibar cedijos jokitut woluluu meyariv poyamew kimejox fowomey jovemez turigua mejobab vedivec mevehad sajotue hasatuf dikitug gutuhah ceyanai mefonaj hadiguk mecelul zemekim povefon pomejoo mehabap jojopoq yayanar dibagus hatucet poluwou yafoluv mesatuw safodix tuluriy ripobaz veyalua tubakib jotupoc bafofod lubadie rijofof fosasag tuluceh gukizei tuzedij mefokik jonaril pojopom wohanan dihameo pozeyap woceluq nakisar zepotus banayat gupopou ceriyav josamew jonacex kigupoy bapowoz zeyacea jogugub ceyaluc.

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

Capability focus: `planning_scheduling_constraint_satisfaction`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
