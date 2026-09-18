---
id: "task_syn_007171"
name: "Professional update transformation 007171"
capability_family: "professional_communication_content_transformation"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003586"
generator_seed: 995327
workspace_files: ["assets/task_syn_007171/workspace/drafting/raw_notes.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007171` for the `queue triage` scenario `yonder-delta-3586`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, excluded distractors, and the intended tone. Do not invent commitments not present in the notes.

Scenario-specific audit anchors: pofomev dinatuw diyadix sadiwoy hasavez zesayaa mewoceb kijowoc jocesad mefotue guvesaf luwonag vefofoh sazeyai kidimej medihak cecejol fofoham hawopon yaveceo joyagup zecediq mejosar veyazes celusat nafoluu lukiwov bamewow yaturix kibahay cejokiz gufobaa luzetub nasadic zebakid zenazee nanahaf mekirig ponameh kivefoi hapozej fobamek woveyal banawom yasanan kikizeo mejobap pobayaq bazelur dicejos zevebat wobasau polumev kiwokiw vecezex kibamey sapoguz pogutua vefojob guvetuc ripohad jovehae yajonaf barisag tukituh lulufoi dipozej baluzek basajol medifom kijowon gubahao vezezep ripojoq kivetur gulukis memebat verizeu kiwofov zewoyaw fowogux namecey fozewoz cediria badigub yazecec dijolud cepovee tusabaf posayag tuporih rihazei popovej fowozek diwobal tudivem.

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
