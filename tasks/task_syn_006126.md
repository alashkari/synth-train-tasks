---
id: "task_syn_006126"
name: "Quantitative reading summary 006126"
capability_family: "statistical_quantitative_analysis"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003063"
generator_seed: 956662
workspace_files: ["assets/task_syn_006126/workspace/measurements/readings.csv"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006126` for the `customer migration` scenario `violet-ember-3063`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Analyze `measurements/readings.csv`. Ignore rows whose group is `ignore` or whose weight is zero. Compute count, mean, median, weighted mean, per-group means, and sample ids with values at least 130.

Scenario-specific audit anchors: diwokiq kibawor riyahas tucekit gucemeu zepokiv jozejow fokitux joveriy vejovez fojovea yanafob dituguc tukifod lumecee rihajof ritukig gufofoh haharii pobakij samesak focewol guyarim bahafon lucepoo napovep diveriq cecefor potubas harisat pomeveu tufosav napoguw kifowox wohapoy yabafoz forizea tukikib dibabac disalud tuyahae haguguf baguyag rijobah jovepoi ceguvej rigukik joforil wodiyam vebadin jomezeo nawojop tusameq ceturir mezedis yazenat wodiguu yababav jovediw zelugux guvediy hacewoz zehamea zerijob tuvesac najorid dihajoe fozecef kidigug barifoh ponanai mepodij nametuk zemefol lucerim bahahan yawojoo fonapop yabafoq kibadir badidis wopodit cepohau bafojov dinavew nafojox lurihay gukipoz potupoa guhaveb fowomec cesawod gulubae zedibaf fokijog zelurih.

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

Capability focus: `statistical_quantitative_analysis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
