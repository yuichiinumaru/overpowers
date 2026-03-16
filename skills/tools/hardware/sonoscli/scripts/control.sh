#!/bin/bash
# Helper script to control Sonos speakers
# Usage: ./control.sh <action> <speaker_name> [args...]

ACTION=$1
NAME=$2
shift 2

if [ -z "$ACTION" ] || [ -z "$NAME" ]; then
  echo "Usage: $0 <action> <speaker_name> [args...]"
  echo "Actions: play, pause, stop, status, volume"
  exit 1
fi

case "$ACTION" in
  volume)
    sonos volume set "$1" --name "$NAME"
    ;;
  *)
    sonos "$ACTION" "$@" --name "$NAME"
    ;;
esac
