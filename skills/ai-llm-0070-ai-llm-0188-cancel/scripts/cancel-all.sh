#!/bin/bash

# Force clear all OMC state files
echo "Force clearing all OMC state..."

# State files to remove
FILES=(
  ".omc/state/autopilot-state.json"
  ".omc/state/ralph-state.json"
  ".omc/state/ralph-plan-state.json"
  ".omc/state/ralph-verification.json"
  ".omc/state/ultrawork-state.json"
  ".omc/state/ecomode-state.json"
  ".omc/state/ultraqa-state.json"
  ".omc/state/swarm.db"
  ".omc/state/swarm.db-wal"
  ".omc/state/swarm.db-shm"
  ".omc/state/swarm-active.marker"
  ".omc/state/swarm-tasks.db"
  ".omc/state/ultrapilot-state.json"
  ".omc/state/ultrapilot-ownership.json"
  ".omc/state/pipeline-state.json"
  ".omc/state/plan-consensus.json"
  ".omc/state/ralplan-state.json"
  ".omc/state/boulder.json"
  ".omc/state/hud-state.json"
  ".omc/state/subagent-tracking.json"
  ".omc/state/subagent-tracker.lock"
  ".omc/state/rate-limit-daemon.pid"
  ".omc/state/rate-limit-daemon.log"
  ".omc/state/team-mcp-workers.json"
)

for f in "${FILES[@]}"; do
  if [ -f "$f" ]; then
    rm -f "$f"
    echo "Removed: $f"
  fi
done

# Directories to remove
DIRS=(
  ".omc/state/checkpoints/"
  ".omc/state/sessions/"
  ".omc/state/team-bridge/"
)

for d in "${DIRS[@]}"; do
  if [ -d "$d" ]; then
    rm -rf "$d"
    echo "Removed directory: $d"
  fi
done

# Kill tmux sessions
echo "Killing omc-team-* tmux sessions..."
tmux list-sessions -F '#{session_name}' 2>/dev/null | grep '^omc-team-' | while read s; do
  tmux kill-session -t "$s" 2>/dev/null
  echo "Killed tmux session: $s"
done

echo "All OMC modes cleared."
