#!/usr/bin/env bash

# Raycast Extension Scaffolder for Fabric
# Usage: ./raycast_extension.sh <pattern-name>

PATTERN=$1

if [ -z "$PATTERN" ]; then
    echo "Usage: ./raycast_extension.sh <pattern-name>"
    exit 1
fi

FILE_NAME="fabric-${PATTERN}.sh"

cat <<EOF > "$FILE_NAME"
#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Fabric: $PATTERN
# @raycast.mode fullOutput
# @raycast.packageName Fabric Utilities
#
# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Input text or path" }

INPUT=\$1

if [ -z "\$INPUT" ]; then
    echo "Please provide input."
    exit 1
fi

# Example calling fabric
echo "\$INPUT" | fabric -p $PATTERN
EOF

chmod +x "$FILE_NAME"
echo "Created Raycast wrapper script: $FILE_NAME"
echo "Move this to your Raycast Script Commands directory."
