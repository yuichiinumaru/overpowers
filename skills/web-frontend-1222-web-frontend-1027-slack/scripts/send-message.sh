#!/bin/bash
# Helper script to send a Slack message using a token
# Usage: ./send-message.sh <channel_id> <message_text> [token]

CHANNEL=$1
TEXT=$2
TOKEN=${3:-$SLACK_BOT_TOKEN}

if [ -z "$CHANNEL" ] || [ -z "$TEXT" ]; then
  echo "Usage: $0 <channel_id> <message_text> [token]"
  exit 1
fi

if [ -z "$TOKEN" ]; then
  echo "Error: Slack token not provided and SLACK_BOT_TOKEN not set."
  exit 1
fi

curl -s -X POST -H "Authorization: Bearer $TOKEN" \
     -H "Content-type: application/json; charset=utf-8" \
     --data "{\"channel\":\"$CHANNEL\",\"text\":\"$TEXT\"}" \
     https://slack.com/api/chat.postMessage
