#!/bin/bash

AGENT=${1:-"claude"}
PROMPT=$2

if [ -z "$PROMPT" ]; then
    echo "Usage: $0 [agent: claude|codex|opencode|pi] <prompt>"
    exit 1
fi

echo "Starting $AGENT in a scratch git repo..."

# Create a temp directory
SCRATCH=$(mktemp -d)
cd "$SCRATCH" || exit 1

# Initialize git (required by some agents like Codex)
git init -q
touch README.md
git add README.md
git commit -m "initial commit" -q

echo "Scratch directory: $SCRATCH"
echo "Running agent..."

case "$AGENT" in
    "codex")
        codex exec "$PROMPT"
        ;;
    "claude")
        claude "$PROMPT"
        ;;
    "opencode")
        opencode run "$PROMPT"
        ;;
    "pi")
        pi "$PROMPT"
        ;;
    *)
        echo "Unknown agent: $AGENT"
        exit 1
        ;;
esac

echo "Agent execution finished. Remember to clean up $SCRATCH if not needed."
