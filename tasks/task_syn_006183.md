---
id: "task_syn_006183"
name: "Captured source synthesis 006183"
capability_family: "web_information_gathering_source_synthesis"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003092"
generator_seed: 958771
workspace_files: ["assets/task_syn_006183/workspace/captured/page_a.md", "assets/task_syn_006183/workspace/captured/page_b.md", "assets/task_syn_006183/workspace/captured/page_c.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006183` for the `queue triage` scenario `yonder-mosaic-3092`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Use the captured source files under `captured/`; do not fetch live pages. Select the metric value by preferring a reviewed source and using latest date only as a tie breaker. Report conflicting metric values and cite the selected file.

Scenario-specific audit anchors: kinaguv bahahaw zekicex meyazey sajojoz tubacea lumedib disapoc medized yadicee tusaluf yasalug venapoh kinazei rimetuj kihaluk tuvedil wodibam josazen lufohao natuzep metuguq tuveyar fokijos kizeyat kisatuu jofocev lusayaw yadirix mekiwoy guzefoz yayajoa bayalub yagucec kisarid jonawoe cewocef nasapog naluzeh digupoi sasapoj tuvetuk tuvehal divejom guvejon tuzekio hatuyap guforiq mehapor kigugus nakifot zeludiu fobaluv zeguzew folufox basawoy napovez wovewoa gupolub vecefoc difosad pocenae vedidif jovefog tunasah ridibai nacevej rikivek cekitul divedim venacen fomerio yazedip sadipoq woyajor jodikis lujorit jozekiu hagusav kipopow josapox cezeguy rigusaz poveyaa didizeb metubac cedidid vefoyae cefopof gufopog gupobah jonamei fosanaj zeveguk yamefol vezewom.

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
