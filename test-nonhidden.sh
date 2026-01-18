#!/bin/bash
# Test script to verify if the issue is with hidden directories or security
# Run from: /home/sephiroth/.config/opencode/Overpowers

export OPENCODE_PERMISSION='"allow"'

MODEL="google/antigravity-claude-sonnet-4-5-thinking"
TEST_DIR="/home/sephiroth/work"

echo "🧪 Testing subagent with NON-HIDDEN directory"
echo "📁 Target: $TEST_DIR"
echo ""

opencode run "Execute: ls -la $TEST_DIR | head -20

Só liste o resultado do comando acima, nada mais." \
  --model "$MODEL" \
  2>&1

echo ""
echo "✅ Test complete"
