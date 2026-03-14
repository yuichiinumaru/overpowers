## [2026-03-14] - MCP Installer Hardening for Real-World Config Drift
### Changed
- Hardened `scripts/install-mcps.sh` to clean legacy/disconnected servers across platforms (`StitchMCP`, `grep_app`, `web_search`).
- Added `memcord` availability checks based on `MEMCORD_PYTHON_PATH`; installer now removes stale memcord entries and skips re-adding when unavailable.
- Updated MCP merge behavior to support in-place server updates (`UPDATE:*`) for normalized entries.
- Improved install output with explicit statuses for removed and unavailable MCPs.
### Fixed
- Eliminated post-install disconnected MCP states in Gemini CLI and OpenCode by removing stale inherited servers and unavailable memcord entries.
- Achieved clean MCP diagnostics across `gemini mcp list`, `opencode mcp list`, and `codex mcp list` via automated end-of-install health checks.
**Author**: Codex Architect

## [2026-03-14] - Gemini Tool-Cap Optimization and MCP Health Checks
### Changed
- Refreshed `scripts/config/gemini-cli-agents.txt` to remove stale/renamed entries and reduce the curated Gemini list from 150 to 75 valid agents.
- Added Rust-focused specialists (`ovp-rust_expert`, `ovp-rust_engineer`, `ovp-actix_expert`) to the Gemini curated list.
- Updated `scripts/deploy-to-gemini-cli.sh` to stop syncing `skills` into `~/.gemini/skills`, preventing conflicts with `~/.agents/skills` under Gemini's newer discovery behavior.
### Added
- Added `scripts/maintenance/test-mcp-clients.sh` to run and filter MCP status issues from `gemini mcp list`, `opencode mcp list`, and `codex mcp list`.
- Integrated MCP health check execution at the end of `scripts/install-mcps.sh`.
### Fixed
- Removed `grep_app` and `web_search` from all active MCP templates and installer merge paths.
- Fixed OpenCode MCP shape incompatibility by migrating legacy entries to OpenCode-native schema during install.
**Author**: Codex Architect

## [2026-03-14] - Gemini Skill Conflict and MCP Schema Remediation
### Changed
- Updated `scripts/deploy-to-gemini-cli.sh` to stop deploying `skills` into `~/.gemini/skills`, preventing duplicate-skill conflicts against `~/.agents/skills`.
- Added migration behavior in Gemini deploy to move legacy `~/.gemini/skills` to a timestamped backup directory.
- Filled non-empty `description` frontmatter fields in six skills that were producing Codex schema warnings.
### Fixed
- Reworked OpenCode MCP template (`templates/configs/mcp-opencode.json`) to native OpenCode schema (`type`, `enabled`, `command[]`, `environment`).
- Enhanced `scripts/install-mcps.sh` OpenCode installer to migrate legacy invalid MCP entries (`command` + `args` + `env`) into valid OpenCode format.
- Removed deprecated `grep_app` and `web_search` from all MCP templates and Codex TOML template.
- Added MCP cleanup logic to remove existing `grep_app` and `web_search` entries from installed configs during install runs.
**Author**: Codex Architect

## [2026-03-14] - Installer Cleanup (No In-Memoria Build + Leaner Banner)
### Changed
- Removed `In-Memoria` from `scripts/setup/build-packages.sh` Node build list so the master installer no longer attempts that package in Phase 0.
- Removed duplicated attribution line from `install.sh` banner (`Based on overpowers by Jesse Vincent • Maintained by Yuichi Inumaru`) to keep startup output cleaner.
**Author**: Codex Architect

## [2026-03-14] - MCP Installer Path and Template Governance Corrections
### Added
- Added `templates/configs/mcp-opencode.json` as the canonical OpenCode MCP template source.
### Changed
- Moved policy template `allow-all-policy.toml` to `templates/configs/` to keep reusable templates centralized.
- Updated `scripts/install-mcps.sh` to use `templates/configs/` as the template source of truth.
- Updated `scripts/install-mcps.sh` to read extracted MCP data from `scripts/extracted_user_mcps.json`.
- Updated `scripts/install-mcps.sh` Kilo target paths to `~/.kilocode/mcp.json`.
- Updated `scripts/install-mcps.sh` argument parsing to fail fast on unknown flags and missing `--env` values.
- Updated generic MCP JSON merge logic to support both `mcpServers` and `mcp` root schemas.
- Reduced Antigravity MCP template payload to a smaller curated set due platform MCP limits.
- Updated `.env.example` to remove deprecated `IN_MEMORIA_PATH` and keep Semgrep as CLI-only guidance.
- Updated `README.md` MCP docs to reference `templates/configs/` instead of legacy `opencode-example.json`.
- Added explicit template centralization rule in `AGENTS.md`.
### Fixed
- Fixed extractor invocation path in `scripts/install-mcps.sh` to `scripts/utils/extract-installed-mcps.py`.
- Fixed `scripts/utils/extract-installed-mcps.py` OpenCode config path to `~/.config/opencode/opencode.json`.
- Fixed default `.env.example` target path resolution in `scripts/utils/extract-installed-mcps.py`.
- Removed deprecated `in_memoria` and MCP `semgrep` entries from MCP templates, including Codex TOML.
- Normalized `desktop_commander` template command format by removing legacy `{env:...}` placeholders.
**Author**: Codex Architect

## [2026-03-14] - Continuity Migration Sweep Across Workflows and Templates
### Changed
- Completed a repository-wide migration of workflow and template references from legacy `continuity.md` to `.agents/continuity-<agent-name>.md`.
- Updated additional workflow definitions (`ovp-start-work`, `ovp-sync-memory`, `ovp-jules-dispatch`, `ovp-agentic-execute`, `ovp-execute-plan`) and their TOML counterparts to use `.agents/` continuity paths.
- Updated template governance docs (`templates/rules/AGENTS.md`, `templates/rules/backup-agents.md`, `templates/docs/execution-state-tracking.md`) to match the `.agents` continuity model.
- Aligned architecture/concept docs that described continuity behavior to the new ledger path conventions.
- Refined Task 0031 objective text to explicitly reference `.agents/continuity-*.md`.
**Author**: Codex Architect

## [2026-03-14] - Cross-Project Continuity and Runtime Guardrail Fixes
### Changed
- Clarified cross-project intent in `AGENTS.md` and reinforced Protocol Zero to read target-project `README.md` first.
- Expanded `README.md` positioning to explicitly frame Overpowers as a cross-project operating layer and updated platform coverage details.
- Updated continuity references in core workflows (`ovp-00` through `ovp-05`, `ovp-bug-fix`, `ovp-refactor`) to use `.agents/continuity-<agent-name>.md`.
- Updated `workflows/ovp-agent-profile.md` to create/read continuity ledgers in `.agents/`.
- Aligned Task 0031 documentation with actual implementation scanning `.agents/` for `continuity-*.md`.
- Marked Task 0027 and Task 0028 status files as completed.
- Updated CEO orchestration guidance with corrected `run-subagent.sh` paths.
### Fixed
- Restored `hooks/runtime/todo_enforcer.py` to check both `docs/tasklist.md` and continuity checklists, with `.agents/` as primary continuity location and root fallback.
- Hardened `scripts/utils/model_selector.py` with configurable and fallback status-file paths for restricted environments.
- Added explicit `up` action and corrected helper path output in `scripts/orchestration/sandbox-launcher.sh`.
**Author**: Codex Architect

## [2026-03-13] - Task 0032: Model Fallback System
### Added
- Integrated `model_selector.py` and `run-subagent.sh` for automatic model fallback and rate limit handling.
- Updated CEO agent prompt (`ovp-000_ceo_orchestrator.md`) with complexity-aware task classification (`high`, `medium`, `low`).
- Added complexity support to subagent execution scripts.
- Created Feature Plan and Technical Design documents for Task 0032.
**Author**: Nova Agent

## [2026-03-13] - Task 0024: Agent Reasoning BDI Evaluation
### Added
- Conducted in-depth research on BDI (Belief-Desire-Intention) architectures for LLM agents.
- Proposed hybrid Neuro-Symbolic architecture for future Overpowers orchestration.
- Saved evaluation as persistent memory: `architecture/research/0024-bdi-evaluation`.
**Author**: Nova Agent

## [2026-03-13] - Task 0028: Memory Lifecycle Integration
### Changed
- Standardized explicit memory read/update operations across core Overpowers workflows (`ovp-01`, `ovp-02`, `ovp-03` series, `ovp-bug-fix`, `ovp-refactor`, and `ovp-00-setup`).
- Added explicit steps to read `continuity.md` and `.agents/memories/` at the start of workflows.
- Added explicit steps to update memory systems at the end of workflows.
- Created Feature Plan and Technical Design documents for Task 0028.
**Author**: Nova Agent

## [2026-03-13] - Task 0034: Installer UX and Modularity
### Added
- Created `scripts/utils/deploy-utils.sh` as a common engine for all deployment scripts.
- Upgraded `install.sh` with `gum` for a modern, interactive TUI experience.
- Added environment validation and core tool detection to the installation process.
### Changed
- Refactored all 9 platform deployment scripts (`deploy-to-*.sh`) to use the unified modular engine.
- Improved consistency across all deployment banners, summaries, and symlink mappings.
**Author**: Epsilon Agent

## [2026-03-13] - Task 0030: Omnara Monitoring
### Added
- Implemented Omnara Flight Recorder, a generalized PTY-based session monitor.
- Created `services/omnara-monitoring/omnara-flight-recorder.py` for binary-safe CLI interaction logging.
- Created `scripts/record-session.sh` helper for easy session recording.
- Added Feature Plan and Technical Design documents for Omnara Monitoring.
**Author**: Epsilon Agent

## [2026-03-13] - Task 0026: Moltbot Memory Hybrid Search
### Added
- Implemented `hybridSearch` method in `MemoryIndexManager` using Reciprocal Rank Fusion (RRF).
- Integrated `sqlite-vec` and `FTS5` for semantic and keyword-based retrieval.
- Created Feature Plan and Technical Design documents for Moltbot Memory integration.
- Added comprehensive test suite for hybrid search verification.
**Author**: Epsilon Agent

## [2026-03-12] - Consolidate Jules Skills
### Changed
- Consolidated `jules-harvest`, `jules-integrate`, and `jules-triage` skills into `ai-llm-jules-dispatch-login`.
- Renamed source `SKILL.md` files to `SKILL-harvest.md`, `SKILL-integrate.md`, and `SKILL-triage.md` during migration.
### Removed
- Archived `safety-sec-jules-dispatch` per Archive Protocol.
- Archived empty source directories for consolidated Jules skills.
**Author**: Overpowers Architect

## [2026-03-12] - Add Reference Repositories
### Added
- Cloned 42 reference repositories into references/ using usernamereponame naming convention.
- Created scripts/clone_references.sh for automated cloning.
**Author**: Overpowers Architect
## [2026-03-10] - Task 0300 Batch 058 Completion
### Added
- Created 9 new helper scripts for skills in Batch 058 (Web & Frontend domain).
- Populated empty `scripts/` directories for skills such as `linear`, `bluebubbles`, `pyzotero`, etc.
### Fixed
- Completed audit and cleanup of 20 skills in Batch 058, removing temporary `.o*` artifacts.
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 057 Completion
### Added
- Created 10 new helper scripts for skills in Batch 057 (Design & Frontend domain).
- Populated empty `scripts/` directories for skills such as `wcag-audit`, `semi-design`, `figma-implement`, etc.
### Fixed
- Added missing `#!/usr/bin/env python3` shebangs to 7 existing Python scripts in Batch 057.
- Completed audit and cleanup of 20 skills in Batch 057, removing temporary `.o*` artifacts.
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 056 Completion
### Added
- Created 11 new helper scripts for skills in Batch 056 (Design & UX domain).
- Populated empty `scripts/` directories for skills such as `gaming-ui`, `gedcom-explorer`, `gog`, `openhue`, `notion`, etc.
### Fixed
- Added missing `#!/usr/bin/env python3` shebangs to 7 existing Python scripts in Batch 056.
- Completed audit and cleanup of 20 skills in Batch 056, removing temporary `.o*` artifacts.
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 025 Completion
### Added
- Created 18 new helper scripts for skills in Batch 025 (Media & Content domain) to replace missing implementations.
- Populated empty `scripts/` directories for skills such as `3d`, `accessibility`, `charts`, `canvas-design`, etc.
### Changed
- Verified and cleaned up existing scripts in Batch 025.
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 017 Completion
### Added
- Created 10 new helper scripts for skills in Batch 017 (`strategy-advisor`, `task-plan`, `tavily-web`, `team-collaboration-standup-notes`, `technical-articles`, `transcribe-captions`, `steady-dancer-wan-ai-video`, `step-audio-editx-voice-cloning`, `subagent-driven-development`, `swarm-orchestration`).
- Initialized missing `scripts/` directories for 4 skills in Batch 017.
### Fixed
- Added missing `#!/usr/bin/env python3` shebang to `ai-llm-statistical-analysis` script.
- Completed audit and cleanup of 20 skills in Batch 017, removing temporary `.o*` artifacts.
### Changed
- Verified all scripts in Batch 017 follow best practices (shebang, main block, environment variables for keys).
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 008 Completion
### Fixed
- Added missing `#!/usr/bin/env python3` shebangs to 3 scripts in Batch 008.
- Created missing `fred_query.py` and `fred_examples.py` for `ai-llm-fred-economic-data` skill.
### Changed
- Completed audit and cleanup of 20 skills in Batch 008, removing temporary `.o*` artifacts.
- Verified all scripts in Batch 008 follow best practices (shebang, main block, environment variables for keys).
**Author**: gemini-engineer

## [2026-03-08] - Semantic Namespacing and GraphRAG Migration
### Added
- Created Kùzu DB GraphRAG foundation (`.agents/skills_graph`) for autonomous skill clustering.
- Extracted 90 tags and 5,115 semantic concepts from 1,277 unique skills.
### Fixed
- Resolved 731 skill conflicts caused by duplicate folder names sharing the same internal skill name across multiple categories.
### Changed
- Migrated all 1,277 `skills/` folders from sequential numbering (`0001` - `1277`) to organic Semantic Namespacing (`[domain]-[subdomain]-[slug]`) derived directly from the Knowledge Graph.
- Re-synchronized the Gemini CLI global configuration via `scripts/deploy-to-gemini-cli.sh`.
- Archived 731 redundant skill folders into `.archive/skills/` to clear Gemini CLI discovery warnings and optimize context usage.
**Author**: Gemini CLI

## [2026-03-07] - Consolidated Parallel PRs for Jules Skill Scripts Batches
### Added
- Evaluated and verified parallel run outputs from Jules agents for the remaining `0300` skill batches.
- Merged and patched the most comprehensive version of scripts generated across 22 parallel batches directly into the main `development` bookmark via Jujutsu, avoiding snapshot corruption of immutable remote branches by using patch diffing.
- Auto-closed the corresponding Github Pull Requests associated with parallel Jules runs.
**Author**: Overpowers Architect (Antigravity)

## [2026-03-06] - Completed Tasks Archival
### Changed
- Extracted 37 completed tasks from `docs/tasklist.json` into a separate `docs/tasks/completed/tasklist-completed.json` manifest file to remove clutter.
- Refactored `docs/tasklist.json` schema to group arrays of payload tasks under a unified `prompt` directive, drastically minimizing repetitive structure.
- Moved the corresponding physical markdown task files from `docs/tasks/` to `docs/tasks/completed/`.
**Author**: Overpowers Architect (Antigravity)

## [2026-03-06] - CFA Helios Prompt Conversion
### Added
- Converted 17 Markdown prompts into structured JSON prompts adhering to the Cognitive Fusion Architecture (CFA) Helios standard.
- Implemented `task_profile`, `agent_profile`, `reasoning_config`, `directives`, and `pipeline` structures for: `architect`, `arxiv`, `doc-updater`, `gatekeeper`, `loom`, `mcps`, `nexus`, `refactor-cleaner`, `release-notes`, `reorganize-docs-agents`, `scout`, `security-reviewer`, `sort-scripts`, `tracker`, `update-memories`, `youtube-ripper`, and `scavenge-planner`.
### Changed
- Standardized naming in `prompts/` directory by removing underscores from Markdown files to match JSON counterparts.
- Aligned `scavenge-planner` naming across .md and .json versions.

## [2026-03-06] - Skill Naming Convention Enforcement
### Changed
- Renamed 13 unnumbered skill directories in `skills/` to follow the `type-subtype-nnnn-name` convention (IDs 1249-1261).
- Updated `name` field in `SKILL.md` for all renamed skills.
- Renamed script utilities in `skills/` and `scripts/utils/` to remove underscores (`consolidate-skills.py`, `consolidate-additional.py`, `skills-report.json`, `analyze-skill.sh`).
- Renamed documentation files in `docs/` to remove underscores (`agno-docs-links.txt`, `skill-creation-guide.md`).
- Moved `lista de skills.md` to `docs/skills-sources.md`.
### Removed
- Archived redundant skill folders (`compound-product-cycle`, `setup-codemap-cli`) and ZIP archives in `skills/` to `.archive/`.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-06] - Skill Directory Cleanup & README Refresh
### Changed
- Executed mass rename of over 1223 skill folders in `skills/` to clean duplicated prefixes.
- Updated component inventory counts dynamically in `README.md`, now totaling 2600+ components (including 1280+ skills and 937+ agents).
- Re-aligned the MCP server documentation in `README.md` to perfectly match `opencode-example.json`.
### Removed
- Removed the `Jules Swarm Integration` section from `README.md` as its capabilities have graduated to native skill status.
**Author**: Overpowers Architect (Antigravity)

## [2026-03-06] - Consolidated Parallel PRs for Jules Skill Scripts Batches
### Added
- Evaluated and verified parallel run outputs from Jules agents for the remaining `0300` skill batches.
- Merged and patched the most comprehensive version of scripts generated across 43 parallel batches directly into the main `development` bookmark via Jujutsu, avoiding snapshot corruption of immutable remote branches by using patch diffing.
- Auto-closed the corresponding Github Pull Requests associated with parallel Jules runs.
**Author**: Overpowers Architect (Antigravity)

## [2026-03-05] - Repository Integrity Fix: Agent Syntax & Skill Conflicts
### Fixed
- Resolved YAML frontmatter syntax errors in `agents/jules-orchestrator.md` and `agents/team-claude--it-ops-orchestrator.md` (mismatched quotes and redundant tool entries).
- Resolved massive skill conflicts by archiving 772 legacy (non-prefixed) skill directories that had modern prefixed counterparts.
- Resolved agent duplication by archiving `agents/claude-it-ops-orchestrator.md` in favor of `agents/team-claude--it-ops-orchestrator.md`.
- Repaired merge conflicts and metadata inconsistencies in `continuity.md`.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 039 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 039 (`sci-bio-0790` to `sci-chem-0810`).
- Created scripts for TCGA preprocessing, ToolUniverse multi-omics searches (expression, protein design, rare diseases, sequences), UniProt API queries, Venue template lookups, Baoyu slide deck initialization, Beads task management, ChEMBL queries, Clinical Decision Support scaffolding, ClinicalTrials.gov search, ClinPGx querying, COSMIC data downloads, Datamol structure analysis, DiffDock CSV generation, Drug Repurposing report scaffolding, DrugBank downloads, ESM model inference, and EDA for scientific formats.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 055 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 055 (`sec-safety-1135` to `ux-design-1155`).
- Created specialized scripts for swarm validation, vibe-coding blueprints, worker-agent mappings, XSS payload generation, YARA-X syntax checking, YouTube transcript extraction, security stack detection, MVP scorecards, PREVC report scaffolding, binary information, track initialization, and accessibility audit checklists.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 007 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 007 (`ai-llm-0133` to `ai-llm-0153`).

## [2026-03-05] - Skill Scripts Batch 006 Deployment
### Added
- Implemented and deployed helper scripts for 21 skills in Batch 006 (`ai-llm-0111` to `ai-llm-0132`).
- Created specialized scripts for daily updates (`claude_digest.py`), A/B testing (`ab_test_calculator.py`), ML drift monitoring (`semantic_drift_monitor.py`), decision making (`decision_frameworks.py`), deep research (`ddg.py`), automated research pipelines (`full_pipeline.py`, `init_research.py`), design tokens (`build_tokens.sh`, `generate_tokens.py`), repository exploration (`list_repos.sh`, `dig_repo.sh`), digital brain logging (`weekly_review.py`, `log_entry.py`), parallel agent dispatching (`task_generator.py`, `dispatch.py`), doc co-authoring (`init_scaffold.py`, `reader_test.py`), document parsing (`batch_convert.py`), changelog generation (`format_changelog.py`, `generate_highlights.py`), documentation seeking (`repomix_pack.sh`, `get_llms_txt.sh`), and various utilities for docstrings, watermarking, and domain name brainstorming.
**Author**: Overpowers Architect (Gemini CLI)
## [2026-03-05] - Skill Scripts Batch 036
### Added
- Helper scripts for 20 skills (`ops-infra-0735` to `sci-bio-0750`).
- New `check_deps.py` utility for dependency validation across multiple skills.
- Domain-specific scripts for Netlify, Render, GitHub CLI, and various Bioinformatics tools.
**Author**: Gemini CLI

- Created specialized scripts for outreach CSV preparation, Excalidraw diagram manipulation, Exa semantic search, Fal.ai API integration, and various domain-specific utilities for email sequences, prompt enhancement, and marketing campaign execution.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 035 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 035 (`ops-infra-0714` to `ops-infra-0733`).
- Created specialized scripts for test failure grouping (`test_grouper.py`), Things 3 management (`things_helper.sh`), Three.js geometry reference (`threejs_geometry_list.py`), documentation mapping (`doc_mapper.py`), Expo upgrades (`expo_upgrade_helper.sh`), file summarization (`summarize_file.sh`), git worktree automation (`worktree_helper.sh`), web fetching/markdown conversion (`fetch.sh`, `web2md_helper.sh`), and Rube MCP automation helpers for Todoist, Trello, Webflow, WhatsApp, Wrike, Zoho CRM, and Zoom.
- Integrated Cloudflare deployment helper (`cloudflare_helper.sh`) and X article publishing guidance.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 038
### Added
- Implemented helper scripts for 20 skills (sci-bio-0771 to sci-bio-0790) to improve operational efficiency.
**Author**: Overpowers Architect

# Changelog

All notable changes to this project will be documented in this file.

> [!CAUTION]
> **IMMUTABLE HISTORY**: Entries in this file must NEVER be deleted or modified (except typo fixes).
> New entries are ALWAYS added at the TOP in descending date order.

---

+++++++ Contents of side #1

## [2026-03-05] - Skill Scripts Batch 005 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 005 (`ai-llm-0086` to `ai-llm-0110`).
- Created specialized scripts for ComfyUI setup/utilities (AEP, Cache DiT, Wan 2.2, Z-Image), mathematical solving (Z3, Sympy), competitive research/intelligence (battlecards, research reporting), component analysis, Conductor track automation, content creation (brand voice, SEO optimization), strategy planning, copy editing (Seven Sweeps), and YAML handoff/plan generation.
- Synchronized internal skill mapping via `parse-skills.js`.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 004 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 004 (`ai-llm-0066` to `ai-llm-0085`).
- Created specialized scripts for C4 component/context generation, cache component checking, campaign brief generation, OMC state clearing, CEO strategy/financial analysis, changelog updates, review alignment checking, Chroma DB utilities, CGD validation, health report generation, Ghostty Vim-nav setup, AGENTS.md scoring, research plan generation, Claude settings auditing, meta-skill creation/validation, skill syncing, README generation, execution runtime setup, and coding agent scratchpad initialization.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 010 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 010 (`ai-llm-0198` to `ai-llm-0219`).
- Created specialized scripts for scientify installation, numerical interpolation, invoice organization, ISO 13485 gap analysis, asset sheet generation, Jira multi-backend handling, JSON Canvas building, Jules branch harvesting, Kagi API clients, knowledge base searching, LangSmith trace debugging, lead research reporting, LLM app scaffolding, RAG BI pipelines, Kubernetes LLM manifests, and batch markdown conversion.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 011 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 011 (`ai-llm-0220` to `ai-llm-0241`).
- Created standardized Python and Bash utilities for market sizing, marketing CAC, A/B testing, MCP interactions, regulatory gap analysis, and more.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-13] - Containerized Sandbox Implementation
### Added
- Implemented isolated Docker execution environment for safe code execution and research.
- Enhanced `scripts/orchestration/sandbox-launcher.sh` with `exec` support, correct project root calculation, and automatic user mapping.
- Created `Guide 0013: Containerized Sandbox` (`.docs/guides/guide-0013-containerized-sandbox.md`).
- Pre-configured sandbox image with Python 3.11, Node.js 20, and Playwright dependencies.
**Author**: omega (Agent)

## [2026-03-13] - Graph-based Continuity (Mindmodel Context)
### Added
- Integrated agent continuity logs (`continuity-*.md`) into the Overpowers Knowledge Graph.
- Updated `overpowers-graph-ext` indexer to support root-level continuity nodes with relationship mapping.
- Established YAML frontmatter standard for session context tracking.
- Created `Guide 0012: Graph-based Continuity` (`.docs/guides/guide-0012-graph-based-continuity.md`).
**Author**: omega (Agent)

## [2026-03-13] - Skill Decision Trees Standardization
### Added
- Created `Guide 0011: Skill Decision Trees` (`.docs/guides/guide-0011-skill-decision-trees.md`) to standardize expert decision logic within skills.
- Established Overpowers Model Heuristics for Tier-based model selection.
- Created reusable template for decision trees in `templates/skill-decision-tree.md`.
- Refactored `imagegen` and `speech` skills to follow the new standardized decision matrix format.
**Author**: omega (Agent)

## [2026-03-13] - Advanced Hooks Integration (Gemini CLI)
### Added
- Integrated Advanced Hooks suite into `hooks/hooks.json` for native Gemini CLI support.
- Standardized `hooks/runtime/todo_enforcer.py` to support multi-agent continuity tracking (`continuity-*.md`).
- Enhanced `hooks/runtime/edit_guard.py` with expanded error detection patterns for robust tool recovery.
- Updated `.docs/hooks-guide.md` with advanced monitoring and utility hooks documentation.
**Author**: omega (Agent)

## [2026-03-04] - Advanced Hooks Implementation
### Added
- Implemented robust `hooks/runtime/todo_enforcer.py` to auto-detect pending tasks from `tasklist.md` and `continuity.md`.
- Implemented intelligent `hooks/runtime/dir_injector.py` for automated context enrichment during directory navigation.
- Implemented `hooks/runtime/edit_guard.py` middleware providing actionable self-recovery hints for agent tool failures.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-04] - External Skill Extraction and Integration

### Added
- Integrated 31 new 🟢 Green skills from external repositories (Anthropics, OpenAI, Vercel, Google Labs).
- Created `media-content-0571-media-content-1246-stitch-remotion-walkthrough` (Differentiated from Remotion hub).
- Created `ops-infra-0739-desktop-screenshot` (Differentiated from marketing screenshots).
- Created `ai-llm-1247-openai-imagegen` (Differentiated from Gemini imagegen).
- Created `ai-llm-1248-openai-speech` (Differentiated from Azure speech-to-text).
- New sequence of skills added to categories: `ai-llm` (1234-1246), `ops-infra` (0733-0738), `web-frontend` (1233-1238), `dev-code` (1144), `data-sci` (0481), `ux-design` (1194), `sec-safety` (1143-1144), `tool-general` (1154).

### Changed
- **Merged and Enriched**: `algorithmic-art`, `brand-guidelines`, `canvas-design`, `react-best-practices` (58 rules), `skill-creator`, `vercel-deploy`, and `web-design-guidelines` with superior official content.
- Updated `continuity.md` to reflect skill mining completion.
**Author**: Overpowers Architect (Gemini CLI)


### Added
- Created `scripts/utils/jj-commit-push.sh` to automate the local JuJutsu staging/commit/push lifecycle.
- Modified `workflows/00-setup.md` to establish global `$OVERPOWERS_PATH` capability to let users execute the setup sequence seamlessly anywhere.
- Added `10.4. Routine State Commits` requirement inside `AGENTS.md` (and template).

## [2026-03-04] - Constitution Template Hardening
### Changed
- Updated `AGENTS.md` and `templates/rules/AGENTS.md` Section 6 to formally enforce templates (`agent.md`, `skill-template/SKILL.md`, `workflow.md`) and mandate the `md-to-toml.py` conversion script for workflows.
- Renamed `docs/guides/` files to strictly follow the standard `type-[subtype]-nnnn-names.md` document convention.
**Author**: Antigravity

## [2026-03-04] - Massive Operation Framework Stress Test
### Added
- Created `.agents/thoughts/massive-operation-framework-stress-test.md` containing analysis and 30 stress-test questions for the universal transformation framework.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-04] - Skill Reorganization
### Changed
- Created `scripts/install-skills.py` for skill integrity verification and local setup.
- Updated `AGENTS.md` and templates with memory management guidelines and terminology clarity.
- Renamed 1237 skill folders following the `type-subtype-nnnn-name` convention for better organization and discovery.
### Added
- Created `docs/tasks/planning/2026-03-04-skill-improvements-plan.md` for future standardization tasks.
**Author**: Overpowers Architect
## [2026-03-03] - System Recovery & Workflow Enhancements

### Added
- **Templates**: `prompts/scavengeplanner.md` template for blueprint assimilation and orchestration planning.
- **Workflows**: `workflows/task-grooming.md` for task extraction and decomposition.
- **Scripts**: `scripts/md-to-toml.py` markdown to TOML workflow parser for Gemini CLI.
- **Reports**: Post-mortem report `.agents/thoughts/jj-bookmark-regression.md` detailing the Jujutsu bookmark regression incident and the 5-stage safe restoration protocol.

### Changed
- **CLI Workflows**: Converted Markdown workflows successfully into TOML formatting for Gemini CLI.
- **System**: Restored repository integrity via Jujutsu operation log recovering lost workflows and tools.
- **System**: Deleted 10 stale/abandoned branches from GitHub and synchronized local repository.
- **Security**: Added `userenv` artifacts explicitly to `.gitignore` to prevent credential leakage.

**Author**: Overpowers Architect (Antigravity)


## [2026-05-24] - Browser Automation & Cleanup

### Added
- **Skills**: `browser-use`, `playwright-skill`, `web-research` (from Moltbot).
- **Agents**: `browser-automator.md` specialized in web interaction.
- **Workflows**: `workflows/web-research.md`.

### Changed
- **Config**: Updated `.gitignore` to exclude build artifacts and caches.
- **Agents**: Regenerated all agent configs.

**Author**: Jules (Agent)

## [2026-05-24] - BMAD Deepening Phase (Workflows)

### Added
- **Workflows**:
  - `workflows/game-dev/dev-story.md`: Full "Dev Story" workflow for Game Dev Agent.
  - `workflows/creative/problem-solving.md`: "Problem Solving" workflow for Creative Agent.
- **Agents**:
  - Updated `agents/game-dev-studio.md` with explicit workflow delegations.
  - Updated `agents/creative-problem-solver.md` with explicit workflow delegations.

### Changed
- **Agents**: `Link Freeman` and `Dr. Quinn` now have executable `workflow="..."` parameters in their prompts.

**Author**: Jules (Agent)

## [2026-05-24] - BMAD & Safety Integration

### Added
- **Safety**: `hooks/safety/destructive-command-blocker.ts` - Prevents catastrophic commands (`rm -rf`, `mkfs`, `circleci context delete`).
- **Agents**:
  - `agents/murat-test-architect.md`: Master Test Architect (from TEA).
  - `agents/game-dev-studio.md`: Game Development Specialist.
  - `agents/creative-problem-solver.md`: TRIZ/Systems Thinking Expert.
- **Knowledge Graph**: `docs/knowledge/testing/` - Massive import of testing patterns (Risk-based, ATDD, Flakiness).
- **Workflows**: `workflows/teach-me-testing.md`.
- **Skills**: `skills/playwright-skill/network-monitor.ts` - Network error monitoring fixture.

### Changed
- **Architecture**: Adopted "Knowledge Graph" pattern. Updated `JULES_ARCHITECTURAL_DIGEST.md`.

**Author**: Jules (Agent)

---

## [2026-05-24] - Bonus Round: Advanced Integration


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
00p+0nges from base to side #2
-## [2026-03-03] - Consolidated Generic AGENTS.md Template
-
-### Added
-- New `scripts/templates/AGENTS.md` — a comprehensive generic template (~550 lines) consolidating all rules from `AGENTS.md`, `AGENTS copy.md`, `AGENTS copy 2.md`, and all 14 `.agents/rules/` files.
-- Template covers: session initialization, core philosophy, changelog protocol, knowledge routing, operational laws, security boundaries, conventions, task system, cognitive workflow & memory management, engineering standards, development practices (TDD, SDD, spec-first), multi-agent safety, VCS rules (Git + Jujutsu), Jules agent rules, delegation strategy, behavioral guidelines, forbidden actions, environment/tooling, and platform-specific rules.
-
-**Author**: Overpowers Architect (Antigravity)
-
-## [2026-03-02] - Merge PRs #45 and #46 via jj
-
-### Added
-- Integrated PR #46: feat: add skills extracted from Unsupervised Learning channel (Batch 1 & 2).
-- Integrated PR #45: YouTube Ripper: Processes batch 7 for @fernandobrasao.
-
-### Fixed
-- Resolved merge conflicts in `CHANGELOG.md`, `.agents/reports/youtube-mining-notes.md`, and `docs/youtube/fernando-brasao.md`.
-
-**Author**: Overpowers Architect (Gemini CLI)
-
-
-## [2026-03-02] - YouTube Skill Mining: Unsupervised Learning Channel (Batch 1 & 2)
-
-### Added
-- **Skills**: `fabric-ai-evaluator` extracted from 'Using the Smartest AI to Rate Other AI' video.
-- **Skills**: `nano-banana-art-generator` extracted from 'My Art Skill With Nano Banana 3' video.
-- **Skills**: `claude-code-neovim-ghostty` extracted from 'Claude Code + Neovim via Ghostty Panes' video.
-- **Skills**: `fabric-raycast-integration` extracted from 'Fabric New Integration with Raycast' video.
-- **Reports**: Appended notes to `youtube-mining-notes.md` for batch 1 & 2 analysis.
-- **Reports**: Added `docs/tasks/youtube-mining-video-analysis-report.md`.
-- **Data**: Initial raw list of videos in `docs/youtube/unsupervised-learning.md`.
-- **Data**: Subtitle and info files for processed videos in `docs/youtube/`.
-
-**Author**: youtube-ripper
-
-## [2026-03-02] - YouTube Ripper: Batch 6 & 7 (fernando-brasao)
-
-### Changed
-- Processed Batch 6 and 7 for @fernandobrasao.
-- Handled HTTP 429 errors from YouTube during transcript extraction.
-- Updated `docs/youtube/fernando-brasao.md` with processing status.
-- Appended evaluation notes to `.agents/reports/youtube-mining-notes.md`.
-
-**Author**: youtube-ripper
-
-## [2026-03-02] - Docs Directory Reorganization
-
-### Added
-- New directory structure for `docs/`: `architecture/`, `guides/`, `tasks/planning/`.
-- `archives/` directory for historical and obsolete documentation.
-- Naming convention `nnn-type-name.md` applied to all core documentation files.
-
-### Changed
-- Reorganized `docs/` root into subdirectories.
-- Moved testing patterns to `docs/guides/testing/`.
-- Moved external service documentation to `docs/guides/services/`.
-- Moved architectural concepts and codebase maps to `docs/architecture/`.
-- Updated `docs/README.md` with new structure and fixed navigation links.
-- Updated `docs/guides/004-guide-services.md` with correct internal paths.
-- Updated `docs/architecture/codemaps/000-arch-index.md` with current file names.
-
-### Fixed
-- Resolved merge conflicts in `docs/README.md`.
-- Completed documentation deduplication tasks (004, 005, 006).
-
-**Author**: Overpowers Architect (Gemini CLI)
-
-## [2026-03-02] - Second Pass Audit and Agent Standardization
-
-### Added
-- New audit report: "docs/architecture/016-second-audit-report.md".
-- New maintenance script: "scripts/fix_agents.py" for standardizing agent frontmatter.
-
-### Fixed
-- **Critical**: Standardized frontmatter for all 938 agents. Fixed missing "tools" fields and corrupted YAML syntax across 832 files.
-- Completed rebranding sweep from "superpowers" to "overpowers" in "README.md", "AGENTS.md", "install.sh", and core documentation.
-- Ensured all agent "color" fields are double-quoted hex codes per constitutional rules.
-
-### Changed
-- Updated "docs/tasklist.md" marking Task 016 as complete.
-
-**Author**: Overpowers Architect (Gemini CLI)
-
-## [2026-03-02] - Enhanced Installation UX and Kilo Code Support
-
-### Added
-- New deployment script "scripts/deploy-to-kilo.sh" for Kilo Code support.
-- Support for "OVERPOWERS_CONFLICT_POLICY" environment variable in all deployment scripts to allow merging assets instead of replacing them.
-- Documentation for Kilo Code in "README.md" and "AGENTS.md".
-
-### Changed
-- Major UX improvements to "install.sh":
-    - Added pre-install explanation of installation steps.
-    - Added data handling disclaimer.
-    - Implemented asset conflict detection for all platforms.
-    - Added interactive prompts for conflict resolution (Replace vs Copy-Only).
-    - Expanded platform selection to include Kilo Code.
-    - Improved final installation summary.
-
-**Author**: Overpowers Architect (Gemini CLI)
-
-## [2026-03-02] - Fix Antigravity and Multi-Platform MCP Configurations
-
-### Fixed
-- Resolved unresolvable "{env:VAR}" and "${VAR}" patterns in "~/.gemini/antigravity/mcp_config.json".
-- Standardized Antigravity, Gemini CLI ("settings.json"), and OpenCode ("opencode.json") MCP configurations with valid absolute paths.
-- Updated "memcord" to use "uvx memcord server" instead of hardcoded virtualenv paths.
-- Corrected "notebooklm" MCP command arguments to include the "run" subcommand.
-- Fixed "semgrep" MCP configuration to use native "semgrep mcp" command.
-
-### Changed
-- Updated "scripts/templates/mcp-antigravity.json" with modern command patterns and Semgrep support.
-- Synchronized "opencode-example.json" with the latest multi-platform configuration standards.
-
-**Author**: Overpowers Architect (Gemini CLI)
+## [2026-03-05] - Skill Scripts Batch 002
+### Added
+- Implemented helper scripts for 20 skills (`ai-llm-0023` to `ai-llm-0045`).
+- Scripts include cost calculators, JSON validators, Brave search wrappers, Amazon ASIN and Product lookup templates, financial ratio calculators, Apify runner, ASO metadata optimizers, Argos URL builders, Art skill notification and generation wrappers, arXiv scanners, coordinate transformers, audio tool detectors and summarizers, and audit case RAG templates.
+- Established consistent directory structures and provided robust base implementations for all new scripts.
+**Author**: Overpowers Architect
+
+## [2026-03-05] - Skill Scripts Batch 001
+### Added
+- Implemented helper scripts for 20 skills (`ai-llm-0001` to `ai-llm-0022`).
+- Scripts include research queries, talking points, lyrics formatters, style analyzers, system monitors, load balancer simulators, board sync helpers, and more.
+- Consolidated repository utility scripts (detect-env, count-lines, search-knowledge) into relevant skill folders.
+**Author**: Overpowers Architect
+
+... [rest of file]
