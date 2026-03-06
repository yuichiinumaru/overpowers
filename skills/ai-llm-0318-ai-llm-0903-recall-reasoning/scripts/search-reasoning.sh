#!/bin/bash
# Wrapper script for artifact_query.py

QUERY=$1
shift

if [ -z "$QUERY" ]; then
    echo "Usage: $0 <query> [options]"
else
    uv run python "$(dirname "$0")/core/artifact_query.py" "$QUERY" "$@"
fi
