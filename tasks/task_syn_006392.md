---
id: "task_syn_006392"
name: "Briefing extraction 006392"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003196"
generator_seed: 966504
workspace_files: ["assets/task_syn_006392/workspace/notes/briefing.md"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_006392` for the `knowledge-base upkeep` scenario `yonder-mosaic-3196`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material. Treat `[accion]` as an action and `[risgo]` as a risk despite the shorthand spelling.

Scenario-specific audit anchors: jofomew cejoyax ditusay fodituz nameyaa jorijob riyasac yaveyad tuyapoe haworif focepog hafoluh dibajoi cerijoj kicerik poriwol digujom fomemen wozehao yapojop fozenaq celusar fodigus venawot kituriu tuwodiv jodibaw harizex babariy sawomez kirifoa natutub tumebac yafoved divenae wojotuf najonag melurih rifonai lusawoj gukihak diripol tuzetum zewohan wodiluo meripop luveluq rizecer zenaves nayacet yawopou nacemev yajodiw lumewox nabanay zewozez hacevea potulub hakidic nahadid tubavee haluluf vemedig yadijoh sagusai hahayaj vesapok gufonal luzekim yabadin cetumeo gukigup najodiq rikitur difokis turijot poyaluu zehariv venabaw yazecex yamehay kiluluz zevewoa dipokib jojokic tuceved babawoe hafojof meludig nabajoh didizei guvemej kifohak ceporil pomewom poponan.

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
Some records mix English with romanized Japanese tags such as kakunin and shuryo; keep the output values deterministic.
This task may require continuing context across multiple session files.

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
