#!/usr/bin/env bash
# =============================================================================
#  ██████  ██    ██ ███████ ██████  ██████   ██████  ██     ██ ███████ ██████  ███████
# ██    ██ ██    ██ ██      ██   ██ ██   ██ ██    ██ ██     ██ ██      ██   ██ ██
# ██    ██ ██    ██ █████   ██████  ██████  ██    ██ ██  █  ██ █████   ██████  ███████
# ██    ██  ██  ██  ██      ██   ██ ██      ██    ██ ██ ███ ██ ██      ██   ██      ██
#  ██████    ████   ███████ ██   ██ ██       ██████   ███ ███  ███████ ██   ██ ███████
#
# install.sh — Master Installer v2.0
# =============================================================================

set -euo pipefail

# --- Initialization ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/scripts/utils/deploy-utils.sh"
DIM='\033[2m'

# --- Environment Validation ---
check_required_tools bash python3 || { echo "Fatal: Missing core dependencies."; exit 1; }

FAST_MODE=0
ENV_FILE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -f|--fast) FAST_MODE=1; export FAST_MODE=1; shift ;;
    -e|--env) ENV_FILE="$2"; shift 2 ;;
    *) echo "Usage: $0 [-f|--fast] [-e|--env <file>]" >&2; exit 1 ;;
  esac
done

# --- Banner ---
clear 2>/dev/null || true
echo -e "${MAGENTA}${BOLD}"
cat << "EOF"
  ██████  ██    ██ ███████ ██████  ██████   ██████  ██     ██ ███████ ██████  ███████
 ██    ██ ██    ██ ██      ██   ██ ██   ██ ██    ██ ██     ██ ██      ██   ██ ██     
 ██    ██ ██    ██ █████   ██████  ██████  ██    ██ ██  █  ██ █████   ██████  ███████
 ██    ██  ██  ██  ██      ██   ██ ██      ██    ██ ██ ███ ██ ██      ██   ██      ██
  ██████    ████   ███████ ██   ██ ██       ██████   ███ ███  ███████ ██   ██ ███████
EOF
echo -e "${NC}"
echo ""

# --- Platform Detection ---
declare -a AUTO_DETECTED=()
[[ -d "${HOME}/.config/opencode" ]] && AUTO_DETECTED+=("OpenCode")
[[ -d "${HOME}/.gemini" ]] && AUTO_DETECTED+=("GeminiCLI" "Antigravity")
[[ -d "${HOME}/.kilocode" ]] && AUTO_DETECTED+=("KiloCode")
[[ -d "${HOME}/.cursor" ]] && AUTO_DETECTED+=("Cursor")
[[ -d "${HOME}/.codeium/windsurf" ]] && AUTO_DETECTED+=("Windsurf")
[[ -d "${HOME}/.codex" ]] && AUTO_DETECTED+=("CodexCLI")
[[ -d "${HOME}/.claude" ]] && AUTO_DETECTED+=("ClaudeCode")
[[ -d "${HOME}/.factory" ]] && AUTO_DETECTED+=("Factory")
[[ -d "${HOME}/.qwen" ]] && AUTO_DETECTED+=("QwenCode")

declare -a SELECTED_PLATFORMS=()

if [[ "${FAST_MODE}" == "1" ]]; then
    log_info "Fast Mode: Deploying to all detected platforms: ${AUTO_DETECTED[*]}"
    SELECTED_PLATFORMS=("${AUTO_DETECTED[@]}")
else
    if command -v gum >/dev/null 2>&1; then
        echo -e "${BOLD}Select platforms to deploy Overpowers assets:${NC}"
        choices=$(gum choose --no-limit \
            $(for p in "${AUTO_DETECTED[@]}"; do echo "--selected $p"; done) \
            "OpenCode" "GeminiCLI" "Antigravity" "KiloCode" "Cursor" "Windsurf" "CodexCLI" "ClaudeCode" "Factory" "QwenCode")

        for choice in $choices; do SELECTED_PLATFORMS+=("$choice"); done
    else
        echo -e "Detected: ${AUTO_DETECTED[*]}"
        read -rp "Deploy to detected only (1) or all 10 (2)? [1/2]: " p_choice
        [[ "$p_choice" == "1" ]] && SELECTED_PLATFORMS=("${AUTO_DETECTED[@]}") || SELECTED_PLATFORMS=("OpenCode" "GeminiCLI" "Antigravity" "KiloCode" "Cursor" "Windsurf" "CodexCLI" "ClaudeCode" "Factory" "QwenCode")
    fi
fi

[[ ${#SELECTED_PLATFORMS[@]} -eq 0 ]] && { log_warn "No platforms selected. Exiting."; exit 0; }

# --- Conflict Policy ---
export OVERPOWERS_CONFLICT_POLICY="replace"
if [[ "${FAST_MODE}" == "0" ]] && command -v gum >/dev/null 2>&1; then
    echo -e "\n${YELLOW}${BOLD}Conflict Policy:${NC}"
    policy=$(gum choose "REPLACE (Back up and Symlink)" "COPY (No symlinks)" "ABORT")
    [[ "$policy" == "ABORT" ]] && exit 0
    [[ "$policy" == "COPY"* ]] && export OVERPOWERS_CONFLICT_POLICY="copy"
fi

# --- Phase 0: Build ---
echo -e "\n${CYAN}Phase 0: Building local packages...${NC}"
bash "${SCRIPT_DIR}/scripts/setup/build-packages.sh" || log_warn "Build skipped or failed."

# --- Phase 1: Deploy ---
echo -e "\n${CYAN}Phase 1: Deploying assets...${NC}"
for p in "${SELECTED_PLATFORMS[@]}"; do
    case "$p" in
        OpenCode) bash "${SCRIPT_DIR}/scripts/deploy-to-opencode.sh" ;;
        GeminiCLI) bash "${SCRIPT_DIR}/scripts/deploy-to-gemini.sh" ;;
        Antigravity) bash "${SCRIPT_DIR}/scripts/deploy-to-antigravity.sh" ;;
        KiloCode) bash "${SCRIPT_DIR}/scripts/deploy-to-kilo.sh" ;;
        Cursor) bash "${SCRIPT_DIR}/scripts/deploy-to-cursor.sh" ;;
        Windsurf) bash "${SCRIPT_DIR}/scripts/deploy-to-windsurf.sh" ;;
        CodexCLI) bash "${SCRIPT_DIR}/scripts/deploy-to-codex.sh" ;;
        ClaudeCode) bash "${SCRIPT_DIR}/scripts/deploy-to-claude-code.sh" ;;
        Factory) bash "${SCRIPT_DIR}/scripts/deploy-to-factory.sh" ;;
        QwenCode) bash "${SCRIPT_DIR}/scripts/deploy-to-qwen.sh" ;;
    esac
done

# --- Phase 2: Environment ---
echo -e "\n${CYAN}Phase 2: Environment Validation...${NC}"
if [[ ! -f "${SCRIPT_DIR}/.env" ]]; then
    if [[ "${FAST_MODE}" == "1" ]] || (command -v gum >/dev/null 2>&1 && gum confirm "Create .env from example?"); then
        cp "${SCRIPT_DIR}/.env.example" "${SCRIPT_DIR}/.env"
        log_info "Created .env file."
    fi
fi

# --- Phase 3: MCPs ---
echo -e "\n${CYAN}Phase 3: MCP Server Installation...${NC}"
if [[ "${FAST_MODE}" == "1" ]] || (command -v gum >/dev/null 2>&1 && gum confirm "Install MCP servers?"); then
    bash "${SCRIPT_DIR}/scripts/install-mcps.sh" ${ENV_FILE:+--env "${ENV_FILE}"}
fi

# --- Phase 4: Plugins ---
echo -e "\n${CYAN}Phase 4: Plugins & Themes Installation...${NC}"
if [[ "${FAST_MODE}" == "1" ]] || (command -v gum >/dev/null 2>&1 && gum confirm "Install additional context plugins or themes?"); then
    if command -v gum >/dev/null 2>&1; then
        echo -e "${BOLD}Select platforms for plugin installation:${NC}"
        p_choices=$(gum choose --no-limit --selected "OpenCode" "OpenCode")
        
        for choice in $p_choices; do
            if [[ "$choice" == "OpenCode" ]]; then
                bash "${SCRIPT_DIR}/scripts/install-plugins-opencode.sh"
            fi
        done
    else
        read -rp "Install plugins for OpenCode? [Y/n]: " p_choice
        p_choice=${p_choice:-Y}
        if [[ "$p_choice" =~ ^[Yy] ]]; then
            bash "${SCRIPT_DIR}/scripts/install-plugins-opencode.sh"
        fi
    fi
fi

echo -e "\n${GREEN}${BOLD}✅ Overpowers Installation Complete!${NC}"
echo -e "${DIM}  Happy coding! 🚀${NC}\n"
