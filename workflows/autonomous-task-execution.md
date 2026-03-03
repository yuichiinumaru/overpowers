# Workflow: Autonomous Task Execution

**ID**: `autonomous-task-v1`
**Description**: A robust workflow for executing complex, multi-step tasks with minimal human supervision. It uses a dual-agent pattern to separate planning from execution and persists its state to the filesystem to ensure reliability.

---

## 1. Actors

This workflow involves three main actors:

1.  **Task Orchestrator (`TaskOrchestrator`)**: The "engine" for the workflow. This is a non-LLM agent responsible for managing the state machine.
2.  **Initializer Agent (`AdminAgent`)**: A "planner" persona. Its role is to take a high-level goal and decompose it into a detailed, structured plan.
3.  **Executor Agent (`DevAgent`)**: A "doer" persona. Its role is to execute a single, specific task from the plan, verify its completion, and update the state.

---

## 2. Triggers

This workflow is triggered when a user or another agent assigns a high-level task that is too complex for a single session.

-   **Entry Point**: `TaskOrchestrator.start_new_task(description: str)`

---

## 3. Workflow Phases

### Phase 1: Initialization

1.  **Orchestrator**: A new task is requested. The `TaskOrchestrator` creates a new `TaskStateManager` instance, which results in the creation of a unique task directory in `workspace/.tasks/<task-id>`.
2.  **Orchestrator**: The orchestrator checks if a `task_list.md` exists in the new directory. It does not.
3.  **Orchestrator**: The orchestrator invokes the **Initializer Agent**.
4.  **Initializer Agent**:
    -   Receives the high-level task description via the `initializer.v1.md` prompt.
    -   Analyzes the request and generates the full, structured content for the `task_list.md` file.
    -   Returns this content to the orchestrator.
5.  **Orchestrator**: The orchestrator writes the returned content to the `task_list.md` file using the `TaskStateManager`.

### Phase 2: Execution Loop

1.  **Orchestrator**: The orchestrator enters a loop that continues as long as `TaskStateManager.is_complete()` is `False` (i.e., there are still unchecked boxes in `task_list.md`).
2.  **Orchestrator**: Inside the loop, the orchestrator invokes the **Executor Agent**.
3.  **Executor Agent**:
    -   Receives the `executor.v1.md` prompt, which instructs it to orient itself by reading the state files.
    -   It reads `task_list.md` and identifies the next single, incomplete task.
    -   It performs the actions required to complete that task (e.g., writing code, running commands).
    -   It verifies that the task is complete.
    -   It updates the `task_list.md` file by changing the task's checkbox from `[ ]` to `[x]`.
    -   It returns a summary of its work to the orchestrator.
4.  **Orchestrator**:
    -   Receives the summary from the Executor.
    -   Appends the summary to the `progress.md` file.
    -   The loop repeats.

### Phase 3: Completion

1.  **Orchestrator**: The execution loop terminates when `is_complete()` returns `True`.
2.  **Orchestrator**: The orchestrator calls its `_archive_to_khala()` method.
3.  **Archiving**: The final `task_list.md`, `progress.md`, and any other generated artifacts (e.g., source code) are saved to the Khala long-term memory system.
4.  **End**: The workflow is complete.

---

## 4. Associated Prompts

-   **Initializer**: `shared-prompts/system/initializer.v1.md`
-   **Executor**: `shared-prompts/system/executor.v1.md`

---

## 5. State Management

-   **Operational State**: Managed entirely on the filesystem in `workspace/.tasks/<task-id>/`.
    -   `task_list.md`: The single source of truth for the plan and its current status.
    -   `progress.md`: A human and machine-readable log of all actions taken.
-   **Long-Term State**: The final, valuable artifacts of the workflow are persisted in the Khala knowledge base.
