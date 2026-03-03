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

# Check dependencies
USE_GUM=0
if command -v gum >/dev/null 2>&1; then
    USE_GUM=1
fi

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
echo -e "${DIM}  Based on overpowers by Jesse Vincent • Maintained by Yuichi Inumaru${NC}"
echo ""
echo -e "${CYAN}╔═══════════════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  ${BOLD}Master Installer${NC}${CYAN}                                                              ║${NC}"
echo -e "${CYAN}║  Deploy agents, skills, workflows, hooks & MCP servers to your AI tools.     ║${NC}"
echo -e "${CYAN}╚═══════════════════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${BOLD}What this installation will do:${NC}"
echo -e "    1. Detect supported AI coding tools on your system."
echo -e "    2. Deploy Overpowers assets via symlinks."
echo -e "    3. Configure MCP servers (Playwright, Serena, etc.)."
echo -e "    4. Enable subagent integrations."
echo ""

# =============================================================================
# Auto-detection of platforms
# =============================================================================
declare -a AUTO_DETECTED=()
[[ -d "${HOME}/.config/opencode" ]] && AUTO_DETECTED+=("opencode")
[[ -d "${HOME}/.gemini" ]] && AUTO_DETECTED+=("gemini" "antigravity")
[[ -d "${HOME}/.kilocode" ]] && AUTO_DETECTED+=("kilo")
[[ -d "${HOME}/.cursor" ]] && AUTO_DETECTED+=("cursor")
[[ -d "${HOME}/.codeium/windsurf" ]] && AUTO_DETECTED+=("windsurf")
[[ -d "${HOME}/.codex" ]] && AUTO_DETECTED+=("codex")
[[ -d "${HOME}/.claude" ]] && AUTO_DETECTED+=("claude-code")
[[ -d "${HOME}/.factory" ]] && AUTO_DETECTED+=("factory")

declare -a SELECTED_PLATFORMS=()

if [[ "${FAST_MODE}" == "1" ]]; then
    echo -e "  ${CYAN}Running in FAST MODE (-f). Auto-selecting detected platforms.${NC}"
    SELECTED_PLATFORMS=("${AUTO_DETECTED[@]}")
else
    if [[ "${USE_GUM}" == "1" ]]; then
        echo -e "  ${BOLD}Which platforms do you want to deploy to? (Space to toggle, Enter to confirm)${NC}"
        # Pre-select detected platforms
        choices=$(gum choose --no-limit \
            $( [[ " ${AUTO_DETECTED[@]} " =~ " opencode " ]] && echo "--selected OpenCode" ) \
            $( [[ " ${AUTO_DETECTED[@]} " =~ " gemini " ]] && echo "--selected GeminiCLI" ) \
            $( [[ " ${AUTO_DETECTED[@]} " =~ " antigravity " ]] && echo "--selected Antigravity" ) \
            $( [[ " ${AUTO_DETECTED[@]} " =~ " kilo " ]] && echo "--selected KiloCode" ) \
            $( [[ " ${AUTO_DETECTED[@]} " =~ " cursor " ]] && echo "--selected Cursor" ) \
            $( [[ " ${AUTO_DETECTED[@]} " =~ " windsurf " ]] && echo "--selected Windsurf" ) \
            $( [[ " ${AUTO_DETECTED[@]} " =~ " codex " ]] && echo "--selected CodexCLI" ) \
            $( [[ " ${AUTO_DETECTED[@]} " =~ " claude-code " ]] && echo "--selected ClaudeCode" ) \
            $( [[ " ${AUTO_DETECTED[@]} " =~ " factory " ]] && echo "--selected Factory" ) \
            "OpenCode" "GeminiCLI" "Antigravity" "KiloCode" "Cursor" "Windsurf" "CodexCLI" "ClaudeCode" "Factory")
        
        for choice in $choices; do
            case "$choice" in
                "OpenCode") SELECTED_PLATFORMS+=("opencode") ;;
                "GeminiCLI") SELECTED_PLATFORMS+=("gemini") ;;
                "Antigravity") SELECTED_PLATFORMS+=("antigravity") ;;
                "KiloCode") SELECTED_PLATFORMS+=("kilo") ;;
                "Cursor") SELECTED_PLATFORMS+=("cursor") ;;
                "Windsurf") SELECTED_PLATFORMS+=("windsurf") ;;
                "CodexCLI") SELECTED_PLATFORMS+=("codex") ;;
                "ClaudeCode") SELECTED_PLATFORMS+=("claude-code") ;;
                "Factory") SELECTED_PLATFORMS+=("factory") ;;
            esac
        done
    else
        echo -e "  ${BOLD}Which platforms do you want to deploy to?${NC}"
        echo "  (Detected: ${AUTO_DETECTED[*]})"
        echo ""
        echo -e "    ${GREEN}1)${NC} Detected platforms only"
        echo -e "    ${GREEN}2)${NC} All 9 platforms"
        echo -e "    ${GREEN}q)${NC} Quit"
        echo ""
        read -rp "  Choose [1/2/q]: " platform_choice

        case "${platform_choice}" in
            1) SELECTED_PLATFORMS=("${AUTO_DETECTED[@]}") ;;
            2) SELECTED_PLATFORMS=("opencode" "gemini" "antigravity" "kilo" "cursor" "windsurf" "codex" "claude-code" "factory") ;;
            q|Q) echo -e "\n  ${DIM}Bye!${NC}"; exit 0 ;;
            *) echo -e "${RED}Invalid choice${NC}"; exit 1 ;;
        esac
    fi
fi

if [[ ${#SELECTED_PLATFORMS[@]} -eq 0 ]]; then
    echo -e "${YELLOW}No platforms selected. Exiting.${NC}"
    exit 0
fi

# =============================================================================
# Conflict Handling Policy
# =============================================================================
CONFLICT_POLICY="replace" # default
if [[ "${FAST_MODE}" == "0" ]]; then
    if [[ "${USE_GUM}" == "1" ]]; then
        echo -e "  ${YELLOW}${BOLD}How should Overpowers handle existing personal agents/skills?${NC}"
        conflict_choice=$(gum choose \
            "REPLACE (Recommended: Back up existing and symlink Overpowers)" \
            "COPY-ONLY (No symlinks, won't auto-update)" \
            "ABORT")
        case "$conflict_choice" in
            "REPLACE"*) CONFLICT_POLICY="replace" ;;
            "COPY-ONLY"*) CONFLICT_POLICY="copy" ;;
            "ABORT") echo -e "\n  ${RED}Installation aborted.${NC}"; exit 0 ;;
        esac
    else
        echo ""
        echo -e "  ${YELLOW}${BOLD}How should Overpowers handle existing personal agents/skills?${NC}"
        echo -e "    ${GREEN}1) REPLACE${NC} (Recommended) - Back up folders to .bak and symlink."
        echo -e "    ${GREEN}2) COPY-ONLY${NC} - Copy assets IN without symlinks."
        echo -e "    ${GREEN}3) ABORT${NC} - Do not modify."
        read -rp "  Choose [1/2/3]: " c_choice
        case "${c_choice}" in
            1) CONFLICT_POLICY="replace" ;;
            2) CONFLICT_POLICY="copy" ;;
            *) echo -e "\n  ${RED}Aborted.${NC}"; exit 0 ;;
        esac
    fi
fi

# =============================================================================
# Deploy assets per platform
# =============================================================================
echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Phase 0: Building local packages${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
bash "${SCRIPT_DIR}/scripts/setup/build-packages.sh" || true

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Phase 1: Deploying assets${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

export OVERPOWERS_CONFLICT_POLICY="${CONFLICT_POLICY}"

for platform in "${SELECTED_PLATFORMS[@]}"; do
    case "${platform}" in
        opencode) bash "${SCRIPT_DIR}/scripts/deploy-to-opencode.sh" ;;
        gemini) bash "${SCRIPT_DIR}/scripts/deploy-to-gemini-cli.sh" ;;
        antigravity) bash "${SCRIPT_DIR}/scripts/deploy-to-antigravity.sh" ;;
        kilo) bash "${SCRIPT_DIR}/scripts/deploy-to-kilo.sh" ;;
        cursor) bash "${SCRIPT_DIR}/scripts/deploy-to-cursor.sh" ;;
        windsurf) bash "${SCRIPT_DIR}/scripts/deploy-to-windsurf.sh" ;;
        codex) bash "${SCRIPT_DIR}/scripts/deploy-to-codex.sh" ;;
        claude-code) bash "${SCRIPT_DIR}/scripts/deploy-to-claude-code.sh" ;;
        factory) bash "${SCRIPT_DIR}/scripts/deploy-to-factory.sh" ;;
    esac
done

# =============================================================================
# ENV file check
# =============================================================================
env_target="${SCRIPT_DIR}/.env"
if [[ ! -f "${env_target}" ]]; then
    echo -e "${YELLOW}No .env file found.${NC}"
    if [[ "${FAST_MODE}" == "0" ]]; then
        if [[ "${USE_GUM}" == "1" ]]; then
            gum confirm "Create .env from .env.example?" && cp "${SCRIPT_DIR}/.env.example" "${env_target}" && echo -e "${GREEN}Created .env file.${NC}"
        else
            read -rp "Create .env from .env.example? [Y/n] " env_choice
            if [[ ! "${env_choice}" =~ ^[Nn]$ ]]; then
                cp "${SCRIPT_DIR}/.env.example" "${env_target}"
                echo -e "${GREEN}Created .env file.${NC}"
            fi
        fi
    else
        # In FAST_MODE, create it automatically if missing to prevent MCP failures
        cp "${SCRIPT_DIR}/.env.example" "${env_target}"
        echo -e "${GREEN}Created missing .env from example (FAST MODE).${NC}"
    fi
fi

# =============================================================================
# MCP installation prompt
# =============================================================================
echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Phase 2: MCP Server Installation${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
if [[ "${FAST_MODE}" == "1" ]]; then
    export FAST_MODE=1
    bash "${SCRIPT_DIR}/scripts/install-mcps.sh" ${ENV_FILE:+--env "${ENV_FILE}"}
else
    mcp_choice="n"
    if [[ "${USE_GUM}" == "1" ]]; then
        if gum confirm "Install MCP servers (Playwright, Semgrep, Serena, Context7, etc.)?"; then
            mcp_choice="y"
        fi
    else
        read -rp "  Install MCP servers? [y/N]: " mc_c
        [[ "${mc_c}" =~ ^[Yy]$ ]] && mcp_choice="y"
    fi

    if [[ "${mcp_choice}" == "y" ]]; then
        bash "${SCRIPT_DIR}/scripts/install-mcps.sh"
    fi
fi

echo ""
echo -e "${GREEN}✅ Installation complete!${NC}"
echo -e "  ${DIM}Happy coding! 🚀${NC}"
