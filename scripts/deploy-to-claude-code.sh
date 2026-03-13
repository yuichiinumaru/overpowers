#!/usr/bin/env bash
# =============================================================================
# deploy-to-claude-code.sh
# =============================================================================
# Creates symbolic links into Claude Code directory.
# =============================================================================

set -euo pipefail

CLAUDE_DIR="${HOME}/.claude"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

source "${SCRIPT_DIR}/utils/create-symlinks.sh"

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers → Claude Code Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""

mkdir -p "${CLAUDE_DIR}"
declare -a SYMLINKS=(
    "skills:skills"
    "workflows/toml:commands"
)
create_symlinks "${CLAUDE_DIR}" "${SYMLINKS[@]}"

if [[ -f "${REPO_ROOT}/AGENTS.md" ]]; then
    if [[ -L "${CLAUDE_DIR}/CLAUDE.md" ]]; then
        rm "${CLAUDE_DIR}/CLAUDE.md"
    elif [[ -e "${CLAUDE_DIR}/CLAUDE.md" ]]; then
        mv "${CLAUDE_DIR}/CLAUDE.md" "${CLAUDE_DIR}/CLAUDE.md.bak"
    fi
    ln -s "${REPO_ROOT}/AGENTS.md" "${CLAUDE_DIR}/CLAUDE.md"
    log_info "CLAUDE.md -> ${REPO_ROOT}/AGENTS.md"
fi

echo ""
echo -e "${GREEN}  Claude Code Deployment complete!${NC}"
echo ""
