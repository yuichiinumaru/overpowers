# Task 0037: Ops Centralize Platform Paths Configuration

**Type:** Operations / Infrastructure  
**Priority:** HIGH  
**Status:** Pending  
**Created:** 2026-03-16  
**Author:** Omega Agent  
**Parent:** Install Scripts Analysis Improvements  

---

## Objective

Centralize all hardcoded platform paths into a single configuration file to improve maintainability, support custom paths, and reduce duplication across install/uninstall scripts.

---

## Problem

Platform directories are hardcoded in 10+ scripts:
```bash
OPENCODE_DIR="${HOME}/.config/opencode"
GEMINI_DIR="${HOME}/.gemini"
ANTIGRAVITY_DIR="${HOME}/.gemini/antigravity"
# ... repeated in deploy-to-*.sh, install-mcps.sh, etc.
```

**Issues:**
- No central configuration
- Difficult to support custom install locations
- Inconsistent path handling
- Maintenance burden (change in 10+ places)

---

## Acceptance Criteria

- [ ] Create `scripts/config/platform-paths.sh` with all platform paths
- [ ] Support environment variable overrides (e.g., `OPENCODE_DIR=/custom/path`)
- [ ] Support custom config file (`~/.overpowers/config`)
- [ ] All deploy scripts source the centralized config
- [ ] All install scripts source the centralized config
- [ ] Update uninstall scripts to use centralized config
- [ ] Document configuration options in README

---

## Implementation Plan

### Step 1: Create Central Config File
```bash
#!/usr/bin/env bash
# scripts/config/platform-paths.sh

# Default platform paths (can be overridden via environment or config file)
export OPENCODE_DIR="${OPENCODE_DIR:-${HOME}/.config/opencode}"
export GEMINI_DIR="${GEMINI_DIR:-${HOME}/.gemini}"
export ANTIGRAVITY_DIR="${ANTIGRAVITY_DIR:-${HOME}/.gemini/antigravity}"
export KILO_DIR="${KILO_DIR:-${HOME}/.kilocode}"
export CURSOR_DIR="${CURSOR_DIR:-${HOME}/.cursor}"
export WINDSURF_DIR="${WINDSURF_DIR:-${HOME}/.codeium/windsurf}"
export CLAUDE_CODE_DIR="${CLAUDE_CODE_DIR:-${HOME}/.claude}"
export CODEX_DIR="${CODEX_DIR:-${HOME}/.codex}"
export FACTORY_DIR="${FACTORY_DIR:-${HOME}/.factory}"
export QWEN_DIR="${QWEN_DIR:-${HOME}/.qwen}"

# Load custom config if exists
if [[ -f "${HOME}/.overpowers/config" ]]; then
    source "${HOME}/.overpowers/config"
fi
```

### Step 2: Update Deploy Scripts
Add to top of each `deploy-to-*.sh`:
```bash
source "${SCRIPT_DIR}/config/platform-paths.sh"
```

### Step 3: Update Install Scripts
Same for `install-mcps.sh`, `install-plugins.sh`, etc.

### Step 4: Documentation
Add to README:
```markdown
## Custom Platform Paths

Create `~/.overpowers/config` with custom paths:
```bash
OPENCODE_DIR=/custom/opencode
GEMINI_DIR=/custom/gemini
```
```

---

## Dependencies

- None (foundational improvement)

## Related Tasks

- Task 0036: Ops Uninstall Scripts Implementation
- Task 0038: Ops Add Dry-Run Support to All Scripts
- Task 0039: Ops Standardize Error Handling

---

**Estimated Effort:** 4 hours  
**Assigned To:** Unassigned
