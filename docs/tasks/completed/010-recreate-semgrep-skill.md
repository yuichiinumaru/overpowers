# Task: 010-recreate-semgrep-skill

## Objective

Recreate the `skills/semgrep-code-security/SKILL.md` skill that was lost during the destructive incident.

## Test Requirements

- Skill file exists and follows SKILL.md format
- Semgrep MCP tools are accessible via the skill
- Agents can invoke Semgrep scanning via the skill

## Exit Conditions (GDD/TDD)

- [x] Create `skills/semgrep-code-security/SKILL.md`
- [x] Verify YAML frontmatter is valid
- [x] Skill covers: CLI usage, MCP tool integration, rule customization, SEMGREP_APP_TOKEN

## Details

### What

Create a comprehensive Semgrep skill that enables agents to use the Semgrep code security scanner, both via CLI and MCP tools. The skill should cover scanning directories, filtering results, creating custom rules, and using the Semgrep App Token for cloud integration.

### Where

- `skills/semgrep-code-security/SKILL.md` [NEW]

### How

Reference the Semgrep MCP server tools already available and the native `semgrep` CLI capabilities.

### Why

The original skill was created during the Gemini session but lost in the incident. It bridges the gap between having the Semgrep MCP configured and agents knowing how to use it effectively.
