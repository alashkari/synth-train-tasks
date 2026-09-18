---
id: "task_syn_006260"
name: "Professional update transformation 006260"
capability_family: "professional_communication_content_transformation"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003130"
generator_seed: 961620
workspace_files: ["assets/task_syn_006260/workspace/drafting/raw_notes.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006260` for the `billing review` scenario `keystone-summit-3130`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, excluded distractors, and the intended tone. Do not invent commitments not present in the notes.

Scenario-specific audit anchors: kifoveu bacehav zejoriw johamex pojotuy rivediz ritugua natufob wopoguc dicelud zeriwoe gubabaf yariveg guhafoh sawotui nazejoj bajovek fosahal hagufom sasaven meluyao kinavep kiguyaq dibazer rikisas yametut mezekiu kizejov wopofow difohax gufoluy wowovez wofobaa mebanab sayadic turitud tuwocee fohatuf jodiwog gukijoh zekikii sayazej meguwok safowol jobanam zerikin kimeveo ribarip posameq gugunar luzelus hatuwot fopomeu gutukiv rihatuw fokizex velusay haguhaz mesayaa pohapob tudinac divewod jorimee habavef didizeg zelupoh samecei yatuzej bazecek fodidil guwodim fodinan mecetuo cevedip lurifoq namepor didisas povetut sasajou rididiv hadihaw fogurix hamefoy wohamez cekisaa yalugub mecetuc pozebad poyadie foponaf wotudig jojoluh ribagui mewozej woriguk cezeril.

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
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.
Some supplied information is intentionally irrelevant; exclude it from the result.

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
