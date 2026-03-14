---
description: Create a technical design spanning multiple features for a new project.
argument-hint: Path to the project's master plan document
---

# /02-plan-all (Global Architecture Design)

**Context**: Use this workflow immediately after `/01-specify-project`. This is for establishing the foundational architecture of the ENTIRE system.

**Goal**: Read a master project plan and generate the core architectural documents, ensuring no architectural drift or broken dependencies.

## Actions

1. **Context Initialization (Explicit Memory Read)**: 
   - Read `.agents/continuity-<agent-name>.md` and check `.agents/memories/` to internalize the project's macro goals and established principles.

2. **Consume Plan**: Read the provided master plan document.

3. **Consult Architecture**: Read `AGENTS.md` and `.archive/SYSTEM_KNOWLEDGE_GRAPH.json` (if applicable) to establish system boundaries, frameworks, and allowed tech stack.

4. **Design Architecture (System Level)**: 
   - Define global dependencies, tech stack choices, and infrastructure patterns.
   - Define global API contracts, database schemas, and architectural boundaries.
   - Document cross-cutting constraints (auth, logging, error handling, performance).

5. **Verify Alignment**: Confirm no unapproved "Architecture Drift" occurs (e.g., using forbidden databases). Enforce the project's established principles.

6. **Output Design**: Generate the structural definition inside `docs/tasks/0000-global-technical-design.md` or equivalent foundational blueprint.

7. **Memory Synchronization (Explicit Memory Update)**: 
   - Update `.agents/continuity-<agent-name>.md` to reflect the global architecture setup.
   - Persist critical architectural boundaries to `.agents/memories/` via Serena.
