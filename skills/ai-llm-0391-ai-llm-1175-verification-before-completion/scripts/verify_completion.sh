#!/bin/bash
# Wrapper script to enforce verification before completion

COMMAND=$@

if [ -z "$COMMAND" ]; then
    echo "Usage: ./verify_completion.sh <command to verify>"
    echo "Example: ./verify_completion.sh npm test"
    exit 1
fi

echo "Running verification command: $COMMAND"
echo "----------------------------------------"
$COMMAND
RESULT=$?
echo "----------------------------------------"

if [ $RESULT -eq 0 ]; then
    echo "✅ Verification passed! You may claim success."
else
    echo "❌ Verification failed. Fix the issues before claiming completion."
    exit 1
fi
