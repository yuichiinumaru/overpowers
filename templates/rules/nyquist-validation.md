# Nyquist Validation Architecture

> **Context:** Originally designed in the "get-shit-done" framework, the Nyquist Validation Architecture ensures that before any single line of code is written by an agent, a formal, automated verifiable constraint must exist to prove that the code achieved the goal.

## The Strategy

When planning an EPIC or extracting tasks (see `goal-backward-planning.md`), the architecture demands a mapping step for all requirements.

### 1. The `VALIDATION.md` Output

Any feature design must be accompanied by, or contain within its design, a strict mapping of features to commands.

If building a standalone project, maintain a `docs/VALIDATION.md`. If writing tasks inside `.md` blocks within `docs/tasks/`, enforce the `<verify>` tag (as shown in `000-gsd-task-template.md`).

### 2. The Verification Feedback Loop

When executing a task, an agent **MUST NOT** consider the task "done" until the automated verification script returns a success code.

*   *Bad:* Writing the code and returning immediately.
*   *Good:* Writing the code, running `npm run test -- --grep "Auth"`, verifying the green output, and **then** declaring the task complete.

## Enforcement (Retroactive Audits)

If a phase or project lacks a proper Nyquist configuration, the executing agent must refuse to implement the code. 
Instead, it should default to Deviation Rule 4 (`checkpoint:decision`), warning the user that no automated validation mechanism has been provided to ensure the quality of the generative code.
