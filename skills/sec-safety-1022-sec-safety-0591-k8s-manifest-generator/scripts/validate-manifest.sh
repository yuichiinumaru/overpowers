#!/bin/bash
set -e

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <manifest.yaml>"
    exit 1
fi

MANIFEST="$1"
if [ ! -f "$MANIFEST" ]; then
    echo "Error: File $MANIFEST not found."
    exit 1
fi

echo "Validating $MANIFEST..."
if command -v kubectl >/dev/null 2>&1; then
    kubectl apply --dry-run=client -f "$MANIFEST"
    echo "Manifest is syntactically valid."
else
    echo "kubectl not found. Checking basic YAML syntax."
    if command -v yq >/dev/null 2>&1; then
        yq e '.' "$MANIFEST" >/dev/null && echo "YAML syntax is valid."
    elif command -v python3 >/dev/null 2>&1; then
        python3 -c "import yaml, sys; list(yaml.safe_load_all(open(sys.argv[1])))" "$MANIFEST" >/dev/null 2>&1 && echo "YAML syntax is valid."
    else
        echo "Please install kubectl, yq, or python3 with pyyaml to validate."
    fi
fi
