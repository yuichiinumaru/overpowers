# Changelog

All notable changes to the Overpowers toolkit are documented in this file.

> [!CAUTION]
> **IMMUTABLE HISTORY**: Entries in this file must NEVER be deleted or modified (except typo fixes).
> New entries are ALWAYS added at the TOP in descending date order.

---

## [2026-05-24] - Sandbox & Unified TUI

### Added
- **Infrastructure**: Docker-based Development Sandbox (`sandbox/`) adapted from `sanity-gravity`.
- **Tooling**: Unified TUI Installer (`./overpowers`) to manage agents, skills, personas, and the sandbox.
- **Documentation**: `docs/INTEGRATION_REPORT_PHASE_2.md` and `docs/analysis/containerization_strategy.md`.

### Changed
- **UX**: Simplified setup process via the new `./overpowers` script.

## [2026-05-24] - Legacy Code Assimilation

### Added
- **Skills**: Imported 19 high-value skills from `antigravity-skills` (including `bdi-mental-states`, `context-optimization`, `remotion`).
- **Scripts**: Added Knowledge Management System (`scripts/knowledge/*.py`) ported from `andy-universal-agent-rules`.
- **Documentation**: `docs/INTEGRATION_REPORT.md` - detailed report of the extraction.

### Changed
- **Knowledge**: `scripts/knowledge/*.py` modified to store data in `docs/knowledge/` instead of legacy paths.

## [2026-05-24] - Project Knowledge Optimization

### Added
- **Documentation**: `docs/SYSTEM_KNOWLEDGE_GRAPH.md` - The "Cognitive Context File" containing architecture, entity relationships, and component registry.
- **Documentation**: `docs/project_structure_map.md` - Full recursive file tree and entity map.
- **Tooling**: `generate_structure_map.py` - Script to regenerate the project structure map.

### Changed
- **Planning**: Initiated "Project Knowledge Optimization" mission.

**Author**: Jules (Agent)

---

## [2026-05-24] - Browser Automation & Cleanup
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
## [2026-05-24] - Mothership Integration (References)

### Added
- **Workflows**:
  - `workflows/compound-product-cycle.md`: Report-to-Code automated workflow.
  - `scripts/compound/`: `auto-compound.sh`, `analyze-report.sh`, `loop.sh`, `compound.config.json`.
- **Agents**:
  - `agents/sisyphus-orchestrator.md`: Updated with OhMyOpenCode logic.
  - `agents/metis-consultant.md`: New consultant agent.
  - `agents/librarian-researcher.md`: New researcher agent.
  - `agents/oracle-architect.md`: New architect agent.
- **Skills**:
  - Ported from Moltbot: `discord`, `slack`, `trello`, `notion`, `1password`, `github`.
- **Documentation**:
  - `docs/research/moltbot-memory.md`: Research on hybrid memory.
  - `docs/protocols/sandbox-guidelines.md`: Execution safety protocols.
  - `JULES_ARCHITECTURAL_DIGEST.md`: Updated with new architecture.
- **Protocols**:
  - Updated `AGENTS.md` with "NPM + 1Password" protocols.

### Changed
- **Architecture**: Integrated "Compound Product Cycle" into core workflow.

**Author**: Jules (Agent)

---

## [2026-01-21] - Activation & Implementation

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
