# Task 009: Rebuild MCP Infrastructure

## Summary
Recreated the MCP local-packages infrastructure lost during the incident of 2026-03-01. Restored the dynamic setup process for locally compiling and managing multiple Model Context Protocol (MCP) packages, alongside configurations dynamically loading absolute paths from relative templates.

## Changes Made
- Created `scripts/setup/build-packages.sh` to run `npm install && npm run build` for Node.js MCPs and `uv sync` for Python MCPs directly in `packages/`.
- Updated `.env.example` to refer to `./packages/...` paths instead of `~/.config/...`.
- Updated `opencode-example.json` to properly format and map all missing environments, changing `desktop-commander` and `serena` to use local targets (`{env:...}`).
- Migrated `semgrep` setup to leverage the global `semgrep mcp` command.
- Enabled relative path resolution dynamically in `scripts/install-mcps.sh` expanding `./packages/` to `$REPO_ROOT/packages/`.
- Updated `scripts/install-mcps.sh` to properly accept `-f`/`--fast` flag for autonomous installation runs.
- Injected `bash scripts/setup/build-packages.sh` before Phase 2 in `install.sh`.
- Updated checklist strictly in `docs/tasks/009-rebuild-mcp-infrastructure.md`.

## Output Validations
- Build packages safely gracefully fallbacks when `packages` directory isn't fully pre-cloned yet or skips absent files.
- Antigravity's test output correctly interpolated node bindings to exact path via `env_vals` in `.gemini/antigravity/mcp_config.json`.
- Task file checks marked correctly.
