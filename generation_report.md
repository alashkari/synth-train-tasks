# Generation Report

## Counts

- Generated candidates considered: 10000
- Accepted tasks: 8000
- Rejected candidates: 2000
- Rejected by reason: `{"duplicate_prompt": 500, "invalid_grader_syntax": 500, "subjective_success_criteria": 500, "superficial_parameter_swap": 500}`

## Distributions

- Capability families: `{"code_debugging": 666, "code_generation": 666, "file_directory_operations": 668, "memory_retrieval_context_continuation": 666, "multi_tool_workflow_orchestration": 666, "planning_scheduling_constraint_satisfaction": 666, "professional_communication_content_transformation": 666, "repository_navigation_software_maintenance": 666, "statistical_quantitative_analysis": 668, "structured_data_transformation": 668, "unstructured_document_analysis": 668, "web_information_gathering_source_synthesis": 666}`
- Intended difficulty bands: `{"1": 1600, "2": 1600, "3": 1600, "4": 1600, "5": 1600}`
- Grading types: `{"automated": 5600, "hybrid": 2000, "llm_judge": 400}`
- Tool-depth bands: `{"deep": 5067, "moderate": 2933}`
- Context-length bands: `{"long": 1600, "medium": 3200, "short": 3200}`
- Splits: `{"development": 800, "synthetic_holdout": 800, "train": 6400}`
- Multi-session tasks: 1000
- Recoverable-failure tasks: 1200
- Verification tasks: 2000
- Distractor tasks: 1600
- Non-English or mixed-language tasks: 1000
- Multi-file or multi-artifact tasks: 4000

## Scenario Families

- Number of base scenarios: 4000
- Average variants per base scenario: 2.0
- Maximum variants per base scenario: 2

## Duplicate Detection

- Exact prompt duplicate pairs: 0
- Normalized prompt duplicate pairs: 0
- High 5-gram-overlap pairs: 0
- Base-scenario fingerprint overflows: 0
- Grader-similarity pairs for inspection: 100
- Max fixture-schema reuse: 668

## Grader Tests

- Automated/hybrid graders tested: 7600
- Grader failures: 0

## Batch Process

- Initial batch size: 50
- Total batches: 41
- Batch validation errors observed: 0
- Initial-batch generator adjustments: added deterministic task-specific anchors and focused the 5-gram duplicate check on task-specific prompt content after the first duplicate pass found boilerplate-driven overlap.

## Known Limitations

- The corpus is synthetic and generated from compositional recipes, so a separate post-generation contamination audit is still required.
- Judge-only tasks require later human or model-judge calibration before use in scoring experiments.
- Automated graders check deterministic artifacts and may not reward every semantically equivalent presentation outside the requested schema.

## Reproduction Commands

```bash
python synthetic_router_corpus/scripts/generate_batch.py synthetic_router_corpus --reset --total-candidates 10000 --accepted-target 8000 --initial-batch-size 50 --batch-size 250
python synthetic_router_corpus/scripts/deduplicate_tasks.py synthetic_router_corpus
python synthetic_router_corpus/scripts/test_graders.py synthetic_router_corpus
python synthetic_router_corpus/scripts/validate_corpus.py synthetic_router_corpus --expected-accepted 8000
python synthetic_router_corpus/scripts/generate_batch.py synthetic_router_corpus --report-only
```

## Firewall Confirmation

- The generation process did not access the external held-out benchmark named in the user specification.
- No final routing labels, model-tier labels, quality-versus-cost rewards, or claimed model outcomes were generated.
- This report does not claim freedom from all possible pretraining contamination; a separate post-generation audit is still required.
