#!/usr/bin/env bash
# =============================================================================
# uninstall-from-gemini.sh - Remove Overpowers from Gemini CLI
# =============================================================================
# Reverses all changes made by deploy-to-gemini.sh
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Source utilities
source "${SCRIPT_DIR}/utils/uninstall-utils.sh"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"

# --- Configuration ---
PLATFORM_NAME="Gemini CLI"
PLATFORM_DIR="${HOME}/.gemini"
BACKUP_PLATFORM="gemini"

# Symlinks created by deploy-to-gemini.sh
declare -A SYMLINKS=(
    ["hooks"]="hooks"
    ["workflows/toml"]="commands"
    ["AGENTS.md"]="GEMINI.md"
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

# --- Handle legacy skills directory ---
echo ""
echo -e "${BOLD}Checking for legacy skills directory...${NC}"
echo ""

LEGACY_SKILLS="${PLATFORM_DIR}/skills"
LEGACY_SKILLS_PATTERN="${PLATFORM_DIR}/skills.overpowers-legacy.*.bak"

# Check for current skills symlink/directory
if [[ -L "${LEGACY_SKILLS}" || -d "${LEGACY_SKILLS}" ]]; then
    log_warn "Found legacy skills directory/symlink: ${LEGACY_SKILLS}"
    backup_before_remove "${LEGACY_SKILLS}" "${BACKUP_DIR}" "skills-legacy"
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Remove legacy skills: ${LEGACY_SKILLS}"
    else
        rm -rf "${LEGACY_SKILLS}"
        log_remove "Removed legacy skills: ${LEGACY_SKILLS}"
        REMOVED_COUNT=$((REMOVED_COUNT + 1))
    fi
fi

# Check for already-backed-up legacy skills (from install script)
shopt -s nullglob
legacy_backups=(${LEGACY_SKILLS_PATTERN})
shopt -u nullglob

if [[ ${#legacy_backups[@]} -gt 0 ]]; then
    log_info "Found ${#legacy_backups[@]} legacy skills backup(s) from installation"
    for backup in "${legacy_backups[@]}"; do
        if [[ "${DRY_RUN}" == "1" ]]; then
            log_dry "Remove legacy backup: ${backup}"
        else
            rm -f "${backup}"
            log_remove "Removed legacy backup: ${backup}"
        fi
    done
fi

# --- Handle settings.json modifications ---
echo ""
echo -e "${BOLD}Checking settings.json...${NC}"
echo ""

SETTINGS_JSON="${PLATFORM_DIR}/settings.json"

if [[ -f "${SETTINGS_JSON}" ]]; then
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Remove experimental.enableAgents from ${SETTINGS_JSON}"
    else
        # Remove the enableAgents setting
        python3 - "${SETTINGS_JSON}" << 'PYEOF'
import json
import sys

config_path = sys.argv[1]

try:
    with open(config_path) as f:
        config = json.load(f)

    modified = False
    if 'experimental' in config and 'enableAgents' in config['experimental']:
        del config['experimental']['enableAgents']
        modified = True
        # Clean up empty experimental block
        if not config['experimental']:
            del config['experimental']

    if modified:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        print("REMOVED:enableAgents")
    else:
        print("SKIP:enableAgents (not found)")
except Exception as e:
    print(f"ERROR:{str(e)}", file=sys.stderr)
    sys.exit(1)
PYEOF
        log_info "Cleaned settings.json"
    fi
else
    log_skip "settings.json not found: ${SETTINGS_JSON}"
fi

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
