#!/usr/bin/env bash
# =============================================================================
# Overpowers Hook: PreToolUse - Write/Edit Guard (unified)
# =============================================================================
# Blocks writes to protected files AND detects secrets in written content.
# Fail-closed: if anything errors, deny by default.
#
# Adapted from: Claude Code Blueprint (Delanoe Pirard / Aedelon, Apache 2.0)
# Adapted for: Overpowers Integrated Agent System
#
# Input: JSON via stdin with tool_input.file_path, tool_input.content, tool_input.new_string
# Output: JSON with permissionDecision deny if dangerous
# =============================================================================

set -euo pipefail

# Fail-closed: if anything errors, deny by default
trap 'echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"Hook error - fail-closed\"}}"; exit 0' ERR

# Read stdin JSON
input=$(cat)

# === 1. Protected file paths ===
# Block writes to sensitive files (credentials, keys, configs)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null || echo "")

if [ -n "$file_path" ]; then
    # Protected patterns: env files, SSH keys, TLS certs, cloud creds, package auth, git creds
    protected_patterns='\.env($|\.local|\.production|\.staging)|\.ssh/|id_(rsa|ed25519|ecdsa)|\.pem$|\.key$|\.p12$|\.pfx$|\.jks$|\.aws/credentials|\.docker/config\.json|kubeconfig|\.npmrc|\.pypirc|\.netrc|\.pgpass|\.htpasswd|\.git-credentials'

    if echo "$file_path" | grep -qiE "$protected_patterns"; then
        echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"Cannot write to protected file: $file_path\"}}"
        exit 0
    fi

    # Block writes to Constitution-protected files (Art. 9 - vedado alterar CHANGELOG entradas pretéritas)
    # Block writes to tasklist.json (Art. 11 §2)
    if echo "$file_path" | grep -qiE '\.docs/tasklist\.json$'; then
        echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Cannot modify tasklist.json without user authorization (Art. 11 §2)"}}'
        exit 0
    fi
fi

# === 2. Secret detection in content ===
# Scan content being written for hardcoded secrets
content=$(echo "$input" | jq -r '(.tool_input.content // "") + (.tool_input.new_string // "")' 2>/dev/null || echo "")

if [ -n "$content" ]; then
    # Secret patterns: API keys, cloud keys, VCS tokens, private keys, JWTs
    secret_patterns='(sk-[a-zA-Z0-9]{20,}|sk-proj-[a-zA-Z0-9-_]{50,})|AKIA[0-9A-Z]{16}|(ghp_|gho_|ghs_|ghr_)[a-zA-Z0-9]{36}|(xoxb-|xoxp-|xoxs-)[0-9a-zA-Z-]+|-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----|eyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*|(sk_live_|pk_live_|rk_live_)[a-zA-Z0-9]+|SG\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|npm_[a-zA-Z0-9]{36}|pypi-AgEIcHlwaS5vcmc[a-zA-Z0-9-_]+'

    if echo "$content" | grep -qE "$secret_patterns"; then
        echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Potential secret/API key detected in content"}}'
        exit 0
    fi
fi

exit 0
