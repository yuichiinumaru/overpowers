# Changelog

All notable changes to the Overpowers toolkit are documented in this file.

> [!CAUTION]
> **IMMUTABLE HISTORY**: Entries in this file must NEVER be deleted or modified (except typo fixes).
> New entries are ALWAYS added at the TOP in descending date order.

---

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
