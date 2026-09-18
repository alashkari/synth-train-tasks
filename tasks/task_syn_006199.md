---
id: "task_syn_006199"
name: "Briefing extraction 006199"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003100"
generator_seed: 959363
workspace_files: ["assets/task_syn_006199/workspace/notes/briefing.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006199` for the `sensor calibration` scenario `glade-brisk-3100`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material.

Scenario-specific audit anchors: gubafol ricerim posaven luvehao dinamep guwoceq dimepor guyakis tunafot cerikiu ceposav jobapow fowojox cetuvey hajojoz zenabaa digudib bazevec mezezed lulucee haluguf babaveg zerikih babapoi joguzej jometuk veyayal jobarim naguzen lujomeo nacedip sasadiq wonafor hasames yaditut sarituu zefotuv haguvew sacesax jofoluy mecebaz zekidia tugujob cepojoc mezekid disasae lucezef guriceg pogubah cejoyai jofocej rivevek luludil mejosam tuvehan bagurio tunanap ceyameq guzesar cefogus diguhat mecefou bananav wopohaw bapojox hadikiy wotuwoz bavebaa fomekib baluwoc hajonad vejozee riguluf kifoyag sapojoh natuzei samejoj dididik joceyal cejopom safojon nayapoo lukipop basazeq bagutur jolubas dibakit lucehau nayabav zejoluw cehajox mecenay luhapoz kiritua natusab fojoyac.

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
