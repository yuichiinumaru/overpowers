#!/usr/bin/env bash
# =============================================================================
# deploy-to-factory.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into Factory.
# Note: Factory reads skills from ~/.agents/skills
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "Factory" "${HOME}/.factory"

# --- Deployment ---
print_deploy_banner

# 1. Base skills (Factory specific path)
AGENTS_DIR="${HOME}/.agents"
mkdir -p "${AGENTS_DIR}"
declare -a SYMLINKS=("skills:skills")
create_symlinks "${AGENTS_DIR}" "${SYMLINKS[@]}"

# 2. Droids (Workflows) 
declare -a FACTORY_LINKS=("workflows/toml:droids")
create_symlinks "${PLATFORM_DIR}" "${FACTORY_LINKS[@]}"

# 3. Rules Handling
if [[ -f "${REPO_ROOT}/AGENTS.md" ]]; then
    AGENTS_MD="${REPO_ROOT}/AGENTS.md"
    FACTORY_RULES_MD="${PLATFORM_DIR}/AGENTS.md"
    
    if [[ -L "${FACTORY_RULES_MD}" ]]; then
        rm "${FACTORY_RULES_MD}"
    elif [[ -e "${FACTORY_RULES_MD}" ]]; then
        mv "${FACTORY_RULES_MD}" "${FACTORY_RULES_MD}.bak"
    fi
    ln -s "${AGENTS_MD}" "${FACTORY_RULES_MD}"
    log_info "AGENTS.md -> ${AGENTS_MD}"
fi

# --- Summary ---
print_deploy_summary
