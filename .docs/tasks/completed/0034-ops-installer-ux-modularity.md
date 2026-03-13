# Task 0034: Installer UX and Modularity

**Status**: [x]
**Priority**: HIGH
**Type**: ops

## Objective
Refactor install.sh and unify deployment scripts (deploy-to-*.sh) into a modular engine using core utilities.

## Sub-tasks
- [x] **Unify Deploys**: Extract symlink engine to `scripts/utils/create-symlinks.sh`.
- [x] **Interactive UI**: Upgrade `install.sh` with `gum` for menus and confirmations.
- [x] **Global Agent Support**: Expand deployment to all 9 supported coding agents (Cursor, Claude Code, etc.).
- [x] **Environment Validation**: Add strict `.env` checks and directory detection before deployment.
