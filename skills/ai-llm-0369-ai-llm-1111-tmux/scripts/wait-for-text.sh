#!/usr/bin/env bash
# wait-for-text.sh

set -e

function usage() {
  echo "Usage: wait-for-text.sh -t <target> -p <pattern> [-F] [-T <timeout>] [-i <interval>] [-l <lines>] [-S <socket>]"
  exit 1
}

TARGET=""
PATTERN=""
FIXED=0
TIMEOUT=15
INTERVAL=0.5
LINES=1000
SOCKET="${OPENCLAW_TMUX_SOCKET_DIR:-${CLAWDBOT_TMUX_SOCKET_DIR:-${TMPDIR:-/tmp}/openclaw-tmux-sockets}}/openclaw.sock"

while [[ "$#" -gt 0 ]]; do
  case $1 in
    -t|--target) TARGET="$2"; shift ;;
    -p|--pattern) PATTERN="$2"; shift ;;
    -F|--fixed) FIXED=1 ;;
    -T|--timeout) TIMEOUT="$2"; shift ;;
    -i|--interval) INTERVAL="$2"; shift ;;
    -l|--lines) LINES="$2"; shift ;;
    -S|--socket) SOCKET="$2"; shift ;;
    *) usage ;;
  esac
  shift
done

if [ -z "$TARGET" ] || [ -z "$PATTERN" ]; then
  usage
fi

START=$(date +%s)

while true; do
  OUTPUT=$(tmux -S "$SOCKET" capture-pane -p -t "$TARGET" -S "-$LINES" || true)

  if [ "$FIXED" -eq 1 ]; then
    if echo "$OUTPUT" | grep -Fq "$PATTERN"; then
      echo "Matched fixed string: $PATTERN"
      exit 0
    fi
  else
    if echo "$OUTPUT" | grep -Eq "$PATTERN"; then
      echo "Matched regex pattern: $PATTERN"
      exit 0
    fi
  fi

  NOW=$(date +%s)
  if [ $((NOW - START)) -ge "$TIMEOUT" ]; then
    echo "Timeout reached after $TIMEOUT seconds waiting for pattern: $PATTERN"
    exit 1
  fi

  sleep "$INTERVAL"
done
