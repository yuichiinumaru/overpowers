---
description: Break down a technical design and feature plan into an actionable task checklist for a single feature.
argument-hint: Feature prefix or paths to the feature's plan and design documents
---

# /03-task-feature (Feature Task Breakdown)

**Context**: Use this workflow when you have a completed Feature Plan (`01-specify-feature`) and Technical Design (`02-plan-feature`) and need an execution checklist to build THAT specific feature.

**Goal**: Read the feature plan and technical design to construct the final execution checklist inside a single master task file.

## Actions

1. **Read Context**: Analyze the unified SDD dual/triplet: 
   - `docs/tasks/nnnn-type-subtype-[name]-feature-plan.md`
   - `docs/tasks/nnnn-type-subtype-[name]-technical-design.md`

2. **Breakdown**: Decompose the feature into a detailed, granular, and sequential checklist of sub-tasks for actual implementation. Identify tasks that can be done in parallel (`01-9`) vs sequence blockers (`0`).

3. **Create Master Task**: 
   - Generate `docs/tasks/nnnn-type-subtype-[name].md`.
   - Embed links or references to the plan and design docs inside the master task.
   - Populate the file with the sub-tasks checklist mapped out in step 2.

4. **Update Status**: 
   - Find this master task in `docs/tasklist.md` (or append it if missing).
   - Mark its status as `[/]` (In Progress).
   - **Crucial**: Reinforce the Jules constitution that Jules Agents NEVER mutate `docs/tasklist.md`.
