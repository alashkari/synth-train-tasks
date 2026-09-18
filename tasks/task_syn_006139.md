---
id: "task_syn_006139"
name: "Professional update transformation 006139"
capability_family: "professional_communication_content_transformation"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003070"
generator_seed: 957143
workspace_files: ["assets/task_syn_006139/workspace/drafting/raw_notes.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006139` for the `release readiness` scenario `cedar-onyx-3070`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, excluded distractors, and the intended tone. Do not invent commitments not present in the notes.

Scenario-specific audit anchors: luyasad rifosae salukif fopopog vezeyah rivedii bajodij poyahak lubazel pofogum cewodin divemeo zejopop lubaceq lukiwor potuves harivet nazezeu josanav jobariw hayarix fopotuy rikituz pobavea bawotub yabakic fotuwod lusanae vetujof yaworig kiluyah pohagui pokiguj luguguk hanawol tuvecem diwopon rikimeo hadijop zevesaq nakifor dinagus lunajot gumefou celuwov fotupow savezex vevecey verituz risalua yafozeb hakipoc sahajod megulue rifokif safonag basaluh pomepoi jozefoj tujotuk yayahal ripogum cecekin gumedio wofonap gukikiq wotuver cegudis memebat meyaguu johapov hahavew kipohax verimey risadiz memewoa pokidib wonanac lukisad posakie zezefof bagupog guyatuh fojocei merisaj jopomek dizevel hadizem barifon bavedio vevecep focenaq jozefor zejopos verisat zekipou.

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
