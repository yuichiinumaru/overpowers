---
description: Document completed feature implementation with API guides, architecture updates, and lessons learned
argument-hint: Optional documentation focus areas or specific sections to update
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

# Document Feature

## Outline

1. **Setup**: Get the current git branch, if it written in format `feature/<number-padded-to-3-digits>-<kebab-case-title>`, part after `feature/` is defined as FEATURE_NAME. Consuquently, FEATURE_DIR is defined as `specs/FEATURE_NAME`, TASKS_FILE is defined as `specs/FEATURE_NAME/tasks.md`.

2. **Load context**: Load and analyze the implementation context from FEATURE_DIR:
   - **REQUIRED**: Read tasks.md to verify task completion
   - **IF EXISTS**: Read plan.md for architecture and file structure
   - **IF EXISTS**: Read spec.md for feature requirements
   - **IF EXISTS**: Read contracts.md for API specifications
   - **IF EXISTS**: Read data-model.md for entities and relationships
   - Note: These files were written during previous stages of SDD workflow (Discovery, Research, Planning, etc.).

3. Continue with Stage 10

## Stage 10: Document Feature

**Goal**: Document feature completion based on implementation results and update project documentation.

### Actions

**Implementation Verification**:

1. Verify implementation status:
   - Review tasks.md to confirm all tasks are marked as completed [X]
   - Identify any incomplete or partially implemented tasks
   - Review codebase for any missing or incomplete functionality

2. **Present to user** any missing or incomplete functionality:
   - List incomplete tasks and their status
   - **Ask if they want to fix it now or later**
   - If user chooses to fix now, launch `developer` agent to address issues before proceeding
   - If there are no issues or user accepts the results as-is, proceed to documentation

**Documentation Update**:

3. Launch `tech-writer` agent to update documentation, using provided prompt exactly, while prefiling required variables:

   ```markdown
   **Goal**: Document feature implementation with API guides, architecture updates, and lessons learned, by following Documentation Update Workflow.

   User Input: {provide user input here if it exists}

   FEATURE_NAME: {FEATURE_NAME}
   FEATURE_DIR: {FEATURE_DIR}
   TASKS_FILE: {TASKS_FILE}

   ```

4. Present agent output to user with summary of documentation updates
