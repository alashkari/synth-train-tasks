---
id: "task_syn_006390"
name: "Quantitative reading summary 006390"
capability_family: "statistical_quantitative_analysis"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003195"
generator_seed: 966430
workspace_files: ["assets/task_syn_006390/workspace/measurements/readings.csv"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006390` for the `sensor calibration` scenario `xenial-ion-3195`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130.

Scenario-specific audit anchors: vediveu jogupov hatuluw gumeyax yalufoy zejotuz cehayaa rifobab tumehac lugutud navelue cemesaf yanahag meverih riricei hawomej havecek folugul dikiyam vemedin zeturio ceworip mesaguq badikir zeyalus lucejot guyatuu riceyav nahaluw cewotux hayapoy turifoz lubawoa jokibab luwodic hawozed womesae jowohaf lufosag kituhah pozecei kidibaj kipojok ridihal lusakim vezewon babatuo woludip merituq savepor dijowos nahagut hazeveu foricev yavemew jotusax metumey sawodiz sajolua kiforib gucebac kisarid cerivee rizehaf mezepog riyameh dihajoi sahacej rifonak kigusal nasarim jocerin fosario luhahap polupoq woyagur dinaris nametut fovewou ribayav yazewow tusafox luhayay kiguluz cekizea mevesab naludic diluzed havemee meyacef tulusag fofobah yawokii rirituj luzedik hamecel.

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

Capability focus: `statistical_quantitative_analysis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
