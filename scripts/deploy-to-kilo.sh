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

for mapping in "${SYMLINKS[@]}"; do
    SRC_REL="${mapping%%:*}"
    TGT_NAME="${mapping##*:}"
    SRC_ABS="${REPO_ROOT}/${SRC_REL}"
    TGT_ABS="${KILO_DIR}/${TGT_NAME}"

    if [[ ! -e "${SRC_ABS}" ]]; then
        log_warn "Source not found: ${SRC_ABS}. Skipping."
        continue
    fi

    if [[ -L "${TGT_ABS}" ]]; then
        CURRENT="$(readlink -f "${TGT_ABS}" 2>/dev/null || echo '<broken>')"
        if [[ "${CURRENT}" == "${SRC_ABS}" ]]; then
            log_skip "${TGT_NAME} already correct."
            continue
        fi
        log_warn "Removing stale symlink: ${TGT_ABS}"
        rm "${TGT_ABS}"
    elif [[ -e "${TGT_ABS}" ]]; then
        if [[ "${OVERPOWERS_CONFLICT_POLICY:-replace}" == "copy" ]]; then
            if [[ -d "${SRC_ABS}" ]]; then
                log_info "Merging assets into existing directory: ${TGT_ABS}"
                mkdir -p "${TGT_ABS}"
                cp -rn "${SRC_ABS}/"* "${TGT_ABS}/" 2>/dev/null || true
            else
                log_info "File already exists, skipping: ${TGT_ABS}"
            fi
            continue
        else
            log_warn "${TGT_ABS} exists. Backing up to ${TGT_ABS}.bak"
            mv "${TGT_ABS}" "${TGT_ABS}.bak"
        fi
    fi

    if [[ "${OVERPOWERS_CONFLICT_POLICY:-replace}" == "copy" ]]; then
        cp -r "${SRC_ABS}" "${TGT_ABS}"
        log_info "${TGT_NAME} (copied) <- ${SRC_ABS}"
    else
        ln -s "${SRC_ABS}" "${TGT_ABS}"
        log_info "${TGT_NAME} (symlinked) -> ${SRC_ABS}"
    fi
done

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
