# Integration Plan: Harmonization of References & Harvest

> **Mission**: Consolidate divergent branches into `feat/system-knowledge-graph` to establish a unified, canonical codebase.
> **Status**: Finalized (Iteration 10/10)

## 1. Scope
*   **Target**: `feat/system-knowledge-graph` (Current Branch)
*   **Source**: `origin/integrate-references-harvest-3671567050920031112` (Active Refinements)
*   **Excluded**: `origin/jules-harvest-mega-session-16505481372407860250` (Obsolete - Ignored)

## 2. Action Items

### A. Apply Structural Fixes (Direct Checkout)
These files in the `integrate_references` branch represent a cleaner, deduplicated state. We will adopt them entirely.

*   **Files**:
    *   `AGENTS.md` (Fixes Title, moves Safety Hooks to bottom)
    *   `JULES_ARCHITECTURAL_DIGEST.md` (Removes duplicated sections)
    *   `agents/creative-problem-solver.md` (Adds workflow links)
    *   `agents/game-dev-studio.md` (Adds workflow links)
    *   `workflows/creative/problem-solving.md` (New file)
    *   `workflows/game-dev/dev-story.md` (New file)

*   **Command**:
    ```bash
    git checkout origin/integrate-references-harvest-3671567050920031112 -- AGENTS.md JULES_ARCHITECTURAL_DIGEST.md agents/creative-problem-solver.md agents/game-dev-studio.md workflows/creative/problem-solving.md workflows/game-dev/dev-story.md
    ```

### B. Harmonize History (Manual Merge)
These files contain historical data where `integrate_references` is missing recent updates from `main`. We must manually merge the new entries from the branch without losing `main`'s history.

*   **Files**:
    *   `CHANGELOG.md`
    *   `continuity.md`

*   **Strategy**:
    1.  Read the content from the branch.
    2.  Extract the specific new blocks (e.g., "[2026-05-24] - BMAD Deepening Phase").
    3.  Prepend them to the *current* file (top of the list), ensuring no existing entries are deleted.

## 3. Execution Sequence

1.  **Checkout** clean files (Action A).
2.  **Patch** `CHANGELOG.md` with the new entry from the branch.
3.  **Patch** `continuity.md` with the new session entry from the branch.
4.  **Verify** integrity of the file system.
5.  **Commit** with message "chore: integrate refinements from reference harvest".

## 4. Rollback Plan
If verification fails, `git reset --hard HEAD` to revert to the pre-integration state.
