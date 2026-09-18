---
id: "task_syn_006212"
name: "Professional update transformation 006212"
capability_family: "professional_communication_content_transformation"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003106"
generator_seed: 959844
workspace_files: ["assets/task_syn_006212/workspace/drafting/raw_notes.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006212` for the `inventory audit` scenario `mosaic-amber-3106`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, excluded distractors, and the intended tone. Do not invent commitments not present in the notes.

Scenario-specific audit anchors: satucey metuvez posafoa dilusab dizeyac johakid mewobae jocetuf hazedig bamebah mewotui celuguj folumek babapol celufom gufodin bacefoo fosatup mediceq yatuhar kiwohas rizerit sanasau hakiyav zerifow satusax havehay kicejoz ceguwoa fotuveb vejodic pocesad haveyae baribaf cezejog yabakih samevei jovepoj badivek poceril merinam guzekin wogutuo vehazep mehanaq veguyar nagugus vezesat saguluu difofov lugumew yaritux veguzey bavediz gunakia lunahab gufomec habagud cevewoe jocekif hafozeg yayayah mevelui rivezej tubajok yajohal namecem gulunan tutuwoo cekikip satuyaq sabadir nafotus didimet vetutuu tupokiv cepotuw hadisax divetuy zehawoz medizea zerikib yacedic yaridid hadizee bapovef cepoveg zezefoh venayai tudiwoj hajokik powocel bagunam joriban zefoguo gumefop.

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
