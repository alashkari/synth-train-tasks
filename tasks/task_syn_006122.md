---
id: "task_syn_006122"
name: "Active file manifest 006122"
capability_family: "file_directory_operations"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003061"
generator_seed: 956514
workspace_files: ["assets/task_syn_006122/workspace/incoming/archive/tundra_ripple_3061_00.md", "assets/task_syn_006122/workspace/incoming/active/tundra_ripple_3061_01.json", "assets/task_syn_006122/workspace/incoming/active/tundra_ripple_3061_02.txt", "assets/task_syn_006122/workspace/incoming/active/tundra_ripple_3061_03.txt", "assets/task_syn_006122/workspace/incoming/archive/tundra_ripple_3061_04.cfg", "assets/task_syn_006122/workspace/incoming/active/tundra_ripple_3061_05.cfg", "assets/task_syn_006122/workspace/incoming/active/tundra_ripple_3061_06.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006122` for the `billing review` scenario `tundra-ripple-3061`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Inspect the files under `incoming/active/` for the billing review workspace. Ignore everything under `incoming/archive/`. Select active files ending in `.cfg` whose byte length is at least 38, count active files by extension, and identify the largest active file.

Scenario-specific audit anchors: nakidim cefogun rifohao nasakip diluhaq wodiver tutupos pozeyat woripou gujobav hawomew pomenax tuluguy dikifoz pojomea wohajob vezedic pofogud lucelue hadituf wojogug guceluh cegufoi nawokij yabaguk riceyal naguzem jocenan cenakio yavefop nawomeq zeritur bafonas guvehat rihahau havesav sapotuw vewopox kirikiy woluluz kiwoyaa zewodib hadikic tubatud metuyae tucehaf jovetug fozekih gufobai riyakij poyayak cerifol nafozem nawonan joyajoo wohawop zediceq sasagur kikipos zepodit vepohau ludiyav tuyatuw ceyahax gujopoy luricez luyatua fozerib fodiluc cebalud hanavee meceyaf tukidig bawofoh fosazei gudidij zevenak kifobal wotuzem nariven ridimeo zesahap joriguq jokibar woluyas fonasat badinau guhabav kihaguw podinax tunamey wonakiz tusacea tucezeb kijojoc poyaved.

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
