#!/bin/bash
# Helper script to react to a Slack message
# Usage: ./react.sh <channel_id> <timestamp> <emoji> [token]

CHANNEL=$1
TIMESTAMP=$2
EMOJI=$3
TOKEN=${4:-$SLACK_BOT_TOKEN}

if [ -z "$CHANNEL" ] || [ -z "$TIMESTAMP" ] || [ -z "$EMOJI" ]; then
  echo "Usage: $0 <channel_id> <timestamp> <emoji> [token]"
  exit 1
fi

if [ -z "$TOKEN" ]; then
  echo "Error: Slack token not provided and SLACK_BOT_TOKEN not set."
  exit 1
fi

curl -s -X POST -H "Authorization: Bearer $TOKEN" \
     -H "Content-type: application/json; charset=utf-8" \
     --data "{\"channel\":\"$CHANNEL\",\"timestamp\":\"$TIMESTAMP\",\"name\":\"$EMOJI\"}" \
     https://slack.com/api/reactions.add
