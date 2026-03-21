#!/usr/bin/env bash
# =============================================================================
# Overpowers Hook: PreToolUse - Bash Guard
# =============================================================================
# Blocks dangerous bash commands before execution.
# Fail-closed: if anything errors, deny by default.
#
# Adapted from: Claude Code Blueprint (Delanoe Pirard / Aedelon, Apache 2.0)
# Adapted for: Overpowers Integrated Agent System
#
# Input: JSON via stdin with tool_input.command
# Output: JSON with permissionDecision deny if dangerous
# =============================================================================

set -euo pipefail

# Fail-closed: if anything errors, deny by default
trap 'echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"Hook error - fail-closed\"}}"; exit 0' ERR

# Read stdin JSON
input=$(cat)

# Extract command from tool_input
command=$(echo "$input" | jq -r '.tool_input.command // empty' 2>/dev/null || echo "")

[ -z "$command" ] && exit 0

# === 1. Privilege escalation (block, not just warn) ===
# Catches: sudo, su, doas, pkexec — at start of command or after ; && || $( `
if echo "$command" | grep -qE '(^|;|&&|\|\||\$\(|`)\s*(sudo|su |doas |pkexec)'; then
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Privilege escalation blocked."}}'
    exit 0
fi

# === 2. Destructive patterns ===
# - Recursive force delete dangerous paths
# - Device writes (mkfs, dd to /dev)
# - Permission bombs (chmod -R 777, chmod +s)
# - Fork bombs
# - Pipe to shell (curl|sh, wget|bash)
# - Data destruction (shred on important paths)
dangerous_patterns='rm\s+(-[a-zA-Z]*f[a-zA-Z]*\s+|--force\s+).*(/|~|\*|\$HOME|\$PWD)|rm\s+-rf\s+/|>\s*/dev/sd|mkfs\.|dd\s+.*of=/dev|chmod\s+-R\s+777|chmod\s+\+s|:\(\)\{\s*:\|:\s*&\s*\}\s*;|curl\s+.*\|\s*(sh|bash)|wget\s+.*\|\s*(sh|bash)|curl\s+.*\|\s*python|wget\s+.*-O-\s*\|\s*(sh|bash)'

if echo "$command" | grep -qE "$dangerous_patterns"; then
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Dangerous command pattern detected"}}'
    exit 0
fi

# === 3. Indirect execution / obfuscation ===
# - eval with variables
# - base64 decode piped to shell
# - bash process substitution with remote sources
obfuscation_patterns='eval\s+.*\$|base64\s+(-d|--decode).*\|\s*(sh|bash|python)|bash\s+<\(curl|bash\s+<\(wget'

if echo "$command" | grep -qE "$obfuscation_patterns"; then
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Obfuscated execution pattern detected"}}'
    exit 0
fi

# === 4. Git state-altering commands (per Constituição Art. 24) ===
if echo "$command" | grep -qE '(^|;|&&|\|\|)\s*git\s+(commit|add|push|checkout|branch|merge|rebase)\b'; then
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Git state-altering command blocked per Art. 24. Use jj instead."}}'
    exit 0
fi

exit 0
