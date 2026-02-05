# Compound Product Cycle: Report to Code

## Overview
The "Compound Product Cycle" is an automated workflow that converts high-level reports into executed code. It uses an agentic loop to analyze reports, generate a PRD (Product Requirements Document), break it down into tasks, and implement them iteratively.

## Workflow Steps

1.  **Report Generation**:
    *   Place a markdown report in `reports/`.
    *   Format: Detailed analysis or feature request.

2.  **Analysis & Planning**:
    *   Run `scripts/compound/auto-compound.sh`.
    *   The system analyzes the latest report in `reports/`.
    *   It identifies the #1 actionable priority.
    *   It creates a Feature Branch (`compound/feature-name`).
    *   It generates a PRD (`tasks/prd-feature-name.md`) and a Task List (`scripts/compound/prd.json`).

3.  **Execution Loop**:
    *   The system enters a loop (max 25 iterations).
    *   **Pick Task**: Selects the next failing task from `prd.json`.
    *   **Implement**: Coding agent implements the task.
    *   **Verify**: Quality checks are run.
    *   **Commit**: Changes are committed if checks pass.
    *   **Mark Complete**: Task is updated in `prd.json`.

4.  **Review**:
    *   A Pull Request is generated automatically (if configured) or the branch is pushed.
    *   Human review is required before merging.

## Usage

```bash
# 1. Add a report
echo "# New Feature Request..." > reports/2026-05-24-feature-request.md

# 2. Run the cycle
./scripts/compound/auto-compound.sh
```

## Configuration
Edit `scripts/compound/compound.config.json` to customize:
*   `tool`: Agent tool to use (e.g., `opencode`, `claude`, `amp`).
*   `qualityChecks`: Array of commands to run for verification.
*   `maxIterations`: Limit to prevent infinite loops.
