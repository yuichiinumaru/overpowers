#!/bin/bash
# Helper script for spogo playback
# Usage: ./spogo-playback.sh <action>

ACTION=$1

if [ -z "$ACTION" ]; then
  echo "Usage: $0 <action>"
  echo "Actions: play, pause, next, prev, status"
  exit 1
fi

if [ "$ACTION" == "status" ]; then
  spogo status
else
  spogo "$ACTION"
fi
