#!/usr/bin/env bash
# =============================================================================
# deploy-to-codex.sh
# =============================================================================
# Creates symbolic links into Codex CLI directory.
# =============================================================================

set -euo pipefail

CODEX_DIR="${HOME}/.codex"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

source "${SCRIPT_DIR}/utils/create-symlinks.sh"

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers → Codex CLI Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""

mkdir -p "${CODEX_DIR}"
declare -a SYMLINKS=(
    "skills:skills"
)
create_symlinks "${CODEX_DIR}" "${SYMLINKS[@]}"

# Handle AGENTS.md -> AGENTS.MD
if [[ -f "${REPO_ROOT}/AGENTS.md" ]]; then
    if [[ -L "${CODEX_DIR}/AGENTS.MD" ]]; then
        rm "${CODEX_DIR}/AGENTS.MD"
    elif [[ -e "${CODEX_DIR}/AGENTS.MD" ]]; then
        mv "${CODEX_DIR}/AGENTS.MD" "${CODEX_DIR}/AGENTS.MD.bak"
    fi
    ln -s "${REPO_ROOT}/AGENTS.md" "${CODEX_DIR}/AGENTS.MD"
    log_info "AGENTS.MD -> ${REPO_ROOT}/AGENTS.md"
fi

echo ""
echo -e "${GREEN}  Codex CLI Deployment complete!${NC}"
echo ""
