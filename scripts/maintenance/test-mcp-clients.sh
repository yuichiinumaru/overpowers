#!/usr/bin/env bash
# =============================================================================
# test-mcp-clients.sh
# =============================================================================
# Runs MCP status checks for Gemini CLI, OpenCode, and Codex CLI.
# Prints filtered issues to help quickly spot broken or disconnected MCPs.
# =============================================================================

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

ERROR_PATTERN='(Error|ERROR|Invalid|invalid|Failed|FAILED|Disconnected|✗|warning|Warning|missing|not found|denied|timed out|cannot|Could not|configuration is invalid)'

run_check() {
  local label="$1"
  shift
  local cmd=("$@")
  local bin="${cmd[0]}"

  echo -e "${CYAN}━━━ ${label} ━━━${NC}"

  if ! command -v "${bin}" >/dev/null 2>&1; then
    echo -e "  ${YELLOW}[!]${NC} ${bin} not found in PATH. Skipping."
    echo ""
    return 0
  fi

  local output status
  set +e
  output="$(${cmd[@]} 2>&1)"
  status=$?
  set -e

  if [[ ${status} -ne 0 ]]; then
    echo -e "  ${RED}[✗]${NC} Command failed (${status}): ${cmd[*]}"
  else
    echo -e "  ${GREEN}[✓]${NC} Command executed: ${cmd[*]}"
  fi

  local issues
  issues="$(printf '%s\n' "${output}" | rg -n "${ERROR_PATTERN}" | rg -v "Skipping extension in .*gemini-extension.json" || true)"

  if [[ -n "${issues}" ]]; then
    echo -e "  ${YELLOW}Filtered issues:${NC}"
    printf '%s\n' "${issues}" | sed 's/^/    /'
  else
    echo -e "  ${GREEN}[✓]${NC} No issue lines matched filter."
  fi

  echo ""
}

echo ""
echo -e "${BOLD}MCP Client Health Check${NC}"
echo -e "${CYAN}=======================================================${NC}"

run_check "Gemini CLI" gemini mcp list
run_check "OpenCode" opencode mcp list
run_check "Codex CLI" codex mcp list

echo -e "${CYAN}=======================================================${NC}"
echo -e "${BOLD}Done.${NC}"
