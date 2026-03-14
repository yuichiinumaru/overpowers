#!/usr/bin/env bash
# =============================================================================
# deploy-to-codex.sh
# =============================================================================
# Creates symbolic links into Codex CLI directory.
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "Codex CLI" "${HOME}/.codex"

# --- Deployment ---
print_deploy_banner

declare -a SYMLINKS=(
    "skills:skills"
)
create_symlinks "${PLATFORM_DIR}" "${SYMLINKS[@]}"

# --- Special Handling: AGENTS.md -> AGENTS.MD ---
if [[ -f "${REPO_ROOT}/AGENTS.md" ]]; then
    AGENTS_MD="${REPO_ROOT}/AGENTS.md"
    CODEX_RULES_MD="${PLATFORM_DIR}/AGENTS.MD"
    
    if [[ -L "${CODEX_RULES_MD}" ]]; then
        rm "${CODEX_RULES_MD}"
    elif [[ -e "${CODEX_RULES_MD}" ]]; then
        mv "${CODEX_RULES_MD}" "${CODEX_RULES_MD}.bak"
    fi
    ln -s "${AGENTS_MD}" "${CODEX_RULES_MD}"
    log_info "AGENTS.MD -> ${AGENTS_MD}"
fi

# --- Summary ---
print_deploy_summary
