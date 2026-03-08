#!/bin/bash
set -e

echo "Checking Linkerd installation..."

if ! command -v linkerd >/dev/null 2>&1; then
    echo "Error: linkerd CLI is not installed."
    echo "Install it with: curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/install | sh"
    exit 1
fi

echo "Running pre-installation checks..."
linkerd check --pre

echo "Checks passed. You can now install Linkerd using:"
echo "linkerd install | kubectl apply -f -"
echo "linkerd check"
