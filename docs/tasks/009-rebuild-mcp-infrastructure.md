# Task: 009-rebuild-mcp-infrastructure

## Objective

Rebuild the MCP infrastructure that was lost during the destructive incident of 2026-03-01. This includes the build script, environment variables, config files, and installation enhancements.

## Test Requirements

- All 11 local MCP packages build successfully via "build-packages.sh"
- "install-mcps.sh -f" runs end-to-end without errors
- All MCPs connect (10/10 green) after installation
- Relative paths ("./packages/...") resolve correctly to absolute paths

## Exit Conditions (GDD/TDD)

- [x] Create "scripts/setup/build-packages.sh" (npm install/build for Node.js, uv sync for Python)
- [x] Update ".env.example" with local "./packages/" paths for all MCPs
- [x] Update "opencode-example.json" to use "{env:VAR}" patterns for local packages
- [x] Update Semgrep MCP to use native "semgrep mcp" command
- [x] Add "-f"/"--fast" flag to "install-mcps.sh"
- [x] Add relative-to-absolute path expansion in "install-mcps.sh"
- [x] Integrate "build-packages.sh" call in "install.sh"
- [x] Run installation and verify all 10+ MCPs connect

## Details

### What

Recreate the complete MCP local-packages infrastructure:
1. "scripts/setup/build-packages.sh" — builds In-Memoria, DesktopCommanderMCP, vibe-check-mcp-server (npm), serena, notebooklm-mcp-cli (uv)
2. ".env.example" — replace "~/.config/opencode/mcp/..." paths with "./packages/..." relative paths
3. "opencode-example.json" — update serena, desktop-commander, in-memoria, vibe-check, notebooklm, semgrep configs
4. "install-mcps.sh" — add "--fast" flag, path expansion logic

### Where

- "scripts/setup/build-packages.sh" [NEW]
- ".env.example" [MODIFY]
- ".opencode/opencode-example.json" [MODIFY]
- "scripts/install-mcps.sh" [MODIFY]
- "scripts/install.sh" [MODIFY]

### How

Follow the exact patterns documented in the Gemini session log and the walkthrough audit.

### Why

These changes were successfully implemented during the Gemini CLI session but were lost when the working tree was restored to an earlier commit after the destructive incident.
