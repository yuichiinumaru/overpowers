#!/bin/bash
# 1Password CLI Helper using tmux session to preserve authentication context
set -e

SOCKET_DIR="${CLAWDBOT_TMUX_SOCKET_DIR:-${TMPDIR:-/tmp}/moltbot-tmux-sockets}"
mkdir -p "$SOCKET_DIR"
SOCKET="$SOCKET_DIR/moltbot-op.sock"
SESSION="op-auth-$(date +%Y%m%d-%H%M%S)"

echo "Starting 1Password helper in tmux session: $SESSION"

# Start tmux session
tmux -S "$SOCKET" new -d -s "$SESSION" -n shell

# Send the command to execute
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op $@" Enter
sleep 2 # give op time to execute and prompt if needed

# Capture the output
OUTPUT=$(tmux -S "$SOCKET" capture-pane -p -J -t "$SESSION":0.0 -S -200)

# Kill the session
tmux -S "$SOCKET" kill-session -t "$SESSION"

echo "Output from op command:"
echo "$OUTPUT"
