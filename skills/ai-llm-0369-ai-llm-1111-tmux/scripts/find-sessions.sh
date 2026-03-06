#!/usr/bin/env bash
# find-sessions.sh

set -e

SOCKET=""
ALL=0

while [[ "$#" -gt 0 ]]; do
  case $1 in
    -S|--socket) SOCKET="$2"; shift ;;
    --all) ALL=1 ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done

if [ "$ALL" -eq 1 ]; then
  SOCKET_DIR="${OPENCLAW_TMUX_SOCKET_DIR:-${CLAWDBOT_TMUX_SOCKET_DIR:-${TMPDIR:-/tmp}/openclaw-tmux-sockets}}"
  echo "Scanning for sockets in $SOCKET_DIR..."
  find "$SOCKET_DIR" -type s | while read sock; do
    echo "Sessions on socket $sock:"
    tmux -S "$sock" list-sessions || true
  done
elif [ -n "$SOCKET" ]; then
  tmux -S "$SOCKET" list-sessions
else
  echo "Usage: $0 [-S <socket>] [--all]"
  exit 1
fi
