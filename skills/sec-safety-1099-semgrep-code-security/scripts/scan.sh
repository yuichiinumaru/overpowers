#!/bin/bash
# Semgrep scanning helper script
PATH_TO_SCAN=${1:-.}
CONFIG=${2:-auto}

if ! command -v semgrep >/dev/null 2>&1; then
    echo "Error: semgrep is not installed."
    echo "Install it with: pip install semgrep"
    exit 1
fi

echo "Running Semgrep scan on $PATH_TO_SCAN with config: $CONFIG..."

case $CONFIG in
    "security")
        semgrep --config p/security-audit "$PATH_TO_SCAN"
        ;;
    "owasp")
        semgrep --config p/owasp-top-ten "$PATH_TO_SCAN"
        ;;
    "auto")
        semgrep --config auto "$PATH_TO_SCAN"
        ;;
    *)
        semgrep --config "$CONFIG" "$PATH_TO_SCAN"
        ;;
esac
