---
description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts, with complexity analysis
argument-hint: Optional task creation guidance or specific areas to focus on
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Get the current git branch, if it written in format `feature/<number-padded-to-3-digits>-<kebab-case-title>`, part after `feature/` is defined as FEATURE_NAME. Consuquently, FEATURE_DIR is defined as `specs/FEATURE_NAME`.

2. **Load context**: Read `specs/constitution.md`, also read files from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts.md (API endpoints), research.md (decisions),
   - Note: These files were written during previus stages of SDD workflow (Discovery, Research, Planining, etc.). Not all projects have all documents. Generate tasks based on what's available.
3. Copy `specs/templates/tasks-template.md` to `FEATURE_DIR/tasks.md` using `cp` command, in future refered as `TASKS_FILE`.
4. Continue with stage 6

## Stage 6: Create Tasks

1. Launch `tech-lead` agent to create tasks, using provided prompt exactly, while prefiling required variables:

    ```markdown
    **Goal**: Create tasks for the implementation.

    User Input: {provide user input here if it exists}

    FEATURE_NAME: {FEATURE_NAME}
    FEATURE_DIR: {FEATURE_DIR}
    TASKS_FILE: {TASKS_FILE}

    Please, fill/improve tasks.md file based on the task generation workflow.

    ```

2. Provide user with agent output and ask to answer on questions if any require clarification and repeat step 1, while adding questions and answers list as user input. Repeat until all questions are answered, no more than 2 times.
