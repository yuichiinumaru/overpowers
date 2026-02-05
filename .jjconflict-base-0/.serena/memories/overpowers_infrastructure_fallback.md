# Overpowers: Infrastructure & Fallback Systems

## Automated Model Fallback
*   **Script**: `skills/subagent-orchestration/scripts/run-subagent.sh`
*   **Mechanism**:
    1.  Attempts execution with Primary Model (Default: `google/antigravity-claude-sonnet-4-5-thinking`).
    2.  Captures `stdout`/`stderr` to a temporary buffer.
    3.  Scans output for Regex triggers: `rate.?limit`, `quota`, `429`, `exceeded`.
    4.  **Fallback Trigger**: If caught, automatically re-runs task with Fallback Model.
*   **Configuration**:
    *   `SUBAGENT_FALLBACK`: Defaults to `windsurf/glm-4.7` (chosen for speed/cost).
    *   `SUBAGENT_ENABLE_FALLBACK`: `true`/`false`.
    *   `SUBAGENT_TIMEOUT`: Default 300s.

## Context & Permissioning
*   **Permissions**: The script exports `OPENCODE_PERMISSION='"allow"'` to bypass interactive prompts during subagent execution.
*   **Safety**: Explicitly checks if running inside `.config` config dir (warns against it to avoid perm issues), although works around it.
