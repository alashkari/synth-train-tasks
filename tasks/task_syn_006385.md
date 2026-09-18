---
id: "task_syn_006385"
name: "Active file manifest 006385"
capability_family: "file_directory_operations"
intended_difficulty_band: 5
grading_type: "llm_judge"
timeout_seconds: 270
base_scenario_id: "scenario_003193"
generator_seed: 966245
workspace_files: ["assets/task_syn_006385/workspace/incoming/archive/violet_zenith_3193_00.txt", "assets/task_syn_006385/workspace/incoming/active/violet_zenith_3193_01.json", "assets/task_syn_006385/workspace/incoming/active/violet_zenith_3193_02.txt", "assets/task_syn_006385/workspace/incoming/active/violet_zenith_3193_03.log", "assets/task_syn_006385/workspace/incoming/archive/violet_zenith_3193_04.txt", "assets/task_syn_006385/workspace/incoming/active/violet_zenith_3193_05.md", "assets/task_syn_006385/workspace/incoming/active/violet_zenith_3193_06.cfg", "assets/task_syn_006385/workspace/incoming/active/violet_zenith_3193_07.cfg", "assets/task_syn_006385/workspace/incoming/archive/violet_zenith_3193_08.md", "assets/task_syn_006385/workspace/incoming/active/violet_zenith_3193_09.cfg", "assets/task_syn_006385/workspace/incoming/archive/distractor_006385.txt"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006385` for the `knowledge-base upkeep` scenario `violet-zenith-3193`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the knowledge-base upkeep workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.txt` whose byte length is at least 59, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: tutubap dituyaq yayayar vevejos veyamet sabaguu zediguv nahacew zezemex ribadiy yasamez zebahaa banameb tujojoc cetugud savedie zehazef guwolug nagupoh diyabai luguyaj fojohak luyafol ludiyam joriban menameo jopodip cewoyaq navejor veceves kiguhat narisau yatutuv hahariw lumedix bametuy ceceyaz kifotua lujopob zenasac zemepod ludijoe lubapof ritubag celunah meharii pojomej kibatuk baricel cezezem meyatun tupobao harivep sasawoq hacebar cekiwos yamevet kisameu sacehav zehatuw rijokix gubabay mesayaz wowohaa cetukib naguguc mekijod metusae safocef vesatug yasaceh sananai yakicej gufosak mefolul poritum baposan badiwoo megufop foguriq luwozer yahahas zemecet fojoyau hasaguv guvebaw bafokix ceriluy gubajoz fodiria savekib pogumec bapoced tukizee kibazef joyadig.

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
