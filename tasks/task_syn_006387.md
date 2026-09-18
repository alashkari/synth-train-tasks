---
id: "task_syn_006387"
name: "Structured table normalization 006387"
capability_family: "structured_data_transformation"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003194"
generator_seed: 966319
workspace_files: ["assets/task_syn_006387/workspace/tables/source_records.csv", "assets/task_syn_006387/workspace/tables/region_map.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006387` for the `customer migration` scenario `willow-yonder-3194`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Transform `tables/source_records.csv` using `tables/region_map.json`. Keep only active rows with `units * unit_cost >= 106`, uppercase each id, map regions to zones, sort by zone then id, and report how many malformed rows were skipped.

Scenario-specific audit anchors: jofocer satudis jopojot kiribau luzewov bavevew ririgux vesawoy riforiz sakisaa lulurib nazehac rimedid yayacee gubadif rikikig gutuzeh bamesai zewovej josaluk pokibal yaditum wocemen woluhao zedihap pobaceq cebarir yamemes pofojot fonanau kivekiv yagufow yakirix veguzey fobajoz metukia pofowob ditukic mefokid bavewoe kidifof hayayag pobazeh riyanai tutuguj diwosak banayal napowom mevezen gusadio lupotup wokidiq fosafor difozes cetufot hafonau luceyav badihaw guhacex tudiriy riridiz josajoa megutub dicetuc cerijod gugukie dizezef ponafog sasarih rituzei medicej jonacek potupol ceverim foponan poririo mebafop wodinaq kiponar wovegus bacelut cefofou hanapov babacew kizevex bapovey kidifoz fozezea sabafob bacenac mesafod cedifoe hamebaf natunag luwoyah verikii.

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

Capability focus: `structured_data_transformation`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
