#!/usr/bin/env bash
# =============================================================================
# deploy-to-gemini.sh
# =============================================================================
# Creates symbolic links into Gemini CLI configuration directory (~/.gemini/).
# Converts workflow .md files to .toml commands before deploying.
# =============================================================================

set -euo pipefail

# --- Core Setup ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils/deploy-utils.sh"
setup_deploy_env "Gemini CLI" "${HOME}/.gemini"

# --- Deployment ---
print_deploy_banner

# --- Convert MD workflows to TOML commands (Gemini CLI uses TOML, not MD) ---
log_info "Converting workflow .md files to .toml commands..."
uv run "${REPO_ROOT}/scripts/generators/md-to-toml.py" \
    "${REPO_ROOT}/workflows" \
    "${REPO_ROOT}/workflows/toml" \
    && log_info "TOML conversion complete." \
    || log_warn "TOML conversion failed — continuing with existing .toml files."

declare -a SYMLINKS=(
    "hooks:hooks"
    "workflows/toml:commands"
)

create_symlinks "${PLATFORM_DIR}" "${SYMLINKS[@]}"

# --- Gemini CLI now discovers skills from ~/.agents/skills ---
LEGACY_SKILLS="${PLATFORM_DIR}/skills"
if [[ -L "${LEGACY_SKILLS}" || -d "${LEGACY_SKILLS}" ]]; then
    LEGACY_SKILLS_BAK="${PLATFORM_DIR}/skills.overpowers-legacy.$(date +%Y%m%d-%H%M%S).bak"
    mv "${LEGACY_SKILLS}" "${LEGACY_SKILLS_BAK}"
    log_warn "Moved legacy ${LEGACY_SKILLS} -> ${LEGACY_SKILLS_BAK} to avoid skill conflicts with ~/.agents/skills."
fi

# --- GEMINI.md (Special handling for AGENTS.md) ---
GEMINI_MD="${PLATFORM_DIR}/GEMINI.md"
AGENTS_MD="${REPO_ROOT}/AGENTS.md"

if [[ -f "${AGENTS_MD}" ]]; then
    if [[ -L "${GEMINI_MD}" ]]; then
        rm "${GEMINI_MD}"
    elif [[ -e "${GEMINI_MD}" ]]; then
        mv "${GEMINI_MD}" "${GEMINI_MD}.bak"
    fi
    ln -s "${AGENTS_MD}" "${GEMINI_MD}"
    log_info "GEMINI.md -> ${AGENTS_MD}"
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

# --- Summary ---
print_deploy_summary
