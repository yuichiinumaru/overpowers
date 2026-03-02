# Task: 011-reinstall-nlm-skill

## Objective

Reinstall the NotebookLM skill via `nlm skill install` that was lost during the destructive incident.

## Test Requirements

- NLM skill directory exists under `skills/`
- Skill integrates with NotebookLM MCP for source-grounded queries

## Exit Conditions (GDD/TDD)

- [x] Run `uv run nlm skill install opencode` (or equivalent)
- [x] Verify skill files are properly installed
- [x] Confirm skill is accessible to agents

## Details

### What

The NotebookLM MCP CLI has its own skill management system. During the Gemini session, `nlm skill install` was used to install the official NLM skill that provides comprehensive CLI usage guides and MCP integration information.

### Where

- `skills/nlm-skill/` or equivalent [NEW via CLI]

### How

Use the `nlm` CLI tool from the `packages/notebooklm-mcp-cli/` local package.

### Why

Lost during the destructive incident. This skill enables agents to leverage NotebookLM for source-grounded, citation-backed research.
