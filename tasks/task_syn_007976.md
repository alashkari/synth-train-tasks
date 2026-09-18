---
id: "task_syn_007976"
name: "Briefing extraction 007976"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003988"
generator_seed: 1025112
workspace_files: ["assets/task_syn_007976/workspace/notes/briefing.md"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_007976` for the `access cleanup` scenario `keystone-xenial-3988`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material. Treat `[accion]` as an action and `[risgo]` as a risk despite the shorthand spelling.

Scenario-specific audit anchors: jotuwou vebakiv cekiriw bafokix gusahay tututuz lujoyaa sajohab kinavec pomehad hazefoe nawozef jorikig ricesah ripovei tunawoj rijotuk pohatul turibam riyanan cewohao worizep zesatuq yafohar nasahas jopotut rimetuu kivevev poyafow woludix poluluy nafotuz rijomea ponatub mepomec satumed poguvee meriyaf tukitug vejodih diwozei mehacej riluzek ritucel yafojom lukisan batuveo joricep jovefoq wowoyar kijonas digugut saponau riririv ditucew jogunax posasay wohafoz gucezea jofosab najoguc josabad ricehae tunavef tuyatug dijopoh hariyai riveyaj fomezek habanal fojosam sasaban tuzezeo namecep savezeq kibacer lujomes foluhat bawosau yadicev gusadiw pojocex vezeguy gujocez forigua kiwowob luvecec harifod hayamee pohahaf guwobag lutubah yazecei mepoluj zececek nahasal.

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
