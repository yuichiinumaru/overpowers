#!/usr/bin/env bash
# =============================================================================
# deploy-to-opencode.sh
# =============================================================================
# Creates symbolic links into OpenCode directory (~/.config/opencode/).
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "OpenCode" "${HOME}/.config/opencode"

# --- Deployment ---
print_deploy_banner

declare -a SYMLINKS=(
    "agents:agents"
    "skills:skills"
    "workflows:commands"
    "hooks:hooks"
    "AGENTS.md:AGENTS.md"
)

# Optional: themes
if [[ -d "${REPO_ROOT}/themes" ]]; then
    SYMLINKS+=("themes:themes")
else
    log_skip "No themes/ directory found in repo. Skipping."
fi

create_symlinks "${PLATFORM_DIR}" "${SYMLINKS[@]}"

# --- Summary ---
print_deploy_summary
