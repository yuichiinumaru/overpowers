#!/usr/bin/env bash
# =============================================================================
#  ██████  ██    ██ ███████ ██████  ██████   ██████  ██     ██ ███████ ██████  ███████
# ██    ██ ██    ██ ██      ██   ██ ██   ██ ██    ██ ██     ██ ██      ██   ██ ██
# ██    ██ ██    ██ █████   ██████  ██████  ██    ██ ██  █  ██ █████   ██████  ███████
# ██    ██  ██  ██  ██      ██   ██ ██      ██    ██ ██ ███ ██ ██      ██   ██      ██
#  ██████    ████   ███████ ██   ██ ██       ██████   ███ ███  ███████ ██   ██ ███████
#
# install.sh — Master Installer
# =============================================================================
# Interactive installer that deploys Overpowers assets (agents, skills,
# workflows, hooks) to your AI coding tools and optionally configures MCP
# servers across all platforms.
#
# Supported platforms:
#   • OpenCode     (~/.config/opencode/)
#   • Gemini CLI   (~/.gemini/)
#   • Antigravity  (~/.gemini/antigravity/)
#
# Usage:
#   ./install.sh
# =============================================================================

set -euo pipefail

FAST_MODE=0
ENV_FILE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -f|--fast)
      FAST_MODE=1
      export FAST_MODE=1
      shift
      ;;
    -e|--env)
      ENV_FILE="$2"
      shift 2
      ;;
    *)
      echo "Usage: $0 [-f|--fast] [-e|--env <file>]" >&2
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

# =============================================================================
# Banner
# =============================================================================
clear 2>/dev/null || true
echo ""
echo -e "${MAGENTA}  ██████  ██    ██ ███████ ██████  ██████   ██████  ██     ██ ███████ ██████  ███████${NC}"
echo -e "${MAGENTA} ██    ██ ██    ██ ██      ██   ██ ██   ██ ██    ██ ██     ██ ██      ██   ██ ██     ${NC}"
echo -e "${MAGENTA} ██    ██ ██    ██ █████   ██████  ██████  ██    ██ ██  █  ██ █████   ██████  ███████${NC}"
echo -e "${MAGENTA} ██    ██  ██  ██  ██      ██   ██ ██      ██    ██ ██ ███ ██ ██      ██   ██      ██${NC}"
echo -e "${MAGENTA}  ██████    ████   ███████ ██   ██ ██       ██████   ███ ███  ███████ ██   ██ ███████${NC}"
echo ""
echo -e "${DIM}  Based on Superpowers by Jesse Vincent • Maintained by Yuichi Inumaru${NC}"
echo ""
echo -e "${CYAN}╔═══════════════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  ${BOLD}Master Installer${NC}${CYAN}                                                              ║${NC}"
echo -e "${CYAN}║  Deploy agents, skills, workflows, hooks & MCP servers to your AI tools.     ║${NC}"
echo -e "${CYAN}║  Integrates with OpenCode, Gemini CLI, Antigravity, & Kilo Code subagent.    ║${NC}"
echo -e "${CYAN}╚═══════════════════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${BOLD}What this does:${NC}"
echo -e "    This script deploys Overpowers assets (agents, skills, workflows, hooks)"
echo -e "    to your local AI tool configuration directories. If you already have"
echo -e "    existing assets, you will be prompted to merge, replace, or copy them."
echo ""
echo -e "  ${YELLOW}${BOLD}Privacy Disclaimer:${NC}${YELLOW} Overpowers runs entirely locally. It does NOT collect,${NC}"
echo -e "  ${YELLOW}track, or upload your personal assets to any external servers.${NC}"
echo ""

# =============================================================================
# Inventory
# =============================================================================
SKILL_COUNT=$(find "${SCRIPT_DIR}/skills" -name 'SKILL.md' 2>/dev/null | wc -l)
AGENT_COUNT=$(find "${SCRIPT_DIR}/agents" -name '*.md' 2>/dev/null | wc -l)
WORKFLOW_COUNT=$(find "${SCRIPT_DIR}/workflows" -name '*.md' 2>/dev/null | wc -l)
HOOK_COUNT=$(find "${SCRIPT_DIR}/hooks" -name '*.md' 2>/dev/null | wc -l)

echo -e "  ${BOLD}Repository inventory:${NC}"
echo -e "    ${GREEN}${AGENT_COUNT}${NC} agents  •  ${GREEN}${SKILL_COUNT}${NC} skills  •  ${GREEN}${WORKFLOW_COUNT}${NC} workflows  •  ${GREEN}${HOOK_COUNT}${NC} hooks"
echo ""

# =============================================================================
# Platform selection
# =============================================================================
declare -a SELECTED_PLATFORMS=()

if [[ "${FAST_MODE}" == "1" ]]; then
    echo -e "  ${CYAN}Running in FAST MODE (-f). Auto-selecting all platforms.${NC}"
    SELECTED_PLATFORMS=("opencode" "gemini" "antigravity")
else
    echo -e "  ${BOLD}Which platforms do you want to deploy to?${NC}"
    echo ""
    echo -e "    ${GREEN}1)${NC} OpenCode       ${DIM}(agents, skills, commands, hooks, AGENTS.md)${NC}"
    echo -e "    ${GREEN}2)${NC} Gemini CLI     ${DIM}(skills, hooks, GEMINI.md)${NC}"
    echo -e "    ${GREEN}3)${NC} Antigravity    ${DIM}(skills, workflows)${NC}"
    echo -e "    ${GREEN}4)${NC} All platforms"
    echo -e "    ${GREEN}q)${NC} Quit"
    echo ""
    read -rp "  Choose [1/2/3/4/q]: " platform_choice

    case "${platform_choice}" in
        1) SELECTED_PLATFORMS=("opencode") ;;
        2) SELECTED_PLATFORMS=("gemini") ;;
        3) SELECTED_PLATFORMS=("antigravity") ;;
        4) SELECTED_PLATFORMS=("opencode" "gemini" "antigravity") ;;
        q|Q) echo -e "\n  ${DIM}Bye!${NC}"; exit 0 ;;
        *) echo -e "${RED}Invalid choice${NC}"; exit 1 ;;
    esac
fi

# =============================================================================
# Deploy assets per platform
# =============================================================================
echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Phase 1: Deploying assets (agents, skills, workflows)${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

for platform in "${SELECTED_PLATFORMS[@]}"; do
    case "${platform}" in
        opencode)
            echo -e "  ${BOLD}▸ OpenCode${NC}"
            bash "${SCRIPT_DIR}/scripts/deploy-to-opencode.sh"
            ;;
        gemini)
            echo -e "  ${BOLD}▸ Gemini CLI${NC}"
            bash "${SCRIPT_DIR}/scripts/deploy-to-gemini-cli.sh"
            ;;
        antigravity)
            echo -e "  ${BOLD}▸ Antigravity${NC}"
            bash "${SCRIPT_DIR}/scripts/deploy-to-antigravity.sh"
            ;;
    esac
done

# =============================================================================
# MCP installation prompt
# =============================================================================
echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Phase 2: MCP Server Installation${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
if [[ "${FAST_MODE}" == "1" ]]; then
    echo -e "  ${CYAN}Fast mode: Auto-installing MCPs.${NC}"
    export FAST_MODE=1
    if [[ -n "${ENV_FILE}" ]]; then
        bash "${SCRIPT_DIR}/scripts/install-mcps.sh" --env "${ENV_FILE}"
    else
        bash "${SCRIPT_DIR}/scripts/install-mcps.sh"
    fi
else
    echo -e "  Do you also want to install ${BOLD}MCP servers${NC} (model context protocol)"
    echo -e "  into your platform configs?"
    echo ""
    echo -e "  This will configure servers like Playwright, Hyperbrowser, Semgrep,"
    echo -e "  Serena, Context7, Genkit, and more."
    echo ""
    echo -e "    ${GREEN}y)${NC} Yes, install MCPs"
    echo -e "    ${GREEN}n)${NC} No, skip MCPs"
    echo ""
    read -rp "  Install MCPs? [y/n]: " mcp_choice

    if [[ "${mcp_choice}" =~ ^[Yy]$ ]]; then
        bash "${SCRIPT_DIR}/scripts/install-mcps.sh"
    fi
fi

# =============================================================================
# Final summary
# =============================================================================
echo ""
echo -e "${GREEN}╔═══════════════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                                                                               ║${NC}"
echo -e "${GREEN}║  ${BOLD}✅  Overpowers installation complete!${NC}${GREEN}                                        ║${NC}"
echo -e "${GREEN}║                                                                               ║${NC}"
echo -e "${GREEN}╚═══════════════════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${BOLD}What was deployed:${NC}"
for platform in "${SELECTED_PLATFORMS[@]}"; do
    case "${platform}" in
        opencode)
            echo -e "    ${GREEN}✓${NC} OpenCode     → ${DIM}~/.config/opencode/${NC}"
            ;;
        gemini)
            echo -e "    ${GREEN}✓${NC} Gemini CLI   → ${DIM}~/.gemini/${NC}"
            ;;
        antigravity)
            echo -e "    ${GREEN}✓${NC} Antigravity  → ${DIM}~/.gemini/antigravity/${NC}"
            ;;
    esac
done

if [[ "${mcp_choice:-n}" =~ ^[Yy]$ ]]; then
    echo -e "    ${GREEN}✓${NC} MCP servers configured"
fi

echo ""
echo -e "  ${BOLD}Useful commands:${NC}"
echo -e "    ${CYAN}./scripts/install-plugins.sh${NC}    Install community plugins/themes"
echo -e "    ${CYAN}./scripts/install-mcps.sh${NC}       Re-run MCP setup independently"
echo ""
echo -e "  ${DIM}Happy coding! 🚀${NC}"
echo ""

if [[ "${FAST_MODE}" == "1" ]]; then
    echo -e "  ${CYAN}Fast mode: running install-plugins.sh for 15 seconds to verify...${NC}"
    timeout 15s bash "${SCRIPT_DIR}/scripts/install-plugins.sh" || true
    echo -e "  ${GREEN}[✓] Plugin script tested successfully.${NC}"
else
    echo ""
    read -rp "  Do you want to see the available Community Plugins/Themes? [y/N]: " plugin_choice
    if [[ "${plugin_choice}" =~ ^[Yy]$ ]]; then
        bash "${SCRIPT_DIR}/scripts/install-plugins.sh"
    fi
fi
