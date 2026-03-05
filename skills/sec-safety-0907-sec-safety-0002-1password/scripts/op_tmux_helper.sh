#!/bin/bash

# Helper to run 1Password CLI commands inside a tmux session as required by SKILL.md.

COMMAND=$1
ACCOUNT=$2

if [ -z "$COMMAND" ]; then
    echo "Usage: $0 <command> [account]"
    echo "Example: $0 'vault list' my.1password.com"
    exit 1
fi

SOCKET_DIR="${CLAWDBOT_TMUX_SOCKET_DIR:-${TMPDIR:-/tmp}/moltbot-tmux-sockets}"
mkdir -p "$SOCKET_DIR"
SOCKET="$SOCKET_DIR/moltbot-op.sock"
SESSION="op-task-$(date +%Y%m%d-%H%M%S)"

OP_CMD="op $COMMAND"
if [ -not -z "$ACCOUNT" ]; then
    OP_CMD="op $COMMAND --account $ACCOUNT"
fi

echo "Starting tmux session $SESSION for command: $OP_CMD"

tmux -S "$SOCKET" new -d -s "$SESSION" -n shell
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op signin" Enter
sleep 2 # Wait for app integration prompt if needed
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "$OP_CMD" Enter
sleep 2 # Wait for command execution
tmux -S "$SOCKET" capture-pane -p -J -t "$SESSION":0.0 -S -200
tmux -S "$SOCKET" kill-session -t "$SESSION"
