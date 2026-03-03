# Changelog

All notable changes to this project will be documented in this file.

> [!CAUTION]
> **IMMUTABLE HISTORY**: Entries in this file must NEVER be deleted or modified (except typo fixes).
> New entries are ALWAYS added at the TOP in descending date order.

---

## [2026-03-03] - Consolidated Generic AGENTS.md Template

### Added
- New `scripts/templates/AGENTS.md` — a comprehensive generic template (~550 lines) consolidating all rules from `AGENTS.md`, `AGENTS copy.md`, `AGENTS copy 2.md`, and all 14 `.agents/rules/` files.
- Template covers: session initialization, core philosophy, changelog protocol, knowledge routing, operational laws, security boundaries, conventions, task system, cognitive workflow & memory management, engineering standards, development practices (TDD, SDD, spec-first), multi-agent safety, VCS rules (Git + Jujutsu), Jules agent rules, delegation strategy, behavioral guidelines, forbidden actions, environment/tooling, and platform-specific rules.

**Author**: Overpowers Architect (Antigravity)

## [2026-03-02] - Merge PRs #45 and #46 via jj

### Added
- Integrated PR #46: feat: add skills extracted from Unsupervised Learning channel (Batch 1 & 2).
- Integrated PR #45: YouTube Ripper: Processes batch 7 for @fernandobrasao.

### Fixed
- Resolved merge conflicts in `CHANGELOG.md`, `.agents/reports/youtube-mining-notes.md`, and `docs/youtube/fernando-brasao.md`.

**Author**: Overpowers Architect (Gemini CLI)


## [2026-03-02] - YouTube Skill Mining: Unsupervised Learning Channel (Batch 1 & 2)

### Added
- **Skills**: `fabric-ai-evaluator` extracted from 'Using the Smartest AI to Rate Other AI' video.
- **Skills**: `nano-banana-art-generator` extracted from 'My Art Skill With Nano Banana 3' video.
- **Skills**: `claude-code-neovim-ghostty` extracted from 'Claude Code + Neovim via Ghostty Panes' video.
- **Skills**: `fabric-raycast-integration` extracted from 'Fabric New Integration with Raycast' video.
- **Reports**: Appended notes to `youtube-mining-notes.md` for batch 1 & 2 analysis.
- **Reports**: Added `docs/tasks/youtube-mining-video-analysis-report.md`.
- **Data**: Initial raw list of videos in `docs/youtube/unsupervised-learning.md`.
- **Data**: Subtitle and info files for processed videos in `docs/youtube/`.

**Author**: youtube-ripper

## [2026-03-02] - YouTube Ripper: Batch 6 & 7 (fernando-brasao)

### Changed
- Processed Batch 6 and 7 for @fernandobrasao.
- Handled HTTP 429 errors from YouTube during transcript extraction.
- Updated `docs/youtube/fernando-brasao.md` with processing status.
- Appended evaluation notes to `.agents/reports/youtube-mining-notes.md`.

**Author**: youtube-ripper

## [2026-03-02] - Docs Directory Reorganization

### Added
- New directory structure for `docs/`: `architecture/`, `guides/`, `tasks/planning/`.
- `archives/` directory for historical and obsolete documentation.
- Naming convention `nnn-type-name.md` applied to all core documentation files.

### Changed
- Reorganized `docs/` root into subdirectories.
- Moved testing patterns to `docs/guides/testing/`.
- Moved external service documentation to `docs/guides/services/`.
- Moved architectural concepts and codebase maps to `docs/architecture/`.
- Updated `docs/README.md` with new structure and fixed navigation links.
- Updated `docs/guides/004-guide-services.md` with correct internal paths.
- Updated `docs/architecture/codemaps/000-arch-index.md` with current file names.

### Fixed
- Resolved merge conflicts in `docs/README.md`.
- Completed documentation deduplication tasks (004, 005, 006).

**Author**: Overpowers Architect (Gemini CLI)

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
