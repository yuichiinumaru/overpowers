# Task: 013-install-script-ux

## Objective

Improve the install.sh user experience with proper symlink handling, asset conflict detection, and user prompts.

## Test Requirements

- Install script detects existing user assets (agents, skills, workflows, hooks)
- Presents clear options: merge, replace, or copy
- Includes disclaimer about data handling
- Mentions all supported platforms (OpenCode, Gemini CLI, Antigravity, Kilo Code)

## Exit Conditions (GDD/TDD)

- [x] Add pre-install explanation of what the installation will do
- [x] Add asset conflict detection (check for existing agents/, skills/, workflows/, hooks/)
- [x] Present user options: copy existing → overpowers + symlink / clean install / copy-only (no symlink)
- [x] Add data disclaimer (Overpowers doesn't collect user assets)
- [x] Mention Kilo Code subagent integration
- [x] Test on fresh directory and directory with existing assets

## Details

### What

The current install script needs UX improvements discussed during the Antigravity session. Users who already have their own agents, skills, commands, hooks etc. need clear options for how Overpowers integrates with their existing setup.

### Where

- `scripts/install.sh` [MODIFY]
- `scripts/deploy-to-*.sh` [MODIFY if needed]

### How

Add interactive prompts before symlink operations. Detect existing content and present merge/replace/copy options.

### Why

Discussed in the Antigravity session as a critical improvement for adoption. Users need to understand what happens to their existing assets before installation.
