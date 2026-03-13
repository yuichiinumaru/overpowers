# Overpowers: Timeline of Recent Changes

## Jan 2026: The "Oh My OpenCode" Migration & Expansion

### 1. Integration of "Oh My OpenCode" (Jan 19)
*   Massive ingestion of components from `oh-my-opencode`.
*   Porting of high-level orchestrators: `Sisyphus` (Orchestrator), `Prometheus` (Planner), `Oracle` (Advisor).
*   Added `interactive-bash` and `tmux-interactive.sh` for safe shell interactions.

### 2. The "Nuclear" Mode & Antigravity (Jan 18-19)
*   Created `install-antigravity-skills.sh` with a "Nuclear Mode" to install ALL 500+ components into the Google Antigravity IDE.
*   Developed `convert-agents-to-skills.py` to bridge OpenCode agents to Antigravity skills.

### 3. Protocol & Naming fixes (Jan 19-23)
*   Addressed "Gemini 400 Bad Request" errors.
*   Sanitized agent names to `snake_case` to comply with stricter model protocols.
*   Fixed `SKILL.md` frontmatter validation issues using `fix-skill-frontmatter.py`.

### 4. Jules Swarm (Jan 16)
*   Integrated `jules-swarm` submodule for parallel task orchestration.
*   Workflows: Dispatch -> Harvest -> Triage -> Integrate.

### 5. Personas Integration (Jan 19)
*   Generated 13 role-based personas (e.g., `devops-engineer`, `security-auditor`).
*   Integrated "YAAMCPL" (Yet Another Awesome MCP List) winners into these personas.

## March 2026: The Great Cleanup & Restructuring

### 1. Jules Pipeline Refactoring (Mar 13)
*   Archived obsolete/redundant Jules scripts.
*   Renamed remaining scripts into a clear 4-stage pipeline (`01-jules-launch.sh`, `02-jules-harvest.py`, `03-jules-preview.py`, `04-jj-apply.sh`).
*   Implemented reactive quota detection (Exit Code 69) to automatically prompt for Google account rotation when Jules API limits are hit.

### 2. Command Collision Resolution (Mar 13)
*   Renamed all workflow markdown files to `ovp-*.md`.
*   Moved compiled TOML commands from `.agents/commands/workflows/` to `workflows/toml/`.
*   Updated `deploy-to-gemini-cli.sh` to symlink the correct new paths, solving collisions with built-in Gemini CLI commands (like `/docs`, `/editor`).

### 3. File & Documentation Organization (Mar 13)
*   Created a clean `docs/` directory for public user-facing documentation and moved internal project planning to `.docs/`.
*   Updated `AGENTS.md` to reflect these directory changes and added Section 10.4 forbidding interactive CLI commands (like `jj log` with pagers) during parallel operations, mandating file redirection to `.agents/thoughts/`.
*   Moved all ad-hoc scripts to `scripts/maintenance/` and `scripts/utils/`.

### 4. Massive Deduplication (Mar 13)
*   Discovered and removed 468 exact duplicate agent markdown files (e.g., legacy files with `--` in names).
*   Consolidated duplicate skill directories (merged content from Anthropic-named folders into primary ones, preserving scripts with collision-safe suffixes).
*   Cleaned up all empty directories in `skills/`, `workflows/`, and `agents/`.

### 5. Automated Component Counting (Mar 13)
*   Created `update_readme_counts.py` to count active `.md` files dynamically across agents, skills, workflows, scripts, and hooks.
*   Updated `AGENTS.md` changelog protocol to strictly require running this counting script before commits, keeping `README.md` permanently synced.
