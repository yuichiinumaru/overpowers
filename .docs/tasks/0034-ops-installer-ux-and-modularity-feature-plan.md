# Feature Plan: Installer UX and Modularity

## 1. Overview
The goal is to modernize the `install.sh` and the various `deploy-to-*.sh` scripts to create a unified, robust, and interactive installation experience. Currently, deployment logic is slightly fragmented across multiple scripts with duplicated boilerplate. We will extract the common logic into a modular engine and upgrade the user interface using `gum`.

## 2. Goals & Success Criteria
- **Goal:** Unify all deployment logic into a single modular engine.
- **Success Criteria:**
  - `install.sh` uses `gum` for all menus, selections, and confirmations (with fallback).
  - `deploy-to-*.sh` scripts are thin wrappers around a common `deploy-utils.sh`.
  - Support all 9 major AI coding agents consistently.
  - Improved environment validation (check `.env`, directory existence, tool presence).

## 3. Vertical Slices & Milestones

### Slice 1: Core Modular Engine
- **Objective:** Extract all common logic (colors, banners, symlink orchestration, validation) into `scripts/utils/deploy-utils.sh`.
- **Deliverables:** `scripts/utils/deploy-utils.sh`.

### Slice 2: Refactor Platform Scripts
- **Objective:** Update all 9 `deploy-to-*.sh` scripts to use the new modular engine.
- **Deliverables:** Refactored scripts for OpenCode, Gemini, Antigravity, Kilo, Cursor, Windsurf, Codex, Claude, and Factory.

### Slice 3: Interactive Installer Upgrade
- **Objective:** Rewrite `install.sh` to use `gum` for a professional TUI experience and integrate with the new modular engine.
- **Deliverables:** Upgraded `install.sh`.

## 4. Risks & Mitigations
- **Broken Symlinks:** -> **Mitigation:** The modular engine will strictly validate source and target paths before applying changes.
- **Missing Dependencies (gum):** -> **Mitigation:** Provide robust fallback to standard `read` and `echo` if `gum` is not installed.
- **Platform Specifics:** -> **Mitigation:** Keep platform-specific logic (like Gemini's agent sanitization) in the respective `deploy-to-*.sh` scripts but called via standard hooks in the engine.

## 5. Exit Conditions
- [ ] `install.sh` runs successfully with `gum` and fallback.
- [ ] All 9 platform scripts are refactored and functional.
- [ ] Environment validation prevents common installation errors.
