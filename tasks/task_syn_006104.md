---
id: "task_syn_006104"
name: "Briefing extraction 006104"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003052"
generator_seed: 955848
workspace_files: ["assets/task_syn_006104/workspace/notes/briefing.md"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_006104` for the `sensor calibration` scenario `keystone-nimbus-3052`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material. Treat `[accion]` as an action and `[risgo]` as a risk despite the shorthand spelling.

Scenario-specific audit anchors: mezetuu kizezev cehazew wojolux sapocey pomeyaz zefonaa ceribab cezefoc kirized dihazee wopozef habazeg gudituh mejojoi tujocej ricepok fopobal megugum zemehan kiverio cedikip bazeveq potuhar satujos mebavet luyaveu sapowov tuyajow fosabax lujofoy rilufoz focefoa jogujob diveguc jokimed kikihae nariyaf gukiceg kihakih poceyai bayawoj yasakik guyacel vemevem memeban nasario zegukip kizekiq fonanar hafotus diguvet vetukiu vemevev kisadiw lucehax joceluy tukiwoz fodidia johameb jojotuc haveced zecepoe fomenaf hahawog rigunah cemeyai yasajoj kibatuk mehasal dizezem cewohan banatuo metugup mejoveq wotuwor vesaves zegusat gucewou mefonav rikipow melupox yalufoy vetuhaz disafoa vedilub dibatuc rimerid hagurie nakituf nawogug focemeh samegui meyatuj kiriguk safocel.

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
