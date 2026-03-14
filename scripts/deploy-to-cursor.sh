#!/usr/bin/env bash
# =============================================================================
# deploy-to-cursor.sh
# =============================================================================
# Creates symbolic links into Cursor configuration directory (~/.cursor/).
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "Cursor" "${HOME}/.cursor"

# --- Deployment ---
print_deploy_banner

declare -a SYMLINKS=(
    "skills:skills"
)

create_symlinks "${PLATFORM_DIR}" "${SYMLINKS[@]}"

# --- Summary ---
print_deploy_summary
