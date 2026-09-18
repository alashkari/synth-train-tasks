---
id: "task_syn_007195"
name: "Professional update transformation 007195"
capability_family: "professional_communication_content_transformation"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003598"
generator_seed: 996215
workspace_files: ["assets/task_syn_007195/workspace/drafting/raw_notes.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007195` for the `billing review` scenario `keystone-zenith-3598`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Turn `drafting/raw_notes.md` into a professional update plan. Capture a concise subject, required points, excluded distractors, and the intended tone. Do not invent commitments not present in the notes.

Scenario-specific audit anchors: dimemet zesazeu natutuv johafow cetumex yaguzey hayadiz lulubaa jodibab wokisac cezefod wojokie dihanaf nacegug pojoyah cehafoi nasasaj dimewok fotukil saguvem tudiwon pocebao ludilup joluyaq worizer joyasas nawopot ludiceu popomev meyaguw porivex tuzemey dihanaz gutuwoa zedikib dicejoc zetutud bacetue foyabaf baworig ridimeh sasayai fozesaj poyarik metusal napomem jovetun kicebao zecevep jobariq vememer vegugus joridit fozehau hasayav hayanaw yawojox sajomey gubabaz wokizea vebazeb vesabac cenatud gucemee cepokif womepog fosadih pogutui riyayaj bavehak jowohal cekikim fosaban hawoveo batukip napohaq zececer veguwos vebazet poguceu kirivev cemeguw foyayax fokibay sapotuz baceria menagub bayaric pocelud jodipoe fovesaf gubatug mepotuh hajowoi luwoluj hafohak.

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
