---
id: "task_syn_006295"
name: "Briefing extraction 006295"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003148"
generator_seed: 962915
workspace_files: ["assets/task_syn_006295/workspace/notes/briefing.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006295` for the `vendor intake` scenario `cedar-onyx-3148`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material.

Scenario-specific audit anchors: nawobad guzemee kiharif gusawog woririh focekii dikisaj dikijok dilumel porimem dipohan josameo joritup tukimeq zedihar kitunas nanamet diriceu bajojov lutujow cejorix hameluy bananaz worisaa gumesab dimezec cesakid zezenae menatuf sanagug sakihah mehayai lukifoj halukik lulufol barizem yaguhan tupoceo memegup lulutuq diririr kizelus foyabat powopou bazehav kipojow sabasax bamebay gufohaz zerijoa bavejob veveguc zekijod nafogue banamef hafohag sadiwoh cekizei megucej badizek fotugul saceyam rihacen kijoguo safolup badijoq sarikir jodiyas sarihat vebajou hajopov polupow mewonax habatuy jogutuz riyavea rifoveb porimec woyayad fofolue badiwof fopofog kipoveh zebagui mebazej batumek turivel mevejom nayamen vewomeo meveyap gunayaq lumegur kimelus namelut riwoceu.

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

Capability focus: `unstructured_document_analysis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
