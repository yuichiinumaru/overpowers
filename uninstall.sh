#!/usr/bin/env bash
# =============================================================================
# uninstall.sh - Master Uninstaller for Overpowers
# =============================================================================
# Orchestrates uninstallation across all supported platforms with safety
# features including backups, dry-run mode, and comprehensive logging.
# =============================================================================

set -euo pipefail

# --- Initialization ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/scripts/utils/uninstall-utils.sh"
source "${SCRIPT_DIR}/scripts/utils/deploy-utils.sh"

# --- Configuration ---
DRY_RUN=0
RESTORE=0
PLATFORMS=()
UNINSTALL_MCPS=1
UNINSTALL_PLUGINS=0
BACKUP_DIR=""

# --- Help Text ---
show_help() {
    cat << EOF
${BOLD}Overpowers Uninstaller${NC}

${BOLD}USAGE:${NC}
    $0 [OPTIONS] [PLATFORMS...]

${BOLD}OPTIONS:${NC}
    -n, --dry-run       Preview changes without making modifications
    -r, --restore       Restore from a previous backup
    -a, --all           Uninstall from all detected platforms
    --no-mcp            Skip MCP server removal
    --plugins           Also uninstall plugins
    -p, --platform      Specify platform(s) to uninstall from
    -h, --help          Show this help message

${BOLD}PLATFORMS:${NC}
    opencode        OpenCode (~/.config/opencode)
    gemini          Gemini CLI (~/.gemini)
    antigravity     Google Antigravity (~/.gemini/antigravity)
    kilo            Kilo Code (~/.kilocode)
    cursor          Cursor (~/.cursor)
    windsurf        Windsurf (~/.codeium/windsurf)
    claude          Claude Code (~/.claude)
    codex           Codex CLI (~/.codex)
    factory         Factory (~/.factory)
    qwen            Qwen Code (~/.qwen)

${BOLD}EXAMPLES:${NC}
    # Preview uninstall across all platforms
    $0 --dry-run --all

    # Uninstall from OpenCode only
    $0 opencode

    # Uninstall from multiple platforms
    $0 --platform opencode --platform cursor --platform claude

    # Restore from backup
    $0 --restore ~/.overpowers/backups/opencode/20260316-143022

${BOLD}BACKUPS:${NC}
    Backups are stored in: ~/.overpowers/backups/<platform>/<timestamp>/
    To restore manually: $0 --restore <backup-directory>

EOF
}

# --- Parse Arguments ---
while [[ $# -gt 0 ]]; do
    case "$1" in
        -n|--dry-run)
            DRY_RUN=1
            export DRY_RUN=1
            shift
            ;;
        -r|--restore)
            RESTORE=1
            BACKUP_DIR="$2"
            shift 2
            ;;
        -a|--all)
            PLATFORMS=("all")
            shift
            ;;
        --no-mcp)
            UNINSTALL_MCPS=0
            shift
            ;;
        --plugins)
            UNINSTALL_PLUGINS=1
            shift
            ;;
        -p|--platform)
            PLATFORMS+=("$2")
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            # Treat as platform name
            PLATFORMS+=("$1")
            shift
            ;;
    esac
done

# --- Validate Tools ---
validate_tools || {
    log_error "Required tools not found. Please install bash and python3."
    exit 1
}

# --- Check Dry Run Mode ---
check_dry_run

# --- Platform Detection ---
detect_platforms() {
    local detected=()
    
    [[ -d "${HOME}/.config/opencode" ]] && detected+=("opencode")
    [[ -d "${HOME}/.gemini" ]] && detected+=("gemini" "antigravity")
    [[ -d "${HOME}/.kilocode" ]] && detected+=("kilo")
    [[ -d "${HOME}/.cursor" ]] && detected+=("cursor")
    [[ -d "${HOME}/.codeium/windsurf" ]] && detected+=("windsurf")
    [[ -d "${HOME}/.claude" ]] && detected+=("claude")
    [[ -d "${HOME}/.codex" ]] && detected+=("codex")
    [[ -d "${HOME}/.factory" ]] && detected+=("factory")
    [[ -d "${HOME}/.qwen" ]] && detected+=("qwen")
    
    echo "${detected[@]}"
}

# --- Select Platforms ---
declare -a SELECTED_PLATFORMS=()

if [[ ${#PLATFORMS[@]} -eq 0 ]]; then
    # Auto-detect platforms
    detected=$(detect_platforms)
    if [[ -z "${detected}" ]]; then
        log_warn "No Overpowers installations detected."
        exit 0
    fi
    
    log_info "Detected Overpowers installations: ${detected}"
    
    if command -v gum >/dev/null 2>&1 && [[ "${DRY_RUN}" != "1" ]]; then
        echo -e "\n${BOLD}Select platforms to uninstall from:${NC}"
        choices=$(gum choose --no-limit ${detected})
        for choice in $choices; do
            SELECTED_PLATFORMS+=("$choice")
        done
    else
        SELECTED_PLATFORMS=(${detected})
    fi
elif [[ "${PLATFORMS[0]}" == "all" ]]; then
    # All platforms
    SELECTED_PLATFORMS=("opencode" "gemini" "antigravity" "kilo" "cursor" "windsurf" "claude" "codex" "factory" "qwen")
else
    # User-specified platforms
    SELECTED_PLATFORMS=("${PLATFORMS[@]}")
fi

if [[ ${#SELECTED_PLATFORMS[@]} -eq 0 ]]; then
    log_warn "No platforms selected. Exiting."
    exit 0
fi

log_info "Uninstalling from: ${SELECTED_PLATFORMS[*]}"

# --- Restore Mode ---
if [[ "${RESTORE}" == "1" ]]; then
    if [[ ! -d "${BACKUP_DIR}" ]]; then
        log_error "Backup directory not found: ${BACKUP_DIR}"
        exit 1
    fi
    
    log_info "Restoring from backup: ${BACKUP_DIR}"
    
    # Extract platform from backup path
    platform=$(echo "${BACKUP_DIR}" | sed 's|.*/backups/||' | cut -d'/' -f1)
    
    # Restore each backup item
    find "${BACKUP_DIR}" -name "*.overpowers-backup.*" | while read -r backup_file; do
        # Determine original path from backup name
        original_name=$(basename "${backup_file}" | sed 's/\.overpowers-backup\.[0-9-]*//')
        original_name="${original_name%.symlink-info}"
        
        # Determine target directory based on platform
        case "${platform}" in
            opencode) target_dir="${HOME}/.config/opencode" ;;
            gemini|antigravity) target_dir="${HOME}/.gemini${platform/gemini/}" ;;
            kilo) target_dir="${HOME}/.kilocode" ;;
            cursor) target_dir="${HOME}/.cursor" ;;
            windsurf) target_dir="${HOME}/.codeium/windsurf" ;;
            claude) target_dir="${HOME}/.claude" ;;
            codex) target_dir="${HOME}/.codex" ;;
            factory) target_dir="${HOME}/.factory" ;;
            qwen) target_dir="${HOME}/.qwen" ;;
        esac
        
        restore_from_backup "${backup_file}" "${target_dir}/${original_name}"
    done
    
    log_info "Restore complete!"
    exit 0
fi

# --- Initialize Backup Directory ---
if [[ "${DRY_RUN}" != "1" ]]; then
    mkdir -p "${BACKUP_ROOT}"
fi

# =============================================================================
# Phase 1: Remove MCP Servers
# =============================================================================
if [[ "${UNINSTALL_MCPS}" == "1" ]]; then
    echo -e "\n${CYAN}Phase 1: Removing MCP Servers...${NC}"
    
    for platform in "${SELECTED_PLATFORMS[@]}"; do
        log_info "Removing MCPs from ${platform}..."
        
        case "${platform}" in
            opencode)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform opencode ${DRY_RUN:+--dry-run}
                ;;
            gemini)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform gemini-cli ${DRY_RUN:+--dry-run}
                ;;
            antigravity)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform antigravity ${DRY_RUN:+--dry-run}
                ;;
            kilo)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform kilo ${DRY_RUN:+--dry-run}
                ;;
            cursor)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform cursor ${DRY_RUN:+--dry-run}
                ;;
            windsurf)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform windsurf ${DRY_RUN:+--dry-run}
                ;;
            claude)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform claude-code ${DRY_RUN:+--dry-run}
                ;;
            codex)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform codex ${DRY_RUN:+--dry-run}
                ;;
            factory)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform factory ${DRY_RUN:+--dry-run}
                ;;
            qwen)
                "${SCRIPT_DIR}/scripts/uninstall-mcps.sh" --platform qwen ${DRY_RUN:+--dry-run}
                ;;
        esac
    done
fi

# =============================================================================
# Phase 2: Remove Platform Symlinks
# =============================================================================
echo -e "\n${CYAN}Phase 2: Removing Platform Symlinks...${NC}"

for platform in "${SELECTED_PLATFORMS[@]}"; do
    log_info "Uninstalling from ${platform}..."
    
    case "${platform}" in
        opencode)
            "${SCRIPT_DIR}/scripts/uninstall-from-opencode.sh" ${DRY_RUN:+--dry-run}
            ;;
        gemini)
            "${SCRIPT_DIR}/scripts/uninstall-from-gemini.sh" ${DRY_RUN:+--dry-run}
            ;;
        antigravity)
            "${SCRIPT_DIR}/scripts/uninstall-from-antigravity.sh" ${DRY_RUN:+--dry-run}
            ;;
        kilo)
            "${SCRIPT_DIR}/scripts/uninstall-from-kilo.sh" ${DRY_RUN:+--dry-run}
            ;;
        cursor)
            "${SCRIPT_DIR}/scripts/uninstall-from-cursor.sh" ${DRY_RUN:+--dry-run}
            ;;
        windsurf)
            "${SCRIPT_DIR}/scripts/uninstall-from-windsurf.sh" ${DRY_RUN:+--dry-run}
            ;;
        claude)
            "${SCRIPT_DIR}/scripts/uninstall-from-claude-code.sh" ${DRY_RUN:+--dry-run}
            ;;
        codex)
            "${SCRIPT_DIR}/scripts/uninstall-from-codex.sh" ${DRY_RUN:+--dry-run}
            ;;
        factory)
            "${SCRIPT_DIR}/scripts/uninstall-from-factory.sh" ${DRY_RUN:+--dry-run}
            ;;
        qwen)
            "${SCRIPT_DIR}/scripts/uninstall-from-qwen.sh" ${DRY_RUN:+--dry-run}
            ;;
        *)
            log_warn "Unknown platform: ${platform}"
            ;;
    esac
done

# =============================================================================
# Phase 3: Remove Plugins (Optional)
# =============================================================================
if [[ "${UNINSTALL_PLUGINS}" == "1" ]]; then
    echo -e "\n${CYAN}Phase 3: Removing Plugins...${NC}"
    log_warn "Plugin uninstall not yet implemented. Manual removal required."
    log_info "To remove plugins manually, edit ~/.config/opencode/opencode.json"
fi

# =============================================================================
# Phase 4: Cleanup
# =============================================================================
echo -e "\n${CYAN}Phase 4: Cleanup...${NC}"

for platform in "${SELECTED_PLATFORMS[@]}"; do
    cleanup_old_backups "${platform}" 5
done

# =============================================================================
# Summary
# =============================================================================
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  ${BOLD}Overpowers Uninstall Complete!${NC}${GREEN}${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo ""

if [[ "${DRY_RUN}" != "1" ]]; then
    echo -e "${BOLD}Platforms uninstalled from:${NC}"
    for platform in "${SELECTED_PLATFORMS[@]}"; do
        echo -e "  ${GREEN}✓${NC} ${platform}"
    done
    echo ""
    
    echo -e "${BOLD}Backups saved to:${NC}"
    echo -e "  ${CYAN}${BACKUP_ROOT}/${NC}"
    echo ""
    
    echo -e "${BOLD}To restore from backup:${NC}"
    echo -e "  ${YELLOW}$0 --restore <backup-directory>${NC}"
    echo ""
    
    echo -e "${DIM}Note: Configuration files and MCP entries have been backed up.${NC}"
    echo -e "${DIM}To completely remove Overpowers, also delete the repository.${NC}"
else
    echo -e "${CYAN}Dry-run complete. No changes were made.${NC}"
    echo ""
    echo -e "To perform actual uninstall, run:"
    echo -e "  ${GREEN}$0 ${SELECTED_PLATFORMS[*]}${NC}"
fi

echo ""
