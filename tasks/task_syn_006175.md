---
id: "task_syn_006175"
name: "Briefing extraction 006175"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003088"
generator_seed: 958475
workspace_files: ["assets/task_syn_006175/workspace/notes/briefing.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006175` for the `vendor intake` scenario `umbra-nimbus-3088`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material.

Scenario-specific audit anchors: lukidin kilunao yakilup guzeriq cewocer tucedis yafojot celuyau jobacev gukinaw gujoyax zezepoy nayatuz guzeyaa tuporib jomeguc nacenad nazefoe guhasaf ribawog badipoh divemei yafojoj guzetuk zedinal satutum womemen jojosao satujop mericeq jozehar haguzes napoyat nakiriu meporiv zekiluw risafox navetuy tuzemez gubasaa disawob wowocec hatutud yajohae vegujof wocepog woriyah kinayai tukifoj harimek nazebal tulumem metulun baridio balucep yacewoq yacerir kigufos cemeyat baceriu yanavev nabatuw naguhax dicejoy luwohaz fosazea sawoveb bakiguc yasafod yarikie hakivef babawog hadijoh nacevei veluvej jojojok bacefol kisapom jonapon pozesao bawobap meyazeq hacehar riponas dijobat riyadiu nahazev johacew yawokix vevepoy yasatuz folufoa yadiceb sasahac bagufod natukie.

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
