#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: validate-manifest.sh <manifest.yaml>"
  # exit 1
fi
echo "Validating $1..."
kubectl apply -f "$1" --dry-run=client
echo "Dry-run complete."
