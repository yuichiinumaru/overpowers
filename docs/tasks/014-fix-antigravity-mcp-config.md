# Task: 014-fix-antigravity-mcp-config

## Objective

Fix the mixed/broken state of the Antigravity MCP config (`~/.gemini/antigravity/mcp_config.json`) where some MCPs use unresolvable `{env:VAR}` patterns while others use hardcoded old paths.

## Test Requirements

- All MCP entries resolve to valid paths
- No unresolved `{env:...}` variables remain
- All MCPs connect successfully

## Exit Conditions (GDD/TDD)

- [x] Audit current Antigravity MCP config state
- [x] Fix Serena: `{env:SERENA_PATH}` → valid local path
- [x] Fix Desktop Commander: `{env:DESKTOP_COMMANDER_PATH}` → valid local path
- [x] Fix Semgrep: old `node` command → `semgrep mcp`
- [x] Update remaining MCPs to use local package paths
- [x] Verify all MCPs connect after fix

## Details

### What

The `install-mcps.sh` was partially run during the Gemini session, leaving the Antigravity config in an inconsistent state. Some MCPs were updated with `{env:VAR}` patterns but the source `.env.example` was reverted, so the vars can't resolve.

### Where

- `~/.gemini/antigravity/mcp_config.json` [MODIFY]
- Depends on 009-rebuild-mcp-infrastructure completing first

### How

Should be resolved automatically once task 009 is complete and `install-mcps.sh` is re-run. This task exists to verify the fix.

### Why

Currently Serena and Desktop Commander in Antigravity are broken (unresolved env vars). Semgrep uses the old node-based command that no longer works.

## Important Rules
1. Save your progress report ONLY in '.agents/reports/014-fix-antigravity-mcp-config.md'. NEVER use dates in filenames.
2. NEVER modify or check off tasks in 'docs/tasklist.md'. Only mark checkboxes inside YOUR task file 'docs/tasks/014-fix-antigravity-mcp-config.md'.
3. Do NOT simplify, summarize, or delete unique details when deduplicating or refactoring. Merge ALL information.