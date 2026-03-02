# Task: 016-second-audit

## Objective

Perform a second comprehensive audit of the codebase to verify all tasks from the first audit were properly captured, identify any remaining gaps, and ensure no orphaned or broken references exist.

## Test Requirements

- All files referenced by tasks actually exist
- No orphaned configs, broken symlinks, or missing dependencies
- All agent frontmatter validates correctly
- All MCP configs are internally consistent

## Exit Conditions (GDD/TDD)

- [x] Re-scan docs/ for any files missed by the first audit
- [x] Verify all 939 agents have valid YAML frontmatter
- [x] Check for orphaned references in scripts (e.g., paths to deleted files)
- [x] Verify all packages/ repos are in buildable state
- [x] Check for any remaining `zuado_` prefixed or broken agents
- [x] Add any newly discovered tasks to the tasklist
- [x] Produce a brief report summarizing findings

## Details

### What

Follow-up audit to catch anything the first audit (from the Antigravity + Gemini session logs) may have missed.

### Where

Entire repository.

### How

Systematic scan of each directory with validation checks.

### Why

First audit was focused on cross-referencing session actions. A second pass with fresh eyes may catch structural issues not related to any specific session.
