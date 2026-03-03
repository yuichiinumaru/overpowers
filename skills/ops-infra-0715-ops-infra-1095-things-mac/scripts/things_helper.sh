#!/bin/bash
# Helper for Things 3 CLI

COMMAND=$1
shift

case $COMMAND in
  "today")
    things today "$@"
    ;;
  "inbox")
    things inbox --limit 50 "$@"
    ;;
  "add")
    TITLE=$1
    shift
    things add "$TITLE" "$@"
    ;;
  "search")
    QUERY=$1
    shift
    things search "$QUERY" "$@"
    ;;
  *)
    echo "Usage: $0 {today|inbox|add|search} [args]"
    exit 1
    ;;
esac
