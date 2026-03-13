#!/usr/bin/env bash
# =============================================================================
# deploy-to-factory.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into Factory
# Note: Factory reads skills from ~/.agents/skills
# =============================================================================

set -euo pipefail

FACTORY_DIR="${HOME}/.factory"
AGENTS_DIR="${HOME}/.agents"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

source "${SCRIPT_DIR}/utils/create-symlinks.sh"

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers → Factory Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""

mkdir -p "${FACTORY_DIR}"
mkdir -p "${AGENTS_DIR}"

# 1. Base skills
declare -a SYMLINKS=("skills:skills")
create_symlinks "${AGENTS_DIR}" "${SYMLINKS[@]}"

# 2. Droids (Workflows) 
# Note: map workflows to droids
declare -a FACTORY_LINKS=("workflows/toml:droids")
create_symlinks "${FACTORY_DIR}" "${FACTORY_LINKS[@]}"

# 3. Handle AGENTS.md -> AGENTS.md
if [[ -f "${REPO_ROOT}/AGENTS.md" ]]; then
    if [[ -L "${FACTORY_DIR}/AGENTS.md" ]]; then
        rm "${FACTORY_DIR}/AGENTS.md"
    elif [[ -e "${FACTORY_DIR}/AGENTS.md" ]]; then
        mv "${FACTORY_DIR}/AGENTS.md" "${FACTORY_DIR}/AGENTS.md.bak"
    fi
    ln -s "${REPO_ROOT}/AGENTS.md" "${FACTORY_DIR}/AGENTS.md"
    log_info "AGENTS.md -> ${REPO_ROOT}/AGENTS.md"
fi

echo ""
echo -e "${GREEN}  Factory Deployment complete!${NC}"
echo ""
