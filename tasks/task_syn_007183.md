---
id: "task_syn_007183"
name: "Briefing extraction 007183"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003592"
generator_seed: 995771
workspace_files: ["assets/task_syn_007183/workspace/notes/briefing.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007183` for the `training roster` scenario `ember-frost-3592`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material.

Scenario-specific audit anchors: hapodih woguwoi bajohaj kivebak riwovel vesagum ribalun dinaluo sadivep zeguluq zegunar fojodis nahatut posaveu yanayav zewojow rihagux disanay jotucez lupohaa meriyab porituc venafod woguzee sagufof kigubag gujotuh banayai gubayaj riwokik cevetul jovegum vewohan woluhao namedip cesameq vediwor mevebas rifoyat badiceu babamev saluyaw hagufox nabamey kikiluz tubatua bariyab divesac kicekid salutue difoyaf halulug tunameh mebapoi kituvej bafoluk woponal menakim narisan hawoceo babalup difoguq cehayar jorihas bafojot wogunau cebacev hafonaw tupoyax cejosay zehajoz ludifoa tuwodib hahatuc johapod pocedie cevekif hafojog yayapoh dicefoi tufosaj veceguk sajopol zejopom cefolun ludimeo foyajop dicefoq dicecer nasaces podiwot wocebau kicesav bahaluw yamecex tuyaluy.

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

Capability focus: `unstructured_document_analysis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
