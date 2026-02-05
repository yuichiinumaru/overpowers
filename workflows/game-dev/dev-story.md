# Workflow: Dev Story (Game Dev Studio)

**Purpose**: Execute a development story by implementing tasks, writing tests, and validating acceptance criteria.
**Source**: `bmad-module-game-dev-studio/src/workflows/4-production/dev-story`

## Critical Constraints
- **Language**: Tailor communication to User's Game Dev Experience.
- **Modifications**: Only modify: Tasks/Subtasks checkboxes, Dev Agent Record, File List, Change Log, Status.
- **Execution**: Continuous execution (Red-Green-Refactor) without stopping until story is COMPLETE.
- **Halt Conditions**: Missing config, 3 consecutive failures, new dependencies required.

## Phase 1: Context & Discovery
1.  **Find Story**:
    *   Check `sprint-status.yaml` for "ready-for-dev".
    *   Or check file system for `*-*-*.md` with status "ready-for-dev".
    *   Or use user-provided path.
2.  **Load Context**:
    *   Read `project-context.md`.
    *   Read Story Dev Notes (architecture, patterns).
3.  **Detect State**:
    *   Is this a fresh start?
    *   Or continuation from Code Review? (Check "Senior Developer Review" section).

## Phase 2: Implementation Loop (Red-Green-Refactor)
*For each incomplete task/subtask:*

1.  **Red**: Write FAILING tests first. Confirm failure.
2.  **Green**: Implement MINIMAL code to pass tests.
3.  **Refactor**: Improve structure, check game loop performance.
4.  **Verify**: Run all tests (regression check).
5.  **Mark**: Update checkbox `[x]` ONLY if validation passes.

## Phase 3: Completion & Review
1.  **Definition of Done (DoD)**:
    *   All tasks marked `[x]`.
    *   All ACs satisfied.
    *   File list updated.
    *   No regressions.
2.  **Status Update**:
    *   Set Story Status to "review".
    *   Update `sprint-status.yaml` to "review".
3.  **Handoff**:
    *   Summarize changes.
    *   Suggest `code-review` workflow.

## Tools
- `tests`: Unit (Vitest/NUnit), Integration, E2E.
- `files`: Read/Write game assets and scripts.
- `sprint`: Manage `sprint-status.yaml`.
