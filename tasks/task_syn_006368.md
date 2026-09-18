---
id: "task_syn_006368"
name: "Briefing extraction 006368"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 3
grading_type: "llm_judge"
timeout_seconds: 210
base_scenario_id: "scenario_003184"
generator_seed: 965616
workspace_files: ["assets/task_syn_006368/workspace/notes/briefing.md"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_006368` for the `training roster` scenario `mosaic-prairie-3184`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material. Treat `[accion]` as an action and `[risgo]` as a risk despite the shorthand spelling.

Scenario-specific audit anchors: sarisay vezekiz lugubaa pojokib melufoc balubad celuhae tudinaf haluyag rihabah riwopoi vevefoj veyaguk wozehal kipomem zenafon hakiveo halumep gunaluq vewowor safolus menadit zepodiu mejomev ripohaw hapowox luyaguy zezebaz bawolua fovesab nababac lufozed jojowoe tugukif sawonag hasabah yapohai ditutuj dijorik kirigul kisapom rinawon rifoceo dimezep yakimeq sayapor natuves mesayat dimewou napowov luvekiw nazesax jofovey gujocez rifogua gumewob cedizec tucezed medilue fosanaf hanarig naguluh badimei lutusaj hasarik dipopol lupofom kiyazen yasawoo gufolup kitubaq mesahar gulujos gutucet gutumeu banayav kididiw najorix meveriy kiguvez digugua veyawob foluzec divewod kiribae dihakif rinajog kihaceh luveyai memesaj ribapok lunayal yababam woyazen tuhadio digudip.

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
