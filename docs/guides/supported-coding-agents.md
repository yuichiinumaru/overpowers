# Supported Coding Agents & Configurations

The Overpowers toolkit provides targeted configurations for 9 AI coding agents. This guide catalogs the expected file paths for rules, skills, workflows, and MCP configurations.

| Coding Agent | Local / Project Rules | Global Rules | Skills (Global / Local) | Commands / Workflows | Global MCP Configuration |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Antigravity** | `.agent/rules/` | `~/.gemini/GEMINI.md` | `~/.gemini/antigravity/skills/` / `.agent/skills/` | *UI only (No native folder)* | `~/.gemini/antigravity/mcp_config.json` |
| **2. Cursor** | `.cursor/rules/` | *UI only (User Rules)* | `~/.cursor/skills/` / `.cursor/skills/` | *UI only (No native folder)* | `~/.cursor/mcp.json` |
| **3. Windsurf** | `.windsurf/rules/` | *UI only (`global_rules.md`)* | *No native folder (reads from `.agents/skills`)* | *UI only (No native folder)* | `~/.codeium/windsurf/mcp_config.json` |
| **4. Gemini CLI** | `GEMINI.md` / `AGENTS.md` | `~/.gemini/GEMINI.md` | `~/.gemini/skills/` / `.gemini/skills/` | *No native folder* | `~/.gemini/settings.json` |
| **5. Codex CLI** | `AGENTS.md` | `~/.codex/AGENTS.MD` | `~/.codex/skills/` / `.codex/skills/` | *No native folder* | `~/.codex/config.toml` |
| **6. Claude Code** | `.claude/rules/` / `CLAUDE.md` | `~/.claude/CLAUDE.md` | `~/.claude/skills/` / `.claude/skills/` | `.claude/commands/` | `~/.claude.json` |
| **7. OpenCode** | `AGENTS.md` / `CLAUDE.md` | `~/.config/opencode/AGENTS.md` | `~/.config/opencode/skills/` / `.opencode/skills/` | `~/.config/opencode/command/` / `.opencode/command/` | `~/.config/opencode/opencode.json` |
| **8. Kilo Code** | `.kilocode/rules/` | `~/.kilocode/rules/` | `~/.kilocode/skills/` / `.kilocode/skills/` | `~/.kilocode/workflows/` / `.kilocode/workflows/` | `~/.config/kilo/kilo.json` |
| **9. Factory Droid** | `AGENTS.md` | `~/.factory/AGENTS.md` | *No native folder (reads from `.agents/skills`)* | `~/.factory/droids/` / `.factory/droids/` | `~/.factory/mcp.json` |

## Notes on Configuration

- **MCP Installations**: Our internal script `scripts/install-mcps.sh` supports all 9 agents by modifying their respective JSON or TOML configuration files.
- **Rule Management**: Most agents read global rules through dedicated system prompts or `.md` files in their user profiles, while parsing local instructions from `AGENTS.md` or `.rules/` folders within the repository root.
- **Verification Notice**: Agent paths are prone to rapid changes over versions. This directory maps what the community and latest SDKs report. Always verify paths mechanically before assuming injection tools will succeed.
