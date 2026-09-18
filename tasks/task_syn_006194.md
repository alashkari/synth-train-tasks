---
id: "task_syn_006194"
name: "Active file manifest 006194"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003097"
generator_seed: 959178
workspace_files: ["assets/task_syn_006194/workspace/incoming/archive/delta_willow_3097_00.cfg", "assets/task_syn_006194/workspace/incoming/active/delta_willow_3097_01.json", "assets/task_syn_006194/workspace/incoming/active/delta_willow_3097_02.cfg", "assets/task_syn_006194/workspace/incoming/active/delta_willow_3097_03.cfg", "assets/task_syn_006194/workspace/incoming/archive/delta_willow_3097_04.md", "assets/task_syn_006194/workspace/incoming/active/delta_willow_3097_05.md", "assets/task_syn_006194/workspace/incoming/active/delta_willow_3097_06.log", "assets/task_syn_006194/workspace/incoming/active/delta_willow_3097_07.cfg", "assets/task_syn_006194/workspace/incoming/archive/delta_willow_3097_08.md", "assets/task_syn_006194/workspace/incoming/active/delta_willow_3097_09.log", "assets/task_syn_006194/workspace/incoming/active/delta_willow_3097_10.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006194` for the `access cleanup` scenario `delta-willow-3097`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: diwohag samezeh kiyamei zenacej fobamek haguzel bahawom gugukin jolujoo guwoyap tuyadiq josagur yarihas bamelut hapopou rizewov tupohaw gugucex riwomey mesajoz savedia poveveb forimec rikidid gusajoe bariguf zekikig dituveh tujocei difoguj risahak mepohal pokirim gutumen jolupoo zejorip focewoq basawor bafoces ceyahat ceyaguu ceridiv yaluluw pohakix luwonay nahaguz tuyasaa cetusab jobahac fowomed hatuhae jomefof hagurig fozeceh vesatui meyasaj dikicek guposal metujom lulurin womezeo cesanap nakiluq kilutur kihawos gusapot foguveu pokiguv dijobaw polugux celuhay tugudiz mekivea halupob sabayac yahasad kibague fojomef gubawog kinasah ririsai diriwoj tubabak zefogul fovebam tugukin mebasao zezegup gucewoq dimenar sazenas navejot pokiwou vesasav joriluw kibagux.

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
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.

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

Capability focus: `file_directory_operations`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
