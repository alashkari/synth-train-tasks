---
id: "task_syn_006205"
name: "Mini repository maintenance scan 006205"
capability_family: "repository_navigation_software_maintenance"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003103"
generator_seed: 959585
workspace_files: ["assets/task_syn_006205/workspace/repo/config/modules.json", "assets/task_syn_006205/workspace/repo/src/ingest.py", "assets/task_syn_006205/workspace/repo/src/export.py", "assets/task_syn_006205/workspace/repo/src/audit.py", "assets/task_syn_006205/workspace/repo/src/notify.py", "assets/task_syn_006205/workspace/repo/src/cleanup.py", "assets/task_syn_006205/workspace/repo/docs/changelog.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006205` for the `inventory audit` scenario `juniper-keystone-3103`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the mini repository under `repo/`. Create a maintenance report with enabled modules, deprecated modules, TODO markers with their module names, and any enabled module whose source file is missing.

Scenario-specific audit anchors: bakipor yaritus kitusat fokiyau gucebav kisasaw kikikix rihapoy sayavez wogugua salupob cebaluc veharid wogufoe vesavef diririg joguluh yawolui riguwoj josaluk melujol vehapom riyakin yadihao haripop guforiq vewojor guluyas harihat habadiu poluwov wohaguw podiwox zedibay wovefoz cejoyaa pokipob salumec luvelud dijolue mecezef mepopog polufoh meyalui venamej tujomek medisal divejom saveven najojoo yanadip dihameq zegujor fomedis vejonat guridiu baguguv luriyaw jokiwox worikiy lusamez naguvea sameceb rijotuc posalud sajodie tukibaf dirisag pomezeh yatuhai saworij sacejok guhayal wopopom yarigun kihafoo fonawop pozefoq dijowor cedigus jolutut potuhau yasahav difofow tudidix meluyay yabanaz hasakia yayazeb fozehac rivegud vebajoe ribabaf diyayag tucesah wokirii.

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

Capability focus: `repository_navigation_software_maintenance`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
