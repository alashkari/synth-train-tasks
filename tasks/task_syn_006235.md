---
id: "task_syn_006235"
name: "Professional update transformation 006235"
capability_family: "professional_communication_content_transformation"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003118"
generator_seed: 960695
workspace_files: ["assets/task_syn_006235/workspace/drafting/raw_notes.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006235` for the `billing review` scenario `yonder-ember-3118`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, excluded distractors, and the intended tone. Do not invent commitments not present in the notes.

Scenario-specific audit anchors: pomeyav diguhaw gubawox cececey ponamez fokicea mevenab rilunac yadijod meturie menajof gucelug hababah balului kibavej nabajok bafobal zefokim ludinan cesaveo kifogup vewofoq pohatur wodiris cedimet woriyau gubazev sagufow jozeyax zevepoy ripozez riwoyaa tutujob bapofoc hagusad vezesae joyarif zenakig yaveguh natuyai zenajoj dicehak sakimel gumefom fonawon luzebao verikip tutuyaq popofor dilufos vekirit sawoluu harimev gupomew gufowox haguguy nameguz lulutua rihafob saricec gujobad kisasae kirizef mesagug balujoh yapopoi lujovej cetupok kirimel wodiham jolumen zetukio bajopop lutuyaq fobaver cezelus hagutut cefokiu samewov ludizew cemefox yahakiy jonacez gukizea nazerib zeworic zevemed vesafoe nanacef dicefog sawoluh jogumei tumefoj lubajok yalupol gululum.

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
