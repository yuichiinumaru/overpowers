#!/usr/bin/env bash
# =============================================================================
# deploy-to-antigravity.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into the Antigravity
# global configuration directory (~/.gemini/antigravity/).
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "Antigravity" "${HOME}/.gemini/antigravity"

# --- Deployment ---
print_deploy_banner

declare -a SYMLINKS=(
    "skills:skills"
    "workflows:global_workflows"
)

create_symlinks "${PLATFORM_DIR}" "${SYMLINKS[@]}"

# --- Cleanup & Summary ---
print_deploy_summary

echo -e "${CYAN}Antigravity will now discover:${NC}"
echo -e "  • ${GREEN}$(find "${REPO_ROOT}/skills" -name 'SKILL.md' 2>/dev/null | wc -l)${NC} skills"
echo -e "  • ${GREEN}$(find "${REPO_ROOT}/workflows" -name '*.md' 2>/dev/null | wc -l)${NC} workflows"
echo ""
echo -e "${YELLOW}NOTE:${NC} For MCP servers, run ${CYAN}./scripts/install-mcps.sh${NC} instead."
echo ""
