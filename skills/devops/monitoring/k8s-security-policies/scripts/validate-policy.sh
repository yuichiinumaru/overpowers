#!/bin/bash
set -e

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <policy-manifest.yaml>"
    exit 1
fi

POLICY_MANIFEST="$1"
if [ ! -f "$POLICY_MANIFEST" ]; then
    echo "Error: File $POLICY_MANIFEST not found."
    exit 1
fi

echo "Validating $POLICY_MANIFEST..."

# Just checking basic yaml syntax as a helper
if command -v yq >/dev/null 2>&1; then
    yq e '.' "$POLICY_MANIFEST" >/dev/null && echo "Policy manifest YAML syntax is valid."
elif command -v python3 >/dev/null 2>&1; then
    python3 -c "import yaml, sys; list(yaml.safe_load_all(open(sys.argv[1])))" "$POLICY_MANIFEST" >/dev/null 2>&1 && echo "Policy manifest YAML syntax is valid."
else
    echo "Please install yq or python3 with pyyaml to validate YAML syntax."
fi

# If kubescape is installed, we can run a quick scan
if command -v kubescape >/dev/null 2>&1; then
    echo "Running Kubescape scan on $POLICY_MANIFEST..."
    kubescape scan framework nsa "$POLICY_MANIFEST"
fi
