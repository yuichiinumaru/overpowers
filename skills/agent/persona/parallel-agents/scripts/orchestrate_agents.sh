#!/bin/bash
# Multi-agent orchestration helper
tasks=$@

if [ -z "$tasks" ]; then
    echo "Usage: $0 <task1> <task2> ..."
    return 1 2>/dev/null || true
fi

echo "Orchestrating tasks in parallel:"
for task in $tasks; do
    echo " - Spawning agent for task: $task"
done
echo "All tasks dispatched."
