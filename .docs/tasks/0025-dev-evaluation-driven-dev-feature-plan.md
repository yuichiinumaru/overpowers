# Feature Plan: Evaluation-Driven Development (EvDD) QA Framework

## Overview
Establish a robust QA framework for Overpowers skills using formal JSON schemas. This framework will ensure structural integrity and metadata consistency across the 1300+ skills in the repository, enabling automated validation and improved reliability.

## User Stories
- As a **Skill Developer**, I want to validate my skill's structure and metadata against a formal specification so that I can catch errors early.
- As an **Orchestrator**, I want to ensure that all loaded skills follow a predictable schema so that I can reliably extract metadata and execute evaluations.
- As a **Maintainer**, I want to run repository-wide audits to identify non-compliant skills.

## Functional Requirements
1.  **JSON Schemas**:
    - Define a JSON schema for `SKILL.md` frontmatter.
    - Define a JSON schema for `evals/evals.json`.
    - Define a JSON schema for `agents/openai.yaml`.
2.  **Validation Tool**:
    - A Python script `scripts/evdd_validate.py` that takes a skill path and validates all components.
    - Support for validating a single skill or all skills in the `skills/` directory.
    - Detailed error reporting pointing to specific schema violations.
3.  **Command Integration**:
    - A new command `/evdd:validate` to trigger validation from the CLI.

## Non-Functional Requirements
- **Performance**: Validation should be fast enough to run as a pre-commit hook.
- **Portability**: The validation script should use standard Python libraries where possible (e.g., `jsonschema`).
- **Extensibility**: The framework should allow adding new schemas for other artifacts (e.g., `grading.json`).

## Out of Scope
- Automated fixing of schema violations (initial version focus is on detection).
- Execution of the evals themselves (this is handled by the `skill-creator` Improve/Benchmark modes).

## Acceptance Criteria
- [ ] JSON schemas are defined and stored in `.agents/schemas/`.
- [ ] `scripts/evdd_validate.py` is implemented and functional.
- [ ] `/evdd:validate` command is available.
- [ ] Documentation for the framework is added to `.docs/guides/evdd-guide.md`.
- [ ] The tool successfully identifies structural errors in a sample of known "broken" skills.
