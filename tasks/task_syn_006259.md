---
id: "task_syn_006259"
name: "Professional update transformation 006259"
capability_family: "professional_communication_content_transformation"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003130"
generator_seed: 961583
workspace_files: ["assets/task_syn_006259/workspace/drafting/raw_notes.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006259` for the `release readiness` scenario `keystone-glade-3130`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, excluded distractors, and the intended tone. Do not invent commitments not present in the notes.

Scenario-specific audit anchors: mesarit wozepou vefojov halubaw vezehax gutufoy pobabaz lujokia zepoceb luceguc harilud dicejoe nalusaf jocedig cesawoh rilunai sazefoj luzeyak mesawol zefoyam divesan yasaceo basakip kirijoq tukirir vediris luwopot poponau zelunav hazemew kibajox luripoy dimediz vedizea wokinab tufoguc powolud jojojoe rihawof gunakig mebajoh fogunai hapoluj saguhak rifokil cebatum tutuhan cesaceo rimeyap zehajoq tuyayar cegugus nakigut podimeu sanabav gumejow cerikix luwomey ripoyaz nafotua riveyab lufofoc habasad folutue nadiluf barilug hatuveh vebayai vewokij bapomek zebanal tubayam yagucen jovejoo luguwop fosaveq zemejor fojokis jokitut nazehau zenabav kijocew cebajox lutunay banaguz joveria zezekib dikipoc satunad poluvee tugupof lucepog hacepoh gugului nasaguj guwofok.

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
