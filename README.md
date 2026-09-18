# Leakage-Resistant Synthetic Router Corpus

This directory contains a deterministic synthetic task corpus for training an
LLM router. The task generation process creates candidate prompts, fixtures,
grading criteria, automated grader snippets, and split metadata. It does not
create final routing labels or claimed model performance outcomes.

The accepted corpus is balanced across twelve generic capability families and
five intended difficulty bands. Difficulty bands are generation-balancing
attributes only; they are not target model tiers.

## Contents

- `generation_plan.md`: process and acceptance plan.
- `taxonomy.yaml`: capability families and intended difficulty definitions.
- `catalog.jsonl`: one JSON object per considered candidate.
- `split_manifest.yaml`: scenario-family split assignment.
- `tasks/`: accepted task markdown files.
- `assets/`: deterministic synthetic fixtures for accepted tasks.
- `rejected/`: rejected candidate task files grouped by rejection class.
- `scripts/`: generator, validators, deduplication, split, summary, and grader
  test tools.

## Validation

From the repository root:

```bash
python synthetic_router_corpus/scripts/validate_corpus.py synthetic_router_corpus --expected-accepted 8000
python synthetic_router_corpus/scripts/test_graders.py synthetic_router_corpus
```

These commands check task structure, metadata, split isolation, distribution
targets, duplicate thresholds, forbidden benchmark references, and automated
grader behavior.
