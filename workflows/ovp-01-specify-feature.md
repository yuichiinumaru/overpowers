---
description: Transform a single feature idea into a structured feature plan document.
argument-hint: Feature description or reference to a planning document
---

# /01-specify-feature (Feature Specification)

**Context**: Use this workflow when the user wants to build ONE specific feature within an already established project.

**Goal**: Transform a raw idea into a formal `nnnn-type-subtype-[name]-feature-plan.md` using Specification-First Development (SDD).

## Actions

1. **Understand Input**: Review the raw idea or the provided document in `docs/tasks/planning/`.

2. **Interview User**: Ask clarifying questions to extract:
   - **Vertical Slices**: How the feature can be divided incrementally into deployable milestones.
   - **Exit Conditions / Acceptance Criteria**: What definitively constitutes the feature as "complete" and ready for testing.
   - **Jobs To Be Done (JTBD)**: The real-world objective the user is trying to accomplish.

3. **Format & Save**: 
   - Generate `docs/tasks/nnnn-type-subtype-[name]-feature-plan.md` using the standard convention.
   - Ensure the template structure (`000-template-feature-plan.md` if available) is strictly followed.
   - **CRITICAL**: No code is to be generated or modified during this stage. This is strictly for requirement clarification.
