---
id: "task_syn_006231"
name: "Captured source synthesis 006231"
capability_family: "web_information_gathering_source_synthesis"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003116"
generator_seed: 960547
workspace_files: ["assets/task_syn_006231/workspace/captured/page_a.md", "assets/task_syn_006231/workspace/captured/page_b.md", "assets/task_syn_006231/workspace/captured/page_c.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006231` for the `vendor intake` scenario `willow-ember-3116`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Use the captured source files under `captured/`; do not fetch live pages. Select the metric value by preferring a reviewed source and using latest date only as a tie breaker. Report conflicting metric values and cite the selected file.

Scenario-specific audit anchors: yaludir mewolus jokikit yadijou woribav wojomew podizex yabamey pocemez rinahaa guveveb veluguc narisad nacewoe lupoguf samebag jorihah wohavei luwoluj zelumek zegumel sahamem sapogun vevewoo luyasap tuzezeq rinadir jonawos wodilut ridikiu nafovev ricejow narijox poyasay zewotuz megujoa risalub habamec sayakid yapogue bagutuf riwojog rimeluh bazegui vetukij gukihak wocecel bapodim gulusan sajofoo diporip ludituq jobagur jomenas fozefot fobayau hadivev jovefow samewox kijotuy nawoluz mesayaa woribab meyaluc babamed hacehae hafohaf bazelug tunahah merihai vewoluj mebahak zevepol melukim lurisan kifofoo zezegup jozefoq nawonar pozegus tumepot yayaguu cececev yafowow riturix bafopoy poceriz jocezea hajobab wogutuc fopodid ritupoe jodidif tujogug guceguh fovegui.

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

Capability focus: `web_information_gathering_source_synthesis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
