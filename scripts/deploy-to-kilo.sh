#!/usr/bin/env bash
# =============================================================================
# deploy-to-kilo.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into the Kilo Code
# global configuration directory (~/.kilocode/).
#
# Kilo Code discovers:
#   - Skills:    ~/.kilocode/skills/<name>/SKILL.md
#   - Workflows: ~/.kilocode/workflows/*.md
#   - Rules:     ~/.kilocode/rules/*.md
#
# Usage:
#   ./scripts/deploy-to-kilo.sh
#
# Mapping:
#   overpowers/skills/     -> ~/.kilocode/skills
#   overpowers/workflows/  -> ~/.kilocode/workflows
#   overpowers/AGENTS.md   -> ~/.kilocode/rules/OVERPOWERS.md
# =============================================================================

set -euo pipefail

# --- Configuration ---
KILO_DIR="${HOME}/.kilocode"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[✓]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[!]${NC} $*"; }
log_skip()  { echo -e "${CYAN}[~]${NC} $*"; }

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers → Kilo Code Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  Repo root:    ${GREEN}${REPO_ROOT}${NC}"
echo -e "  Kilo dir:     ${GREEN}${KILO_DIR}${NC}"
echo ""

mkdir -p "${KILO_DIR}/skills"
mkdir -p "${KILO_DIR}/workflows"
mkdir -p "${KILO_DIR}/rules"

# --- Define symlink mappings ---
declare -a SYMLINKS=(
    "skills:skills"
    "workflows:workflows"
)

source "${SCRIPT_DIR}/utils/create-symlinks.sh"
create_symlinks "${KILO_DIR}" "${SYMLINKS[@]}"

# --- Rules (Special handling for AGENTS.md) ---
AGENTS_MD="${REPO_ROOT}/AGENTS.md"
KILO_RULES_MD="${KILO_DIR}/rules/OVERPOWERS.md"

if [[ -f "${AGENTS_MD}" ]]; then
    if [[ -L "${KILO_RULES_MD}" ]]; then
        rm "${KILO_RULES_MD}"
    elif [[ -e "${KILO_RULES_MD}" ]]; then
        mv "${KILO_RULES_MD}" "${KILO_RULES_MD}.bak"
    fi
    ln -s "${AGENTS_MD}" "${KILO_RULES_MD}"
    log_info "rules/OVERPOWERS.md -> ${AGENTS_MD}"
fi

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Deployment complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo ""
