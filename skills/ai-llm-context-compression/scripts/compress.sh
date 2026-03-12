#!/bin/bash

# Wrapper for compress_session.py
# Usage: ./compress.sh --intent "Fixing auth" --state "Passed tests" ...

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
python3 "$SCRIPT_DIR/compress_session.py" "$@"
