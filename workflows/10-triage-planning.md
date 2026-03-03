---
description: Triage docs/tasks/planning/ proposals against the codebase and promote viable ones to approved tasks.
argument-hint: Optional filter keywords or specific proposal files to triage
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Objective

Review all proposals in `docs/tasks/planning/`, compare them against the current codebase state, and either promote them to approved tasks, archive them as already-done, or flag them for user decision.

## Execution Flow

1. **Inventory planning proposals.**
   - List all files in `docs/tasks/planning/`.
   - Read each proposal and extract: title, objective, and key deliverables.

2. **Compare each proposal against the codebase.**
   - For each proposal, search the codebase for evidence that the work has already been done:
     - Search for key function names, class names, or features mentioned in the proposal.
     - Check git log for related commits (read-only: `git log --oneline --grep="keyword"`).
     - Look for relevant test files that would indicate implementation.
   - Classify each proposal as:
     - **IMPLEMENTED**: The feature/fix already exists in the codebase. → Move to `.archive/docs/tasks/planning/`.
     - **PROMOTE**: The work has NOT been done and is still valuable. → Create approved task in `docs/tasks/`.
     - **UNCERTAIN**: Cannot definitively determine status. → Flag for user decision.

3. **Promote viable proposals.**
   - For each `PROMOTE` proposal:
     - Determine the next available `nnnn` task number based on existing tasks in `docs/tasks/`.
     - Determine if the task is a `feature` type (requires feature-plan and technical-design companions).
     - Create the task file following the standard template: `nnnn-type-subtype-names.md`.
     - If it is a feature, also create:
       - `nnnn-type-subtype-names-feature-plan.md`
       - `nnnn-type-subtype-names-technical-design.md`
     - Update `docs/tasklist.md` with the new task entry.

4. **Archive implemented proposals.**
   - Move completed proposals to `.archive/docs/tasks/planning/` using `mv`.

5. **Present uncertain proposals to user.**
   - For each `UNCERTAIN` proposal, present:
     - The proposal summary.
     - Why it is uncertain (what evidence was found/not found).
     - A recommendation (lean towards promote or archive).
   - Wait for user decision before acting.

6. **Report summary.**
   - Proposals promoted to tasks (count and list with new task filenames).
   - Proposals archived as already-implemented (count and list).
   - Proposals pending user decision (count and list).
   - Updated `docs/tasklist.md` state.
