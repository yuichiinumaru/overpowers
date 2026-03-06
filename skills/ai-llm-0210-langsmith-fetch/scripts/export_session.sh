#!/bin/bash
# Export debug session from LangSmith

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
SESSION_DIR="langsmith-debug/session-$TIMESTAMP"

echo "📂 Creating session directory: $SESSION_DIR"
mkdir -p "$SESSION_DIR"

# Export traces
echo "📥 Exporting traces..."
langsmith-fetch traces "$SESSION_DIR/traces" --last-n-minutes 30 --limit 50 --include-metadata

# Export threads (conversations)
echo "📥 Exporting threads..."
langsmith-fetch threads "$SESSION_DIR/threads" --limit 20

echo ""
echo "✅ Session exported successfully!"
echo "Location: $SESSION_DIR"
