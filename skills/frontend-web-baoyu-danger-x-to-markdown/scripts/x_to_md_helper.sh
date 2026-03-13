#!/usr/bin/env bash
# Helper for X to Markdown conversion

if [ -z "$1" ]; then
    echo "Usage: x_to_md_helper.sh <url> [options]"
    exit 1
fi

URL=$1
shift
OPTIONS=$@

# Consent logic (stub as per SKILL.md)
CONSENT_FILE="$HOME/.local/share/baoyu-skills/x-to-markdown/consent.json"
mkdir -p "$(dirname "$CONSENT_FILE")"

if [ ! -f "$CONSENT_FILE" ]; then
    echo "DISCLAIMER: This tool uses a reverse-engineered X API. Use at your own risk."
    echo "Run 'echo \"{\\\"accepted\\\": true}\" > $CONSENT_FILE' to accept terms."
    exit 1
fi

# Path resolution for main.ts
SKILL_DIR=$(cd "$(dirname "$0")/.." && pwd)
SCRIPT_PATH="${SKILL_DIR}/scripts/main.ts"

if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: main.ts not found at $SCRIPT_PATH"
    exit 1
fi

bun "$SCRIPT_PATH" "$URL" $OPTIONS
