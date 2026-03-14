#!/usr/bin/env bash
# =============================================================================
# deploy-to-windsurf.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into Windsurf.
# Note: Windsurf reads skills from ~/.agents/skills
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "Windsurf" "${HOME}/.codeium/windsurf"

# --- Deployment ---
print_deploy_banner

# Windsurf uses ~/.agents for skills
AGENTS_DIR="${HOME}/.agents"
mkdir -p "${AGENTS_DIR}"
declare -a SYMLINKS=(
    "skills:skills"
)

create_symlinks "${AGENTS_DIR}" "${SYMLINKS[@]}"

# --- Summary ---
print_deploy_summary "${AGENTS_DIR}"
