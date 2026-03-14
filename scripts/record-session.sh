#!/bin/bash
# record-session.sh - Helper to launch the Omnara Flight Recorder

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RECORDER_PATH="$(cd "$SCRIPT_DIR/../services/omnara-monitoring" && pwd)/omnara-flight-recorder.py"

if [ ! -f "$RECORDER_PATH" ]; then
    echo "Error: recorder script not found at $RECORDER_PATH"
    exit 1
fi

python3 "$RECORDER_PATH" "$@"
