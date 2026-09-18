---
id: "task_syn_008000"
name: "Briefing extraction 008000"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_004000"
generator_seed: 1026000
workspace_files: ["assets/task_syn_008000/workspace/notes/briefing.md"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_008000` for the `vendor intake` scenario `willow-glade-4000`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material. Treat `[accion]` as an action and `[risgo]` as a risk despite the shorthand spelling.

Scenario-specific audit anchors: jofogus joyafot wocezeu nabawov rididiw dicezex wohawoy mekikiz bavecea foluhab wojoluc diyakid tufonae rifoluf kiguzeg naripoh hadirii sacewoj guwoyak jowolul fojomem zenadin yagunao naguyap nahapoq sakikir ceguves vedinat rituwou diguluv fozekiw gusapox megusay zenaguz tukinaa najozeb jojozec guzenad nanayae rifozef metuveg bapoceh zelukii vevebaj pomecek wogudil sapolum rijotun jonaguo cebavep dijomeq josapor zeriwos wowoyat joyawou guwopov fotuvew fozenax kijomey napowoz bazejoa dilutub menawoc zehasad bayajoe worikif nagutug tuzenah bacelui tudizej basarik pomebal hasarim yasaban cevesao tufomep polubaq ribarir luyaris zenamet fomemeu kinatuv pogukiw tubasax diridiy vewodiz kisakia fogunab poguguc mevelud forisae zepohaf yavehag lufopoh yamewoi sapozej.

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
Before finishing, verify that the output agrees with the relevant fixture files and record the check in `verification`.
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.
Some supplied information is intentionally irrelevant; exclude it from the result.
Some records mix English with romanized Japanese tags such as kakunin and shuryo; keep the output values deterministic.
This task may require continuing context across multiple session files.

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
