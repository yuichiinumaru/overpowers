#!/bin/bash

# Wrapper script to spawn a Hive Mind swarm with specific options

if [ -z "$1" ]; then
  echo "Usage: hive_mind_spawn.sh <objective> [queen-type] [consensus-algorithm] [max-workers]"
  echo "Example: hive_mind_spawn.sh \"Build microservices architecture\" strategic byzantine 8"
  exit 1
fi

OBJECTIVE=$1
QUEEN_TYPE=${2:-"strategic"}
CONSENSUS=${3:-"majority"}
MAX_WORKERS=${4:-"8"}

echo "🚀 Spawning Hive Mind Swarm..."
echo "Objective: $OBJECTIVE"
echo "Queen Type: $QUEEN_TYPE"
echo "Consensus: $CONSENSUS"
echo "Max Workers: $MAX_WORKERS"

npx claude-flow hive-mind spawn "$OBJECTIVE" \
  --queen-type "$QUEEN_TYPE" \
  --consensus "$CONSENSUS" \
  --max-workers "$MAX_WORKERS"

if [ $? -eq 0 ]; then
  echo "✅ Hive Mind swarm spawned successfully."
else
  echo "❌ Failed to spawn Hive Mind swarm."
fi
