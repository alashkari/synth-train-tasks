---
id: "task_syn_006207"
name: "Captured source synthesis 006207"
capability_family: "web_information_gathering_source_synthesis"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003104"
generator_seed: 959659
workspace_files: ["assets/task_syn_006207/workspace/captured/page_a.md", "assets/task_syn_006207/workspace/captured/page_b.md", "assets/task_syn_006207/workspace/captured/page_c.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006207` for the `policy review` scenario `keystone-juniper-3104`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Use the captured source files under `captured/`; do not fetch live pages. Select the metric value by preferring a reviewed source and using latest date only as a tie breaker. Report conflicting metric values and cite the selected file.

Scenario-specific audit anchors: ribadit zekiriu zetuvev jojoriw vedifox zemefoy lujofoz vehatua josatub menasac wodisad yayamee fojofof cevelug pozenah mecevei fotuguj woceyak zenacel podipom bapofon banaceo gukirip cesapoq mebarir wozelus sakikit popofou ririsav riricew wonacex fovenay ribajoz jogunaa bavesab forikic dinawod ricerie jozefof zewofog cesanah kigufoi luzehaj jobafok wodifol vevezem poditun kiceveo wojoyap dituguq veguver guhagus yayafot meyadiu mezeyav mebavew fojogux rivehay fobadiz cejogua cezehab zevehac tufojod risacee diguguf nalulug hagurih ririjoi nalurij lufoyak guhajol turifom vefohan sapopoo halurip bayabaq rijorir yaripos kivedit dizeluu hananav cetuzew gusayax nadiriy saluluz dirihaa hacenab ponawoc bazeyad dibabae zevevef yariceg yadisah risasai nahapoj wovevek.

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
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.

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

Capability focus: `web_information_gathering_source_synthesis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
