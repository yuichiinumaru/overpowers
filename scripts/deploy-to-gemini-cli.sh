#!/usr/bin/env bash
# =============================================================================
# deploy-to-gemini-cli.sh
# =============================================================================
# Creates symbolic links from the Overpowers repository into the Gemini CLI
# global configuration directory (~/.gemini/).
#
# Gemini CLI discovers skills from:
#   - User skills:  ~/.gemini/skills/<name>/SKILL.md
#   - Or alias:     ~/.agents/skills/<name>/SKILL.md
#   - Global rules: ~/.gemini/GEMINI.md
#
# This script symlinks overpowers assets so Gemini CLI can use them globally.
#
# Usage:
#   ./skills/vercel-deploy/scripts/deploy-to-gemini-cli.sh
#
# Mapping:
#   overpowers/skills/     -> ~/.gemini/skills
#   overpowers/AGENTS.md   -> ~/.gemini/GEMINI.md   (global context/rules)
#   overpowers/hooks/      -> ~/.gemini/hooks        (if hooks are enabled)
# =============================================================================

set -euo pipefail

# --- Configuration ---
GEMINI_DIR="${HOME}/.gemini"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[✓]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[!]${NC} $*"; }
log_skip()  { echo -e "${CYAN}[~]${NC} $*"; }
log_error() { echo -e "${RED}[✗]${NC} $*"; }

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers → Gemini CLI Deployment Script${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  Repo root:     ${GREEN}${REPO_ROOT}${NC}"
echo -e "  Gemini CLI dir: ${GREEN}${GEMINI_DIR}${NC}"
echo ""

# --- Ensure gemini config dir exists ---
mkdir -p "${GEMINI_DIR}"

# --- Define symlink mappings ---
# Format: "source_relative:target_name"
# Note: agents are handled separately (curated list) due to Gemini API 512 tool limit
declare -a SYMLINKS=(
    "skills:skills"
    "hooks:hooks"
)

# --- Process main symlinks ---
for mapping in "${SYMLINKS[@]}"; do
    SRC_REL="${mapping%%:*}"
    TGT_NAME="${mapping##*:}"

    SRC_ABS="${REPO_ROOT}/${SRC_REL}"
    TGT_ABS="${GEMINI_DIR}/${TGT_NAME}"

    if [[ ! -e "${SRC_ABS}" ]]; then
        log_warn "Source not found: ${SRC_ABS}. Skipping ${TGT_NAME}."
        continue
    fi

    if [[ -L "${TGT_ABS}" ]]; then
        CURRENT_TARGET="$(readlink -f "${TGT_ABS}" 2>/dev/null || echo '<broken>')"
        if [[ "${CURRENT_TARGET}" == "${SRC_ABS}" ]]; then
            log_skip "${TGT_NAME} already points to the correct source."
            continue
        fi
        log_warn "Removing stale symlink: ${TGT_ABS} -> ${CURRENT_TARGET}"
        rm "${TGT_ABS}"
    elif [[ -e "${TGT_ABS}" ]]; then
        if [[ "${OVERPOWERS_CONFLICT_POLICY:-replace}" == "copy" ]]; then
            if [[ -d "${SRC_ABS}" ]]; then
                log_info "Merging assets into existing directory: ${TGT_ABS}"
                mkdir -p "${TGT_ABS}"
                cp -rn "${SRC_ABS}/"* "${TGT_ABS}/" 2>/dev/null || true
            else
                log_info "File already exists, skipping: ${TGT_ABS}"
            fi
            continue
        else
            log_warn "${TGT_ABS} exists as a real file/directory. Backing up to ${TGT_ABS}.bak"
            mv "${TGT_ABS}" "${TGT_ABS}.bak"
        fi
    fi

    if [[ "${OVERPOWERS_CONFLICT_POLICY:-replace}" == "copy" ]]; then
        cp -r "${SRC_ABS}" "${TGT_ABS}"
        log_info "${TGT_NAME} (copied) <- ${SRC_ABS}"
    else
        ln -s "${SRC_ABS}" "${TGT_ABS}"
        log_info "${TGT_NAME} (symlinked) -> ${SRC_ABS}"
    fi
done

# --- Deploy curated agents (NOT a symlink — limited by Gemini API 512 tool cap) ---
# The Gemini API enforces a max of 512 function declarations per request.
# Each subagent counts as one function declaration. With 900+ agents + ~100 MCP
# tools, the limit is exceeded. We deploy only a curated subset (~150 agents)
# from scripts/config/gemini-cli-agents.txt.
AGENTS_LIST="${REPO_ROOT}/scripts/config/gemini-cli-agents.txt"
AGENTS_TGT="${GEMINI_DIR}/agents"

if [[ -f "${AGENTS_LIST}" ]]; then
    # Remove symlink if exists (from old deploy)
    [[ -L "${AGENTS_TGT}" ]] && rm "${AGENTS_TGT}"
    mkdir -p "${AGENTS_TGT}"
    # Clear old agents
    rm -f "${AGENTS_TGT}"/*.md
    # Copy curated subset
    agent_count=0
    while IFS= read -r agent_file; do
        [[ -z "$agent_file" ]] && continue
        src="${REPO_ROOT}/agents/${agent_file}"
        if [[ -f "$src" ]]; then
            cp "$src" "${AGENTS_TGT}/"
            agent_count=$((agent_count + 1))
        fi
    done < "${AGENTS_LIST}"
    log_info "Deployed ${agent_count} curated agents (of $(wc -l < "${AGENTS_LIST}") in list)"
    log_warn "Gemini API limit: 512 function declarations. Full roster (900+) exceeds this."
    log_warn "Edit scripts/config/gemini-cli-agents.txt to customize which agents are deployed."

    # Sanitize agent frontmatter for Gemini CLI compatibility
    # Valid keys: name, description, kind, tools, model, temperature, max_turns, timeout_mins
    log_info "Sanitizing agent frontmatter for Gemini CLI schema..."
    python3 -c "
import os, re, yaml
# Gemini CLI valid keys (tools excluded: our tool names are OpenCode-specific)
VALID = {'name','description','kind','model','temperature','max_turns','timeout_mins'}
d = '${AGENTS_TGT}'
fixed = 0
for fn in os.listdir(d):
    if not fn.endswith('.md'): continue
    p = os.path.join(d, fn)
    with open(p) as f: c = f.read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)', c, re.DOTALL)
    if not m: continue
    raw = re.sub(r'^\s*-\s*\*\s*$', '', m.group(1), flags=re.MULTILINE)
    try: fm = yaml.safe_load(raw)
    except: continue
    if not isinstance(fm, dict): continue
    body = m.group(2)
    ch = False
    for k in [k for k in fm if k not in VALID]: del fm[k]; ch = True
    if 'name' in fm and isinstance(fm['name'], str):
        cn = fm['name'].replace('_','-').replace('.','-')
        if cn != fm['name']: fm['name'] = cn; ch = True
    if 'kind' not in fm: fm['kind'] = 'local'; ch = True
    if ch:
        lines = ['---']
        for key in ['name','description','kind','model','temperature','max_turns','timeout_mins']:
            if key not in fm: continue
            lines.append(f'{key}: {fm[key]}')
        lines += ['---', '']
        with open(p,'w') as f: f.write('\n'.join(lines) + body)
        fixed += 1
print(f'  Sanitized {fixed} agents')
"
else
    log_warn "Curated agent list not found: ${AGENTS_LIST}"
    log_warn "Run: python3 scripts/select-gemini-agents.py to generate it."
fi

# --- GEMINI.md (special handling) ---
# Gemini CLI reads ~/.gemini/GEMINI.md but our repo has AGENTS.md
# We symlink AGENTS.md -> GEMINI.md
GEMINI_MD="${GEMINI_DIR}/GEMINI.md"
AGENTS_MD="${REPO_ROOT}/AGENTS.md"

if [[ -f "${AGENTS_MD}" ]]; then
    if [[ -L "${GEMINI_MD}" ]]; then
        CURRENT="$(readlink -f "${GEMINI_MD}" 2>/dev/null || echo '<broken>')"
        if [[ "${CURRENT}" == "${AGENTS_MD}" ]]; then
            log_skip "GEMINI.md already points to AGENTS.md."
        else
            log_warn "Removing stale symlink: GEMINI.md -> ${CURRENT}"
            rm "${GEMINI_MD}"
            ln -s "${AGENTS_MD}" "${GEMINI_MD}"
            log_info "GEMINI.md -> ${AGENTS_MD}"
        fi
    elif [[ -e "${GEMINI_MD}" ]]; then
        log_warn "GEMINI.md exists. Backing up to GEMINI.md.bak"
        mv "${GEMINI_MD}" "${GEMINI_MD}.bak"
        ln -s "${AGENTS_MD}" "${GEMINI_MD}"
        log_info "GEMINI.md -> ${AGENTS_MD}"
    else
        ln -s "${AGENTS_MD}" "${GEMINI_MD}"
        log_info "GEMINI.md -> ${AGENTS_MD}"
    fi
else
    log_warn "AGENTS.md not found in repo. Skipping GEMINI.md link."
fi

# --- Enable subagents in settings.json ---
SETTINGS_JSON="${GEMINI_DIR}/settings.json"
if [[ -f "${SETTINGS_JSON}" ]]; then
    # Check if enableAgents is already set
    if python3 -c "import json; d=json.load(open('${SETTINGS_JSON}')); assert d.get('experimental',{}).get('enableAgents') == True" 2>/dev/null; then
        log_skip "experimental.enableAgents already enabled in settings.json"
    else
        python3 -c "
import json
with open('${SETTINGS_JSON}') as f:
    d = json.load(f)
d.setdefault('experimental', {})['enableAgents'] = True
with open('${SETTINGS_JSON}', 'w') as f:
    json.dump(d, f, indent=2)
"
        log_info "Enabled experimental.enableAgents in settings.json"
    fi
else
    # Create minimal settings.json with enableAgents
    echo '{"experimental": {"enableAgents": true}}' > "${SETTINGS_JSON}"
    log_info "Created settings.json with experimental.enableAgents enabled"
fi

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Deployment complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo ""

# --- Summary ---
echo "Current symlinks in ${GEMINI_DIR}:"
ls -la "${GEMINI_DIR}" | grep "^l" || echo "  (none)"
echo ""
AGENT_COUNT=$(find "${REPO_ROOT}/agents" -name '*.md' 2>/dev/null | wc -l)
SKILL_COUNT=$(find "${REPO_ROOT}/skills" -name 'SKILL.md' 2>/dev/null | wc -l)
echo -e "${CYAN}Gemini CLI will now discover:${NC}"
echo -e "  • ${GREEN}${AGENT_COUNT}${NC} subagents from overpowers/agents/"
echo -e "  • ${GREEN}${SKILL_COUNT}${NC} skills from overpowers/skills/"
echo -e "  • Global rules from ${GREEN}AGENTS.md${NC} (as GEMINI.md)"
echo -e "  • ${GREEN}experimental.enableAgents${NC} = true"
echo ""
