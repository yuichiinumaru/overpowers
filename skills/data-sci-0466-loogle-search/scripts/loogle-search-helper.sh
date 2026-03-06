#!/bin/bash
# Loogle Search - Mathlib Type Signature Search Helper Script

if [ -z "$1" ]; then
    echo "Usage: $0 \"pattern\" [--json]"
    echo "Example: $0 \"Nontrivial _ ↔ _\""
    exit 1
fi

PATTERN=$1
shift

if [ "$1" == "--json" ]; then
    loogle-search "$PATTERN" --json
else
    loogle-search "$PATTERN"
fi