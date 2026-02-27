#!/usr/bin/env bash
# =============================================================================
# deploy-to-gemini-cli.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into the Gemini CLI
# global configuration directory (~/.gemini/).
#
# Gemini CLI discovers skills from:
#   - User skills:  ~/.gemini/skills/<name>/SKILL.md
#   - Or alias:     ~/.agents/skills/<name>/SKILL.md
#   - Global rules: ~/.gemini/GEMINI.md
#
# This script symlinks overpowers assets so Gemini CLI can use them globally.
#
# Usage:
#   ./scripts/deploy-to-gemini-cli.sh
#
# Mapping:
#   overpowers/skills/     -> ~/.gemini/skills
#   overpowers/AGENTS.md   -> ~/.gemini/GEMINI.md   (global context/rules)
#   overpowers/hooks/      -> ~/.gemini/hooks        (if hooks are enabled)
# =============================================================================

set -euo pipefail

# --- Configuration ---
GEMINI_DIR="${HOME}/.gemini"
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
log_error() { echo -e "${RED}[✗]${NC} $*"; }

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers → Gemini CLI Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  Repo root:     ${GREEN}${REPO_ROOT}${NC}"
echo -e "  Gemini CLI dir: ${GREEN}${GEMINI_DIR}${NC}"
echo ""

# --- Ensure gemini config dir exists ---
mkdir -p "${GEMINI_DIR}"

# --- Define symlink mappings ---
# Format: "source_relative:target_name"
# Note: Gemini CLI uses GEMINI.md (not AGENTS.md) for global context
declare -a SYMLINKS=(
    "skills:skills"
    "hooks:hooks"
)

# --- Process main symlinks ---
for mapping in "${SYMLINKS[@]}"; do
    SRC_REL="${mapping%%:*}"
    TGT_NAME="${mapping##*:}"

    SRC_ABS="${REPO_ROOT}/${SRC_REL}"
    TGT_ABS="${GEMINI_DIR}/${TGT_NAME}"

    if [[ ! -e "${SRC_ABS}" ]]; then
        log_warn "Source not found: ${SRC_ABS}. Skipping ${TGT_NAME}."
        continue
    fi

    if [[ -L "${TGT_ABS}" ]]; then
        CURRENT_TARGET="$(readlink -f "${TGT_ABS}" 2>/dev/null || echo '<broken>')"
        if [[ "${CURRENT_TARGET}" == "${SRC_ABS}" ]]; then
            log_skip "${TGT_NAME} already points to the correct source."
            continue
        fi
        log_warn "Removing stale symlink: ${TGT_ABS} -> ${CURRENT_TARGET}"
        rm "${TGT_ABS}"
    elif [[ -e "${TGT_ABS}" ]]; then
        log_warn "${TGT_ABS} exists as a real file/directory. Backing up to ${TGT_ABS}.bak"
        mv "${TGT_ABS}" "${TGT_ABS}.bak"
    fi

    ln -s "${SRC_ABS}" "${TGT_ABS}"
    log_info "${TGT_NAME} -> ${SRC_ABS}"
done

# --- GEMINI.md (special handling) ---
# Gemini CLI reads ~/.gemini/GEMINI.md but our repo has AGENTS.md
# We symlink AGENTS.md -> GEMINI.md
GEMINI_MD="${GEMINI_DIR}/GEMINI.md"
AGENTS_MD="${REPO_ROOT}/AGENTS.md"

if [[ -f "${AGENTS_MD}" ]]; then
    if [[ -L "${GEMINI_MD}" ]]; then
        CURRENT="$(readlink -f "${GEMINI_MD}" 2>/dev/null || echo '<broken>')"
        if [[ "${CURRENT}" == "${AGENTS_MD}" ]]; then
            log_skip "GEMINI.md already points to AGENTS.md."
        else
            log_warn "Removing stale symlink: GEMINI.md -> ${CURRENT}"
            rm "${GEMINI_MD}"
            ln -s "${AGENTS_MD}" "${GEMINI_MD}"
            log_info "GEMINI.md -> ${AGENTS_MD}"
        fi
    elif [[ -e "${GEMINI_MD}" ]]; then
        log_warn "GEMINI.md exists. Backing up to GEMINI.md.bak"
        mv "${GEMINI_MD}" "${GEMINI_MD}.bak"
        ln -s "${AGENTS_MD}" "${GEMINI_MD}"
        log_info "GEMINI.md -> ${AGENTS_MD}"
    else
        ln -s "${AGENTS_MD}" "${GEMINI_MD}"
        log_info "GEMINI.md -> ${AGENTS_MD}"
    fi
else
    log_warn "AGENTS.md not found in repo. Skipping GEMINI.md link."
fi

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Deployment complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo ""

# --- Summary ---
echo "Current symlinks in ${GEMINI_DIR}:"
ls -la "${GEMINI_DIR}" | grep "^l" || echo "  (none)"
echo ""
echo -e "${CYAN}Gemini CLI will now discover:${NC}"
echo -e "  • ${GREEN}$(find "${REPO_ROOT}/skills" -name 'SKILL.md' 2>/dev/null | wc -l)${NC} skills from overpowers/skills/"
echo -e "  • Global rules from ${GREEN}AGENTS.md${NC} (as GEMINI.md)"
echo ""
