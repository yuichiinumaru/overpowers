# Changelog

All notable changes to the Overpowers toolkit are documented in this file.

> [!CAUTION]
> **IMMUTABLE HISTORY**: Entries in this file must NEVER be deleted or modified (except typo fixes).
> New entries are ALWAYS added at the TOP in descending date order.

---

## [2026-01-19] - CEO Agent & Model Fallback System

### Added
- **`agents/000-ceo-orchestrator.md`** - Chief Executive Orchestrator agent
  - Delegation-focused master coordinator (does NOT execute, only delegates)
  - Task decomposition framework with complexity classification
  - When to use Jules vs subagents vs direct agents
  - Correct skill documentation for subagent dispatch
  
- **`configure-persona.sh`** - Interactive MCP configuration wizard
  - Risk levels (HIGH/MEDIUM/LOW) for each MCP
  - Enable/disable individual MCPs
  - API key prompts for required env vars
  - Security-conscious defaults (filesystem/terminal default OFF)

- **GLM 4.7 Fallback** in `run-subagent.sh`
  - Auto-fallback to `glm-4-7-zen` on rate limit detection
  - Configurable via `SUBAGENT_FALLBACK` env var
  - Can disable with `SUBAGENT_ENABLE_FALLBACK=false`

- **`docs/model-fallback-system-design.md`** - Future design document
  - 4 implementation options (script, round-robin, task-based, health queue)
  - Phase-based roadmap for quota management

**Author**: Antigravity + Yuichi Inumaru

---

## [2026-01-19] - YAAMCPL Integration & Persona Generation

### Added
- **13 Personas** generated from 396 agents in `personas/` directory
  - Each persona includes: `persona.yaml`, `mcp.json`, `README.md`
  - Categories: devops-engineer, security-auditor, fullstack-developer, ai-ml-engineer, comprehensive-researcher, database-specialist, qa-engineer, documentation-writer, system-architect, language-specialist, mobile-developer, product-manager, general-assistant
  
- **`install-personas.sh`** - Interactive script to install persona MCP configs
  - Lists available personas with descriptions
  - Backs up existing `.mcp.json` before installing
  - Shows configured MCPs with YAAMCPL source notes

- **YAAMCPL Winners** integrated into `ROLE_MCPS`:
  - developer: `github` (kurdin, 89 tools), `filesystem` (mark3labs)
  - devops: `terminal` (mcp-shell), `docker`, `kubernetes`, `grafana`
  - researcher: `memory` (chroma), `browser` (playwright)
  - security: `terminal` (mcp-shell with audit)
  - database: `mysql` (f4ww4z), `gateway` (centralmind), `redis`
  - ai-ml: `memory` (chroma)

### Changed
- **`scripts/sync-agents-to-personas.py`** - Updated with YAAMCPL validated MCPs
- **`database-specialist`** persona now uses `database` role instead of `developer`

**Author**: Antigravity + Yuichi Inumaru

---

## [2026-01-19] - Skill Frontmatter Validation Fixes

### Fixed
- **41 SKILL.md files** with frontmatter validation errors after Phase 2 integration
  - Removed `allowed-tools` field (15 files) - OpenCode subagent config not used by Antigravity
  - Added missing `---` YAML delimiter (8 files)
  - Normalized skill names to lowercase-alphanumeric-with-hyphens (17 security skills)
  - Added complete frontmatter to `multi-agent-file-coordination/SKILL.md`

### Added
- **`scripts/fix-skill-frontmatter.py`** - Reusable script to validate and fix SKILL.md frontmatter

### Discovered
- Distinction between OpenCode/Claude Code "skills" (which are actually subagent profiles with `allowed-tools`) and true Antigravity skills (just `name` + `description`)
- Many community "skills" were subagent profiles disguised as skills

**Author**: Antigravity + Yuichi Inumaru

---

## [2026-01-18] - Antigravity Skills Installer & Subagent Orchestration

### Added
- **`install-antigravity-skills.sh`** - Interactive installer for deploying Overpowers skills to Google Antigravity IDE
  - 🌐 Multi-language support (English / Português BR)
  - ☢️ **Nuclear Mode** - Install ALL 500+ components with confirmation ("TEM CERTEZA DISSO, BICHO? OLOKO!")
  - 📋 Automatic workflows installation
  - 🔄 Agent-to-skill conversion (392 agents converted inline)
  - 🔍 Local Overpowers detection before downloading
  
- **`skills/subagent-orchestration/`** - New skill for OpenCode subagent orchestration
  - `run-subagent.sh` - Run single subagent with auto-permissions
  - `parallel-tasks.sh` - Run multiple subagents in parallel
  - `batch-analyze.sh` - Analyze multiple repositories in batch
  - Uses `OPENCODE_PERMISSION='"allow"'` for non-interactive mode
  
- **`scripts/convert-agents-to-skills.py`** - Python script to convert OpenCode agents to Antigravity-compatible skills

### Discovered
- OpenCode subagents cannot access `.config/opencode/` directory in non-interactive mode (security restriction)
- Workaround: Run scripts from regular directories like `~/work`

**Author**: Antigravity + Yuichi Inumaru

---

## [2026-01-18] - Claude Identity Issue Resolution

### Discovered
- **Claude Opus 4.5 works correctly** via Antigravity despite appearing broken
- LLMs cannot self-identify correctly - identity is configured via system prompt, not learned during training
- Model responded "Claude 3.5 Sonnet" when asked its name, but knowledge cutoff tests confirmed Opus 4.5
- Created `docs/claude-identity-issue.md` documenting this behavior

### Validated
- Knowledge cutoff test: Nobel Peace Prize 2024 (Nihon Hidankyo) ✅
- Knowledge cutoff test: Euro 2024 (Spain champion, England runner-up, 2-1) ✅
- Both tests confirm March 2025 cutoff consistent with Opus 4.5

### Added
- `docs/claude-identity-issue.md` - Documentation on LLM identity crisis

**Author**: Antigravity + Yuichi Inumaru

---

## [2026-01-18] - Agent Army Deployment

### Added
- `generate-agent-configs.py` - Script to scan agents and generate modular JSON configs by category
- `inject-agents-to-config.py` - Script to inject all agents into `opencode.json` with automatic backup
- `deploy-agent-army.sh` - One-click script to run generation and injection
- `config/agents/` directory with categorized agent JSON files:
  - `agents-security.json`
  - `agents-testing.json`
  - `agents-frontend.json`
  - `agents-backend.json`
  - `agents-devops.json`
  - `agents-ai-ml.json`
  - `agents-research.json`
  - `agents-documentation.json`
  - `agents-all.json` (master file)
- `AGENTS.md` - Toolkit constitution with changelog protocol
- `continuity.md` - Session state tracking ledger
- `CHANGELOG.md` - This file

### Changed
- `lib/skills-core.js` - Added `findAgentsInDir()` and `extractAgentData()` utilities
- `.opencode/plugin/Overpowers.js` - Added dynamic agent discovery and registration

**Author**: Antigravity + Yuichi Inumaru

---

## [2026-01-17] - Documentation Reorganization

### Added
- `docs/README.md` - Installation guides for OpenCode, Claude Code, and Codex
- `docs/hooks-guide.md` - Documentation for 29 event-driven hooks
- `docs/scripts-guide.md` - Documentation for 89 DevOps scripts
- `docs/workflows-guide.md` - Documentation for 16 multi-step workflows
- `docs/services-guide.md` - Documentation for 13 external service integrations

### Removed
- Moved legacy docs to archive:
  - `docs/testing.md` → `archive/overpowers-legacy-docs/`
  - `docs/README.codex.md` → `archive/overpowers-legacy-docs/`
  - `docs/README.opencode.md` → `archive/overpowers-legacy-docs/`
  - `docs/windows/` → `archive/overpowers-legacy-docs/`
  - `docs/plans/` → `archive/overpowers-legacy-docs/`

**Author**: Antigravity

---

## [2026-01-17] - OpenCode Startup Debugging

### Fixed
- Fixed plugin path from `superpowers` to `Overpowers` in `opencode.json`
- Renamed skill `using-superpowers` to `using-overpowers` for consistency
- Updated `Overpowers.js` to reference correct skill name
- Created `fix-skill-names.py` to correct SKILL.md frontmatter mismatches

### Removed
- Removed broken plugins from `opencode.json`:
  - `opencode-dynamic-context-pruning`
  - `subtask2`
  - `opencode-background-agents`

**Author**: Antigravity

---

## [2026-01-17] - Repository Rebranding

### Changed
- Renamed toolkit from "Superpowers" to "Overpowers"
- Updated all GitHub URLs from `obra/Overpowers` to `yuichiinumaru/overpowers`
- Updated `LICENSE` copyright holder
- Updated `README.md` with credits to Jesse Vincent
- Updated Claude plugin metadata

### Added
- `.gitignore` for local state, caches, logs
- `opencode-example.json` with recommended plugin configuration

**Author**: Yuichi Inumaru

---

## [2026-01-16] - Jules Swarm Integration

### Added
- Jules Swarm skills:
  - `skills/jules-dispatch/SKILL.md`
  - `skills/jules-harvest/SKILL.md`
  - `skills/jules-triage/SKILL.md`
  - `skills/jules-integrate/SKILL.md`
- `packages/jules-swarm/` submodule for parallel task orchestration

### Added
- Marketing agents:
  - `agents/growth-hacker.md`
  - `agents/app-store-optimizer.md`
  - `agents/tiktok-strategist.md`
  - `agents/reddit-community-builder.md`
- Product agents:
  - `agents/feedback-synthesizer.md`
  - `agents/sprint-prioritizer.md`
  - `agents/trend-researcher.md`
- Design agents:
  - `agents/whimsy-injector.md`
  - `agents/visual-storyteller.md`
- Engineering agents:
  - `agents/rapid-prototyper.md`
  - `agents/workflow-optimizer.md`
- Other agents:
  - `agents/project-shipper.md`
  - `agents/joker.md`

**Author**: Yuichi Inumaru

---

## [2026-01-16] - Workflow Expansion

### Added
- `workflows/swarm-development.md` - Multi-agent parallel development
- `workflows/research-to-product.md` - Transform research into features
- `workflows/security-hardening.md` - Security audit workflow
- `workflows/marketing-launch.md` - Product launch coordination
- `workflows/jules-orchestration.md` - Jules parallel task workflow
- `workflows/legal-review.md` - Legal document review
- `workflows/full-stack-feature.md` - End-to-end feature development
- `workflows/agent-discovery.md` - Navigate 390+ agents and 149 skills

**Author**: Antigravity

---

## [2026-01-15] - Initial Fork

### Added
- Forked from [obra/superpowers](https://github.com/obra/superpowers)
- Initial agent collection (127 agents)
- Initial skill collection (80 skills)
- OpenCode and Claude Code plugin support

**Author**: Yuichi Inumaru
