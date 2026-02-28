---
name: gemini-cli-administration
description: Teaches how to administer Gemini CLI environments (MCPs, extensions, settings)
---

# ⚙️ Gemini CLI Administration Skill

This skill teaches agents how to administer the `gemini` CLI tool for a user or project. This involves modifying settings, managing extensions, configuring MCP servers, and handling Agent Skills.

## 🛠 Settings Configuration

Gemini CLI uses a hierarchical configuration. The primary configuration files are:
1. **User-level:** `~/.gemini/settings.json`
2. **Project-level:** `.gemini/settings.json` (inside the current working directory)

Important settings you might need to adjust manually or via scripts:
- `general.yoloMode`: Enables auto-approval in interactive sessions (`true`/`false`).
- `tools.useRipgrep`: Uses `rg` instead of grep.
- `skills.enabled`: Enables the custom skills framework (`true`/`false`).
- `model.name`: Sets the default model alias.

*(Note: You can also use the interactive `/settings` command inside a Gemini chat session).*

## 🔌 MCP Server Management

To install and manage Model Context Protocol (MCP) servers:

- **Add an MCP server via npm command:**
  ```bash
  gemini mcp add <name> <cmd>
  # Example: gemini mcp add github npx -y @modelcontextprotocol/server-github
  ```

- **Add an MCP server via URL:**
  ```bash
  gemini mcp add <name> <url> --transport http
  ```

- **Set Env Vars or Tools:**
  ```bash
  gemini mcp add mydb node db.js --env DB_PW=123 --include-tools query,insert
  ```

- **List active MCP servers:**
  ```bash
  gemini mcp list
  ```

- **Remove an MCP server:**
  ```bash
  gemini mcp remove <name>
  ```

## 🧩 Extensions Management

Extensions provide bundled tools, agents, and custom subagents.

- **Install an extension:**
  ```bash
  gemini extensions install <github_url_or_path>
  ```

- **Enable / Disable / List:**
  ```bash
  gemini extensions list
  gemini extensions enable <name>
  gemini extensions disable <name>
  ```

## 🧠 Skills Management

Skills empower agents with specialized context.

- **List installed skills:**
  ```bash
  gemini skills list
  ```

- **Install or Link local skills:**
  ```bash
  gemini skills install <github_url>
  gemini skills link /absolute/path/to/local/skills/dir
  ```

- **Enable / Disable:**
  ```bash
  gemini skills enable <name>
  gemini skills disable <name>
  # Or toggle all:
  gemini skills enable --all
  ```
