#!/usr/bin/env bash
# =============================================================================
# install-plugins.sh
# =============================================================================
# Interactive installer for OpenCode plugins and themes from the
# awesome-opencode community list.
#
# Usage:
#   ./scripts/install-plugins.sh
#
# What it does:
#   1. Presents a menu of curated plugins and themes.
#   2. Lets you select which ones to install.
#   3. Installs them via npm and injects them into your opencode.json
#      in a non-destructive manner (preserving existing config).
# =============================================================================

set -euo pipefail

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# --- Config ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
OPENCODE_DIR="${HOME}/.config/opencode"
OPENCODE_JSON="${OPENCODE_DIR}/opencode.json"

# --- Plugin catalog ---
# Format: "npm_package_or_github|display_name|description|type(plugin|theme)"
declare -a CATALOG=(
    # === PLUGINS ===
    "opencode-agent-memory|Agent Memory|Persistent memory across sessions|plugin"
    "opencode-agent-skills|Agent Skills|Curated agent skill sets|plugin"
    "opencode-antigravity-auth|Antigravity Auth|Multi-provider authentication|plugin"
    "opencode-antigravity-multi-auth|Multi Auth|Multi-account auth rotation|plugin"
    "opencode-background|Background|Background task execution|plugin"
    "opencode-background-agents|Background Agents|Run agents in background|plugin"
    "opencode-beads|Beads|Session bookmarking and navigation|plugin"
    "claude-code-safety-net|Safety Net|Safety checks for destructive commands|plugin"
    "opencode-context-analysis-plugin|Context Analysis|Deep context analysis|plugin"
    "opencode-devcontainers|DevContainers|Dev container integration|plugin"
    "opencode-direnv|Direnv|Direnv environment integration|plugin"
    "opencode-dynamic-context-pruning|Context Pruning|Smart context management|plugin"
    "envsitter-guard|Envsitter Guard|Environment variable protection|plugin"
    "opencode-froggy|Froggy|Fun terminal mascot|plugin"
    "opencode-gemini-auth|Gemini Auth|Google Gemini authentication|plugin"
    "opencode-google-ai-search-plugin|Google AI Search|Google AI-powered search|plugin"
    "opencode-handoff|Handoff|Session handoff between agents|plugin"
    "opencode-model-announcer|Model Announcer|Announce model switches|plugin"
    "opencode-morph-fast-apply|Morph Fast Apply|Fast code application|plugin"
    "oh-my-opencode|Oh My Opencode|Feature-rich plugin bundle|plugin"
    "oh-my-opencode-slim|Oh My Opencode Slim|Lightweight plugin bundle|plugin"
    "opencode-openai-codex-auth|OpenAI Codex Auth|OpenAI authentication|plugin"
    "opencode-canvas|Canvas|Visual canvas interface|plugin"
    "opencode-ignore|Ignore|Git-style ignore patterns|plugin"
    "opencode-mem|Mem|Memory management|plugin"
    "opencode-notify|Notify|Desktop notifications|plugin"
    "opencode-quota|Quota|API quota tracking|plugin"
    "opencode-roadmap|Roadmap|Project roadmap management|plugin"
    "opencode-sessions|Sessions|Advanced session management|plugin"
    "opencode-skills|Skills|Community skill manager|plugin"
    "opencode-snippets|Snippets|Code snippet library|plugin"
    "opencode-synced|Synced|Cloud sync for sessions|plugin"
    "opencode-workspace|Workspace|Workspace management|plugin"
    "opencode-worktree|Worktree|Git worktree management|plugin"
    "opencode-mystatus|MyStatus|Status dashboard|plugin"
    "opencode-shell-strategy|Shell Strategy|Smart shell command strategies|plugin"
    "opencode-simple-memory|Simple Memory|Lightweight memory plugin|plugin"
    "opencode-smart-title|Smart Title|AI-generated session titles|plugin"
    "opencode-smart-voice-notify|Smart Voice Notify|Voice notifications|plugin"
    "subtask2|Subtask2|Advanced subtask management|plugin"
    "opencode-swarm-plugin|Swarm|Multi-agent swarm coordination|plugin"
    "opencode-tokenscope|TokenScope|Token usage visualization|plugin"
    "opencode-wakatime|WakaTime|WakaTime time tracking|plugin"
    "opencode-warcraft-notifications|Warcraft Notifications|Fun Warcraft-style alerts|plugin"
    "with-context-mcp|With Context MCP|MCP context enhancement|plugin"
    "opencode-optimal-model-temps|Optimal Model Temps|Optimized temperature routing|plugin"
    "opencode-pilot|Pilot|Autonomous pilot mode|plugin"
    "plannotator|Plannotator|Plan annotation helper|plugin"
    "pocket-universe|Pocket Universe|Sandboxed execution|plugin"
    "opencode-ralph-wiggum|Ralph Wiggum|Humorous guardrails|plugin"
    "opencode-zellij-namer|Zellij Namer|Zellij pane naming|plugin"
    # === THEMES ===
    "opencode-ayu-theme|Ayu Theme|Ayu color scheme|theme"
    "opencode-ai-poimandres-theme|Poimandres Theme|Poimandres dark theme|theme"
)

# =============================================================================
# Helper functions
# =============================================================================

ensure_opencode_json() {
    mkdir -p "${OPENCODE_DIR}"
    if [[ ! -f "${OPENCODE_JSON}" ]]; then
        echo '{"$schema": "https://opencode.ai/config.json"}' > "${OPENCODE_JSON}"
        echo -e "${YELLOW}[!]${NC} Created new ${OPENCODE_JSON}"
    fi
}

plugin_is_installed() {
    local pkg="$1"
    python3 -c "
import json, sys
with open('${OPENCODE_JSON}') as f:
    data = json.load(f)
plugins = data.get('plugin', [])
sys.exit(0 if '${pkg}' in plugins else 1)
" 2>/dev/null
}

inject_plugin() {
    local pkg="$1"
    python3 -c "
import json
with open('${OPENCODE_JSON}') as f:
    data = json.load(f)
plugins = data.get('plugin', [])
if '${pkg}' not in plugins:
    plugins.append('${pkg}')
    data['plugin'] = plugins
    with open('${OPENCODE_JSON}', 'w') as f:
        json.dump(data, f, indent=4)
    print('injected')
else:
    print('already_present')
"
}

install_theme() {
    local pkg="$1"
    local theme_dir="${OPENCODE_DIR}/themes"
    mkdir -p "${theme_dir}"
    echo -e "${CYAN}[~]${NC} Themes are installed as JSON files in ${theme_dir}/"
    echo -e "${CYAN}[~]${NC} Check the package repo for the theme JSON: npm info ${pkg} homepage"
}

# =============================================================================
# Main interactive menu
# =============================================================================

main() {
    ensure_opencode_json

    echo ""
    echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}  Overpowers Plugin & Theme Installer${NC}"
    echo -e "${CYAN}  Source: awesome-opencode community list${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
    echo ""

    # Build display arrays
    local -a names=()
    local -a packages=()
    local -a descriptions=()
    local -a types=()
    local -a statuses=()

    for entry in "${CATALOG[@]}"; do
        IFS='|' read -r pkg name desc type <<< "${entry}"
        packages+=("${pkg}")
        names+=("${name}")
        descriptions+=("${desc}")
        types+=("${type}")
        if plugin_is_installed "${pkg}"; then
            statuses+=("installed")
        else
            statuses+=("")
        fi
    done

    # Choose category
    echo -e "  ${BOLD}Categories:${NC}"
    echo -e "    ${GREEN}1)${NC} Plugins"
    echo -e "    ${GREEN}2)${NC} Themes"
    echo -e "    ${GREEN}3)${NC} Show all"
    echo -e "    ${GREEN}q)${NC} Quit"
    echo ""
    read -rp "  Choose category [1/2/3/q]: " category_choice

    local filter_type=""
    case "${category_choice}" in
        1) filter_type="plugin" ;;
        2) filter_type="theme" ;;
        3) filter_type="" ;;
        q|Q) echo "Bye!"; exit 0 ;;
        *) echo "Invalid choice"; exit 1 ;;
    esac

    # Display filtered list
    echo ""
    echo -e "  ${BOLD}Available items:${NC}"
    echo ""

    local -a filtered_indices=()
    local display_idx=1
    for i in "${!packages[@]}"; do
        if [[ -n "${filter_type}" && "${types[$i]}" != "${filter_type}" ]]; then
            continue
        fi

        local status_badge=""
        if [[ "${statuses[$i]}" == "installed" ]]; then
            status_badge="${GREEN}[✓]${NC} "
        fi

        local type_badge=""
        if [[ "${types[$i]}" == "theme" ]]; then
            type_badge="${YELLOW}[T]${NC} "
        fi

        printf "    ${GREEN}%2d)${NC} %b%b%-30s ${CYAN}%s${NC}\n" \
            "${display_idx}" "${status_badge}" "${type_badge}" "${names[$i]}" "${descriptions[$i]}"

        filtered_indices+=("${i}")
        ((display_idx++))
    done

    echo ""
    echo -e "  Enter numbers separated by spaces (e.g. ${GREEN}1 3 5${NC}), ${GREEN}all${NC}, or ${GREEN}q${NC} to quit:"
    read -rp "  > " selection

    if [[ "${selection}" == "q" || "${selection}" == "Q" ]]; then
        echo "Bye!"; exit 0
    fi

    # Parse selection
    local -a selected_indices=()
    if [[ "${selection}" == "all" ]]; then
        selected_indices=("${filtered_indices[@]}")
    else
        for num in ${selection}; do
            local idx=$((num - 1))
            if [[ ${idx} -ge 0 && ${idx} -lt ${#filtered_indices[@]} ]]; then
                selected_indices+=("${filtered_indices[$idx]}")
            fi
        done
    fi

    if [[ ${#selected_indices[@]} -eq 0 ]]; then
        echo -e "${RED}[✗]${NC} No valid selection. Exiting."
        exit 1
    fi

    # Install selected items
    echo ""
    echo -e "${CYAN}  Installing ${#selected_indices[@]} item(s)...${NC}"
    echo ""

    for i in "${selected_indices[@]}"; do
        local pkg="${packages[$i]}"
        local name="${names[$i]}"
        local type="${types[$i]}"

        echo -e "  ${BOLD}→ ${name}${NC} (${pkg})"

        if [[ "${statuses[$i]}" == "installed" ]]; then
            echo -e "    ${GREEN}[✓]${NC} Already in opencode.json. Skipping."
            continue
        fi

        # npm install
        echo -e "    ${CYAN}[~]${NC} npm install..."
        if npm install --save "${pkg}" --prefix "${OPENCODE_DIR}" 2>/dev/null; then
            echo -e "    ${GREEN}[✓]${NC} npm install OK"
        else
            echo -e "    ${YELLOW}[!]${NC} npm install failed (may be a GitHub-only package)."
            echo -e "    ${YELLOW}[!]${NC} You may need to install manually: npm install ${pkg}"
        fi

        # Inject into opencode.json
        if [[ "${type}" == "plugin" ]]; then
            local result
            result="$(inject_plugin "${pkg}")"
            if [[ "${result}" == "injected" ]]; then
                echo -e "    ${GREEN}[✓]${NC} Added to opencode.json plugin list"
            else
                echo -e "    ${CYAN}[~]${NC} Already in opencode.json"
            fi
        elif [[ "${type}" == "theme" ]]; then
            install_theme "${pkg}"
        fi

        echo ""
    done

    echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  Installation complete!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "  Your opencode.json: ${CYAN}${OPENCODE_JSON}${NC}"
    echo ""
}

main "$@"
