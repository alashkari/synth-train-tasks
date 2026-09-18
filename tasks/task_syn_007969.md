---
id: "task_syn_007969"
name: "Active file manifest 007969"
capability_family: "file_directory_operations"
intended_difficulty_band: 4
grading_type: "llm_judge"
timeout_seconds: 240
base_scenario_id: "scenario_003985"
generator_seed: 1024853
workspace_files: ["assets/task_syn_007969/workspace/incoming/archive/harbor_quartz_3985_00.cfg", "assets/task_syn_007969/workspace/incoming/active/harbor_quartz_3985_01.txt", "assets/task_syn_007969/workspace/incoming/active/harbor_quartz_3985_02.json", "assets/task_syn_007969/workspace/incoming/active/harbor_quartz_3985_03.md", "assets/task_syn_007969/workspace/incoming/archive/harbor_quartz_3985_04.md", "assets/task_syn_007969/workspace/incoming/active/harbor_quartz_3985_05.cfg", "assets/task_syn_007969/workspace/incoming/active/harbor_quartz_3985_06.log", "assets/task_syn_007969/workspace/incoming/active/harbor_quartz_3985_07.txt", "assets/task_syn_007969/workspace/incoming/archive/harbor_quartz_3985_08.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_007969` for the `access cleanup` scenario `harbor-quartz-3985`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the access cleanup workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.json` whose byte length is at least 52, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: rinanan ridifoo gukibap yanazeq kiyayar dihalus wojowot batujou yaceriv yayadiw tulukix tubabay bazebaz hapocea jobadib ricecec nacetud sazevee nakivef posasag sawobah tunabai vegusaj jonanak pohadil pomedim veyajon tujoguo wonakip dirifoq jopogur nakibas foluyat hasariu kizeluv lufohaw jocelux bariguy sakituz hamenaa diyalub meluzec kimeced vesamee tututuf cepolug guzetuh hawodii guririj ditusak yaludil nanawom wolusan mecezeo mesawop risawoq wowodir metusas nawobat fomenau jomejov sagupow cetubax vesajoy baposaz mezelua lujofob jobaric mecejod nazejoe luzehaf sarimeg ripokih yajozei nagufoj wonabak fotuhal mewofom vezejon riyakio basazep barijoq gutudir fozegus sarivet fowoluu cehamev medicew riluhax gumeriy fosaluz jotunaa kipohab cebavec wogulud cerijoe.

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

Capability focus: `file_directory_operations`.

# Additional Notes

All names, records, source pages, logs, and code fixtures in this task are synthetic. Do not infer a final model route or model tier from this metadata.
