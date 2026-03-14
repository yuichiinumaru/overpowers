#!/usr/bin/env bash
# =============================================================================
# deploy-to-claude-code.sh
# =============================================================================
# Creates symbolic links into Claude Code directory.
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "Claude Code" "${HOME}/.claude"

# --- Deployment ---
print_deploy_banner

declare -a SYMLINKS=(
    "skills:skills"
    "workflows/toml:commands"
)
create_symlinks "${PLATFORM_DIR}" "${SYMLINKS[@]}"

# --- Special Handling: AGENTS.md -> CLAUDE.md ---
if [[ -f "${REPO_ROOT}/AGENTS.md" ]]; then
    AGENTS_MD="${REPO_ROOT}/AGENTS.md"
    CLAUDE_MD="${PLATFORM_DIR}/CLAUDE.md"
    
    if [[ -L "${CLAUDE_MD}" ]]; then
        rm "${CLAUDE_MD}"
    elif [[ -e "${CLAUDE_MD}" ]]; then
        mv "${CLAUDE_MD}" "${CLAUDE_MD}.bak"
    fi
    ln -s "${AGENTS_MD}" "${CLAUDE_MD}"
    log_info "CLAUDE.md -> ${AGENTS_MD}"
fi

# --- Summary ---
print_deploy_summary
