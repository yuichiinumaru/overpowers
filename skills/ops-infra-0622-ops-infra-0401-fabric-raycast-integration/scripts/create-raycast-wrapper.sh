#!/bin/bash
# Create a wrapper script for Raycast
OUTPUT_FILE="${1:-raycast-fabric-wrapper.sh}"

cat << 'BASH_EOF' > "$OUTPUT_FILE"
#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Fabric Script
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description Run Fabric script

fabric "$@"
BASH_EOF

echo "Raycast Fabric wrapper script created at $OUTPUT_FILE"
