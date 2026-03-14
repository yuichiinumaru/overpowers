#!/usr/bin/env bash
# =============================================================================
# deploy-to-kilo.sh
# =============================================================================
# Creates symbolic links into Kilo Code directory (~/.kilocode/).
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "Kilo Code" "${HOME}/.kilocode"

# --- Deployment ---
print_deploy_banner

mkdir -p "${PLATFORM_DIR}/skills"
mkdir -p "${PLATFORM_DIR}/workflows"
mkdir -p "${PLATFORM_DIR}/rules"

declare -a SYMLINKS=(
    "skills:skills"
    "workflows:workflows"
)

create_symlinks "${PLATFORM_DIR}" "${SYMLINKS[@]}"

# --- Rules Handling ---
if [[ -f "${REPO_ROOT}/AGENTS.md" ]]; then
    AGENTS_MD="${REPO_ROOT}/AGENTS.md"
    KILO_RULES_MD="${PLATFORM_DIR}/rules/OVERPOWERS.md"
    
    if [[ -L "${KILO_RULES_MD}" ]]; then
        rm "${KILO_RULES_MD}"
    elif [[ -e "${KILO_RULES_MD}" ]]; then
        mv "${KILO_RULES_MD}" "${KILO_RULES_MD}.bak"
    fi
    ln -s "${AGENTS_MD}" "${KILO_RULES_MD}"
    log_info "rules/OVERPOWERS.md -> ${AGENTS_MD}"
fi

# --- Summary ---
print_deploy_summary
