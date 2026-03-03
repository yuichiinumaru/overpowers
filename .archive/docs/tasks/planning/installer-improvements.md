# Installer UX and Modularity Improvements

## Objective
Refactor and improve the Overpowers installation and configuration scripts to be more modular, DRY, and user-friendly.

## Key Areas for Improvement

### 1. Deduplication and Modularization of Deploys (`deploy-to-*.sh`)
**Problem:** The `deploy-to-opencode.sh`, `deploy-to-gemini-cli.sh`, `deploy-to-antigravity.sh`, and `deploy-to-kilo.sh` scripts share ~80% of the same code (the symlink engine and `OVERPOWERS_CONFLICT_POLICY` logic). Bug fixes in one require manual syncing across all four.
**Proposed Solution:** Extract the symlink engine into a core utility script (e.g., `scripts/utils/create-symlinks.sh`), where the parent script merely defines the target variables. Alternatively, unify them into a single `scripts/deploy.sh --target <platform>` script.

### 2. Enhancing Master Installer UX (`install.sh`) with `gum`
**Problem:** While `install.sh` checks for and installs `gum` (an interactive CLI tool), the main menu and conflict resolution (`replace/copy/abort`) screens still use basic `read -p` commands. Conversely, `install-plugins.sh` provides a beautiful interactive experience using `gum choose`.
**Proposed Solution:** Upgrade the prompts in `install.sh` to use `gum choose` or `gum confirm` for navigable menus using arrow keys, with a graceful fallback to `read -p` if `gum` fails.

### 3. Consolidating OpenCode Resources
**Problem:** The OpenCode setup is currently fragmented across `install-personas.sh`, `install-plugins.sh`, and `deploy-to-opencode.sh`. All interact with `~/.config/opencode/`.
**Proposed Solution:** The `deploy-to-opencode.sh` script (or a unified opencode setup wrapper) should automatically embed or call `install-personas.sh` to prevent it from being an isolated, easily forgotten step.

### 4. Integrating API Key Management into Base Installation
**Problem:** `setup-local-api-keys.sh` is a robust centralized secret manager (Single Source of Truth) that loads keys into subsequent sessions via shell configs. However, it's not actively invoked during the main installation or MCP setup.
**Proposed Solution:** At the end of or during the MCP setup (`install-mcps.sh` or `install.sh`), provide an optional, interactive prompt that lists missing `.env` keys and asks the user to input them (calling `setup-local-api-keys.sh add`). This ensures MCP tools are functional out-of-the-box.

### 5. Maintaining Visual Consistency for Standalone Add-ons
**Problem:** Scripts like `setup-vibe-kanban.sh` and `setup-browser-use.sh` exist as isolated islands. They don't share the same start banners, standardized color palettes, or strict validations (e.g., if NPM is missing, the vibe kanban script crashes abruptly).
**Proposed Solution:** Standardize banners and color palettes to match `install-mcps.sh` or `install.sh`. Additionally, include these scripts as optional "Add-on Toolkits" in the main installer's menu.

### 6. Utilizing Python for Generic Parsing Tasks
**Problem:** `install-skills.py` (which lints the `SKILL.md` manifests) is executed manually, and `extract-installed-mcps.py` coexists with complex JSON/`jq` conversions in shell scripts.
**Proposed Solution:** Integrate the linting process (`install-skills.py`) into an automated pre-commit hook or a formal linting pipeline. This ensures no skill is merged into the repository unless it passes validation.

## Next Steps
- Review this proposed plan.
- Create execution tasks based on the points above.
- Create automated tests where possible.

### 7. Refactoring the YOLO (`-f` / `--fast`) Installation Mode
**Problem:** The `-f` flag in `install.sh` acts as a dry "mkdir -p" everywhere without checking if the user actually has the tools installed. It blindly creates `~/.cursor` and `~/.codeium/windsurf` paths, cluttering the user's home folder.
**Proposed Solution:** Add simple environment detection checks (`if [[ -d ~/.cursor ]]`) so plugins are only deployed into existing, "alive" directories.

### 8. Fixing MCP Configuration Updates (`install-mcps.sh`)
**Problem:** During MCP insertion, if the target tool's JSON already has a key (e.g. `"serena"`) via python dictionary checks, it skips the update completely. This blocks receiving new environment variables or altered tool arguments.
**Proposed Solution:** Implement deep-merging or a forced override policy for `-f` or regular updates, so existing MCP nodes get their configuration correctly updated mapped against `.env` instead of being skipped.

### 9. Handling Missing `.env` Files During Automation
**Problem:** Running `-f` without a populated `.env` causes the installer to copy `.env.example` and execute with broken, template values, because it does not stop for configuration.
**Proposed Solution:** Introduce a strict check against the environment file contents. If a template is copied, the installer should prompt or error out telling the user to fill the values, rather than propagating invalid placeholders to `settings.json` and others.

### Important Note on Coding Agents Documentation
> [!WARNING]
> We must treat the research document (`docs/guides/supported-coding-agents.md`) with skepticism. As analyzed during the study, LLM-generated tables and paths might contain hallucinations or partially incorrect system locations. We must verify every directory's actual functional existence for all 9 coding agents during script execution before assuming 100% compatibility.

### 10. Gaps in Global Asset Deployment (`install.sh`)
**Problem:** The `install-mcps.sh` correctly lists paths for all 9 coding agents (OpenCode, Cursor, Windsurf, Gemini, Codex, Claude Code, Kilo, Factory, and Antigravity). However, `install.sh` only supports creating symlinks for 4 platforms (OpenCode, Gemini, Antigravity, Kilo).
**Current Deficit:**
- **Cursor**: Missing `deploy-to-cursor.sh` (needs to link `~/.cursor/skills` and `~/.cursor/rules/`).
- **Claude Code**: Missing `deploy-to-claude-code.sh` (needs to link `~/.claude/skills`, `~/.claude/commands` and `~/.claude/CLAUDE.md`).
- **Codex CLI**: Missing `deploy-to-codex.sh` (needs to link `~/.codex/skills/` and `~/.codex/AGENTS.MD`).
- **Windsurf & Factory**: Rely on the default `~/.agents/skills` standard. Our installer currently doesn't provision a `.agents` folder for these agents.
**Proposed Solution:** While unifying the symlink engine (Point 1), we MUST expand its target configurations to dynamically provision the missing `deploy-to-*.sh` routines for ALL 9 agents mapped in our `supported-coding-agents.md` research.
