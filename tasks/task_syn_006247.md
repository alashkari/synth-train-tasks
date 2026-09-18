---
id: "task_syn_006247"
name: "Briefing extraction 006247"
capability_family: "unstructured_document_analysis"
intended_difficulty_band: 2
grading_type: "llm_judge"
timeout_seconds: 180
base_scenario_id: "scenario_003124"
generator_seed: 961139
workspace_files: ["assets/task_syn_006247/workspace/notes/briefing.md"]
multi_session: false
---

# Prompt

You are working on synthetic task `task_syn_006247` for the `knowledge-base upkeep` scenario `ember-prairie-3124`.
Use only the files supplied in the workspace. Do not fetch live data or use credentials.

Read `notes/briefing.md` and extract action items, risk counts, high-risk topics, and decisions. Do not include ordinary notes or unrelated agenda material.

Scenario-specific audit anchors: hacekih kizerii bakihaj fowonak ceveril diforim zediban nazejoo batugup wofoluq potufor kicegus turimet joyaluu mejojov nadicew sabasax ponawoy difopoz woworia kikilub venaric disarid joyayae wolucef merihag batuguh josawoi ludivej gutufok rijokil cejotum jolukin vefoguo rilulup wokihaq yafocer cemeris zebacet wodikiu jodifov gukiguw wonazex lunamey zepoyaz jolucea hahaveb fogudic dikibad vebakie hawomef poyahag wohameh hapogui verizej natukik sajobal yajotum meririn wozebao forivep foyaluq venazer hamegus yagufot kiveriu womenav nasadiw vewojox hawocey sakiguz gukizea kitusab ceyanac mehazed hapowoe ponamef turitug wobapoh hatucei ricewoj menawok fokivel hadipom tufofon veyahao yababap tuhatuq haluhar cecegus luzevet guwobau lufonav kijosaw joguzex vekimey.

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
If a malformed row, impossible dependency, or unusable entry appears, skip it and report the skip count instead of failing.

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
