#!/usr/bin/env bash

set -euo pipefail

# --- Colors ---
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
PACKAGES_DIR="${REPO_ROOT}/packages"

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Building Local MCP Packages${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [[ ! -d "${PACKAGES_DIR}" ]]; then
    echo -e "  ${YELLOW}[!]${NC} No packages directory found at ${PACKAGES_DIR}. Skipping."
    exit 0
fi

# Node.js Projects
NODE_PACKAGES=("in-memoria" "DesktopCommanderMCP" "vibe-check-mcp-server" "semgrep")
for pkg in "${NODE_PACKAGES[@]}"; do
    pkg_dir="${PACKAGES_DIR}/${pkg}"
    if [[ -d "${pkg_dir}" ]]; then
        echo -e "\n  ${BOLD}Building Node.js package: ${pkg}${NC}"
        pushd "${pkg_dir}" > /dev/null || continue
        if [[ -f "package.json" ]]; then
            npm install
            if grep -q '"build"' package.json; then
                npm run build
            fi
            echo -e "  ${GREEN}✓${NC} ${pkg} built successfully."
        else
            echo -e "  ${YELLOW}[!]${NC} No package.json found in ${pkg_dir}."
        fi
        popd > /dev/null || continue
    fi
done

# Python Projects
PYTHON_PACKAGES=("serena" "notebooklm-mcp-cli" "memcord")
for pkg in "${PYTHON_PACKAGES[@]}"; do
    pkg_dir="${PACKAGES_DIR}/${pkg}"
    if [[ -d "${pkg_dir}" ]]; then
        echo -e "\n  ${BOLD}Building Python package: ${pkg}${NC}"
        pushd "${pkg_dir}" > /dev/null || continue
        if [[ -f "pyproject.toml" ]]; then
            if command -v uv >/dev/null 2>&1; then
                uv sync
                echo -e "  ${GREEN}✓${NC} ${pkg} built successfully."
            else
                echo -e "  ${YELLOW}[!]${NC} 'uv' is not installed. Skipping Python build."
            fi
        else
            echo -e "  ${YELLOW}[!]${NC} No pyproject.toml found in ${pkg_dir}."
        fi
        popd > /dev/null || continue
    fi
done

echo -e "\n  ${GREEN}✓${NC} Local MCP packages build process complete."
