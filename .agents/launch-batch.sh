#!/bin/bash
# Batch Launch Script for Paralellizable Tasks in Overpowers
# Usage: ./.agents/launch-batch.sh
# Note: Launch in sets to avoid rate limits

export PATH=$PATH:/usr/local/bin:/usr/bin:/bin:/home/sephiroth/.local/bin
cd "/home/sephiroth/Work/overpowers" || exit 1

echo "=========================================================="
echo "🚀 INICIANDO ONDA DE TAREFAS PARALELAS OVERPOWERS 🚀"
echo "=========================================================="

# Tarefas a serem executadas
WAVE=(
    "001-feature-mcp-integrations.md"
    "002-feature-advanced-hooks.md"
    "003-refactor-moltbot-memory.md"
)

# Qual prompt usar? (foreman, common, etc)
PROMPT_NAME="foreman"

# Convert array to a comma-separated string
TASKS_STR=$(IFS=,; echo "${WAVE[*]}")

echo "Disparando ${#WAVE[@]} tarefas para o agente usando o prompt '${PROMPT_NAME}'..."
# Insira aqui o caminho do seu script orquestrador local do overpowers, ex:
# ./scripts/jules-launcher.sh -r overpowers -p "$PROMPT_NAME" -t "$TASKS_STR"
# Ou então os comandos via CLI do Jules:
for task in "${WAVE[@]}"; do
    # Isso simula o disparo. Substitua pelo jules remote new real ou seu script launcher.
    echo " -> jules remote new --prompt .agents/prompts/${PROMPT_NAME}.md --task docs/tasks/${task}"
done

echo "=========================================================="
echo "✅ ONDA LANÇADA."
echo "=========================================================="
