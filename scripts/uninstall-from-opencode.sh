#!/usr/bin/env bash
# =============================================================================
# uninstall-from-opencode.sh - Remove Overpowers from OpenCode
# =============================================================================
# Reverses all changes made by deploy-to-opencode.sh
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Source utilities
source "${SCRIPT_DIR}/utils/uninstall-utils.sh"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"

# --- Configuration ---
PLATFORM_NAME="OpenCode"
PLATFORM_DIR="${HOME}/.config/opencode"
BACKUP_PLATFORM="opencode"

# Symlinks created by deploy-to-opencode.sh
declare -A SYMLINKS=(
    ["agents"]="agents"
    ["skills"]="skills"
    ["workflows"]="commands"
    ["hooks"]="hooks"
    ["AGENTS.md"]="AGENTS.md"
    ["themes"]="themes"
)

# --- Main Execution ---
print_uninstall_banner "${PLATFORM_NAME}"
check_dry_run

# Validate tools
validate_tools || exit 1

# Initialize backup directory
BACKUP_DIR=$(init_backup_dir "${BACKUP_PLATFORM}")

# Track removals for summary
REMOVED_COUNT=0
SKIPPED_COUNT=0
ERRORS=()

echo -e "${BOLD}Removing symlinks...${NC}"
echo ""

for repo_item in "${!SYMLINKS[@]}"; do
    platform_item="${SYMLINKS[${repo_item}]}"
    target_path="${PLATFORM_DIR}/${platform_item}"
    source_path="${REPO_ROOT}/${repo_item}"

    # Check if symlink exists
    if [[ ! -L "${target_path}" ]]; then
        if [[ -e "${target_path}" ]]; then
            log_warn "Not a symlink (skipping): ${target_path}"
            SKIPPED_COUNT=$((SKIPPED_COUNT + 1))
        else
            log_skip "Does not exist: ${target_path}"
            SKIPPED_COUNT=$((SKIPPED_COUNT + 1))
        fi
        continue
    fi

    # Verify symlink points to expected target
    current_target=$(readlink "${target_path}")
    if [[ "${current_target}" != "${source_path}" ]]; then
        log_warn "Symlink points to unexpected target: ${target_path} → ${current_target}"
        log_warn "Expected: ${source_path}"
        SKIPPED_COUNT=$((SKIPPED_COUNT + 1))
        continue
    fi

    # Backup before removal
    backup_before_remove "${target_path}" "${BACKUP_DIR}" "${platform_item}"

    # Remove symlink
    if remove_symlink "${target_path}"; then
        REMOVED_COUNT=$((REMOVED_COUNT + 1))
        
        # Verify removal
        if verify_removal "${target_path}"; then
            : # Verification passed
        else
            ERRORS+=("Failed to verify removal: ${target_path}")
        fi
    else
        ERRORS+=("Failed to remove: ${target_path}")
    fi
done

# Cleanup old backups
cleanup_old_backups "${BACKUP_PLATFORM}" "${BACKUP_RETENTION_COUNT}"

# --- Summary ---
echo ""
echo -e "${BOLD}Removal Summary:${NC}"
echo -e "  Removed:  ${GREEN}${REMOVED_COUNT}${NC}"
echo -e "  Skipped:  ${CYAN}${SKIPPED_COUNT}${NC}"

if [[ ${#ERRORS[@]} -gt 0 ]]; then
    echo ""
    echo -e "${RED}Errors:${NC}"
    for error in "${ERRORS[@]}"; do
        echo -e "  ${RED}•${NC} ${error}"
    done
fi

echo ""
if [[ -d "${BACKUP_DIR}" ]]; then
    echo -e "Backups saved to: ${CYAN}${BACKUP_DIR}${NC}"
    echo -e "To restore: ${YELLOW}Source the backup files manually or use restore scripts${NC}"
fi

echo ""
print_uninstall_summary "${PLATFORM_NAME}" "${BACKUP_DIR}"

# Exit with error if there were errors
if [[ ${#ERRORS[@]} -gt 0 ]]; then
    exit 1
fi

exit 0
