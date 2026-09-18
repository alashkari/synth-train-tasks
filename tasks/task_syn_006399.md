---
id: "task_syn_006399"
name: "Captured source synthesis 006399"
capability_family: "web_information_gathering_source_synthesis"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003200"
generator_seed: 966763
workspace_files: ["assets/task_syn_006399/workspace/captured/page_a.md", "assets/task_syn_006399/workspace/captured/page_b.md", "assets/task_syn_006399/workspace/captured/page_c.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006399` for the `inventory audit` scenario `cedar-summit-3200`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Use the captured source files under `captured/`; do not fetch live pages. Select the metric value by preferring a reviewed source and using latest date only as a tie breaker. Report conflicting metric values and cite the selected file.

Scenario-specific audit anchors: babaved fohajoe diposaf yakifog bakituh risacei kicejoj fopovek hanamel luwotum mekihan yarizeo lubahap dibameq yavebar rikifos sakipot basasau hagucev naguhaw kiyagux yanadiy dihafoz sanatua tuvelub bazecec fogujod riwowoe hakiwof kizetug ripozeh sazesai fobacej guyasak luhakil vevewom salumen gukiceo yasafop guposaq menamer gucelus fogukit fomejou mehadiv mewokiw kiverix zeyayay hamepoz fokizea kirizeb zemefoc lunadid cesahae yalufof metuhag nahayah vezeyai wotujoj safopok wolupol wotuzem tuyaban hajotuo nasabap yacemeq fofover mevekis luponat vesafou cekiwov baturiw ridinax poluwoy gumejoz saveria hatugub zecemec navewod vewonae ripomef navenag jogutuh safokii zepotuj cehatuk powogul jobavem josayan pobaceo bagucep vefowoq harisar pofolus lufonat cebaveu.

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
