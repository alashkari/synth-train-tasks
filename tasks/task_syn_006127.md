---
id: "task_syn_006127"
name: "Briefing extraction 006127"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003064"
generator_seed: 956699
workspace_files: ["assets/task_syn_006127/workspace/notes/briefing.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006127` for the `knowledge-base upkeep` scenario `willow-delta-3064`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material.

Scenario-specific audit anchors: meyabar zediwos kitulut diwokiu mekidiv tuzepow poguwox sadivey hafodiz jocenaa ceponab meharic navepod jojonae sabafof tuwonag venayah diwotui vewoyaj hanatuk divegul joriyam zewojon lufokio bahagup cehaveq lumeyar barifos mesabat ceguluu lufoyav dipozew bahagux zewoguy vepomez foyacea pojolub luluric luvesad josadie gucedif lulugug potukih diririi mejotuj tuhahak woharil mesagum cesahan gurikio vepolup kizetuq lupocer dinajos cemenat zenafou haguguv fobasaw dizerix veyakiy vepotuz rivemea sapopob yajohac forijod turigue ribavef gugujog dibarih rigudii cezekij mevezek fobavel hazefom yaverin ritukio bapomep hakiriq nakisar zefogus hazehat bafomeu cegujov savepow lubacex luyawoy tuvemez yacejoa lujosab tulusac rinaved balufoe pokikif zejofog merijoh cevewoi.

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

Capability focus: `unstructured_document_analysis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
