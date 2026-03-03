---
description: Read the next eligible task in docs/tasks/, compile a JSON payload adhering to the Jules Orchestration Protocol, and dispatch it via CLI.
argument-hint: Optional specific task number
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Objective

Automate the "DELEGUE!" protocol by transforming a human-readable task and its technical design into a structured, deterministic JSON prompt that can be safely dispatched to the Jules background agent.

## Execution Flow

1. **Select Target Task.**
   - Parse `docs/tasklist.md` to find the next `[/]` in progress or pending unassigned blocker task.
   - Check if a specific task was requested in `$ARGUMENTS`.
   - Verify the task has a companion `TECHNICAL_DESIGN.md` if it's a feature.

2. **Synthesize JSON Prompt.**
   - Read the task, design, and plan files.
   - Construct a JSON prompt conforming to the JSON Prompt Architecture (Regra 9.1).
   - Ensure the JSON includes:
     - `"directives": { "always_do": [...], "never_do": [...] }`
     - `"pipeline": [...]`
   - Explicitly add the mandatory final pipeline step: *"Launch the Code Review. If there are observations, fix them and repeat. If flawless, finish execution."*
   - Explicitly forbid shell commands like `git checkout` within the JSON (Regra 9.2).

3. **Prepare Jules payload.**
   - Save the assembled JSON to `prompts/jules-dispatch-[task-number].json`.

4. **Dispatch Execution.**
   - Inform the user of the payload creation.
   - Ask for confirmation before firing the CLI command (e.g., `jules execute --prompt prompts/jules-dispatch-[task-number].json`).
   - If approved, launch the command inside a terminal block formatted as `command > .agents/thoughts/jules-[task-number]-output.md &`.

5. **Update Ledger.**
   - Log the dispatch event in `continuity.md` and the relevant task file.
