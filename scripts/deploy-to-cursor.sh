#!/usr/bin/env bash
# =============================================================================
# deploy-to-cursor.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into the Cursor
# global configuration directory (~/.cursor/).
# =============================================================================

set -euo pipefail

CURSOR_DIR="${HOME}/.cursor"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

source "${SCRIPT_DIR}/utils/create-symlinks.sh"

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers → Cursor Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""

mkdir -p "${CURSOR_DIR}"
declare -a SYMLINKS=(
    "skills:skills"
)

create_symlinks "${CURSOR_DIR}" "${SYMLINKS[@]}"

echo ""
echo -e "${GREEN}  Cursor Deployment complete!${NC}"
echo ""
