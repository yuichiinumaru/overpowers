# Task 0038: Ops Add Dry-Run Support to All Scripts

**Type:** Operations / Infrastructure  
**Priority:** HIGH  
**Status:** Pending  
**Created:** 2026-03-16  
**Author:** Omega Agent  
**Parent:** Install Scripts Analysis Improvements  

---

## Objective

Add `--dry-run` flag support to all install, deploy, and uninstall scripts to allow users to preview changes before applying them.

---

## Problem

Currently, no script supports dry-run mode. Users must:
- Trust the script without verification
- Manually audit code before running
- Risk unintended changes

**Impact:** Reduced trust, potential for accidental damage, no audit capability.

---

## Acceptance Criteria

- [ ] Add `--dry-run` / `-n` flag to all deploy scripts
- [ ] Add `--dry-run` / `-n` flag to install.sh
- [ ] Add `--dry-run` / `-n` flag to install-mcps.sh
- [ ] Add `--dry-run` / `-n` flag to all uninstall scripts
- [ ] Dry-run output shows exactly what would change
- [ ] No actual changes made in dry-run mode
- [ ] Clear visual distinction for dry-run output (e.g., `[DRY-RUN]` prefix)
- [ ] Update help text in all scripts

---

## Implementation Pattern

### Standard Implementation
```bash
# Add flag parsing
DRY_RUN=0
while [[ $# -gt 0 ]]; do
    case "$1" in
        -n|--dry-run) DRY_RUN=1; shift ;;
        *) ... ;;
    esac
done

# Add to uninstall-utils.sh (shared)
log_dry() {
    if [[ "${DRY_RUN:-0}" == "1" ]]; then
        echo -e "${CYAN}[DRY-RUN]${NC} Would: $*"
    fi
}

# Usage in scripts
if [[ "${DRY_RUN}" == "1" ]]; then
    log_dry "Remove symlink ${target}"
    continue
fi
# ... actual removal code
```

---

## Scripts to Update

### Root Directory
- [ ] `install.sh`
- [ ] `install-mcps.sh`
- [ ] `install-plugins.sh`

### Deploy Scripts
- [ ] `deploy-to-opencode.sh`
- [ ] `deploy-to-gemini.sh`
- [ ] `deploy-to-antigravity.sh`
- [ ] `deploy-to-kilo.sh`
- [ ] `deploy-to-cursor.sh`
- [ ] `deploy-to-windsurf.sh`
- [ ] `deploy-to-claude-code.sh`
- [ ] `deploy-to-codex.sh`
- [ ] `deploy-to-factory.sh`
- [ ] `deploy-to-qwen.sh`

### Uninstall Scripts (when created)
- [ ] `uninstall.sh`
- [ ] All `uninstall-from-*.sh`
- [ ] `uninstall-mcps.sh`
- [ ] `uninstall-plugins.sh`

---

## Example Output

```bash
$ ./install.sh --dry-run

Phase 1: Deploying assets...
[DRY-RUN] Would: Create symlink ~/.config/opencode/agents -> /repo/agents
[DRY-RUN] Would: Create symlink ~/.config/opencode/skills -> /repo/skills
[DRY-RUN] Would: Convert workflows to TOML
[DRY-RUN] Would: Create symlink ~/.config/opencode/commands -> /repo/workflows/toml

Phase 2: Environment Validation...
[DRY-RUN] Would: Create .env from .env.example

Phase 3: MCP Server Installation...
[DRY-RUN] Would: Add MCP "serena" to opencode.json
[DRY-RUN] Would: Add MCP "vibe-check" to opencode.json
```

---

## Dependencies

- Task 0037: Centralize Platform Paths (recommended first)
- Task 0036: Uninstall Scripts Implementation

---

**Estimated Effort:** 8 hours (20 scripts × 20 min each + testing)  
**Assigned To:** Unassigned
