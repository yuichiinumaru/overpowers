#!/usr/bin/env bash
# =============================================================================
# uninstall-mcps.sh - Unified Multi-Platform MCP Server Uninstaller
# =============================================================================
# Removes ONLY Overpowers-installed MCP servers from multiple platforms:
#   - OpenCode     (~/.config/opencode/opencode.json)
#   - Gemini CLI   (~/.gemini/settings.json)
#   - Antigravity  (~/.gemini/antigravity/mcp_config.json)
#   - Cursor       (~/.cursor/mcp.json)
#   - Windsurf     (~/.codeium/windsurf/mcp_config.json)
#   - Claude Code  (~/.claude.json)
#   - Kilo Code    (~/.kilocode/mcp.json)
#   - Factory      (~/.factory/mcp.json)
#   - Qwen Code    (~/.qwen/settings.json)
#   - Codex CLI    (~/.codex/config.toml)
#
# Usage:
#   ./scripts/uninstall-mcps.sh [OPTIONS]
#
# Options:
#   --dry-run           Show what would be removed without making changes
#   --platform <name>   Target specific platform (can be used multiple times)
#   --all               Remove from all platforms (default if no --platform specified)
#   --list-platforms    List available platforms and exit
#   --help, -h          Show this help message
#
# Examples:
#   ./scripts/uninstall-mcps.sh --dry-run
#   ./scripts/uninstall-mcps.sh --platform opencode --platform cursor
#   ./scripts/uninstall-mcps.sh --all
# =============================================================================

set -euo pipefail

# --- Configuration ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Source utilities
source "${SCRIPT_DIR}/utils/uninstall-utils.sh"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

# --- Global Flags ---
DRY_RUN="${DRY_RUN:-0}"
PLATFORMS=()
LIST_PLATFORMS=0
SHOW_HELP=0

# --- Platform Configurations ---
declare -A PLATFORM_CONFIGS=(
    [opencode]="${HOME}/.config/opencode/opencode.json"
    [gemini-cli]="${HOME}/.gemini/settings.json"
    [antigravity]="${HOME}/.gemini/antigravity/mcp_config.json"
    [cursor]="${HOME}/.cursor/mcp.json"
    [windsurf]="${HOME}/.codeium/windsurf/mcp_config.json"
    [claude-code]="${HOME}/.claude.json"
    [kilo]="${HOME}/.kilocode/mcp.json"
    [factory]="${HOME}/.factory/mcp.json"
    [qwen]="${HOME}/.qwen/settings.json"
    [codex]="${HOME}/.codex/config.toml"
)

# Overpowers MCPs to remove
OVERPOWERS_MCPS=(
    "serena"
    "vibe-check"
    "desktop-commander"
    "hyperbrowser"
    "genkit"
    "memcord"
    "playwright-browser"
    "context7"
    "notebooklm"
)

# Config key per platform (mcpServers vs mcp)
declare -A PLATFORM_CONFIG_KEYS=(
    [opencode]="mcp"
    [gemini-cli]="mcpServers"
    [antigravity]="mcpServers"
    [cursor]="mcpServers"
    [windsurf]="mcpServers"
    [claude-code]="mcpServers"
    [kilo]="mcp"
    [factory]="mcpServers"
    [qwen]="mcpServers"
    [codex]="toml"
)

# =============================================================================
# Helper Functions
# =============================================================================

print_help() {
    cat << 'EOF'
uninstall-mcps.sh - Unified Multi-Platform MCP Server Uninstaller

USAGE:
    ./scripts/uninstall-mcps.sh [OPTIONS]

OPTIONS:
    --dry-run           Show what would be removed without making changes
    --platform <name>   Target specific platform (can be used multiple times)
                        Available: opencode, gemini-cli, antigravity, cursor,
                                   windsurf, claude-code, kilo, factory, qwen, codex
    --all               Remove from all platforms (default if no --platform specified)
    --list-platforms    List available platforms and exit
    --help, -h          Show this help message

EXAMPLES:
    # Dry run - see what would be removed
    ./scripts/uninstall-mcps.sh --dry-run

    # Remove from specific platforms
    ./scripts/uninstall-mcps.sh --platform opencode --platform cursor

    # Remove from all platforms
    ./scripts/uninstall-mcps.sh --all

NOTES:
    - Only Overpowers-installed MCPs are removed
    - User-installed MCPs are preserved
    - Backups are created before modifications
    - Config files are validated after modifications

OVERPOWERS MCPS REMOVED:
    serena, vibe-check, desktop-commander, hyperbrowser, genkit,
    memcord, playwright-browser, context7, notebooklm

EOF
}

print_banner() {
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║  ${BOLD}Overpowers MCP Server Uninstaller${NC}${CYAN}                             ║${NC}"
    echo -e "${CYAN}║  Supports: OpenCode • Antigravity • Cursor • Windsurf          ${CYAN}║${NC}"
    echo -e "${CYAN}║           Gemini CLI • Codex CLI • Claude Code • Kilo • Factory ${CYAN}║${NC}"
    echo -e "${CYAN}║           Qwen Code                                               ${CYAN}║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_platforms() {
    echo ""
    echo -e "${BOLD}Available Platforms:${NC}"
    echo ""
    for platform in "${!PLATFORM_CONFIGS[@]}"; do
        config_file="${PLATFORM_CONFIGS[${platform}]}"
        config_type="${PLATFORM_CONFIG_KEYS[${platform}]}"
        echo -e "  ${GREEN}•${NC} ${BOLD}${platform}${NC}"
        echo -e "    Config: ${DIM}${config_file}${NC}"
        echo -e "    Format: ${DIM}${config_type}${NC}"
        echo ""
    done
}

# Parse command line arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --dry-run)
                DRY_RUN=1
                export DRY_RUN
                shift
                ;;
            --platform)
                if [[ $# -lt 2 ]]; then
                    log_error "--platform requires a platform name argument"
                    exit 1
                fi
                PLATFORMS+=("$2")
                shift 2
                ;;
            --all)
                # Will be handled after parsing
                shift
                ;;
            --list-platforms)
                LIST_PLATFORMS=1
                shift
                ;;
            -h|--help)
                SHOW_HELP=1
                shift
                ;;
            *)
                log_error "Unknown argument: $1"
                echo "Use --help for usage information" >&2
                exit 1
                ;;
        esac
    done

    # If no platforms specified and not --all, default to all
    if [[ ${#PLATFORMS[@]} -eq 0 && "${LIST_PLATFORMS}" -eq 0 && "${SHOW_HELP}" -eq 0 ]]; then
        PLATFORMS=("${!PLATFORM_CONFIGS[@]}")
    fi

    # Validate platforms
    for platform in "${PLATFORMS[@]}"; do
        if [[ ! -v "PLATFORM_CONFIGS[${platform}]" ]]; then
            log_error "Unknown platform: ${platform}"
            echo "Use --list-platforms to see available platforms" >&2
            exit 1
        fi
    done
}

# =============================================================================
# MCP Removal Functions
# =============================================================================

# Remove MCPs from JSON config
remove_mcps_json() {
    local platform="$1"
    local config_file="$2"
    local config_key="$3"
    local backup_dir="$4"

    if [[ ! -f "${config_file}" ]]; then
        log_skip "Config file does not exist: ${config_file}"
        return 0
    fi

    # Backup config file
    backup_before_remove "${config_file}" "${backup_dir}" "$(basename "${config_file}")"

    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Remove Overpowers MCPs from ${config_file}"
        for mcp in "${OVERPOWERS_MCPS[@]}"; do
            log_dry "  Would remove: ${mcp}"
        done
        return 0
    fi

    python3 - "${config_file}" "${config_key}" "${OVERPOWERS_MCPS[*]}" << 'PYEOF'
import json
import sys

config_path = sys.argv[1]
config_key = sys.argv[2]
mcps_to_remove = sys.argv[3].split()

try:
    with open(config_path) as f:
        config = json.load(f)

    if config_key not in config or not isinstance(config[config_key], dict):
        print(f"SKIP: No {config_key} in config")
        sys.exit(0)

    mcps = config[config_key]
    removed = []
    skipped = []

    for mcp_name in mcps_to_remove:
        if mcp_name in mcps:
            del mcps[mcp_name]
            removed.append(mcp_name)
        else:
            skipped.append(mcp_name)

    # Write back
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
        f.write('\n')

    # Report results
    for mcp in removed:
        print(f"REMOVED:{mcp}")
    for mcp in skipped:
        print(f"SKIP:{mcp} (not found)")

    # Validate JSON
    json.dumps(config)  # Will raise if invalid
    print("VALID:JSON")

except json.JSONDecodeError as e:
    print(f"ERROR:Invalid JSON after modification: {e}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"ERROR:{str(e)}", file=sys.stderr)
    sys.exit(1)
PYEOF
}

# Remove MCPs from TOML config (Codex CLI)
remove_mcps_toml() {
    local platform="$1"
    local config_file="$2"
    local backup_dir="$3"

    if [[ ! -f "${config_file}" ]]; then
        log_skip "Config file does not exist: ${config_file}"
        return 0
    fi

    # Backup config file
    backup_before_remove "${config_file}" "${backup_dir}" "$(basename "${config_file}")"

    if [[ "${DRY_RUN}" == "1" ]]; then
        log_dry "Remove Overpowers MCPs from ${config_file} (TOML)"
        for mcp in "${OVERPOWERS_MCPS[@]}"; do
            log_dry "  Would remove: ${mcp}"
        done
        return 0
    fi

    python3 - "${config_file}" "${OVERPOWERS_MCPS[*]}" << 'PYEOF'
import sys
import re

config_path = sys.argv[1]
mcps_to_remove = sys.argv[2].split()

try:
    with open(config_path) as f:
        content = f.read()

    removed = []
    skipped = []

    for mcp_name in mcps_to_remove:
        # Remove [mcp_servers.NAME] block
        pattern = rf'\n?\[mcp_servers\.{re.escape(mcp_name)}\][\s\S]*?(?=\n\[mcp_servers\.|\Z)'

        if re.search(pattern, content):
            content = re.sub(pattern, '\n', content)
            removed.append(mcp_name)
        else:
            skipped.append(mcp_name)

    # Clean up multiple consecutive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(config_path, 'w') as f:
        f.write(content.strip() + '\n')

    # Report results
    for mcp in removed:
        print(f"REMOVED:{mcp}")
    for mcp in skipped:
        print(f"SKIP:{mcp} (not found)")

    # Validate TOML
    try:
        import tomllib
    except ImportError:
        import tomli as tomllib

    with open(config_path, 'rb') as f:
        tomllib.load(f)
    print("VALID:TOML")

except Exception as e:
    print(f"ERROR:{str(e)}", file=sys.stderr)
    sys.exit(1)
PYEOF
}

# Validate config after modification
validate_config() {
    local platform="$1"
    local config_file="$2"
    local config_type="$3"

    if [[ ! -f "${config_file}" ]]; then
        return 0
    fi

    if [[ "${config_type}" == "toml" ]]; then
        validate_toml "${config_file}"
    else
        validate_json "${config_file}"
    fi
}

# =============================================================================
# Main Uninstall Logic
# =============================================================================

uninstall_platform() {
    local platform="$1"
    local config_file="${PLATFORM_CONFIGS[${platform}]}"
    local config_key="${PLATFORM_CONFIG_KEYS[${platform}]}"
    local backup_platform="${platform}"

    echo ""
    echo -e "${CYAN}━━━ ${platform} ━━━${NC}"
    echo -e "  Config: ${DIM}${config_file}${NC}"

    # Check if config exists
    if [[ ! -f "${config_file}" ]]; then
        log_skip "Config file does not exist: ${config_file}"
        return 0
    fi

    # Initialize backup directory
    local backup_dir
    backup_dir=$(init_backup_dir "${backup_platform}")

    # Track results
    local removed_count=0
    local skipped_count=0
    local validation_failed=0

    # Remove MCPs
    local removal_output
    if [[ "${config_key}" == "toml" ]]; then
        removal_output=$(remove_mcps_toml "${platform}" "${config_file}" "${backup_dir}" 2>&1)
    else
        removal_output=$(remove_mcps_json "${platform}" "${config_file}" "${config_key}" "${backup_dir}" 2>&1)
    fi

    # Parse output
    while IFS= read -r line; do
        if [[ "${line}" == REMOVED:* ]]; then
            echo -e "    ${GREEN}[✓]${NC} Removed: ${BOLD}${line#REMOVED:}${NC}"
            removed_count=$((removed_count + 1))
        elif [[ "${line}" == SKIP:* ]]; then
            echo -e "    ${CYAN}[~]${NC} Not found: ${line#SKIP:}"
            skipped_count=$((skipped_count + 1))
        elif [[ "${line}" == VALID:* ]]; then
            echo -e "    ${GREEN}[✓]${NC} Config validated: ${line#VALID:}"
        elif [[ "${line}" == ERROR:* ]]; then
            echo -e "    ${RED}[✗]${NC} Error: ${line#ERROR:}"
            validation_failed=1
        fi
    done <<< "${removal_output}"

    # Validate config
    if [[ "${validation_failed}" -eq 0 && "${DRY_RUN}" -eq 0 ]]; then
        if ! validate_config "${platform}" "${config_file}" "${config_key}"; then
            log_error "Config validation failed: ${config_file}"
            log_warn "Backup available at: ${backup_dir}"
            return 1
        fi
    fi

    # Cleanup old backups
    if [[ "${DRY_RUN}" -eq 0 ]]; then
        cleanup_old_backups "${backup_platform}" "${BACKUP_RETENTION_COUNT}"
    fi

    echo ""
    echo -e "  Summary: ${GREEN}${removed_count} removed${NC}, ${CYAN}${skipped_count} not found${NC}"

    return 0
}

# =============================================================================
# Main Execution
# =============================================================================

main() {
    parse_args "$@"

    # Handle special flags
    if [[ "${SHOW_HELP}" -eq 1 ]]; then
        print_help
        exit 0
    fi

    if [[ "${LIST_PLATFORMS}" -eq 1 ]]; then
        print_banner
        print_platforms
        exit 0
    fi

    # Print banner
    print_banner

    # Check dry-run mode
    check_dry_run

    # Validate tools
    validate_tools || exit 1

    echo -e "${BOLD}Overpowers MCPs to remove:${NC}"
    for mcp in "${OVERPOWERS_MCPS[@]}"; do
        echo -e "  ${YELLOW}•${NC} ${mcp}"
    done
    echo ""

    echo -e "${BOLD}Target platforms:${NC}"
    for platform in "${PLATFORMS[@]}"; do
        echo -e "  ${GREEN}•${NC} ${platform}"
    done
    echo ""

    # Track overall results
    local total_removed=0
    local total_skipped=0
    local platforms_processed=0
    local platforms_failed=0

    # Process each platform
    for platform in "${PLATFORMS[@]}"; do
        if uninstall_platform "${platform}"; then
            platforms_processed=$((platforms_processed + 1))
        else
            platforms_failed=$((platforms_failed + 1))
        fi
    done

    # Print final summary
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  ${BOLD}Uninstall Complete!${NC}${GREEN}                              ${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "Platforms processed: ${GREEN}${platforms_processed}${NC}"
    if [[ ${platforms_failed} -gt 0 ]]; then
        echo -e "Platforms failed:    ${RED}${platforms_failed}${NC}"
    fi
    echo ""

    if [[ "${DRY_RUN}" -eq 1 ]]; then
        echo -e "${CYAN}[!]${NC} This was a dry run. No changes were made."
        echo -e "${CYAN}[!]${NC} Run without --dry-run to actually remove MCPs."
    else
        echo -e "${GREEN}[✓]${NC} All Overpowers MCPs have been removed."
        echo -e "${GREEN}[✓]${NC} User-installed MCPs have been preserved."
        echo ""
        echo -e "Backups saved to: ${CYAN}${BACKUP_ROOT}${NC}"
        echo -e "To restore manually: copy backup files to original locations"
    fi

    echo ""

    # Exit with error if any platforms failed
    if [[ ${platforms_failed} -gt 0 ]]; then
        exit 1
    fi

    exit 0
}

# Run main function
main "$@"
