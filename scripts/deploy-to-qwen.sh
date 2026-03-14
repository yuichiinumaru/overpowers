#!/usr/bin/env bash
# =============================================================================
# deploy-to-qwen.sh
# =============================================================================
# Creates symbolic links into Qwen Code configuration directory (~/.qwen/).
# Qwen Code uses Markdown for commands (TOML is deprecated).
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "Qwen Code" "${HOME}/.qwen"

# --- Deployment ---
print_deploy_banner

# Qwen Code uses Markdown for commands (TOML deprecated)
# We symlink workflows directly to commands directory
declare -a SYMLINKS=(
    "agents:agents"
    "skills:skills"
    "workflows:commands"
    "hooks:hooks"
)

# Optional: themes
if [[ -d "${REPO_ROOT}/themes" ]]; then
    SYMLINKS+=("themes:themes")
else
    log_skip "No themes/ directory found in repo. Skipping."
fi

# --- QWEN.md (Special handling for AGENTS.md) ---
QWEN_MD="${PLATFORM_DIR}/QWEN.md"
AGENTS_MD="${REPO_ROOT}/AGENTS.md"

if [[ -f "${AGENTS_MD}" ]]; then
    if [[ -L "${QWEN_MD}" ]]; then
        rm "${QWEN_MD}"
    elif [[ -e "${QWEN_MD}" ]]; then
        mv "${QWEN_MD}" "${QWEN_MD}.bak"
    fi
    ln -s "${AGENTS_MD}" "${QWEN_MD}"
    log_info "QWEN.md -> ${AGENTS_MD}"
fi

# --- Enable subagents in settings.json ---
SETTINGS_JSON="${PLATFORM_DIR}/settings.json"
python3 -c "
import json, os
path = '${SETTINGS_JSON}'
if os.path.exists(path):
    with open(path) as f: d = json.load(f)
else: d = {}
d.setdefault('experimental', {})['enableAgents'] = True
with open(path, 'w') as f: json.dump(d, f, indent=2)
" && log_info "Enabled experimental.enableAgents in settings.json"

create_symlinks "${PLATFORM_DIR}" "${SYMLINKS[@]}"

# --- Summary ---
print_deploy_summary
