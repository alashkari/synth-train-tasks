# Synthetic Router Corpus Instructions

This directory contains synthetic candidate tasks for a cost-aware LLM routing
model. The corpus must remain separate from any external held-out benchmark.

## Firewall

- Do not open, search for, retrieve, clone, run, or inspect the held-out
  benchmark named in the original user request.
- Do not copy, paraphrase, mutate, or otherwise derive tasks from any external
  benchmark.
- Do not add final routing labels or model-tier labels to tasks, catalog
  records, reports, or split manifests.
- Work only from this specification, the local corpus files, generic
  agent-workflow knowledge, and synthetic fixtures created here.

## Corpus Rules

- Accepted tasks live in `tasks/`.
- Rejected candidates live in one of the `rejected/` subdirectories.
- `catalog.jsonl` contains one record per considered candidate.
- `split_manifest.yaml` assigns complete base-scenario families to exactly one
  split.
- Automated grader snippets must use only Python standard-library modules, avoid
  network calls, handle missing outputs, and return scores bounded by `0.0` and
  `1.0`.

## Reproduction

Run the commands listed in `generation_report.md` from this directory's parent.
They recreate the corpus deterministically from the generator version and seeds
stored in `catalog.jsonl`.
