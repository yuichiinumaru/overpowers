# Wave Parallelism & Math-Based Workflows

> **Context:** When orchestrating multiple asynchronous agents (like Jules), GitHub PRs and Jujutsu snapshots often encounter severe merge conflicts if two agents try to modify the same file concurrently. Wave Parallelism uses math-based `<files_modified>` ownership to guarantee zero conflicts.

## The Core Concept
A "Wave" is a grouping of tasks that are 100% independent of each other. Tasks in the same wave can be deployed to completely independent, parallel AI agents without fear of repository corruption.

## Designing the Dependency Graph
When generating task lists (e.g., in `docs/tasklist.md` or via JSON orchestrators), every task must explicitly declare:
1.  **`<files_modified>`:** The exact absolute or relative paths the agent is allowed to create or edit.
2.  **`needs`:** Which files or previous tasks must be completed before this one begins.

### The Immutable Rule of File Ownership
*   **Rule:** If `Task A` and `Task B` touch the exact same file in their `<files_modified>` lists, they **CANNOT** exist in the same Wave.
*   **Result:** One task must be deferred to the next Wave (e.g., `Task A` runs in Wave 1. `Task B` runs in Wave 2 and depends on `Task A`).

## Vertical Slices over Horizontal Layers
To maximize the number of parallel agents you can run simultaneously (large Waves), prefer designing tasks vertically.

*   **Vertical (Good - Parallelizable):**
    *   *Task 001:* Build User Auth Model + User API (Touches `models/user.ts`, `api/user.ts`)
    *   *Task 002:* Build Content Model + Content API (Touches `models/content.ts`, `api/content.ts`)
    *   *Wave Analysis:* No overlapping files. Run in parallel!
    
*   **Horizontal (Bad - Sequential Bottleneck):**
    *   *Task 001:* Build All Models (Touches `models/user.ts`, `models/content.ts`)
    *   *Task 002:* Build All APIs (Touches `api/user.ts`, `api/content.ts`)
    *   *Wave Analysis:* Task 002 `needs` the models from Task 001. Must run sequentially.

## Enforcing Waves via Nomenclature
In the `nnnn-type-name.md` nomenclature of Overpowers:
*   The first three digits define the sequential chronology (the Wave).
*   The last digit defines parallelization (0 is a blocker/sequential, 1-9 are parallel items within the wave).

Whenever dispatching a batch of tasks to Jules, you **must only dispatch tasks belonging to the current active wave.**
