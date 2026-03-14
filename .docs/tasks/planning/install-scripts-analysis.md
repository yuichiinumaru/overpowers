# Install Scripts Analysis & Uninstall Architecture Proposal

**Document Type:** Planning & Research  
**Created:** 2026-03-16  
**Author:** Omega Agent  
**Status:** Draft  

---

## Executive Summary

This document provides a comprehensive analysis of all installation, deployment, and setup scripts in the Overpowers repository. It identifies engineering issues, improvement opportunities, and proposes a unified uninstall script architecture that reverses installation actions safely while sharing core logic (DRY principle).

**Key Findings:**
- **28 install-related scripts** discovered across root and skills directories
- **53 setup scripts** (mostly skill-specific environment setups)
- **20 deploy scripts** (platform-specific deployments)
- **Centralized utilities** in `scripts/utils/deploy-utils.sh`
- **No uninstall mechanism** exists (critical gap)
- **Strong patterns** present but inconsistent application
- **Hardcoded paths** and **missing validation** in several scripts

---

## Part 1: Script Analysis Matrix

### 1.1 Root Directory Scripts

| Script | What | How | When | Where | Why |
|--------|------|-----|------|-------|-----|
| `install.sh` | Master installer orchestrator | Sources deploy-utils.sh, detects platforms, runs phases (build→deploy→env→MCP), supports fast mode (-f) and env file (-e) | Initial installation, re-installation | Root → all platform config dirs | Single entry point for complete Overpowers deployment |
| `install-plugins.sh` | Interactive plugin/theme installer | Menu-driven selection from catalog, npm install, injects into opencode.json | Post-install customization | ~/.config/opencode/ | Community plugin integration |
| `install-personas.sh` | System personas installer | Copies persona files to platform directories | Optional setup | Platform-specific | Personality customization |
| `install-antigravity-skills.sh` | Antigravity-specific skills | Installs curated skills for Antigravity platform | Antigravity setup | ~/.gemini/antigravity/ | Platform-specific skill set |
| `install-mcps.sh` | Unified MCP server installer | Platform selection, .env wizard, JSON/TOML config merging, non-destructive merge | Post-deploy configuration | All platform MCP configs | Centralized MCP management |
| `setup-browser-use.sh` | Browser automation setup | Installs Playwright, configures browser binaries | When browser automation needed | System-wide | Browser automation capability |
| `setup-local-api-keys.sh` | Local API key management | Secure key storage setup, validation | Initial setup or key rotation | ~/.config/opencode/ | API authentication |
| `setup-vibe-kanban.sh` | Vibe Kanban board setup | Installs and configures kanban dashboard | Optional productivity setup | Project root | Visual task management |

### 1.2 Deploy Scripts (scripts/)

| Script | What | How | When | Where | Why |
|--------|------|-----|------|-------|-----|
| `deploy-to-opencode.sh` | OpenCode deployment | Symlinks agents, skills, workflows, hooks, AGENTS.md | Install/update | ~/.config/opencode/ | OpenCode integration |
| `deploy-to-gemini.sh` | Gemini CLI deployment | Symlinks hooks, converts workflows to TOML, removes legacy skills | Install/update | ~/.gemini/ | Gemini CLI integration |
| `deploy-to-antigravity.sh` | Antigravity deployment | Symlinks skills and workflows | Install/update | ~/.gemini/antigravity/ | Antigravity integration |
| `deploy-to-kilo.sh` | Kilo Code deployment | Symlinks skills, workflows, rules | Install/update | ~/.kilocode/ | Kilo Code integration |
| `deploy-to-codex.sh` | Codex CLI deployment | Symlinks skills + AGENTS.MD | Install/update | ~/.codex/ | Codex CLI integration |
| `deploy-to-claude-code.sh` | Claude Code deployment | Symlinks skills/commands, links AGENTS.md→CLAUDE.md | Install/update | ~/.claude/ | Claude Code integration |
| `deploy-to-cursor.sh` | Cursor deployment | Symlinks skills | Install/update | ~/.cursor/ | Cursor integration |
| `deploy-to-windsurf.sh` | Windsurf deployment | Symlinks skills to ~/.agents/skills | Install/update | ~/.codeium/windsurf/ | Windsurf integration |
| `deploy-to-factory.sh` | Factory deployment | Symlinks skills + workflows/toml + AGENTS.md | Install/update | ~/.factory/ | Factory integration |
| `deploy-to-qwen.sh` | Qwen Code deployment | Symlinks skills, links AGENTS.md | Install/update | ~/.qwen/ | Qwen Code integration |
| `deploy-agent-army.sh` | Mass agent deployment | Generates configs, injects 475+ agents | Advanced setup | All platforms | Complete agent coverage |

### 1.3 Utility Scripts

| Script | What | How | When | Where | Why |
|--------|------|-----|------|-------|-----|
| `utils/deploy-utils.sh` | Core deployment utilities | Provides logging, symlink creation, banner printing, environment validation | Called by all deploy scripts | N/A | Code reuse and consistency |
| `utils/create-symlinks.sh` | Symlink creation helper | Creates individual symlinks with backup logic | During deployment | Target directories | Safe symlink management |
| `utils/deploy-mcpservers.py` | MCP config translator | Converts between platform MCP schemas (OpenCode vs Antigravity vs TOML) | MCP installation | Platform MCP configs | Schema compatibility |
| `utils/extract-installed-mcps.py` | User MCP scanner | Extracts existing MCPs from platform configs, merges with template | MCP install (optional) | N/A | Preserve user configuration |

### 1.4 Skill-Specific Scripts (Sample)

| Script | What | How | When | Where | Why |
|--------|------|-----|------|-------|-----|
| `skills/*/scripts/install.sh` | Skill dependency installer | Varies by skill (pip, npm, system packages) | Skill activation | Skill directory | Skill-specific requirements |
| `skills/*/scripts/setup*.sh` | Skill environment setup | Configures API keys, creates directories, validates environment | First use | Skill directory | Skill initialization |
| `skills/*/scripts/deploy/*.sh` | Skill deployment | Deploys skill components to target systems | Skill deployment | External systems | Skill distribution |

---

## Part 2: Engineering Review

### 2.1 Critical Issues (Severity: HIGH)

#### 2.1.1 No Uninstall Mechanism
**Issue:** No script exists to reverse installation actions.  
**Impact:** Users cannot cleanly remove Overpowers, leading to config pollution.  
**Risk:** Permanent symlinks, orphaned MCP configs, leftover environment variables.  
**Fix Priority:** CRITICAL

#### 2.1.2 Hardcoded Platform Paths
**Issue:** Platform directories hardcoded in multiple scripts:
```bash
OPENCODE_DIR="${HOME}/.config/opencode"
GEMINI_DIR="${HOME}/.gemini"
# ... repeated in 10+ scripts
```
**Impact:** No central configuration, difficult to support custom paths.  
**Fix:** Centralize in config file or environment variable with defaults.

#### 2.1.3 Inconsistent Error Handling
**Issue:** Mixed use of `set -euo pipefail`:
- `install.sh`: Has it ✓
- `deploy-to-*.sh`: Has it ✓
- `install-plugins.sh`: Has it ✓
- Some skill scripts: Missing ✗

**Impact:** Silent failures, partial installations.  
**Fix:** Enforce in all scripts, add trap handlers for cleanup.

#### 2.1.4 Missing Dry-Run Mode
**Issue:** No script supports `--dry-run` to preview changes.  
**Impact:** Users cannot audit changes before applying.  
**Fix:** Add `--dry-run` flag to all deploy/uninstall scripts.

### 2.2 Moderate Issues (Severity: MEDIUM)

#### 2.2.1 Backup Strategy Inconsistency
**Issue:** Different backup naming conventions:
```bash
# In deploy-to-gemini.sh
skills.overpowers-legacy.$(date +%Y%m%d-%H%M%S).bak

# In deploy-to-claude-code.sh
CLAUDE.md.bak

# In install-mcps.sh
No backup, just removes deprecated servers
```
**Impact:** Confusing cleanup, inconsistent recovery points.  
**Fix:** Standardize backup naming in deploy-utils.sh.

#### 2.2.2 No Rollback Mechanism
**Issue:** Failed deployments leave partial state.  
**Example:** If `deploy-to-opencode.sh` fails at symlink 3 of 5, first 2 remain.  
**Fix:** Transaction-like behavior with atomic rollback on failure.

#### 2.2.3 Redundant MCP Logic
**Issue:** `install-mcps.sh` has 700+ lines with repetitive platform installers:
```bash
install_opencode() { ... }
install_antigravity() { ... }  # Similar logic
install_cursor() { ... }        # Similar logic
# ... 7 more
```
**Fix:** Generic `install_mcp_platform()` with schema templates.

#### 2.2.4 Missing Validation
**Issue:** No post-install verification:
- Symlinks not validated after creation
- MCP configs not tested for JSON validity
- No smoke tests for deployed agents/skills

**Fix:** Add `verify_deployment()` function to deploy-utils.sh.

### 2.3 Minor Issues (Severity: LOW)

#### 2.3.1 Color Code Duplication
**Issue:** Colors defined in every script:
```bash
RED='\033[0;31m'
GREEN='\033[0;32m'
# ... repeated 20+ times
```
**Fix:** Already in deploy-utils.sh but scripts redefine locally.

#### 2.3.2 Inconsistent Logging
**Issue:** Mixed logging styles:
```bash
# Style 1
echo -e "${GREEN}[✓]${NC} Message"

# Style 2
log_info "Message"

# Style 3
echo "Message"
```
**Fix:** Enforce log_* functions from deploy-utils.sh.

#### 2.3.3 No Progress Indicators
**Issue:** Long operations (agent army deploy) show no progress.  
**Fix:** Add progress bars using `gum` or simple counters.

### 2.4 Security Concerns

#### 2.4.1 API Key Handling
**Current:** `.env` file with plaintext keys.  
**Risk:** Accidental commits (mitigated by .gitignore), file permission issues.  
**Improvement:** 
- Validate .env permissions (chmod 600)
- Offer keychain/secret manager integration

#### 2.4.2 Symlink Trust
**Issue:** Symlinks to repo files mean repo compromise → platform compromise.  
**Mitigation:** Already documented in security guidelines.  
**Enhancement:** Add symlink audit command.

---

## Part 3: Uninstall Script Architecture Proposal

### 3.1 Design Principles

1. **Symmetry:** Every install action has a corresponding uninstall action
2. **Safety:** Backup before removal, validate before backup
3. **DRY:** Share core logic with install scripts
4. **Idempotency:** Running uninstall twice is safe
5. **Auditability:** Log all actions with timestamps
6. **Reversibility:** Support `--restore` to undo uninstall

### 3.2 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   uninstall.sh (Master)                     │
│  - Orchestrates all uninstall operations                    │
│  - Platform selection (like install.sh)                     │
│  - Dry-run support                                          │
│  - Backup creation before removal                           │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐  ┌─────────────────┐  ┌──────────────┐
│ uninstall-    │  │ uninstall-mcps  │  │ uninstall-   │
│ platforms.sh  │  │ .sh             │  │ plugins.sh   │
│ (per-platform)│  │ (MCP removal)   │  │ (plugin clean│
│               │  │                 │  │   up)        │
└───────────────┘  └─────────────────┘  └──────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                            ▼
                  ┌─────────────────┐
                  │  uninstall-utils│
                  │  .sh            │
                  │  (shared logic) │
                  └─────────────────┘
```

### 3.3 Core Functions (uninstall-utils.sh)

```bash
#!/usr/bin/env bash
# uninstall-utils.sh - Shared utilities for uninstall scripts

# Create timestamped backup before removal
backup_before_remove() {
    local source="$1"
    local backup_dir="$2"
    local timestamp=$(date +%Y%m%d-%H%M%S)
    
    if [[ -L "${source}" ]]; then
        # Backup symlink target info
        local target=$(readlink "${source}")
        echo "${target}" > "${backup_dir}/$(basename "${source}").symlink-info.${timestamp}"
    elif [[ -e "${source}" ]]; then
        cp -r "${source}" "${backup_dir}/$(basename "${source}").backup.${timestamp}"
    fi
}

# Remove symlink safely
remove_symlink() {
    local link="$1"
    if [[ -L "${link}" ]]; then
        rm "${link}"
        log_info "Removed symlink: ${link}"
    elif [[ -e "${link}" ]]; then
        log_warn "Not a symlink (skipping): ${link}"
        return 1
    else
        log_skip "Does not exist: ${link}"
    fi
}

# Restore from backup
restore_from_backup() {
    local backup_file="$1"
    local target_dir="$2"
    # Implementation for --restore flag
}

# Verify removal
verify_removal() {
    local path="$1"
    if [[ -e "${path}" ]]; then
        log_error "Removal failed: ${path} still exists"
        return 1
    fi
    log_info "Verified removal: ${path}"
    return 0
}

# Dry-run logger
log_dry() {
    if [[ "${DRY_RUN:-0}" == "1" ]]; then
        echo -e "${CYAN}[DRY-RUN]${NC} Would: $*"
    fi
}
```

### 3.4 Uninstall Script Templates

#### 3.4.1 Master Uninstall (uninstall.sh)

```bash
#!/usr/bin/env bash
# uninstall.sh - Master uninstaller

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/scripts/utils/uninstall-utils.sh"
source "${SCRIPT_DIR}/scripts/utils/deploy-utils.sh"  # Reuse colors, logging

# --- Flags ---
DRY_RUN=0
RESTORE=0
PLATFORMS=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=1; shift ;;
        --restore) RESTORE=1; shift ;;
        --platform) PLATFORMS+=("$2"); shift 2 ;;
        *) echo "Usage: $0 [--dry-run] [--restore] [--platform <name>]"; exit 1 ;;
    esac
done

# --- Platform Detection ---
# (Same as install.sh for consistency)

# --- Phase 1: Backup ---
echo -e "\n${CYAN}Phase 1: Creating backups...${NC}"
for platform in "${PLATFORMS[@]}"; do
    backup_platform "${platform}"
done

# --- Phase 2: Remove MCPs ---
echo -e "\n${CYAN}Phase 2: Removing MCP configurations...${NC}"
bash "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" ${DRY_RUN:+--dry-run} "${PLATFORMS[@]}"

# --- Phase 3: Remove Symlinks ---
echo -e "\n${CYAN}Phase 3: Removing deployed symlinks...${NC}"
for platform in "${PLATFORMS[@]}"; do
    case "$platform" in
        OpenCode) bash "${SCRIPT_DIR}/scripts/uninstall-from-opencode.sh" ;;
        # ... other platforms
    esac
done

# --- Phase 4: Cleanup ---
echo -e "\n${CYAN}Phase 4: Cleaning up...${NC}"
# Remove empty directories, orphaned configs, etc.

echo -e "\n${GREEN}${BOLD}✅ Uninstall Complete!${NC}"
echo -e "Backups saved to: ${BACKUP_ROOT}"
echo -e "To restore: $0 --restore ${BACKUP_ID}"
```

#### 3.4.2 Platform Uninstall (uninstall-from-opencode.sh)

```bash
#!/usr/bin/env bash
# uninstall-from-opencode.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/uninstall-utils.sh"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"

setup_deploy_env "OpenCode" "${HOME}/.config/opencode"

print_uninstall_banner() {
    echo -e "${YELLOW}════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}  Removing Overpowers from OpenCode${NC}"
    echo -e "${YELLOW}════════════════════════════════════════════${NC}"
}

# Define what to remove (reverse of deploy)
declare -a TO_REMOVE=(
    "agents"
    "skills"
    "commands"
    "hooks"
    "AGENTS.md"
)

print_uninstall_banner

for item in "${TO_REMOVE[@]}"; do
    target="${PLATFORM_DIR}/${item}"
    
    if [[ "${DRY_RUN:-0}" == "1" ]]; then
        log_dry "Remove ${target}"
        continue
    fi
    
    # Backup first
    backup_before_remove "${target}" "${BACKUP_DIR}"
    
    # Then remove
    remove_symlink "${target}"
    
    # Verify
    verify_removal "${target}" || exit 1
done

print_uninstall_summary
```

#### 3.4.3 MCP Uninstall (uninstall-mcps.sh)

```bash
#!/usr/bin/env bash
# uninstall-mcps.sh

set -euo pipefail

# Remove ONLY Overpowers-installed MCPs (preserve user MCPs)
# Uses metadata from install to identify what was added

remove_mcp_entry() {
    local platform="$1"
    local mcp_name="$2"
    local config_file="$3"
    
    # Python script to safely remove from JSON/TOML
    python3 - "${config_file}" "${mcp_name}" << 'PYEOF'
import json, sys

config_path = sys.argv[1]
mcp_name = sys.argv[2]

with open(config_path) as f:
    config = json.load(f)

if "mcpServers" in config and mcp_name in config["mcpServers"]:
    del config["mcpServers"][mcp_name]
    print(f"REMOVED:{mcp_name}")
elif "mcp" in config and mcp_name in config["mcp"]:
    del config["mcp"][mcp_name]
    print(f"REMOVED:{mcp_name}")

with open(config_path, "w") as f:
    json.dump(config, f, indent=2)
PYEOF
}

# List of Overpowers MCPs (from templates)
OVERPOWERS_MCPS=(
    "serena"
    "vibe-check"
    "desktop-commander"
    # ... others
)

for platform in "${PLATFORMS[@]}"; do
    for mcp in "${OVERPOWERS_MCPS[@]}"; do
        remove_mcp_entry "${platform}" "${mcp}" "${PLATFORM_CONFIG}"
    done
done
```

### 3.5 Implementation Roadmap

#### Phase 1: Foundation (Week 1)
- [ ] Create `scripts/utils/uninstall-utils.sh`
- [ ] Implement backup/restore functions
- [ ] Add dry-run support utilities
- [ ] Create test framework for uninstall safety

#### Phase 2: Platform Uninstalls (Week 2)
- [ ] `uninstall-from-opencode.sh`
- [ ] `uninstall-from-gemini.sh`
- [ ] `uninstall-from-antigravity.sh`
- [ ] `uninstall-from-kilo.sh`
- [ ] `uninstall-from-cursor.sh`
- [ ] `uninstall-from-windsurf.sh`
- [ ] `uninstall-from-claude-code.sh`
- [ ] `uninstall-from-codex.sh`
- [ ] `uninstall-from-factory.sh`
- [ ] `uninstall-from-qwen.sh`

#### Phase 3: MCP & Plugin Uninstall (Week 3)
- [ ] `uninstall-mcps.sh`
- [ ] `uninstall-plugins.sh`
- [ ] `uninstall-personas.sh`

#### Phase 4: Master Orchestrator (Week 4)
- [ ] `uninstall.sh` (master script)
- [ ] Integration testing
- [ ] Documentation
- [ ] User acceptance testing

### 3.6 Code Reuse Strategy

| Install Logic | Reuse in Uninstall | How |
|---------------|-------------------|-----|
| `deploy-utils.sh` colors/logging | Direct source | `source scripts/utils/deploy-utils.sh` |
| Platform detection | Copy + adapt | Same logic, different output |
| Symlink creation | Reverse function | `remove_symlink()` instead of `create_symlink()` |
| MCP config parsing | Reuse Python code | Extract to shared module |
| .env handling | Reuse validation | Shared validation function |
| Backup on conflict | Enhanced version | Always backup before remove |

### 3.7 Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Accidental data loss | Mandatory backups before any removal |
| Partial uninstall leaves broken state | Transaction-like rollback on failure |
| User MCPs removed | Only remove Overpowers-installed MCPs (tracked via metadata) |
| Symlinks to wrong targets | Verify symlink target before removal |
| Permissions issues | Validate write access before starting |

---

## Part 4: Recommendations & Priority

### 4.1 Immediate Actions (This Sprint)

1. **Create `uninstall-utils.sh`** (2 hours)
   - Backup/restore functions
   - Dry-run support
   - Verification helpers

2. **Implement `uninstall-from-opencode.sh`** as reference (4 hours)
   - Full test coverage
   - Documentation

3. **Add validation to existing deploy scripts** (4 hours)
   - Post-deploy verification
   - Symlink validation

### 4.2 Short-Term (Next Sprint)

4. **Complete all platform uninstall scripts** (16 hours)
   - 10 platforms × 1.5 hours each + testing

5. **Implement MCP uninstall** (4 hours)
   - Careful tracking of what was installed

6. **Create master `uninstall.sh`** (4 hours)
   - Orchestration, platform selection

### 4.3 Long-Term Improvements

7. **Refactor deploy scripts to use shared logic** (8 hours)
   - Reduce duplication
   - Enforce standards

8. **Add configuration file for paths** (2 hours)
   - Centralize hardcoded paths
   - Support custom locations

9. **Implement transaction support** (8 hours)
   - Atomic operations
   - Automatic rollback

10. **Add comprehensive testing** (8 hours)
    - CI/CD integration
    - Automated regression tests

---

## Appendix A: Script Inventory Summary

**Total Scripts Analyzed:** 101
- Install scripts: 28
- Setup scripts: 53
- Deploy scripts: 20

**Lines of Code:** ~8,000 (install/deploy related)

**Platforms Supported:** 10
- OpenCode, Gemini CLI, Antigravity, Kilo Code, Cursor, Windsurf, Codex CLI, Claude Code, Factory, Qwen Code

**MCP Servers Managed:** 13+

---

## Appendix B: Glossary

- **DRY:** Don't Repeat Yourself
- **MCP:** Model Context Protocol
- **Symlink:** Symbolic link (filesystem pointer)
- **Idempotent:** Operation that can be applied multiple times without changing result
- **TOML:** Tom's Obvious, Minimal Language (config format)

---

**Document Status:** ✅ Complete  
**Next Review:** After uninstall implementation  
**Stakeholders:** @yuichiinumaru (maintainer), All Overpowers users
