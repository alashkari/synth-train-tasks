# Generation Plan

## Objective

Generate 10,000 synthetic candidate tasks and retain 8,000 accepted tasks for a
cost-aware LLM router training corpus. The generation stage produces task
instructions, deterministic fixtures, expected behavior, grading criteria,
automated graders where applicable, judge rubrics where applicable, and
difficulty-factor metadata. It deliberately does not assign final routing labels
or model-tier labels.

## Benchmark Firewall

Before generation, the working directory is checked for paths that appear to
reference the external held-out benchmark. Generation uses only this
specification, the local scripts, and synthetic fixtures created by the
generator. No external benchmark repository, task file, prompt, issue, manifest,
asset, grader, transcript, leaderboard, or score is accessed.

Generated task files and catalog entries avoid benchmark-specific names and do
not contain final routing labels.

## Process

1. Create this plan and `taxonomy.yaml`.
2. Implement validators and grader tests before generating the full corpus.
3. Generate an initial deterministic batch of 50 candidates.
4. Validate the initial batch with `validate_corpus.py` and `test_graders.py`.
5. Record pipeline adjustments in `generation_report.md`.
6. Generate remaining candidates in deterministic batches of at most 250.
7. After each batch, validate task syntax and metadata, test grader snippets,
   run duplicate checks, update distribution counts, and accept only candidates
   that keep the corpus inside the target allocation.
8. Stop after 10,000 candidates have been considered, 8,000 accepted tasks are
   present, split isolation passes, duplicate thresholds pass, and corpus
   validation exits successfully.

## Distribution Strategy

- Accepted count: 8,000.
- Candidate count: 10,000.
- Scenario families: 4,000 accepted base scenarios, two accepted variants per
  scenario, with no scenario crossing splits.
- Split assignment by scenario family: 80% training, 10% development, 10%
  synthetic holdout.
- Capability families: balanced at 666 or 667 accepted tasks per family.
- Intended difficulty bands: exactly 1,600 accepted tasks per band.
- Grading type: 5,600 automated, 2,000 hybrid, 400 judge-only.
- Multi-session target: 1,000 accepted tasks.
- Recoverable failure target: 1,200 accepted tasks.
- Verification target: 2,000 accepted tasks.
- Distractor target: 1,600 accepted tasks.
- Non-English or mixed-language target: 1,000 accepted tasks.
- Multi-file/artifact target: 2,400 accepted tasks.

## Duplicate Resistance

The generator varies capability family, task recipe, fixture schema, domain
vocabulary, filenames, field names, output contract, source texture, and grader
criteria. The duplicate script checks exact prompt hashes, normalized prompt
hashes, base-scenario fingerprint counts, token 5-gram overlap, grader-code
similarity, and repeated fixture schemas.

## Initial Batch Notes

The initial 50-candidate batch is generated before the full run. The validation
results and any generator changes are recorded in `generation_report.md`.
