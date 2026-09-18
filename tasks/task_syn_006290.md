---
id: "task_syn_006290"
name: "Active file manifest 006290"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003145"
generator_seed: 962730
workspace_files: ["assets/task_syn_006290/workspace/incoming/archive/zenith_zenith_3145_00.cfg", "assets/task_syn_006290/workspace/incoming/active/zenith_zenith_3145_01.cfg", "assets/task_syn_006290/workspace/incoming/active/zenith_zenith_3145_02.txt", "assets/task_syn_006290/workspace/incoming/active/zenith_zenith_3145_03.md", "assets/task_syn_006290/workspace/incoming/archive/zenith_zenith_3145_04.log", "assets/task_syn_006290/workspace/incoming/active/zenith_zenith_3145_05.txt", "assets/task_syn_006290/workspace/incoming/active/zenith_zenith_3145_06.txt", "assets/task_syn_006290/workspace/incoming/active/zenith_zenith_3145_07.cfg", "assets/task_syn_006290/workspace/incoming/archive/zenith_zenith_3145_08.json", "assets/task_syn_006290/workspace/incoming/active/zenith_zenith_3145_09.cfg", "assets/task_syn_006290/workspace/incoming/active/zenith_zenith_3145_10.log", "assets/task_syn_006290/workspace/incoming/active/zenith_zenith_3145_11.cfg", "assets/task_syn_006290/workspace/incoming/archive/distractor_006290.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006290` for the `knowledge-base upkeep` scenario `zenith-zenith-3145`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: sacezey kifotuz basazea nakimeb zefowoc mehajod ludihae sakijof meyawog wowoluh zesafoi tuyafoj jonarik kigujol sarinam naposan zegukio luriwop fohaluq vewomer yavebas rilufot johaguu pohafov lutujow pocebax jonapoy sasayaz hasaria zetulub zetutuc yalugud cerizee hatupof tusarig mepoveh povetui verinaj sazesak wojomel tututum gukiban guwofoo johafop yabajoq wojotur sacehas gubacet yaveceu yamefov vesaguw riyagux kijomey baveyaz hafocea yapohab yacecec bavejod yatudie fojonaf tuzefog wotupoh forinai luwobaj hazedik sazedil tufosam jonanan gufosao jovepop yanaluq samefor cehazes tujojot dilujou tuzenav banafow jofovex rifosay nafomez cecehaa nalubab yaporic kiditud lusazee yahajof zehazeg jotukih gunalui samejoj hafofok luwopol yabaham vetugun sazetuo vetufop.

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
Some supplied information is intentionally irrelevant; exclude it from the result.

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
