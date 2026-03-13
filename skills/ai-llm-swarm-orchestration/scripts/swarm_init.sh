#!/bin/bash
# Swarm Initialization Helper

if [ -z "$1" ]; then
    TOPOLOGY="mesh"
else
    TOPOLOGY="$1"
fi

if [ -z "$2" ]; then
    MAX_AGENTS=5
else
    MAX_AGENTS="$2"
fi

echo "--- Swarm Initialization Procedure ---"
echo "Topology: $TOPOLOGY"
echo "Max Agents: $MAX_AGENTS"
echo ""
echo "Step 1: Initialize the swarm"
echo "Command: npx agentic-flow hooks swarm-init --topology $TOPOLOGY --max-agents $MAX_AGENTS"
echo ""
echo "Step 2: Spawn initial agents"
echo "Command: npx agentic-flow hooks agent-spawn --type coder"
echo "Command: npx agentic-flow hooks agent-spawn --type reviewer"
echo ""
echo "Step 3: Monitor swarm status"
echo "Command: npx agentic-flow hooks swarm-status"
