# Changelog

All notable changes to this project will be documented in this file.

> [!CAUTION]
> **IMMUTABLE HISTORY**: Entries in this file must NEVER be deleted or modified (except typo fixes).
> New entries are ALWAYS added at the TOP in descending date order.

---

## [2026-03-02] - Second Pass Audit and Agent Standardization

### Added
- New audit report: "docs/architecture/016-second-audit-report.md".
- New maintenance script: "scripts/fix_agents.py" for standardizing agent frontmatter.

### Fixed
- **Critical**: Standardized frontmatter for all 938 agents. Fixed missing "tools" fields and corrupted YAML syntax across 832 files.
- Completed rebranding sweep from "superpowers" to "overpowers" in "README.md", "AGENTS.md", "install.sh", and core documentation.
- Ensured all agent "color" fields are double-quoted hex codes per constitutional rules.

### Changed
- Updated "docs/tasklist.md" marking Task 016 as complete.

**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-02] - Enhanced Installation UX and Kilo Code Support

### Added
- New deployment script "scripts/deploy-to-kilo.sh" for Kilo Code support.
- Support for "OVERPOWERS_CONFLICT_POLICY" environment variable in all deployment scripts to allow merging assets instead of replacing them.
- Documentation for Kilo Code in "README.md" and "AGENTS.md".

### Changed
- Major UX improvements to "install.sh":
    - Added pre-install explanation of installation steps.
    - Added data handling disclaimer.
    - Implemented asset conflict detection for all platforms.
    - Added interactive prompts for conflict resolution (Replace vs Copy-Only).
    - Expanded platform selection to include Kilo Code.
    - Improved final installation summary.

**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-02] - Fix Antigravity and Multi-Platform MCP Configurations

### Fixed
- Resolved unresolvable "{env:VAR}" and "${VAR}" patterns in "~/.gemini/antigravity/mcp_config.json".
- Standardized Antigravity, Gemini CLI ("settings.json"), and OpenCode ("opencode.json") MCP configurations with valid absolute paths.
- Updated "memcord" to use "uvx memcord server" instead of hardcoded virtualenv paths.
- Corrected "notebooklm" MCP command arguments to include the "run" subcommand.
- Fixed "semgrep" MCP configuration to use native "semgrep mcp" command.

### Changed
- Updated "scripts/templates/mcp-antigravity.json" with modern command patterns and Semgrep support.
- Synchronized "opencode-example.json" with the latest multi-platform configuration standards.

**Author**: Overpowers Architect (Gemini CLI)
