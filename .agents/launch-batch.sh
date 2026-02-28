#!/bin/bash
# Batch Launch Script for Paralellizable Tasks in Overpowers
# Usage: ./.agents/launch-batch.sh
# Note: Launch in sets to avoid rate limits

export PATH=$PATH:/usr/local/bin:/usr/bin:/bin:/home/sephiroth/.local/bin
cd "/home/sephiroth/Work/overpowers" || exit 1

echo "=========================================================="
echo "🚀 INICIANDO ONDA DE TAREFAS PARALELAS OVERPOWERS 🚀"
echo "=========================================================="

# ── Wave 1: Deduplication + Rename (safe parallelism — different dirs) ──
WAVE=(
    "004-dedup-docs-docs.md"
    "005-dedup-docs-analysis.md"
    "006-dedup-docs-knowledge.md"
    "007-rename-superpowers-to-overpowers.md"
)

# ── Wave 2: Feature implementation (depends on clean repo state) ──
# WAVE=(
#     "001-feature-mcp-integrations.md"
#     "002-feature-advanced-hooks.md"
#     "003-refactor-moltbot-memory.md"
# )

# Qual prompt usar? (foreman, common, etc)
PROMPT_NAME="foreman"
PROMPT_PATH=".agents/prompts/${PROMPT_NAME}.md"
COMMON_PATH=".agents/prompts/common.md"

echo "Disparando ${#WAVE[@]} tarefas usando prompt '${PROMPT_NAME}'..."
echo ""

for task in "${WAVE[@]}"; do
    TASK_PATH="docs/tasks/${task}"
    TASK_NAME="${task%.md}"

    if [ ! -f "$TASK_PATH" ]; then
        echo "⚠️  Arquivo não encontrado: $TASK_PATH — pulando."
        continue
    fi

    echo "🚀 Lançando: ${TASK_NAME}"
    
    # Read the prompt + common preamble + task file and compose the instruction
    INSTRUCTION=$(cat <<EOF
You are working on the Overpowers toolkit repository.

$(cat "$COMMON_PATH" 2>/dev/null)

$(cat "$PROMPT_PATH")

--- TASK ---
$(cat "$TASK_PATH")
EOF
)

    # Launch via Jules CLI
    jules remote new "$INSTRUCTION" \
        --repo "yuichiinumaru/overpowers" \
        2>&1 | head -5
    
    echo "   ✅ Task ${TASK_NAME} dispatched."
    echo ""
    
    # Small delay between launches to avoid rate limits
    sleep 2
done

echo "=========================================================="
echo "✅ ONDA LANÇADA. ${#WAVE[@]} tasks disparadas."
echo "=========================================================="
