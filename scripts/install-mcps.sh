#!/usr/bin/env bash
# =============================================================================
# install-mcps.sh  (Unified Multi-Platform MCP Installer)
# =============================================================================
# Installs the Overpowers MCP server configurations into one or more platforms:
#   - OpenCode     (~/.config/opencode/opencode.json)
#   - Gemini CLI   (~/.gemini/settings.json)
#   - Antigravity  (~/.gemini/antigravity/mcp_config.json)
#
# Usage:
#   ./scripts/install-mcps.sh
#
# Features:
#   - Non-destructive: never overwrites existing MCP entries
#   - Centralized .env file for all API keys and paths
#   - Asks the user whether to enter values now or later
#   - Translates between the different MCP config schemas automatically
# =============================================================================

set -euo pipefail

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

# --- Config ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
EXAMPLE_JSON="${REPO_ROOT}/opencode-example.json"
ENV_TEMPLATE="${REPO_ROOT}/.env.example"

# Platform config paths
OPENCODE_DIR="${HOME}/.config/opencode"
OPENCODE_JSON="${OPENCODE_DIR}/opencode.json"
GEMINI_DIR="${HOME}/.gemini"
GEMINI_SETTINGS="${GEMINI_DIR}/settings.json"
ANTIGRAVITY_DIR="${HOME}/.gemini/antigravity"
ANTIGRAVITY_MCP="${ANTIGRAVITY_DIR}/mcp_config.json"

# Centralized .env location
CENTRAL_ENV="${REPO_ROOT}/.env"

# =============================================================================
# Banner
# =============================================================================
echo ""
echo -e "${CYAN}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  ${BOLD}Overpowers Unified MCP Server Installer${NC}${CYAN}              ║${NC}"
echo -e "${CYAN}║  Installs MCPs to: OpenCode • Gemini CLI • Antigravity${NC}${CYAN}║${NC}"
echo -e "${CYAN}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# =============================================================================
# Step 1: Choose platforms
# =============================================================================
echo -e "  ${BOLD}Which platforms do you want to install MCPs into?${NC}"
echo ""
echo -e "    ${GREEN}1)${NC} OpenCode       (${DIM}${OPENCODE_JSON}${NC})"
echo -e "    ${GREEN}2)${NC} Antigravity    (${DIM}${ANTIGRAVITY_MCP}${NC})"
echo -e "    ${GREEN}3)${NC} All platforms"
echo -e "    ${GREEN}q)${NC} Quit"
echo ""
read -rp "  Choose [1/2/3/q]: " platform_choice

declare -a PLATFORMS=()
case "${platform_choice}" in
    1) PLATFORMS=("opencode") ;;
    2) PLATFORMS=("antigravity") ;;
    3) PLATFORMS=("opencode" "antigravity") ;;
    q|Q) echo "Bye!"; exit 0 ;;
    *) echo "Invalid choice"; exit 1 ;;
esac

# =============================================================================
# Step 2: Handle .env configuration
# =============================================================================
echo ""
echo -e "${YELLOW}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║  ${BOLD}⚠️  ATENÇÃO: CONFIGURAÇÃO DE VARIÁVEIS DE AMBIENTE${NC}${YELLOW}   ║${NC}"
echo -e "${YELLOW}╠═══════════════════════════════════════════════════════╣${NC}"
echo -e "${YELLOW}║${NC}                                                       ${YELLOW}║${NC}"
echo -e "${YELLOW}║${NC}  O arquivo ${BOLD}.env${NC} centralizado vai ficar em:            ${YELLOW}║${NC}"
echo -e "${YELLOW}║${NC}  ${CYAN}${CENTRAL_ENV}${NC}"
echo -e "${YELLOW}║${NC}                                                       ${YELLOW}║${NC}"
echo -e "${YELLOW}║${NC}  Todas as plataformas vão ler as chaves de lá.        ${YELLOW}║${NC}"
echo -e "${YELLOW}║${NC}  ${RED}NUNCA commite esse arquivo!${NC} Ele está no ${BOLD}.gitignore${NC}.  ${YELLOW}║${NC}"
echo -e "${YELLOW}║${NC}                                                       ${YELLOW}║${NC}"
echo -e "${YELLOW}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if .env already exists
if [[ -f "${CENTRAL_ENV}" ]]; then
    echo -e "  ${GREEN}[✓]${NC} .env already exists at ${CYAN}${CENTRAL_ENV}${NC}"
    echo ""
    echo -e "  Do you want to:"
    echo -e "    ${GREEN}1)${NC} Keep existing values (just install MCPs)"
    echo -e "    ${GREEN}2)${NC} Re-enter values now (update .env interactively)"
    read -rp "  Choose [1/2]: " env_choice
else
    echo -e "  ${YELLOW}[!]${NC} No .env found. Let's set one up."
    echo ""
    echo -e "  Do you want to:"
    echo -e "    ${GREEN}1)${NC} Enter API keys and paths now (interactive)"
    echo -e "    ${GREEN}2)${NC} Skip — I'll fill them in manually later"
    read -rp "  Choose [1/2]: " env_choice

    if [[ "${env_choice}" == "2" ]]; then
        # Copy template
        cp "${ENV_TEMPLATE}" "${CENTRAL_ENV}"
        echo -e "  ${GREEN}[✓]${NC} Template copied to ${CYAN}${CENTRAL_ENV}${NC}"
        echo -e "  ${YELLOW}[!]${NC} Remember to edit it with your real values before using MCPs!"
        env_choice="1"  # skip the interactive section
    fi
fi

if [[ "${env_choice}" == "2" || ( ! -f "${CENTRAL_ENV}" && "${env_choice}" == "1" ) ]]; then
    echo ""
    echo -e "  ${BOLD}Enter your values (press Enter to keep default/empty):${NC}"
    echo ""

    # Read defaults from template
    declare -A ENV_DEFAULTS=()
    if [[ -f "${ENV_TEMPLATE}" ]]; then
        while IFS= read -r line; do
            [[ "${line}" =~ ^#.*$ || -z "${line}" ]] && continue
            key="${line%%=*}"
            val="${line#*=}"
            val="${val//\'/}"
            ENV_DEFAULTS["${key}"]="${val}"
        done < "${ENV_TEMPLATE}"
    fi

    declare -A ENV_VALUES=()
    for key in GEMINI_API_KEY HYPERBROWSER_API_KEY CONTEXT7_API_KEY \
               VIBE_CHECK_PATH HYPERTOOL_MCP_CONFIG_PATH \
               MEMCORD_PYTHON_PATH MEMCORD_SRC_PATH \
               SEMGREP_PATH SEMGREP_SYSTEM_PATH \
               IN_MEMORIA_PATH NOTEBOOKLM_PATH; do

        default="${ENV_DEFAULTS[${key}]:-}"
        if [[ "${key}" == *"API_KEY"* ]]; then
            prompt_label="${YELLOW}${key}${NC}"
        else
            prompt_label="${CYAN}${key}${NC}"
        fi

        if [[ -n "${default}" && "${default}" != *"your_"* ]]; then
            echo -ne "  ${prompt_label} [${DIM}${default}${NC}]: "
        else
            echo -ne "  ${prompt_label}: "
        fi

        read -r input_val
        if [[ -n "${input_val}" ]]; then
            ENV_VALUES["${key}"]="${input_val}"
        elif [[ -n "${default}" ]]; then
            ENV_VALUES["${key}"]="${default}"
        fi
    done

    # Write .env
    {
        echo "# ============================================================================="
        echo "# Overpowers Centralized Environment Variables"
        echo "# Generated by install-mcps.sh on $(date +%Y-%m-%d)"
        echo "# ============================================================================="
        echo ""
        echo "# --- API Keys ---"
        for key in GEMINI_API_KEY HYPERBROWSER_API_KEY CONTEXT7_API_KEY; do
            echo "${key}='${ENV_VALUES[${key}]:-}'"
        done
        echo ""
        echo "# --- MCP Server Paths ---"
        for key in VIBE_CHECK_PATH HYPERTOOL_MCP_CONFIG_PATH \
                   MEMCORD_PYTHON_PATH MEMCORD_SRC_PATH \
                   SEMGREP_PATH SEMGREP_SYSTEM_PATH \
                   IN_MEMORIA_PATH NOTEBOOKLM_PATH; do
            echo "${key}='${ENV_VALUES[${key}]:-}'"
        done
    } > "${CENTRAL_ENV}"

    echo ""
    echo -e "  ${GREEN}[✓]${NC} .env saved to ${CYAN}${CENTRAL_ENV}${NC}"
fi

# =============================================================================
# Step 3: Load .env values
# =============================================================================
declare -A ENV_LOADED=()
if [[ -f "${CENTRAL_ENV}" ]]; then
    while IFS= read -r line; do
        [[ "${line}" =~ ^#.*$ || -z "${line}" ]] && continue
        key="${line%%=*}"
        val="${line#*=}"
        val="${val//\'/}"
        ENV_LOADED["${key}"]="${val}"
    done < "${CENTRAL_ENV}"
fi

# =============================================================================
# Step 4: Install MCPs per platform
# =============================================================================
echo ""
echo -e "  ${BOLD}Installing MCP servers...${NC}"
echo ""

# --- Helper: resolve env var references ---
resolve_env() {
    local val="$1"
    # Replace {env:VAR} with actual value from .env
    for key in "${!ENV_LOADED[@]}"; do
        val="${val//\{env:${key}\}/${ENV_LOADED[${key}]}}"
    done
    echo "${val}"
}

# ========== OPENCODE ==========
install_opencode() {
    echo -e "  ${CYAN}━━━ OpenCode ━━━${NC}"
    mkdir -p "${OPENCODE_DIR}"

    if [[ ! -f "${OPENCODE_JSON}" ]]; then
        echo '{"$schema": "https://opencode.ai/config.json"}' > "${OPENCODE_JSON}"
        echo -e "  ${YELLOW}[!]${NC} Created new opencode.json"
    fi

    python3 - "${EXAMPLE_JSON}" "${OPENCODE_JSON}" << 'PYEOF'
import json, sys

with open(sys.argv[1]) as f:
    example = json.load(f)
with open(sys.argv[2]) as f:
    target = json.load(f)

src_mcps = example.get("mcp", {})
tgt_mcps = target.get("mcp", {})

for name, config in src_mcps.items():
    if name in tgt_mcps:
        print(f"SKIP:{name}")
    else:
        tgt_mcps[name] = config
        print(f"ADD:{name}")

target["mcp"] = tgt_mcps
with open(sys.argv[2], "w") as f:
    json.dump(target, f, indent=4)
PYEOF
}

# ========== ANTIGRAVITY ==========
install_antigravity() {
    echo -e "  ${CYAN}━━━ Antigravity ━━━${NC}"
    mkdir -p "${ANTIGRAVITY_DIR}"

    if [[ ! -f "${ANTIGRAVITY_MCP}" ]]; then
        echo '{"mcpServers": {}}' > "${ANTIGRAVITY_MCP}"
        echo -e "  ${YELLOW}[!]${NC} Created new mcp_config.json"
    fi

    # Antigravity uses standard MCP format: command (string), args (array), env (object)
    # OpenCode uses: command (array), environment (object)
    # We need to translate from our opencode-example.json format
    python3 - "${EXAMPLE_JSON}" "${ANTIGRAVITY_MCP}" "${CENTRAL_ENV}" << 'PYEOF'
import json, sys, os

with open(sys.argv[1]) as f:
    example = json.load(f)

with open(sys.argv[2]) as f:
    target = json.load(f)

# Load .env for resolving {env:VAR}
env_vals = {}
env_path = sys.argv[3]
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            key, _, val = line.partition('=')
            env_vals[key] = val.strip("'\"")

def resolve(val):
    """Replace {env:VAR} with actual values."""
    import re
    def repl(m):
        return env_vals.get(m.group(1), m.group(0))
    return re.sub(r'\{env:(\w+)\}', repl, str(val))

src_mcps = example.get("mcp", {})
tgt_mcps = target.get("mcpServers", {})

for name, config in src_mcps.items():
    if name in tgt_mcps:
        print(f"SKIP:{name}")
        continue

    # Translate OpenCode format -> standard MCP format
    entry = {}

    cmd_list = config.get("command", [])
    if isinstance(cmd_list, list) and len(cmd_list) > 0:
        entry["command"] = resolve(cmd_list[0])
        if len(cmd_list) > 1:
            entry["args"] = [resolve(a) for a in cmd_list[1:]]
    elif isinstance(cmd_list, str):
        entry["command"] = resolve(cmd_list)

    # Environment -> env
    env_data = config.get("environment", {})
    if env_data:
        resolved_env = {}
        for k, v in env_data.items():
            resolved_env[k] = resolve(v)
        entry["env"] = resolved_env

    tgt_mcps[name] = entry
    print(f"ADD:{name}")

target["mcpServers"] = tgt_mcps
with open(sys.argv[2], "w") as f:
    json.dump(target, f, indent=2)
PYEOF
}

# --- Run installations ---
for platform in "${PLATFORMS[@]}"; do
    RESULT=""
    case "${platform}" in
        opencode)    RESULT="$(install_opencode 2>&1)" ;;
        antigravity) RESULT="$(install_antigravity 2>&1)" ;;
    esac

    while IFS= read -r line; do
        if [[ "${line}" == ADD:* ]]; then
            echo -e "    ${GREEN}[✓]${NC} Added: ${BOLD}${line#ADD:}${NC}"
        elif [[ "${line}" == SKIP:* ]]; then
            echo -e "    ${CYAN}[~]${NC} Already exists: ${line#SKIP:}"
        elif [[ -n "${line}" ]]; then
            echo -e "    ${line}"
        fi
    done <<< "${RESULT}"
    echo ""
done

# =============================================================================
# Step 5: Copy .env to platform dirs that need it
# =============================================================================
echo -e "  ${BOLD}Distributing .env to platform config directories...${NC}"
echo ""

if [[ -f "${CENTRAL_ENV}" ]]; then
    for platform in "${PLATFORMS[@]}"; do
        case "${platform}" in
            opencode)
                if [[ ! -f "${OPENCODE_DIR}/.env" ]] || ! diff -q "${CENTRAL_ENV}" "${OPENCODE_DIR}/.env" &>/dev/null; then
                    cp "${CENTRAL_ENV}" "${OPENCODE_DIR}/.env"
                    echo -e "    ${GREEN}[✓]${NC} Copied .env -> ${CYAN}${OPENCODE_DIR}/.env${NC}"
                else
                    echo -e "    ${CYAN}[~]${NC} ${OPENCODE_DIR}/.env already up-to-date"
                fi
                ;;
        esac
    done
fi

# =============================================================================
# Final summary
# =============================================================================
echo ""
echo -e "${GREEN}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  ${BOLD}Installation Complete!${NC}${GREEN}                                ║${NC}"
echo -e "${GREEN}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${BOLD}Centralized .env:${NC} ${CYAN}${CENTRAL_ENV}${NC}"
echo ""
echo -e "  ${BOLD}Platform configs updated:${NC}"
for platform in "${PLATFORMS[@]}"; do
    case "${platform}" in
        opencode)    echo -e "    ${GREEN}✓${NC} OpenCode:    ${DIM}${OPENCODE_JSON}${NC}" ;;
        antigravity) echo -e "    ${GREEN}✓${NC} Antigravity: ${DIM}${ANTIGRAVITY_MCP}${NC}" ;;
    esac
done

echo ""
echo -e "  ${YELLOW}LEMBRETE:${NC} Se você não preencheu as chaves de API ainda,"
echo -e "  edite o arquivo: ${CYAN}${CENTRAL_ENV}${NC}"
echo -e "  ${DIM}(Ele foi gerado a partir do .env.example do repositório)${NC}"
echo ""
