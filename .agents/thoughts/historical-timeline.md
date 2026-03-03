# Overpowers MCP & Orchestration Setup - Historical Timeline

## Phase 1: Analysis & Template Generation
*   **Action:** Analyzed `AGENTS.md` and rule files from `.agents/rules/`.
*   **Result:** Created a unified, generic `AGENTS.md` template in `scripts/templates/` encompassing operational rules and identity for future agents.

## Phase 2: MCP Script Consolidation
*   **Action:** Refactored `scripts/install-mcps.sh` into a unified installer for OpenCode, Gemini CLI, and Antigravity.
*   **Result:** Developed standard JSON and TOML templates for 9 MCP platforms, mapping tools and environments centrally.

## Phase 3: Gemini CLI 512 Tools Limit (Agent Frontmatter validation)
*   **Action:** Identified that 914 agents + MCP tools exceeded Gemini CLI's 512-tool hard limit.
*   **Result:** Curated a list of the 150 most critical agents (coding, security, devops) and updated `deploy-to-gemini-cli.sh` to copy only these 150 agents.

## Phase 4: Fixing Agent Definitions (Schema Validation)
*   **Action:** Encountered schema validation failures on agent loads (invalid slugs, `tools` as objects, unrecognized keys).
*   **Result:** Created a Python batch script to sanitize all 150 agents (removing invalid keys, fixing array structures). Integrated this sanitization into the deploy script.

## Phase 5: In-Memoria & Final MCP Config Selection
*   **Action:** Manually tested `in_memoria` MCP on the codebase; persisted insights successfully but `auto_learn` timed out due to repo size.
*   **Result:** User requested removal of `in_memoria` and `semgrep` from configs, and adding `StitchMCP`. Updated templates and scripts accordingly to establish exactly 10 finalized MCPs.

## Phase 6: Fresh Installation Across All Clients
*   **Action:** Wiped existing MCP configs for 9 clients (Antigravity, Gemini CLI, OpenCode, Cursor, Clause, Kilo, Factory, Windsurf, Codex CLI).
*   **Result:** Executed a fresh install of the 10 finalized MCPs across all clients. Resolved edge cases where templates incorrectly propagated outdated configs.

## Phase 7: Edge Cases & API Key Rotation
*   **Action:** Fixed `memcord` dropping (`uv` instead of `uvx`), removed `playwright_browser` from Antigravity (native support exists), and stripped the invalid "run" param from `notebooklm`.
*   **Result:** User purged revoked unused API tokens from `.env`. Wrote a comprehensive testing script (`scripts/test-api-keys.py` and `scripts/test-mcps.sh`) to systematically validate and ping keys and integrated MCPs.

## Phase 8: Post-installation Testing & Tool Validation
*   **Action:** Validated execution and connectivity with CLI tests (`opencode mcp list`, `kilo mcp list`, etc.).
*   **Result:** Successfully tested single-tool queries on Serena, Memcord, Context7, Stitch, and Genkit inside Antigravity. Hyperbrowser/Vibe Check identified for minor fixes.

## Phase 9: Workflow and TOML Converter Fixes
*   **Action:** Harvested useful Markdown skills and scripts from `packages/rust-skills/`. Solved TOML parsing errors in `~/.gemini/commands/`.
*   **Result:** Fixed the `md-to-toml.py` converter to use literal strings (`'''`), which eliminated escape character crashes and successfully validated all 266 Gemini CLI command workflows.

## Phase 10: Remote Branch and Jules Session Triage
*   **Action:** Examined GitHub open PRs and `jules` remote sessions.
*   **Result:** Fetched 15 remote diffs (`jules remote pull --session`) to scan for keywords (`youtube`, `fernando`, `ibm`). Deleted 12 stale or merged remote branches.

## Phase 11: The Jujutsu (jj) Conflict and Repository Snapshot (The Git/Jujutsu Error)
*   **Action:** The agent used `git push origin --delete <branch>` and other Git native commands in a Jujutsu-managed repository.
*   **Result (The "Cagada"):** Directly manipulating git state under the hood caused local Jujutsu divergence and conflicts during `jj resolve` handling (specifically around `packages/auth-monster/`). The user warned about losing codebase history by mixing Git/Jujutsu natively. The agent mitigated the damage by forcefully squashing the changes and re-mapping the `main`/`staging` bookmarks accurately before pushing.
