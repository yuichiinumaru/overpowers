#!/usr/bin/env bash
# =============================================================================
# deploy-to-antigravity.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into the Antigravity
# global configuration directory (~/.gemini/antigravity/).
#
# Antigravity discovers:
#   - Skills:    ~/.gemini/antigravity/skills/<name>/SKILL.md
#   - Workflows: ~/.gemini/antigravity/global_workflows/
#   - Rules:     via ~/.gemini/GEMINI.md (shared with Gemini CLI)
#
# Usage:
#   ./scripts/deploy-to-antigravity.sh
#
# Mapping:
#   overpowers/skills/     -> ~/.gemini/antigravity/skills
#   overpowers/workflows/  -> ~/.gemini/antigravity/global_workflows
# =============================================================================

set -euo pipefail

# --- Configuration ---
ANTIGRAVITY_DIR="${HOME}/.gemini/antigravity"
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
echo -e "${CYAN}  Overpowers → Antigravity Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  Repo root:        ${GREEN}${REPO_ROOT}${NC}"
echo -e "  Antigravity dir:  ${GREEN}${ANTIGRAVITY_DIR}${NC}"
echo ""

mkdir -p "${ANTIGRAVITY_DIR}"

# --- Define symlink mappings ---
declare -a SYMLINKS=(
    "skills:skills"
    "workflows:global_workflows"
)

for mapping in "${SYMLINKS[@]}"; do
    SRC_REL="${mapping%%:*}"
    TGT_NAME="${mapping##*:}"
    SRC_ABS="${REPO_ROOT}/${SRC_REL}"
    TGT_ABS="${ANTIGRAVITY_DIR}/${TGT_NAME}"

    if [[ ! -e "${SRC_ABS}" ]]; then
        log_warn "Source not found: ${SRC_ABS}. Skipping."
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
        ln -s "${SRC_ABS}" "${TGT_ABS}"
        log_info "${TGT_NAME} -> ${SRC_ABS}"
    elif [[ -e "${TGT_ABS}" ]]; then
        if [[ "${FAST_MODE:-0}" == "1" ]]; then
            log_warn "${TGT_ABS} exists as a real file/directory. Fast mode: Backing up to ${TGT_ABS}.bak"
            mv "${TGT_ABS}" "${TGT_ABS}.bak"
            ln -s "${SRC_ABS}" "${TGT_ABS}"
            log_info "${TGT_NAME} -> ${SRC_ABS}"
        else
            echo -e "  ${YELLOW}Conflict detected:${NC} ${TGT_ABS} already exists."
            echo -e "  How would you like to handle this?"
            echo -e "    ${GREEN}m)${NC} Merge    (Copy your existing assets to Overpowers, then symlink)"
            echo -e "    ${GREEN}r)${NC} Replace  (Backup existing to .bak, then symlink Overpowers)"
            echo -e "    ${GREEN}c)${NC} Copy     (Copy Overpowers to your directory, no symlink)"
            echo -e "    ${GREEN}s)${NC} Skip     (Leave existing untouched)"
            read -rp "  Choose [m/r/c/s]: " conflict_choice

            case "${conflict_choice}" in
                m|M)
                    log_info "Merging existing contents into ${SRC_ABS}..."
                    cp -R "${TGT_ABS}"/* "${SRC_ABS}"/ 2>/dev/null || true
                    rm -rf "${TGT_ABS}"
                    ln -s "${SRC_ABS}" "${TGT_ABS}"
                    log_info "${TGT_NAME} merged and symlinked."
                    ;;
                r|R)
                    log_warn "Backing up to ${TGT_ABS}.bak"
                    mv "${TGT_ABS}" "${TGT_ABS}.bak"
                    ln -s "${SRC_ABS}" "${TGT_ABS}"
                    log_info "${TGT_NAME} -> ${SRC_ABS}"
                    ;;
                c|C)
                    log_info "Copying Overpowers contents into ${TGT_ABS}..."
                    cp -R "${SRC_ABS}"/* "${TGT_ABS}"/ 2>/dev/null || true
                    log_info "${TGT_NAME} updated via copy."
                    ;;
                *)
                    log_skip "Skipping ${TGT_NAME}."
                    ;;
            esac
        fi
    else
        ln -s "${SRC_ABS}" "${TGT_ABS}"
        log_info "${TGT_NAME} -> ${SRC_ABS}"
    fi
done

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Deployment complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo ""
echo "Current symlinks in ${ANTIGRAVITY_DIR}:"
ls -la "${ANTIGRAVITY_DIR}" | grep "^l" || echo "  (none)"
echo ""
echo -e "${CYAN}Antigravity will now discover:${NC}"
echo -e "  • ${GREEN}$(find "${REPO_ROOT}/skills" -name 'SKILL.md' 2>/dev/null | wc -l)${NC} skills"
echo -e "  • ${GREEN}$(find "${REPO_ROOT}/workflows" -name '*.md' 2>/dev/null | wc -l)${NC} workflows"
echo ""
echo -e "${YELLOW}NOTE:${NC} For MCP servers, run ${CYAN}./scripts/install-mcps.sh${NC} instead."
echo ""
