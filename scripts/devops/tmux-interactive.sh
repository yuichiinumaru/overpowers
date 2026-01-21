#!/bin/bash
# tmux-interactive.sh - Wrapper for secure tmux interaction
# Usage: ./tmux-interactive.sh <tmux_subcommand_and_args>

# Blocked subcommands (for security/stability)
BLOCKED=("capture-pane" "capturep" "save-buffer" "saveb" "show-buffer" "showb" "pipe-pane" "pipep")

CMD_STR="$*"
SUB_CMD=$(echo "$1" | tr '[:upper:]' '[:lower:]')

# Check for blocked subcommands
for blocked in "${BLOCKED[@]}"; do
    if [[ "$SUB_CMD" == "$blocked" ]]; then
        echo "Error: '$SUB_CMD' is blocked. Use direct 'tmux $SUB_CMD' via Bash tool instead."
        exit 1
    fi
done

# Execute tmux command
# Note: We rely on the caller to provide valid arguments
tmux "$@"
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo "Error: Command failed with exit code $EXIT_CODE"
    exit $EXIT_CODE
fi
