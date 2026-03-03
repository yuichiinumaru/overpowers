#!/bin/bash
# Quick test script to generate and inject all agents

set -e

cd ~/.config/opencode/Overpowers || cd "$(dirname "$0")/.."

echo "🔧 Step 1: Generating modular agent configs..."
python3 scripts/generators/generate-agent-configs.py

echo ""
echo "💉 Step 2: Injecting agents into opencode.json..."
python3 scripts/utils/inject-agents-to-config.py

echo ""
echo "✅ Done! Check ~/.config/opencode/opencode.json"
echo "🔥 Restart OpenCode to unleash the 390+ agent army!"
