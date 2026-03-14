# Task 0034: Installer UX and Modularity

**Status**: [x]
**Priority**: HIGH
**Type**: ops

## Objective
Refactor install.sh and unify deployment scripts (deploy-to-*.sh) into a modular engine using core utilities.

## References
- [Feature Plan](0034-ops-installer-ux-and-modularity-feature-plan.md)
- [Technical Design](0034-ops-installer-ux-and-modularity-technical-design.md)

## Sub-tasks
- [x] **Unify Deploys**: Extracted boilerplate and unified UI logic to `scripts/utils/deploy-utils.sh`.
- [x] **Interactive UI**: Upgraded `install.sh` with `gum` for professional menus and confirmations.
- [x] **Global Agent Support**: Refactored all 9 deployment scripts (OpenCode, Gemini, Antigravity, Kilo, Cursor, Windsurf, Codex, Claude, Factory).
- [x] **Environment Validation**: Added tool detection and automated `.env` setup.
