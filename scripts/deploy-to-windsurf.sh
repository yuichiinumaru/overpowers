#!/usr/bin/env bash
# =============================================================================
# deploy-to-windsurf.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into Windsurf
# Note: Windsurf reads skills from ~/.agents/skills
# =============================================================================

set -euo pipefail

WINDSURF_DIR="${HOME}/.codeium/windsurf"
AGENTS_DIR="${HOME}/.agents"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

source "${SCRIPT_DIR}/utils/create-symlinks.sh"

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers → Windsurf Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""

mkdir -p "${AGENTS_DIR}"
declare -a SYMLINKS=(
    "skills:skills"
)

create_symlinks "${AGENTS_DIR}" "${SYMLINKS[@]}"

echo ""
echo -e "${GREEN}  Windsurf Deployment complete! (using ~/.agents/)${NC}"
echo ""
