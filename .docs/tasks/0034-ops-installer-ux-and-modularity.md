# Task 0034: Installer UX and Modularity

**Status**: [ ]
**Priority**: HIGH
**Type**: ops

## Objective
Refactor install.sh and unify deployment scripts (deploy-to-*.sh) into a modular engine using core utilities.

## Sub-tasks
- [ ] **Unify Deploys**: Extract symlink engine to `scripts/utils/create-symlinks.sh`.
- [ ] **Interactive UI**: Upgrade `install.sh` with `gum` for menus and confirmations.
- [ ] **Global Agent Support**: Expand deployment to all 9 supported coding agents (Cursor, Claude Code, etc.).
- [ ] **Environment Validation**: Add strict `.env` checks and directory detection before deployment.
