# Overpowers: Orchestration System

The orchestration layer is composed of three primary agents ensuring task decomposition and execution strategies.

## 1. The CEO (Chief Executive Orchestrator)
*   **File**: `agents/000_ceo_orchestrator.md`
*   **Philosophy**: "Do not do. Delegate."
*   **Function**: Pure routing and delegation. Does not execute code or research.
*   **Delegation Matrix**:
    *   **Small/Fast**: OpenCode Subagent (Local).
    *   **Medium/Specialized**: Invoke Agent (e.g., `/invoke security-auditor`).
    *   **Large/Parallel**: Jules Swarm (Remote).
*   **Tools**: Uses `subagent-orchestration` skill and `jules-dispatch`.

## 2. Sisyphus (The Executor)
*   **File**: `agents/sisyphus/sisyphus-orchestrator.md`
*   **Role**: Senior Engineer. Handles complex multi-step tasks.
*   **Logic**:
    *   **Phase 0 (Intent Gate)**: Checks for Skills -> Triviality -> Exploration.
    *   **Mandatory Planning**: Must use `update_plan` to register TODOs before acting.
    *   **Parallelism**: Spawns `explore` (internal grep) and `librarian` (external research) agents in background.

## 3. Prometheus (The Planner)
*   **File**: `agents/prometheus/prometheus-planner.md`
*   **Role**: Strategic Consultant. STRICTLY NO CODING.
*   **Workflow**:
    *   **Interview**: Discuss requirements.
    *   **Research**: Use subagents to gather context.
    *   **Draft**: Create drafts in `.sisyphus/drafts/`.
    *   **Plan**: Finalize detailed plans in `.sisyphus/plans/`.
