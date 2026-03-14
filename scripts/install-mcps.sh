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

FAST_MODE=0
ENV_FILE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -f|--fast)
      FAST_MODE=1
      shift
      ;;
    --env)
      if [[ $# -lt 2 ]]; then
        echo "Error: --env requires a file path argument." >&2
        exit 1
      fi
      ENV_FILE="$2"
      shift 2
      ;;
    *)
      echo "Error: Unknown argument: $1" >&2
      echo "Usage: $0 [-f|--fast] [--env <file>]" >&2
      exit 1
      ;;
  esac
done

# --- Helper: expand relative paths to absolute ---
expand_path() {
  local p="$1"
  # Expand ~ to $HOME
  p="${p/#\~/$HOME}"
  # Expand ./ to REPO_ROOT (set later, but called after)
  if [[ "$p" == ./* ]]; then
    p="${REPO_ROOT}${p:1}"
  fi
  echo "$p"
}


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
OPENCODE_TEMPLATE_JSON="${REPO_ROOT}/templates/configs/mcp-opencode.json"
EXTRACTED_USER_MCPS_JSON="${REPO_ROOT}/scripts/extracted_user_mcps.json"
ENV_TEMPLATE="${REPO_ROOT}/.env.example"

# Platform config paths
OPENCODE_DIR="${HOME}/.config/opencode"
OPENCODE_JSON="${OPENCODE_DIR}/opencode.json"
GEMINI_DIR="${HOME}/.gemini"
GEMINI_SETTINGS="${GEMINI_DIR}/settings.json"
ANTIGRAVITY_DIR="${HOME}/.gemini/antigravity"
ANTIGRAVITY_MCP="${ANTIGRAVITY_DIR}/mcp_config.json"
CURSOR_DIR="${HOME}/.cursor"
CURSOR_MCP="${CURSOR_DIR}/mcp.json"
WINDSURF_DIR="${HOME}/.codeium/windsurf"
WINDSURF_MCP="${WINDSURF_DIR}/mcp_config.json"
CLAUDE_CODE_JSON="${HOME}/.claude.json"
CODEX_DIR="${HOME}/.codex"
CODEX_TOML="${CODEX_DIR}/config.toml"
KILO_DIR="${HOME}/.kilocode"
KILO_JSON="${KILO_DIR}/mcp.json"
FACTORY_DIR="${HOME}/.factory"
FACTORY_MCP="${FACTORY_DIR}/mcp.json"
TEMPLATES_DIR="${REPO_ROOT}/templates/configs"

# Centralized .env location
CENTRAL_ENV="${REPO_ROOT}/.env"

# =============================================================================
# Banner
# =============================================================================
echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  ${BOLD}Overpowers Unified MCP Server Installer${NC}${CYAN}                         ║${NC}"
echo -e "${CYAN}║  Supports: OpenCode • Antigravity • Cursor • Windsurf          ${CYAN}║${NC}"
echo -e "${CYAN}║           Gemini CLI • Codex CLI • Claude Code • Kilo • Factory ${CYAN}║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# =============================================================================
# Step 1: Choose platforms
# =============================================================================
ALL_PLATFORMS=("opencode" "antigravity" "cursor" "windsurf" "gemini-cli" "codex" "claude-code" "kilo" "factory")
declare -a PLATFORMS=()

if [[ "${FAST_MODE:-0}" == "1" ]]; then
    echo -e "  ${CYAN}Running in FAST MODE. Auto-selecting all platforms.${NC}"
    PLATFORMS=("${ALL_PLATFORMS[@]}")
else
    echo -e "  ${BOLD}Which platforms do you want to install MCPs into?${NC}"
    echo ""
    echo -e "    ${GREEN}1)${NC} OpenCode       (${DIM}${OPENCODE_JSON}${NC})"
    echo -e "    ${GREEN}2)${NC} Antigravity    (${DIM}${ANTIGRAVITY_MCP}${NC})"
    echo -e "    ${GREEN}3)${NC} Cursor         (${DIM}${CURSOR_MCP}${NC})"
    echo -e "    ${GREEN}4)${NC} Windsurf       (${DIM}${WINDSURF_MCP}${NC})"
    echo -e "    ${GREEN}5)${NC} Gemini CLI     (${DIM}${GEMINI_SETTINGS}${NC})"
    echo -e "    ${GREEN}6)${NC} Codex CLI      (${DIM}${CODEX_TOML}${NC}) ${DIM}[TOML]${NC}"
    echo -e "    ${GREEN}7)${NC} Claude Code    (${DIM}${CLAUDE_CODE_JSON}${NC})"
    echo -e "    ${GREEN}8)${NC} Kilo Code      (${DIM}${KILO_JSON}${NC})"
    echo -e "    ${GREEN}9)${NC} Factory Droid  (${DIM}${FACTORY_MCP}${NC})"
    echo -e "    ${GREEN}a)${NC} All platforms"
    echo -e "    ${GREEN}q)${NC} Quit"
    echo ""
    read -rp "  Choose [1-9/a/q] (comma-separated for multiple): " platform_choice

    case "${platform_choice}" in
        1) PLATFORMS=("opencode") ;;
        2) PLATFORMS=("antigravity") ;;
        3) PLATFORMS=("cursor") ;;
        4) PLATFORMS=("windsurf") ;;
        5) PLATFORMS=("gemini-cli") ;;
        6) PLATFORMS=("codex") ;;
        7) PLATFORMS=("claude-code") ;;
        8) PLATFORMS=("kilo") ;;
        9) PLATFORMS=("factory") ;;
        a|A) PLATFORMS=("${ALL_PLATFORMS[@]}") ;;
        q|Q) echo "Bye!"; exit 0 ;;
        *)
            # Parse comma-separated choices
            IFS=',' read -ra choices <<< "${platform_choice}"
            for c in "${choices[@]}"; do
                c="$(echo "$c" | xargs)"  # trim whitespace
                idx=$((c - 1))
                if [[ $idx -ge 0 && $idx -lt ${#ALL_PLATFORMS[@]} ]]; then
                    PLATFORMS+=("${ALL_PLATFORMS[$idx]}")
                fi
            done
            if [[ ${#PLATFORMS[@]} -eq 0 ]]; then
                echo "Invalid choice"; exit 1
            fi
            ;;
    esac
fi

# =============================================================================
# Step 1.5: Scan user MCPs
# =============================================================================
if [[ "${FAST_MODE:-0}" == "1" ]]; then
    echo -e "  ${CYAN}Fast mode: Auto-scanning user MCPs for merging.${NC}"
    scan_choice="1"
else
    echo ""
    echo -e "  ${BOLD}Do you want to scan your local configs to extract and standardize existing MCPs?${NC}"
    echo -e "  This will merge your installed MCPs (OpenCode, Antigravity, Gemini) with ours."
    echo ""
    echo -e "    ${GREEN}1)${NC} Yes, scan and merge my existing MCPs"
    echo -e "    ${GREEN}2)${NC} No, just install the repository's MCPs"
    read -rp "  Choose [1/2]: " scan_choice
fi

if [[ "${scan_choice}" == "1" ]]; then
    echo ""
    echo -e "  ${CYAN}Scanning installed MCPs...${NC}"
    
    EXTRACT_CMD=("python3" "${SCRIPT_DIR}/utils/extract-installed-mcps.py")
    if [[ -n "${ENV_FILE}" ]]; then
        EXTRACT_CMD+=("--env" "${ENV_FILE}")
    fi

    if "${EXTRACT_CMD[@]}"; then
        echo -e "  ${GREEN}[✓]${NC} Successfully extracted user MCPs and ENV variables."
    else
        echo -e "  ${YELLOW}[!]${NC} Scanning failed or encountered an error."
    fi
fi

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
    
    if [[ "${FAST_MODE:-0}" == "1" ]]; then
        env_choice="1"
    else
        echo ""
        echo -e "  Do you want to:"
        echo -e "    ${GREEN}1)${NC} Keep existing values (just install MCPs)"
        echo -e "    ${GREEN}2)${NC} Re-enter values now (update .env interactively)"
        read -rp "  Choose [1/2]: " env_choice
    fi
else
    echo -e "  ${YELLOW}[!]${NC} No .env found. Let's set one up."
    
    if [[ "${FAST_MODE:-0}" == "1" ]]; then
        if [[ -n "${ENV_FILE}" && -f "${ENV_FILE}" ]]; then
            cp "${ENV_FILE}" "${CENTRAL_ENV}"
            echo -e "  ${GREEN}[✓]${NC} External ENV copied to ${CYAN}${CENTRAL_ENV}${NC}"
        else
            cp "${ENV_TEMPLATE}" "${CENTRAL_ENV}"
            echo -e "  ${GREEN}[✓]${NC} Template copied to ${CYAN}${CENTRAL_ENV}${NC}"
        fi
        env_choice="1"
    else
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
fi

if [[ "${FAST_MODE:-0}" == "0" && ( "${env_choice}" == "2" || ( ! -f "${CENTRAL_ENV}" && "${env_choice}" == "1" ) ) ]]; then
    echo ""
    echo -e "  ${BOLD}Enter your values (press Enter to keep default/empty):${NC}"
    echo ""

    # Read defaults from template
    declare -A ENV_DEFAULTS=()
    declare -a ALL_KEYS=()
    if [[ -f "${ENV_TEMPLATE}" ]]; then
        while IFS= read -r line; do
            [[ "${line}" =~ ^#.*$ || -z "${line}" ]] && continue
            key="${line%%=*}"
            val="${line#*=}"
            val="${val//\'/}"
            ENV_DEFAULTS["${key}"]="${val}"
            ALL_KEYS+=("${key}")
        done < "${ENV_TEMPLATE}"
    fi

    declare -A ENV_VALUES=()
    for key in "${ALL_KEYS[@]}"; do
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
        for key in "${ALL_KEYS[@]}"; do
            echo "${key}=${ENV_VALUES[${key}]:-}"
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
        # Expand relative paths (./packages/...) to absolute paths
        if [[ "$val" == ./* ]]; then
            val=$(expand_path "$val")
        fi
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

    python3 - "${OPENCODE_TEMPLATE_JSON}" "${OPENCODE_JSON}" "${EXTRACTED_USER_MCPS_JSON}" "${CENTRAL_ENV}" << 'PYEOF'
import json, sys, os
import re

REMOVED_SERVERS = {"grep_app", "web_search", "StitchMCP", "stitchmcp"}

env_vals = {}
env_path = sys.argv[4]
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, _, val = line.partition("=")
            env_vals[key.strip()] = val.strip("'\"")

def resolve_env(v):
    if isinstance(v, str):
        return re.sub(r"\$\{(\w+)\}", lambda m: env_vals.get(m.group(1), m.group(0)), v)
    if isinstance(v, list):
        return [resolve_env(i) for i in v]
    if isinstance(v, dict):
        return {k: resolve_env(val) for k, val in v.items()}
    return v

memcord_path = env_vals.get("MEMCORD_PYTHON_PATH", "")
memcord_available = bool(memcord_path and os.path.exists(memcord_path))

with open(sys.argv[1]) as f:
    example = json.load(f)
with open(sys.argv[2]) as f:
    target = json.load(f)

src_mcps = example.get("mcp", {})

extracted_path = sys.argv[3]
if os.path.exists(extracted_path):
    with open(extracted_path) as f:
        user_mcps = json.load(f).get("mcp", {})
        for name, config in user_mcps.items():
            if name in REMOVED_SERVERS:
                continue
            if name not in src_mcps:
                src_mcps[name] = config

tgt_mcps = target.get("mcp", {})

# Remove deprecated MCPs from target
for name in REMOVED_SERVERS:
    if name in tgt_mcps:
        del tgt_mcps[name]
        print(f"REMOVE:{name}")

# Normalize legacy injected schema (command+args+env) to OpenCode schema
for name, cfg in list(tgt_mcps.items()):
    if not isinstance(cfg, dict):
        continue
    if "type" in cfg and "command" in cfg and isinstance(cfg["command"], list):
        continue
    cmd = cfg.get("command")
    args = cfg.get("args", [])
    env = cfg.get("environment") or cfg.get("env") or {}
    if isinstance(cmd, str):
        merged_cmd = [cmd] + (args if isinstance(args, list) else [])
        normalized = {
            "type": "local",
            "enabled": cfg.get("enabled", True),
            "command": resolve_env(merged_cmd),
        }
        if isinstance(env, dict) and env:
            normalized["environment"] = resolve_env(env)
        tgt_mcps[name] = normalized
        print(f"MIGRATE:{name}")

for name, config in src_mcps.items():
    if name in REMOVED_SERVERS:
        continue
    if name == "memcord" and not memcord_available:
        if name in tgt_mcps:
            del tgt_mcps[name]
            print("REMOVE:memcord")
        print("SKIP_UNAVAILABLE:memcord")
        continue
    if name in tgt_mcps:
        if name == "memcord":
            tgt_mcps[name] = resolve_env(config)
            print("UPDATE:memcord")
        else:
            print(f"SKIP:{name}")
    else:
        tgt_mcps[name] = resolve_env(config)
        print(f"ADD:{name}")

target["mcp"] = tgt_mcps
with open(sys.argv[2], "w") as f:
    json.dump(target, f, indent=4)
PYEOF
}

# ========== ANTIGRAVITY ==========
install_antigravity() {
    install_mcpservers_platform "Antigravity" "${ANTIGRAVITY_DIR}" "${ANTIGRAVITY_MCP}" "${TEMPLATES_DIR}/mcp-antigravity.json"
}

# ========== CURSOR ==========
install_cursor() {
    install_mcpservers_platform "Cursor" "${CURSOR_DIR}" "${CURSOR_MCP}" "${TEMPLATES_DIR}/mcp-cursor.json"
}

# ========== WINDSURF ==========
install_windsurf() {
    install_mcpservers_platform "Windsurf" "${WINDSURF_DIR}" "${WINDSURF_MCP}" "${TEMPLATES_DIR}/mcp-windsurf.json"
}

# ========== GEMINI CLI ==========
install_gemini_cli() {
    install_mcpservers_platform "Gemini CLI" "${GEMINI_DIR}" "${GEMINI_SETTINGS}" "${TEMPLATES_DIR}/mcp-gemini-cli.json"
}

# ========== CLAUDE CODE ==========
install_claude_code() {
    install_mcpservers_platform "Claude Code" "${HOME}" "${CLAUDE_CODE_JSON}" "${TEMPLATES_DIR}/mcp-claude-code.json"
}

# ========== KILO CODE ==========
install_kilo() {
    install_mcpservers_platform "Kilo Code" "${KILO_DIR}" "${KILO_JSON}" "${TEMPLATES_DIR}/mcp-kilo.json"
}

# ========== FACTORY DROID ==========
install_factory() {
    install_mcpservers_platform "Factory Droid" "${FACTORY_DIR}" "${FACTORY_MCP}" "${TEMPLATES_DIR}/mcp-factory.json"
}

# ========== CODEX CLI (TOML) ==========
install_codex() {
    echo -e "  ${CYAN}━━━ Codex CLI ━━━${NC}"
    mkdir -p "${CODEX_DIR}"
    if [[ ! -f "${CODEX_TOML}" ]]; then
        touch "${CODEX_TOML}"
        echo -e "  ${YELLOW}[!]${NC} Created new config.toml"
    fi
    # Codex uses TOML — expand env vars in template and append new servers
    python3 - "${TEMPLATES_DIR}/mcp-codex.toml" "${CODEX_TOML}" "${CENTRAL_ENV}" << 'PYEOF'
import sys, os, re
REMOVED_SERVERS = {"grep_app", "web_search", "StitchMCP", "stitchmcp"}

env_vals = {}
env_path = sys.argv[3]
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): continue
            key, _, val = line.partition('=')
            env_vals[key.strip()] = val.strip("'\"")

def resolve(val):
    return re.sub(r'\$\{(\w+)\}', lambda m: env_vals.get(m.group(1), m.group(0)), str(val))

with open(sys.argv[1]) as f:
    template = f.read()

with open(sys.argv[2]) as f:
    existing = f.read()

# Remove deprecated server blocks from existing config
for server in REMOVED_SERVERS:
    pattern = rf'\n?\[mcp_servers\.{re.escape(server)}\][\s\S]*?(?=\n\[mcp_servers\.|\Z)'
    if re.search(pattern, existing):
        existing = re.sub(pattern, '\n', existing).rstrip() + '\n'
        print(f"REMOVE:{server}")

# Find which servers already exist
existing_servers = set(re.findall(r'\[mcp_servers\.(\w[\w-]*)\]', existing))
template_blocks = re.split(r'(?=^\[mcp_servers\.)', template, flags=re.MULTILINE)

memcord_path = env_vals.get("MEMCORD_PYTHON_PATH", "")
memcord_available = bool(memcord_path and os.path.exists(memcord_path))

added = []
for block in template_blocks:
    m = re.match(r'\[mcp_servers\.(\w[\w-]*)\]', block)
    if not m: continue
    name = m.group(1)
    if name == "memcord" and not memcord_available:
        print("SKIP_UNAVAILABLE:memcord")
        continue
    if name in existing_servers:
        print(f"SKIP:{name}")
    else:
        resolved_block = resolve(block)
        existing += "\n" + resolved_block
        print(f"ADD:{name}")
        added.append(name)

if added:
    with open(sys.argv[2], 'w') as f:
        f.write(existing)
PYEOF
}

# ========== GENERIC JSON MCP INSTALLER ==========
# Used by: Antigravity, Cursor, Windsurf, Gemini CLI, Claude Code, Kilo, Factory
install_mcpservers_platform() {
    local label="$1" dir="$2" target_file="$3" template="$4"
    echo -e "  ${CYAN}━━━ ${label} ━━━${NC}"
    
    if [[ ! -d "${dir}" ]]; then
        mkdir -p "${dir}"
        echo -e "  ${YELLOW}[!]${NC} Created directory: ${dir}"
    fi

    if [[ ! -f "${target_file}" ]]; then
        if [[ "$(basename "${template}")" == "mcp-kilo.json" ]]; then
            echo '{"mcp": {}}' > "${target_file}"
        else
            echo '{"mcpServers": {}}' > "${target_file}"
        fi
        echo -e "  ${YELLOW}[!]${NC} Created new $(basename "${target_file}")"
    fi

    python3 - "${template}" "${target_file}" "${CENTRAL_ENV}" << 'PYEOF'
import json, sys, os, re

try:
    env_vals = {}
    env_path = sys.argv[3]
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'): continue
                key, _, val = line.partition('=')
                env_vals[key.strip()] = val.strip("'\"")

    def resolve(val):
        return re.sub(r'\$\{(\w+)\}', lambda m: env_vals.get(m.group(1), m.group(0)), str(val))

    def resolve_deep(obj):
        if isinstance(obj, str): return resolve(obj)
        if isinstance(obj, list): return [resolve_deep(i) for i in obj]
        if isinstance(obj, dict): return {k: resolve_deep(v) for k, v in obj.items()}
        return obj

    with open(sys.argv[1]) as f:
        template = json.load(f)
    with open(sys.argv[2]) as f:
        target = json.load(f)

    REMOVED_SERVERS = {"grep_app", "web_search", "StitchMCP", "stitchmcp"}

    if "mcpServers" in template and isinstance(template["mcpServers"], dict):
        key = "mcpServers"
    elif "mcp" in template and isinstance(template["mcp"], dict):
        key = "mcp"
    else:
        raise ValueError("Template must contain either 'mcpServers' or 'mcp' object")

    src = template.get(key, {})
    tgt = target.get(key, {})

    if not isinstance(tgt, dict):
        tgt = {}

    for name in REMOVED_SERVERS:
        if name in tgt:
            del tgt[name]
            print(f"REMOVE:{name}")

    memcord_path = env_vals.get("MEMCORD_PYTHON_PATH", "")
    memcord_available = bool(memcord_path and os.path.exists(memcord_path))

    for name, config in src.items():
        if name == "memcord" and not memcord_available:
            if name in tgt:
                del tgt[name]
                print("REMOVE:memcord")
            print("SKIP_UNAVAILABLE:memcord")
            continue
        if name in tgt:
            if name == "memcord":
                tgt[name] = resolve_deep(config)
                print("UPDATE:memcord")
            else:
                print(f"SKIP:{name}")
        else:
            tgt[name] = resolve_deep(config)
            print(f"ADD:{name}")

    target[key] = tgt
    with open(sys.argv[2], "w") as f:
        json.dump(target, f, indent=2)
except Exception as e:
    print(f"ERROR:{str(e)}")
    sys.exit(1)
PYEOF
}

# --- Run installations ---
for platform in "${PLATFORMS[@]}"; do
    RESULT=""
    case "${platform}" in
        opencode)    RESULT="$(install_opencode 2>&1)" ;;
        antigravity) RESULT="$(install_antigravity 2>&1)" ;;
        cursor)      RESULT="$(install_cursor 2>&1)" ;;
        windsurf)    RESULT="$(install_windsurf 2>&1)" ;;
        gemini-cli)  RESULT="$(install_gemini_cli 2>&1)" ;;
        codex)       RESULT="$(install_codex 2>&1)" ;;
        claude-code) RESULT="$(install_claude_code 2>&1)" ;;
        kilo)        RESULT="$(install_kilo 2>&1)" ;;
        factory)     RESULT="$(install_factory 2>&1)" ;;
    esac

    while IFS= read -r line; do
        if [[ "${line}" == ADD:* ]]; then
            echo -e "    ${GREEN}[✓]${NC} Added: ${BOLD}${line#ADD:}${NC}"
        elif [[ "${line}" == UPDATE:* ]]; then
            echo -e "    ${GREEN}[✓]${NC} Updated: ${BOLD}${line#UPDATE:}${NC}"
        elif [[ "${line}" == SKIP:* ]]; then
            echo -e "    ${CYAN}[~]${NC} Already exists: ${line#SKIP:}"
        elif [[ "${line}" == REMOVE:* ]]; then
            echo -e "    ${YELLOW}[-]${NC} Removed: ${line#REMOVE:}"
        elif [[ "${line}" == SKIP_UNAVAILABLE:* ]]; then
            echo -e "    ${YELLOW}[!]${NC} Skipped unavailable: ${line#SKIP_UNAVAILABLE:}"
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
        opencode)    echo -e "    ${GREEN}✓${NC} OpenCode:      ${DIM}${OPENCODE_JSON}${NC}" ;;
        antigravity) echo -e "    ${GREEN}✓${NC} Antigravity:   ${DIM}${ANTIGRAVITY_MCP}${NC}" ;;
        cursor)      echo -e "    ${GREEN}✓${NC} Cursor:        ${DIM}${CURSOR_MCP}${NC}" ;;
        windsurf)    echo -e "    ${GREEN}✓${NC} Windsurf:      ${DIM}${WINDSURF_MCP}${NC}" ;;
        gemini-cli)  echo -e "    ${GREEN}✓${NC} Gemini CLI:    ${DIM}${GEMINI_SETTINGS}${NC}" ;;
        codex)       echo -e "    ${GREEN}✓${NC} Codex CLI:     ${DIM}${CODEX_TOML}${NC}" ;;
        claude-code) echo -e "    ${GREEN}✓${NC} Claude Code:   ${DIM}${CLAUDE_CODE_JSON}${NC}" ;;
        kilo)        echo -e "    ${GREEN}✓${NC} Kilo Code:     ${DIM}${KILO_JSON}${NC}" ;;
        factory)     echo -e "    ${GREEN}✓${NC} Factory Droid: ${DIM}${FACTORY_MCP}${NC}" ;;
    esac
done

echo ""
echo -e "  ${YELLOW}LEMBRETE:${NC} Se você não preencheu as chaves de API ainda,"
echo -e "  edite o arquivo: ${CYAN}${CENTRAL_ENV}${NC}"
echo -e "  ${DIM}(Ele foi gerado a partir do .env.example do repositório)${NC}"
echo ""

# =============================================================================
# Step 6: MCP client health check
# =============================================================================
HEALTH_CHECK_SCRIPT="${SCRIPT_DIR}/maintenance/test-mcp-clients.sh"
if [[ -x "${HEALTH_CHECK_SCRIPT}" ]]; then
    echo -e "  ${BOLD}Running MCP client health check...${NC}"
    echo ""
    "${HEALTH_CHECK_SCRIPT}" || true
fi
