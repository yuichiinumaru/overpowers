---
description: Decompose a master project plan into high-level tasks or epics.
argument-hint: Path to the master project plan
---

# /03-task-project (Project Epic Breakdown)

**Context**: Use this workflow after `01-specify-project` and `02-plan-all` to break down the global architecture into distinct chunks (epics/features) that will later be planned individually.

**Goal**: Establish the high-level roadmap and generate the sequence of `01-specify-feature` tasks needed to build the entire system.

## Actions

1. **Read Context**: Analyze the master documents:
   - `0000-project-master-plan.md`
   - `0000-global-technical-design.md`

2. **Breakdown Epics/Features**: Decompose the entire project into major deliverables (epics). 
   - Determine the correct chronological sequence (`nnnn`) for these epics (e.g., Database setup first, Auth second, UI third).
   - Identify which epics block others (`0`) and which can happen in parallel (`1-9`).

3. **Populate Tasklist**: 
   - Add these high-level epics directly into `docs/tasklist.md`.
   - Instead of breaking down code-level subtasks, these epics represent the macro sequence. 
   - Note that each of these epics will eventually be passed through `/01-specify-feature` and `/02-plan-feature` when it's time to build them.
