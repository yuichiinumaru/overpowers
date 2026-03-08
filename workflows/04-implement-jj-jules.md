---
description: Orchestrate the execution of tasks from the master task file.
argument-hint: Path to the master task file (nnnn-type-subtype-names.md)
---

# /04-implement (Execution Orchestrator)

**Goal**: Act as the master orchestrator to execute the granular checklist mapped in the master task file, dynamically deciding whether to delegate asynchronously via Jules or solve locally.

## Actions

1. **Context Initialization (Explicit Memory Read)**:
   - Read `continuity.md` to align with the current session focus and active branches.
   - Check `.agents/memories/` for any recent architectural decisions or context relevant to the task.
   - Read the provided master task file `docs/tasks/nnnn-type-subtype-names.md` completely before proceeding.

2. **Analyze Task Complexity**: 
   - Consume the provided master tracking file `docs/tasks/nnnn-type-subtype-names.md`.
   - Evaluate the computational complexity of the remaining uncompleted sub-items.

2. **Execution Strategy**:
   - **Heavy/Complex/Time-consuming Tasks**: 
     Assemble the necessary context, prep the prompt, and trigger the `/13-jules-dispatch` workflow to offload this chunk of work gracefully onto Jules infrastructure, awaiting PR creation.
   - **Light/Local/Immediate Tasks**: 
     1. Switch into an isolated local `jj` bookmark.
     2. Execute the implementation locally.
     3. **TDD Principle**: Follow `AGENTS.md` guidelines for RED-GREEN-REFACTOR. Always write/run the failing test first, make it pass, and clean up.

3. **Iterate & Check-off**: Iteratively strike through sub-items using the `[x]` tag inside the `nnnn-type-subtype-names.md` document as they achieve completion.

4. **Code Quality Gates**: At milestones or prior to concluding the workflow, invoke `/clean` and `/check` to guarantee the codebase holds perfectly aligned with the repository's linting and formatting prerequisites.

5. **Memory Synchronization (Explicit Memory Update)**:
   - Update `continuity.md` to reflect the progress made or the completion of the task.
   - If new architectural or procedural insights were discovered, use `/11-sync-memory` to persist them to `.agents/memories/` and Serena.
