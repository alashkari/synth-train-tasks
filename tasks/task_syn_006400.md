---
id: "task_syn_006400"
name: "Captured source synthesis 006400"
capability_family: "web_information_gathering_source_synthesis"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003200"
generator_seed: 966800
workspace_files: ["assets/task_syn_006400/workspace/captured/page_a.md", "assets/task_syn_006400/workspace/captured/page_b.md", "assets/task_syn_006400/workspace/captured/page_c.md"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_006400` for the `incident follow-up` scenario `cedar-xenial-3200`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Use the captured source files under `captured/`; do not fetch live pages. Select the metric value by preferring a reviewed source and using latest date only as a tie breaker. Report conflicting metric values and cite the selected file.

Scenario-specific audit anchors: kihasae tukisaf zemepog nazerih luwofoi hagubaj povecek kibajol hatucem kipodin jonawoo nafowop diyameq yatubar haluzes jocesat podinau hahayav fomenaw bavepox wowofoy risakiz basatua guzeveb sarihac nawoved satulue menayaf pojoveg tuguguh riyadii nacecej poyatuk fozepol dimemem vevewon gurituo rizekip gufokiq yamegur lukices jogusat yaririu guhafov cewozew luhanax metuwoy kikijoz zewoyaa bafoceb vewodic vekihad mebahae ludidif jozeceg tuyahah sanatui sakikij fovekik nadihal sacedim tuhasan diwobao poluwop vepotuq kihahar luyabas yayapot yanahau wovetuv rikiluw hadinax hapokiy foriluz cediyaa wopogub ditusac cemefod safozee yajonaf ribadig diguveh dibalui yakiwoj hamefok kimetul lucesam zegumen lugujoo zelupop tutuveq hapofor jodisas tuyakit yanaguu wotupov.

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
Some source notes include French words such as priorite, preuve, and etape; keep the output schema in English.
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

Capability focus: `web_information_gathering_source_synthesis`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
