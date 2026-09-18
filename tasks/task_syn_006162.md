---
id: "task_syn_006162"
name: "Constraint schedule build 006162"
capability_family: "planning_scheduling_constraint_satisfaction"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003081"
generator_seed: 957994
workspace_files: ["assets/task_syn_006162/workspace/plan/constraints.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006162` for the `queue triage` scenario `nimbus-ion-3081`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Create a deterministic schedule from `plan/constraints.json`. Process tasks in listed order, honor dependencies, start at the given workday hour, skip tasks with impossible dependencies or non-positive duration, and report finish time.

Scenario-specific audit anchors: ririmea wozehab guwonac kisakid cediwoe luhafof ripokig pozewoh savetui wocevej woceyak medigul kimejom josanan guhaceo lubalup povejoq rizelur lupogus yadiyat dicemeu lumevev gumediw babadix cefonay badijoz pohamea nayayab kivemec tukigud potutue wotuhaf guyawog tugutuh naponai poyakij pojojok tuyakil lugujom yayazen yahaluo sazeyap popodiq sadicer vevezes wometut yapofou zefodiv sajozew luwohax saguluy hameguz narijoa zevesab tuvejoc luvefod wogubae yatunaf cevewog nayatuh gudiyai gubarij nayayak zezenal bahafom banatun bacefoo potudip sacepoq cewokir cevemes tunajot cewomeu cesaguv fofovew lubakix gurikiy jolukiz namenaa luturib sabakic jogufod wolunae nafosaf tudirig zedimeh cemenai cebahaj tumebak cegudil vepofom kigugun posawoo melujop venapoq fokisar.

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
