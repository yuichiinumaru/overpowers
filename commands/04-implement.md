---
description: Execute the implementation plan by processing and executing all tasks defined in tasks.md
argument-hint: Optional implementation preferences or specific tasks to prioritize
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

# Implement Feature

## Outline

1. **Setup**: Get the current git branch, if it written in format `feature/<number-padded-to-3-digits>-<kebab-case-title>`, part after `feature/` is defined as FEATURE_NAME. Consuquently, FEATURE_DIR is defined as `specs/FEATURE_NAME`.
2. **Load context**: Load and analyze the implementation context from FEATURE_DIR:
   - **REQUIRED**: Read tasks.md for the complete task list and execution plan
   - **REQUIRED**: Read plan.md for tech stack, architecture, and file structure
   - **IF EXISTS**: Read data-model.md for entities and relationships
   - **IF EXISTS**: Read contracts.md for API specifications and test requirements
   - **IF EXISTS**: Read research.md for technical decisions and constraints
3. Continue with Stage 8

## Stage 8: Implement

**Goal**: Implement taks list written in `FEATURE_DIR/tasks.md` file.

**Actions**:

1. Read all relevant files identified in previous phases.
2. Parse tasks.md structure and extract:
   - **Task phases**: Setup, Tests, Core, Integration, Polish
   - **Task dependencies**: Sequential vs parallel execution rules
   - **Task details**: ID, description, file paths, parallel markers [P]
   - **Execution flow**: Order and dependency requirements

### Phase Execution

For each phase in `tasks.md` file perform following actions:

1. Execute implementation by launching new `developer` agent to implement each phase, verify that all tasks are completed in order and without errors:
   - **Phase-by-phase execution**: Complete each phase before moving to the next
   - **Respect dependencies**: Run sequential tasks in order, parallel tasks [P] can run together  
   - **Follow TDD approach**: Execute test tasks before their corresponding implementation tasks
   - **File-based coordination**: Tasks affecting the same files must run sequentially
   - **Validation checkpoints**: Verify each phase completion before proceeding

   Use provided prompt exactly, while prefiling required variables:

      ```markdown
      **Goal**: Implement {phase name} phase of tasks.md file by following Tasks.md Execution Workflow.

      User Input: {provide user input here if it exists}

      FEATURE_NAME: {FEATURE_NAME}
      FEATURE_DIR: {FEATURE_DIR}
      TASKS_FILE: {TASKS_FILE}
      ```

2. Progress tracking and error handling:
   - Report progress after each completed phase
   - Halt execution if any non-parallel phase fails
   - For parallel phase [P], continue with successful phase, report failed ones
   - Provide clear error messages with context for debugging
   - Suggest next steps if implementation cannot proceed
   - **IMPORTANT** For completed phase, make sure that all tasks in that phase are marked off as [X] in the tasks.md file.

3. Completion validation - Launch new `developer` agent to verify that all tasks are completed in order and without errors by using provided prompt exactly, while prefiling required variables:

   ```markdown
   **Goal**: Verify that all tasks in tasks.md file are completed in order and without errors.
      - Verify all required tasks are completed
      - Check that implemented features match the original specification
      - Validate that tests pass and coverage meets requirements
      - Confirm the implementation follows the technical plan
      - Report final status with summary of completed work

   User Input: {provide user input here if it exists}

   FEATURE_NAME: {FEATURE_NAME}
   FEATURE_DIR: {FEATURE_DIR}
   TASKS_FILE: {TASKS_FILE}
   ```

4. If not all phases are completed, repeat steps 1-4 for the next phase.

## Stage 9: Quality Review

1. Perform `/code-review:review-local-changes` command if it is available, if not then launch 3 `developer` agent to review code quality by using provided prompt exactly, while prefiling required variables, each of them should focus on different aspect of code quality: simplicity/DRY/elegance, bugs/functional correctness, project conventions/abstractions. Prompt for each agent:

   ```markdown
   **Goal**: Tasks.md file is implemented, review newly implemented code. Focus on {focus area}.

   User Input: {provide user input here if it exists}

   FEATURE_NAME: {FEATURE_NAME}
   FEATURE_DIR: {FEATURE_DIR}
   TASKS_FILE: {TASKS_FILE}
   ```

2. Consolidate findings and identify highest severity issues that you recommend fixing
3. **Present findings to user and ask what they want to do** (fix now, fix later, or proceed as-is)
4. Launch new `developer` agent to address issues based on user decision

### Guidelines

- DO NOT CREATE new specification files
- Maintain consistent documentation style across all documents
- Include practical examples where appropriate
- Cross-reference related documentation sections
- Document best practices and lessons learned during implementation
- Ensure documentation reflects actual implementation, not just plans
