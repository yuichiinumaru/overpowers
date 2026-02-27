#!/bin/bash
# Test script for parallel subagents with OPENCODE_PERMISSION
# Run from: /home/sephiroth/.config/opencode/Overpowers

export OPENCODE_PERMISSION='"allow"'

ARCHIVE="/home/sephiroth/.config/opencode/archive"
OUTPUT_DIR="/home/sephiroth/.config/opencode/Overpowers/docs"
MODEL="google/antigravity-gemini-3-flash"

# Test with just ONE repo first
REPO="AIPex"

echo "🧪 Testing subagent with OPENCODE_PERMISSION=allow"
echo "📁 Repo: $ARCHIVE/$REPO"
echo "📤 Output: $OUTPUT_DIR/02-$REPO.md"
echo ""

# Use --agent plan for read-only analysis (less permission issues)
opencode run "Analise o repositório em $ARCHIVE/$REPO.

Use os comandos bash disponíveis para:
1. ls -la $ARCHIVE/$REPO 
2. cat $ARCHIVE/$REPO/README.md (se existir)
3. find $ARCHIVE/$REPO -name '*.md' -type f | head -10

OUTPUT (máximo 20 linhas):
## Repositório: $REPO
## O que é
## Assets úteis (se houver)" \
  --model "$MODEL" \
  --agent build \
  2>&1 | tee "$OUTPUT_DIR/02-$REPO.md"

echo ""
echo "✅ Done! Check: $OUTPUT_DIR/02-$REPO.md"
