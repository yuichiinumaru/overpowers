#!/usr/bin/env bash
# =============================================================================
# uninstall-utils.sh - Core utilities for Overpowers uninstall scripts
# =============================================================================
# Provides shared functions for backup, removal, verification, and logging
# across all uninstall operations.
# =============================================================================

set -euo pipefail

# --- Colors (reuse from deploy-utils.sh if available) ---
if ! declare -F log_info &>/dev/null; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    CYAN='\033[0;36m'
    MAGENTA='\033[0;35m'
    BOLD='\033[1m'
    DIM='\033[2m'
    NC='\033[0m'
fi

# --- Global Configuration ---
export DRY_RUN="${DRY_RUN:-0}"
export BACKUP_ROOT="${BACKUP_ROOT:-${HOME}/.overpowers/backups}"
export LOG_FILE="${LOG_FILE:-}"
export BACKUP_RETENTION_COUNT="${BACKUP_RETENTION_COUNT:-5}"

# =============================================================================
# Logging Functions
# =============================================================================

log_info() {
    echo -e "${GREEN}[✓]${NC} $*"
    _log_to_file "INFO" "$*"
}

log_warn() {
    echo -e "${YELLOW}[!]${NC} $*" >&2
    _log_to_file "WARN" "$*"
}

log_error() {
    echo -e "${RED}[✗]${NC} $*" >&2
    _log_to_file "ERROR" "$*"
}

log_skip() {
    echo -e "${CYAN}[~]${NC} $*"
    _log_to_file "SKIP" "$*"
}

log_dry() {
    if [[ "${DRY_RUN}" == "1" ]]; then
        echo -e "${CYAN}[DRY-RUN]${NC} Would: $*"
    fi
    _log_to_file "DRY-RUN" "$*"
}

log_backup() {
    echo -e "${MAGENTA}[BACKUP]${NC} $*"
    _log_to_file "BACKUP" "$*"
}

log_remove() {
    echo -e "${RED}[REMOVE]${NC} $*"
    _log_to_file "REMOVE" "$*"
}

log_verify() {
    echo -e "${GREEN}[VERIFY]${NC} $*"
    _log_to_file "VERIFY" "$*"
}

_log_to_file() {
    local level="$1"
    local message="$2"
    if [[ -n "${LOG_FILE}" ]]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') [${level}] ${message}" >> "${LOG_FILE}"
    fi
}

# =============================================================================
# Backup Functions
# =============================================================================

# Create backup directory with timestamp
init_backup_dir() {
    local platform="$1"
    local timestamp
    timestamp=$(date +%Y%m%d-%H%M%S)
    local backup_dir="${BACKUP_ROOT}/${platform}/${timestamp}"
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Create backup directory: ${backup_dir}"
        echo "${backup_dir}"
        return 0
    fi
    
    mkdir -p "${backup_dir}"
    log_backup "Created backup directory: ${backup_dir}"
    echo "${backup_dir}"
}

# Backup a file, directory, or symlink before removal
# Usage: backup_before_remove <source> <backup_dir> [item_name]
backup_before_remove() {
    local source="$1"
    local backup_dir="$2"
    local item_name="${3:-$(basename "${source}")}"
    local timestamp
    timestamp=$(date +%Y%m%d-%H%M%S)
    
    if [[ ! -e "${source}" && ! -L "${source}" ]]; then
        log_skip "Nothing to backup: ${source} does not exist"
        return 0
    fi
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Backup ${source} → ${backup_dir}/${item_name}.overpowers-backup.${timestamp}"
        return 0
    fi
    
    local backup_name="${item_name}.overpowers-backup.${timestamp}"
    local backup_path="${backup_dir}/${backup_name}"
    
    if [[ -L "${source}" ]]; then
        # Backup symlink info
        local target
        target=$(readlink "${source}")
        echo "${target}" > "${backup_path}.symlink-info"
        log_backup "Backed up symlink info: ${source} → ${target}"
    elif [[ -d "${source}" ]]; then
        # Backup directory
        cp -r "${source}" "${backup_path}"
        log_backup "Backed up directory: ${source} → ${backup_path}"
    elif [[ -f "${source}" ]]; then
        # Backup file
        cp "${source}" "${backup_path}"
        log_backup "Backed up file: ${source} → ${backup_path}"
    fi
    
    echo "${backup_path}"
}

# Cleanup old backups, keeping only the most recent N
cleanup_old_backups() {
    local platform="$1"
    local retention="${2:-${BACKUP_RETENTION_COUNT}}"
    local platform_backup_dir="${BACKUP_ROOT}/${platform}"
    
    if [[ ! -d "${platform_backup_dir}" ]]; then
        return 0
    fi
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Cleanup old backups for ${platform}, keeping last ${retention}"
        return 0
    fi
    
    local backup_count
    backup_count=$(find "${platform_backup_dir}" -maxdepth 1 -type d -name "20*" | wc -l)
    
    if [[ ${backup_count} -gt ${retention} ]]; then
        local to_delete=$((backup_count - retention))
        log_info "Cleaning up ${to_delete} old backup(s) for ${platform}"
        
        find "${platform_backup_dir}" -maxdepth 1 -type d -name "20*" | sort | head -n "${to_delete}" | while read -r old_backup; do
            rm -rf "${old_backup}"
            log_info "Deleted old backup: ${old_backup}"
        done
    fi
}

# Restore from backup
# Usage: restore_from_backup <backup_path> <target_path>
restore_from_backup() {
    local backup_path="$1"
    local target_path="$2"
    
    if [[ ! -e "${backup_path}" ]]; then
        log_error "Backup not found: ${backup_path}"
        return 1
    fi
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Restore ${backup_path} → ${target_path}"
        return 0
    fi
    
    # Remove current item if exists
    if [[ -e "${target_path}" || -L "${target_path}" ]]; then
        rm -rf "${target_path}"
    fi
    
    # Check if it was a symlink
    if [[ "${backup_path}" == *.symlink-info ]]; then
        local target
        target=$(cat "${backup_path}")
        local original_path="${backup_path%.symlink-info}"
        ln -s "${target}" "${original_path}"
        log_info "Restored symlink: ${original_path} → ${target}"
    else
        # Restore file/directory
        if [[ -d "${backup_path}" ]]; then
            cp -r "${backup_path}" "${target_path}"
        else
            cp "${backup_path}" "${target_path}"
        fi
        log_info "Restored: ${target_path}"
    fi
    
    return 0
}

# =============================================================================
# Removal Functions
# =============================================================================

# Remove symlink safely
# Usage: remove_symlink <link_path>
remove_symlink() {
    local link="$1"
    
    if [[ ! -L "${link}" ]]; then
        if [[ -e "${link}" ]]; then
            log_warn "Not a symlink (skipping): ${link}"
        else
            log_skip "Does not exist: ${link}"
        fi
        return 1
    fi
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Remove symlink: ${link}"
        return 0
    fi
    
    rm "${link}"
    log_remove "Removed symlink: ${link}"
    return 0
}

# Remove directory safely (with backup)
# Usage: remove_directory <dir_path> <backup_dir>
remove_directory() {
    local dir="$1"
    local backup_dir="$2"
    
    if [[ ! -d "${dir}" ]]; then
        log_skip "Directory does not exist: ${dir}"
        return 0
    fi
    
    # Backup first
    backup_before_remove "${dir}" "${backup_dir}"
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Remove directory: ${dir}"
        return 0
    fi
    
    rm -rf "${dir}"
    log_remove "Removed directory: ${dir}"
    return 0
}

# Remove file safely (with backup)
# Usage: remove_file <file_path> <backup_dir>
remove_file() {
    local file="$1"
    local backup_dir="$2"
    
    if [[ ! -f "${file}" ]]; then
        log_skip "File does not exist: ${file}"
        return 0
    fi
    
    # Backup first
    backup_before_remove "${file}" "${backup_dir}"
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Remove file: ${file}"
        return 0
    fi
    
    rm "${file}"
    log_remove "Removed file: ${file}"
    return 0
}

# Remove MCP entry from JSON config
# Usage: remove_mcp_entry <config_file> <mcp_name> [config_key]
remove_mcp_entry() {
    local config_file="$1"
    local mcp_name="$2"
    local config_key="${3:-mcpServers}"
    
    if [[ ! -f "${config_file}" ]]; then
        log_skip "Config file does not exist: ${config_file}"
        return 0
    fi
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Remove MCP entry '${mcp_name}' from ${config_file}"
        return 0
    fi
    
    python3 - "${config_file}" "${mcp_name}" "${config_key}" << 'PYEOF'
import json
import sys

config_path = sys.argv[1]
mcp_name = sys.argv[2]
config_key = sys.argv[3]

try:
    with open(config_path) as f:
        config = json.load(f)
    
    if config_key in config and isinstance(config[config_key], dict):
        if mcp_name in config[config_key]:
            del config[config_key][mcp_name]
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=2)
            print(f"REMOVED:{mcp_name}")
        else:
            print(f"SKIP:{mcp_name} (not found)")
    else:
        print(f"SKIP:{mcp_name} (no {config_key} in config)")
except Exception as e:
    print(f"ERROR:{str(e)}", file=sys.stderr)
    sys.exit(1)
PYEOF
}

# Remove MCP entry from TOML config (Codex CLI)
# Usage: remove_mcp_toml_entry <config_file> <mcp_name>
remove_mcp_toml_entry() {
    local config_file="$1"
    local mcp_name="$2"
    
    if [[ ! -f "${config_file}" ]]; then
        log_skip "Config file does not exist: ${config_file}"
        return 0
    fi
    
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Remove MCP entry '${mcp_name}' from ${config_file} (TOML)"
        return 0
    fi
    
    python3 - "${config_file}" "${mcp_name}" << 'PYEOF'
import sys
import re

config_path = sys.argv[1]
mcp_name = sys.argv[2]

try:
    with open(config_path) as f:
        content = f.read()
    
    # Remove [mcp_servers.NAME] block
    pattern = rf'\n?\[mcp_servers\.{re.escape(mcp_name)}\][\s\S]*?(?=\n\[mcp_servers\.|\Z)'
    
    if re.search(pattern, content):
        content = re.sub(pattern, '\n', content)
        # Clean up multiple consecutive newlines
        content = re.sub(r'\n{{3,}}', '\n\n', content)
        
        with open(config_path, 'w') as f:
            f.write(content.strip() + '\n')
        print(f"REMOVED:{mcp_name}")
    else:
        print(f"SKIP:{mcp_name} (not found)")
except Exception as e:
    print(f"ERROR:{str(e)}", file=sys.stderr)
    sys.exit(1)
PYEOF
}

# =============================================================================
# Verification Functions
# =============================================================================

# Verify removal was successful
# Usage: verify_removal <path>
verify_removal() {
    local path="$1"

    # Skip verification in dry-run mode
    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Verify removal: ${path} (skipped in dry-run)"
        return 0
    fi

    if [[ -e "${path}" || -L "${path}" ]]; then
        log_error "Removal failed: ${path} still exists"
        return 1
    fi

    log_verify "Verified removal: ${path}"
    return 0
}

# Verify symlink target exists
# Usage: verify_symlink_target <symlink_path>
verify_symlink_target() {
    local link="$1"
    
    if [[ ! -L "${link}" ]]; then
        log_skip "Not a symlink: ${link}"
        return 0
    fi
    
    if [[ -e "${link}" ]]; then
        log_verify "Symlink target exists: ${link}"
        return 0
    else
        log_error "Broken symlink: ${link}"
        return 1
    fi
}

# Validate JSON config file
# Usage: validate_json <file_path>
validate_json() {
    local file="$1"
    
    if [[ ! -f "${file}" ]]; then
        log_skip "File does not exist: ${file}"
        return 0
    fi
    
    if python3 -m json.tool "${file}" > /dev/null 2>&1; then
        log_verify "Valid JSON: ${file}"
        return 0
    else
        log_error "Invalid JSON: ${file}"
        return 1
    fi
}

# Validate TOML config file
# Usage: validate_toml <file_path>
validate_toml() {
    local file="$1"
    
    if [[ ! -f "${file}" ]]; then
        log_skip "File does not exist: ${file}"
        return 0
    fi
    
    if python3 -c "import tomllib; tomllib.load(open('${file}', 'rb'))" 2>/dev/null; then
        log_verify "Valid TOML: ${file}"
        return 0
    else
        log_error "Invalid TOML: ${file}"
        return 1
    fi
}

# =============================================================================
# Utility Functions
# =============================================================================

# Print uninstall banner
print_uninstall_banner() {
    local platform="${1:-Platform}"
    echo ""
    echo -e "${YELLOW}═══════════════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}  Removing Overpowers from ${platform}${NC}"
    echo -e "${YELLOW}═══════════════════════════════════════════════════════${NC}"
    echo ""
}

# Print uninstall summary
print_uninstall_summary() {
    local platform="${1:-Platform}"
    local backup_dir="${2:-}"
    
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  ${platform} Uninstall Complete!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo ""
    
    if [[ -n "${backup_dir}" && -d "${backup_dir}" ]]; then
        echo -e "Backups saved to: ${CYAN}${backup_dir}${NC}"
        echo -e "To restore: ${YELLOW}./uninstall.sh --restore${NC}"
        echo ""
    fi
}

# Check if running in dry-run mode
check_dry_run() {
    if [[ "${DRY_RUN}" == "1" ]]; then
        echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
        echo -e "${CYAN}  DRY-RUN MODE - No changes will be made${NC}"
        echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
        echo ""
    fi
}

# Validate required tools
validate_tools() {
    local required_tools=("bash" "python3")
    local missing=()
    
    for tool in "${required_tools[@]}"; do
        if ! command -v "${tool}" &>/dev/null; then
            missing+=("${tool}")
        fi
    done
    
    if [[ ${#missing[@]} -gt 0 ]]; then
        log_error "Missing required tools: ${missing[*]}"
        return 1
    fi
    
    return 0
}

# Source deploy-utils.sh for shared functions (colors, logging if not defined)
UNINSTALL_UTILS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "${UNINSTALL_UTILS_DIR}/deploy-utils.sh" ]]; then
    # Only source functions that aren't already defined
    source "${UNINSTALL_UTILS_DIR}/deploy-utils.sh" 2>/dev/null || true
fi
