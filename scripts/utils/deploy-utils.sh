#!/usr/bin/env bash
# =============================================================================
# deploy-utils.sh
# =============================================================================
# Core utilities for Overpowers deployment scripts.
# =============================================================================

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
BOLD='\033[1m'
NC='\033[0m'

# Helpers
log_info()  { echo -e "${GREEN}[✓]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[!]${NC} $*"; }
log_skip()  { echo -e "${CYAN}[~]${NC} $*"; }
log_error() { echo -e "${RED}[✗]${NC} $*"; }

setup_deploy_env() {
    local platform_name="$1"
    local platform_dir="$2"
    
    # Export for sub-scripts
    export PLATFORM_NAME="${platform_name}"
    export PLATFORM_DIR="${platform_dir}"
    
    # Resolve roots
    export SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[1]}")" && pwd)"
    export REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
    
    # Ensure platform directory exists
    if [[ ! -d "${PLATFORM_DIR}" ]]; then
        log_warn "Platform directory not found: ${PLATFORM_DIR}. Creating it."
        mkdir -p "${PLATFORM_DIR}"
    fi
}

check_required_tools() {
    local missing=0
    for tool in "$@"; do
        if ! command -v "$tool" &>/dev/null; then
            log_error "Missing required tool: $tool"
            missing=1
        fi
    done
    return $missing
}

print_deploy_banner() {
    local name="${1:-${PLATFORM_NAME:-Platform}}"
    echo ""
    echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}  Overpowers → ${name} Deployment Script${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "  Repo root:    ${GREEN}${REPO_ROOT:-.}${NC}"
    echo -e "  Target dir:   ${GREEN}${PLATFORM_DIR:-.}${NC}"
    echo ""
}

print_deploy_summary() {
    local target="${1:-${PLATFORM_DIR}}"
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  ${PLATFORM_NAME:-Deployment} complete!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo ""
    if [[ -d "${target}" ]]; then
        echo "Current symlinks in ${target}:"
        ls -la "${target}" | grep "^l" || echo "  (none)"
    fi
    echo ""
}

# Source create-symlinks automatically
UTILS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "${UTILS_DIR}/create-symlinks.sh" ]]; then
    source "${UTILS_DIR}/create-symlinks.sh"
fi
