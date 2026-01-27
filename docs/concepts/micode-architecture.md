# Micode Architecture & Concepts

Extracted from [Micode](https://github.com/vtemian/micode), this architecture focuses on a "Brainstorm-Plan-Implement" workflow with persistent state management.

## Core Concepts

### Mindmodel
A structured data representation of the project context, storing:
- **Goals**: High-level objectives.
- **Tasks**: Breakdown of work.
- **Artifacts**: Code, docs, plans.
- **Relationships**: Graph-based links between entities.

### Ledger
A chronological record of all actions, decisions, and outcomes. Similar to the `continuity.md` concept but automated.
- **Session Ledger**: Tracks current session activity.
- **Global Ledger**: Tracks cross-session history.

### Graph-Based Context
Instead of linear text, context is modeled as a graph, allowing agents to traverse relationships between:
- Code files (dependencies)
- Tasks (blockers/dependencies)
- Concepts (related topics)

## Workflow

1.  **Brainstorm**: Generate ideas and options (Agent: `brainstormer`).
2.  **Plan**: Select an option and break it down (Agent: `planner`).
3.  **Implement**: Execute the plan with code changes (Agent: `implementer`).
4.  **Review**: Verify against goals (Agent: `reviewer`).

## Key Agents

*   **Brainstormer**: Divergent thinking, generating multiple approaches.
*   **Planner**: Convergent thinking, selecting the best path.
*   **Executor/Implementer**: Code generation and file manipulation.
*   **Codebase Analyzer**: AST-aware analysis of existing code.
*   **Ledger Creator**: Maintains the continuity of the session.

## Integration Value
While Micode is TypeScript-based, its *concepts* are valuable for our `000_ceo_orchestrator` and `continuity.md` protocols.
- **Adoption**: We have adopted the "Ledger" concept in our `continuity.md`.
- **Future**: Consider implementing a "Mindmodel" MCP server for structured context.
