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
source "${SCRIPT_DIR}/utils/create-symlinks.sh"
create_symlinks "${OPENCODE_DIR}" "${SYMLINKS[@]}"

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Deployment complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo ""

# --- Summary ---
echo "Current symlinks in ${OPENCODE_DIR}:"
ls -la "${OPENCODE_DIR}" | grep "^l" || echo "  (none)"
echo ""
