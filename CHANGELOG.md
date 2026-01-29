# Changelog

All notable changes to the Overpowers toolkit are documented in this file.

> [!CAUTION]
> **IMMUTABLE HISTORY**: Entries in this file must NEVER be deleted or modified (except typo fixes).
> New entries are ALWAYS added at the TOP in descending date order.

---

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

## [2026-05-24] - Bonus Round: Advanced Integration
## [2026-01-21] - Activation & Implementation
