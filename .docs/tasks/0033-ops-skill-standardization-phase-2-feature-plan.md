# Feature Plan: Skill Standardization Phase 2

## Overview
Execute a repository-wide standardization sweep across 1300+ skills to ensure metadata consistency, structural alignment with Overpowers templates, and linguistic uniformity (English-only).

## User Stories
- As a **Maintainer**, I want all skills to have standardized YAML frontmatter so that automation tools can reliably parse skill metadata.
- As an **AI Agent**, I want a consistent 'Inputs/Process/Outputs' structure in all skills so that I can quickly understand how to use any skill.
- As a **Global User**, I want all skills to be in English to ensure broad accessibility and consistent reasoning performance.

## Functional Requirements
1.  **Metadata Standardization**:
    - Ensure `name` and `description` are present and valid (using `evdd_validate.py`).
    - Add `version`, `category`, and `tags` if missing (inference based on folder structure).
2.  **Structural Update**:
    - Inject standard sections: `## Inputs`, `## Process`, `## Outputs` into `SKILL.md` if they don't follow a clear workflow pattern.
3.  **Linguistic Sweep**:
    - Identify skills with Portuguese content.
    - Translate body and metadata to English using LLM-assisted translation.
4.  **Integrity Restoration**:
    - Repair invalid skills identified in the EvDD audit.
    - Archive skills that are redundant or beyond repair.

## Execution Strategy (Batch-Based)
Due to the volume of skills (1300+), work will be divided into batches:
- **Batch 1 (Audit & Triage)**: Run full EvDD audit and generate an "Invalid Skills" report.
- **Batch 2 (Core Metadata)**: Standardize frontmatter for all skills using a script.
- **Batch 3 (Translation)**: Process Portuguese-heavy categories (e.g. `growth-biz`, `content-media`).
- **Batch 4 (Structural Sections)**: Apply workflow templates to high-use skills first.

## Non-Functional Requirements
- **Safety**: Do not overwrite unique procedural logic during standardization.
- **Brevity**: Maintain the "Concise is Key" principle of Overpowers.

## Out of Scope
- Performance benchmarking of the skills (Standardization only).
- Creating new evaluations (Task 0025 already covers the framework).

## Acceptance Criteria
- [ ] 100% of skills pass `evdd_validate.py`.
- [ ] All `SKILL.md` files are in English.
- [ ] Frontmatter contains `version`, `category`, and `tags`.
- [ ] High-priority skills (orchestration, core dev) follow the standard 'Inputs/Process/Outputs' structure.
