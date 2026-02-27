# Workflow: Specification-Driven Development (SDD)

**ID**: `spec-driven-development-v1`
**Description**: A rigorous, 7-phase workflow for taking a high-level feature request from concept to a fully specified, planned, and implemented reality. This workflow ensures quality, consistency, and alignment with project principles.

---

## 1. Actors

-   **Chief Architect (`ChiefArchitect`)**: The orchestrator of the entire SDD workflow.
-   **Business Analyst (`AdminAgent`)**: Responsible for clarifying requirements and creating the initial specification.
-   **Planner (`ChiefArchitect`)**: The architect agent itself is responsible for creating the technical plan.
-   **Task Decomposer (`AdminAgent` as Initializer)**: Responsible for breaking the technical plan into a granular task list.
-   **Quality Assurance (`RevisorAgent`)**: Responsible for analyzing the plan for consistency and completeness before implementation.
-   **Implementer (`DevAgent` as Executor)**: Responsible for executing the task list.

---

## 2. Triggers

This workflow is triggered when a user or another agent requests a new feature that requires a formal design process.

-   **Entry Point**: `ChiefArchitect.design_and_implement_feature(description: str)`

---

## 3. Workflow Phases

### Phase 1: Constitution
1.  **Architect**: Reads the `AGENTS.md` file to load the project's governing principles into its context.

### Phase 2: Specify
1.  **Architect**: Invokes the **Business Analyst** (`AdminAgent`) with the feature description.
2.  **Business Analyst**: Analyzes the request, identifies ambiguities, and generates a detailed `spec.md` file using a standardized template. This artifact is saved to a temporary workspace.

### Phase 3: Clarify
1.  **Architect**: Reviews the generated `spec.md` for ambiguities.
2.  **Architect**: If necessary, enters a dialogue with the user to clarify the requirements. The `spec.md` is updated based on the user's feedback.

### Phase 4: Plan
1.  **Architect**: Takes the finalized `spec.md` and creates a high-level technical plan, `plan.md`. This includes architectural decisions, component design, and data models. This artifact is saved to the workspace.

### Phase 5: Tasks
1.  **Architect**: Invokes the `TaskOrchestrator`'s **Initializer role** (`AdminAgent`).
2.  **Task Decomposer**: The `AdminAgent` receives the `plan.md` as its input and generates a detailed, dependency-ordered `tasks.md` file.

### Phase 6: Analyze
1.  **Architect**: Invokes the **Quality Assurance** agent (`RevisorAgent`).
2.  **QA Agent**: Reads the `constitution.md`, `spec.md`, `plan.md`, and `tasks.md` files. It performs a read-only analysis to ensure that all requirements are covered by tasks and that the plan is consistent and feasible.
3.  **Architect**: If the analysis passes, the workflow proceeds. If it fails, the architect moves the process back to the appropriate phase to correct the errors.

### Phase 7: Implement
1.  **Architect**: Hands off the validated task list to the `TaskOrchestrator`.
2.  **Orchestrator**: The `TaskOrchestrator` begins its standard **Execution Loop**, using the `DevAgent` as the **Implementer** to work through the `tasks.md` file until the feature is complete.

### Phase 8: Completion
1.  **Architect**: Once the `TaskOrchestrator` reports completion, the `ChiefArchitect` archives all the generated artifacts (`spec.md`, `plan.md`, `tasks.md`, plus the implementation logs) to the Khala memory system.

---

## 4. Associated Prompts

-   This workflow will require a new set of prompts for each phase, to be stored in `shared-prompts/system/sdd/`:
    -   `specify.v1.md`
    -   `plan.v1.md`
    -   `analyze.v1.md`
