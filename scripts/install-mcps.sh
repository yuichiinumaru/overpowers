#!/usr/bin/env bash
# =============================================================================
# install-mcps.sh
# =============================================================================
# Injects the MCP server configurations from overpowers/opencode-example.json
# into the user's ~/.config/opencode/opencode.json in a non-destructive way.
#
# Usage:
#   ./scripts/install-mcps.sh
#
# What it does:
#   1. Reads MCP definitions from this repo's opencode-example.json.
#   2. Merges them into the user's opencode.json under the "mcp" key.
#   3. Does NOT overwrite existing MCP entries — only adds new ones.
#   4. Reminds the user to populate their .env with the required keys.
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
EXAMPLE_JSON="${REPO_ROOT}/opencode-example.json"
ENV_EXAMPLE="${REPO_ROOT}/.env.example"

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  Overpowers MCP Server Installer${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
echo ""

# --- Sanity checks ---
if [[ ! -f "${EXAMPLE_JSON}" ]]; then
    echo -e "${RED}[✗]${NC} opencode-example.json not found at: ${EXAMPLE_JSON}"
    exit 1
fi

# --- Ensure opencode.json exists ---
mkdir -p "${OPENCODE_DIR}"
if [[ ! -f "${OPENCODE_JSON}" ]]; then
    echo '{"$schema": "https://opencode.ai/config.json"}' > "${OPENCODE_JSON}"
    echo -e "${YELLOW}[!]${NC} Created new ${OPENCODE_JSON}"
fi

# --- Merge MCPs ---
python3 << 'PYEOF'
import json
import sys
import os

example_path = os.environ.get("EXAMPLE_JSON")
target_path = os.environ.get("OPENCODE_JSON")

with open(example_path) as f:
    example = json.load(f)

with open(target_path) as f:
    target = json.load(f)

example_mcps = example.get("mcp", {})
target_mcps = target.get("mcp", {})

added = []
skipped = []

for name, config in example_mcps.items():
    if name in target_mcps:
        skipped.append(name)
    else:
        target_mcps[name] = config
        added.append(name)

target["mcp"] = target_mcps

with open(target_path, "w") as f:
    json.dump(target, f, indent=4)

# Output results
for name in added:
    print(f"ADDED:{name}")
for name in skipped:
    print(f"SKIPPED:{name}")
PYEOF

# Run the Python merger and process output
RESULT=$(EXAMPLE_JSON="${EXAMPLE_JSON}" OPENCODE_JSON="${OPENCODE_JSON}" python3 << 'PYEOF'
import json
import sys
import os

example_path = os.environ["EXAMPLE_JSON"]
target_path = os.environ["OPENCODE_JSON"]

with open(example_path) as f:
    example = json.load(f)

with open(target_path) as f:
    target = json.load(f)

example_mcps = example.get("mcp", {})
target_mcps = target.get("mcp", {})

added = []
skipped = []

for name, config in example_mcps.items():
    if name in target_mcps:
        skipped.append(name)
    else:
        target_mcps[name] = config
        added.append(name)

target["mcp"] = target_mcps

with open(target_path, "w") as f:
    json.dump(target, f, indent=4)

for name in added:
    print(f"ADDED:{name}")
for name in skipped:
    print(f"SKIPPED:{name}")
PYEOF
)

# Display results
echo -e "  ${BOLD}MCP Servers:${NC}"
echo ""

while IFS= read -r line; do
    action="${line%%:*}"
    name="${line#*:}"
    if [[ "${action}" == "ADDED" ]]; then
        echo -e "    ${GREEN}[✓]${NC} Added: ${BOLD}${name}${NC}"
    elif [[ "${action}" == "SKIPPED" ]]; then
        echo -e "    ${CYAN}[~]${NC} Already exists: ${name}"
    fi
done <<< "${RESULT}"

echo ""

# --- Remind about .env ---
echo -e "${YELLOW}═══════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}  IMPORTANT: Environment Variables Required${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  Some MCPs reference environment variables via ${CYAN}{env:VAR}${NC}."
echo -e "  Make sure you have a ${GREEN}.env${NC} file at:"
echo -e "    ${CYAN}${OPENCODE_DIR}/.env${NC}"
echo ""

if [[ -f "${ENV_EXAMPLE}" ]]; then
    echo -e "  Required variables (from .env.example):"
    echo ""
    grep -v '^#' "${ENV_EXAMPLE}" | grep -v '^$' | while IFS= read -r line; do
        varname="${line%%=*}"
        echo -e "    ${YELLOW}•${NC} ${varname}"
    done
    echo ""
    echo -e "  Copy the template: ${CYAN}cp ${ENV_EXAMPLE} ${OPENCODE_DIR}/.env${NC}"
    echo -e "  Then edit with your real values."
fi

echo ""
echo -e "${GREEN}  Done! Restart OpenCode to load the new MCP servers.${NC}"
echo ""
