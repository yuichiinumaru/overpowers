#!/usr/bin/env bash
# =============================================================================
# deploy-to-opencode.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into the OpenCode
# global configuration directory (~/.config/opencode/).
#
# This allows all agents, skills, commands (from workflows), hooks, and themes
# defined in the Overpowers repo to be automatically discovered by OpenCode
# without manual copying.
#
# Usage:
#   ./scripts/deploy-to-opencode.sh
#
# What it does:
#   1. Detects the Overpowers repo root (where this script lives).
#   2. Removes any stale/broken symlinks in ~/.config/opencode/.
#   3. Creates fresh absolute symlinks for each asset type.
#   4. Optionally symlinks AGENTS.md as the global rules file.
#
# Mapping:
#   overpowers/agents/     -> ~/.config/opencode/agents
#   overpowers/skills/     -> ~/.config/opencode/skills
#   overpowers/workflows/  -> ~/.config/opencode/commands   (opencode calls them "commands")
#   overpowers/hooks/      -> ~/.config/opencode/hooks
#   overpowers/themes/     -> ~/.config/opencode/themes     (created empty if missing)
#   overpowers/AGENTS.md   -> ~/.config/opencode/AGENTS.md  (global rules)
# =============================================================================

set -euo pipefail

# --- Configuration ---
OPENCODE_DIR="${HOME}/.config/opencode"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

log_info()  { echo -e "${GREEN}[✓]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[!]${NC} $*"; }
log_skip()  { echo -e "${CYAN}[~]${NC} $*"; }
log_error() { echo -e "${RED}[✗]${NC} $*"; }

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers → OpenCode Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  Repo root:    ${GREEN}${REPO_ROOT}${NC}"
echo -e "  OpenCode dir: ${GREEN}${OPENCODE_DIR}${NC}"
echo ""

# --- Ensure opencode config dir exists ---
mkdir -p "${OPENCODE_DIR}"

# --- Define symlink mappings ---
# Format: "source_relative:target_name"
declare -a SYMLINKS=(
    "agents:agents"
    "skills:skills"
    "workflows:commands"
    "hooks:hooks"
    "AGENTS.md:AGENTS.md"
)

# --- Optional: themes (create dir in repo if missing) ---
if [[ -d "${REPO_ROOT}/themes" ]]; then
    SYMLINKS+=("themes:themes")
else
    log_skip "No themes/ directory found in repo. Skipping. (Create one and re-run to deploy.)"
fi

# --- Process each symlink ---
for mapping in "${SYMLINKS[@]}"; do
    SRC_REL="${mapping%%:*}"
    TGT_NAME="${mapping##*:}"

    SRC_ABS="${REPO_ROOT}/${SRC_REL}"
    TGT_ABS="${OPENCODE_DIR}/${TGT_NAME}"

    # Check if source exists
    if [[ ! -e "${SRC_ABS}" ]]; then
        log_warn "Source not found: ${SRC_ABS}. Skipping ${TGT_NAME}."
        continue
    fi

    # Remove existing symlink or warn about existing real dir
    if [[ -L "${TGT_ABS}" ]]; then
        CURRENT_TARGET="$(readlink -f "${TGT_ABS}" 2>/dev/null || echo '<broken>')"
        if [[ "${CURRENT_TARGET}" == "${SRC_ABS}" ]]; then
            log_skip "${TGT_NAME} already points to the correct source. Skipping."
            continue
        fi
        log_warn "Removing stale symlink: ${TGT_ABS} -> ${CURRENT_TARGET}"
        rm "${TGT_ABS}"
    elif [[ -e "${TGT_ABS}" ]]; then
        log_warn "${TGT_ABS} exists as a real file/directory. Backing up to ${TGT_ABS}.bak"
        mv "${TGT_ABS}" "${TGT_ABS}.bak"
    fi

    # Create symlink
    ln -s "${SRC_ABS}" "${TGT_ABS}"
    log_info "${TGT_NAME} -> ${SRC_ABS}"
done

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Deployment complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo ""

# --- Summary ---
echo "Current symlinks in ${OPENCODE_DIR}:"
ls -la "${OPENCODE_DIR}" | grep "^l" || echo "  (none)"
echo ""
