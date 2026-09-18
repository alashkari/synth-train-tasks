---
id: "task_syn_006296"
name: "Briefing extraction 006296"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 1
grading_type: "llm_judge"
timeout_seconds: 150
base_scenario_id: "scenario_003148"
generator_seed: 962952
workspace_files: ["assets/task_syn_006296/workspace/notes/briefing.md"]
multi_session: true
---

# Prompt

You are working on synthetic task `task_syn_006296` for the `access cleanup` scenario `cedar-lumen-3148`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material. Treat `[accion]` as an action and `[risgo]` as a risk despite the shorthand spelling.

Scenario-specific audit anchors: zewojoe vebayaf gudipog dinatuh riwohai bapodij podizek basajol tunajom lunacen bavesao kigubap powodiq wotugur povepos venatut rihabau yakiluv zekivew rizecex saporiy savejoz hatumea rifonab fojokic pojofod luyanae kifowof bafozeg merikih pozerii mekiluj gupoguk pobazel nacegum riwokin rikizeo bahadip womebaq riguyar fohapos lunajot zefoyau vewonav jowozew kisawox kiridiy veveyaz jojojoa yajoceb mekisac luriced fosanae yaveyaf wogukig jonadih nalutui kizesaj cefoguk sasasal riwopom mezehan basakio ditugup focetuq didifor lurilus sajomet wowofou babazev luyasaw jokiwox zejojoy folupoz luludia yazefob jovecec tupogud povenae veluluf wobahag nawoceh rilugui nabanaj jotusak lulugul powokim lubalun jovemeo tuposap wovediq zebatur basatus vefojot mekimeu bajomev.

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
