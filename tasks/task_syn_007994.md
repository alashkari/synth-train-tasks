---
id: "task_syn_007994"
name: "Active file manifest 007994"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003997"
generator_seed: 1025778
workspace_files: ["assets/task_syn_007994/workspace/incoming/archive/tundra_summit_3997_00.md", "assets/task_syn_007994/workspace/incoming/active/tundra_summit_3997_01.cfg", "assets/task_syn_007994/workspace/incoming/active/tundra_summit_3997_02.log", "assets/task_syn_007994/workspace/incoming/active/tundra_summit_3997_03.cfg", "assets/task_syn_007994/workspace/incoming/archive/tundra_summit_3997_04.log", "assets/task_syn_007994/workspace/incoming/active/tundra_summit_3997_05.log", "assets/task_syn_007994/workspace/incoming/active/tundra_summit_3997_06.cfg", "assets/task_syn_007994/workspace/incoming/active/tundra_summit_3997_07.md", "assets/task_syn_007994/workspace/incoming/archive/tundra_summit_3997_08.txt", "assets/task_syn_007994/workspace/incoming/active/tundra_summit_3997_09.md", "assets/task_syn_007994/workspace/incoming/active/tundra_summit_3997_10.json"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007994` for the `access cleanup` scenario `tundra-summit-3997`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: cewozem vepoven satutuo rijobap diyanaq medijor fohaves zejomet vetuhau joguzev rimekiw dinajox cesawoy hadinaz navejoa focebab pobakic wopowod veyarie venajof zekiveg wofomeh diguzei hafonaj kiwoyak metuhal navenam fobayan navebao lukimep sanaguq kituver poriwos metuzet nayazeu yaluluv gucekiw rivedix nariguy banamez kiwocea jodiceb zewofoc mecenad tudirie pojoluf guvelug dibadih ricehai guyasaj yahavek zeveril tufomem jolutun zevekio diluhap diwodiq fojozer yatubas veyadit kigudiu sayavev guhabaw turicex melukiy yatuhaz riyayaa meyatub harikic poribad sarivee kiveguf yazefog rimenah yayapoi hanavej gusadik zehasal ceribam ponajon guceceo habakip tuvepoq gutufor dipodis fobanat venaceu kibaluv pobahaw nadimex bacenay lukihaz dibazea tubahab gudijoc pohamed.

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
