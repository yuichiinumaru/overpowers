---
name: multi-agent-file-coordination
description: Protocol for multiple agents to work on the same codebase simultaneously without conflicts using a lock-based system. Use when coordinating parallel agent work on shared files.
---

# Multi-Agent File Coordination Protocol

Based on the `cooperating_agents_improvement_prompt_for_python_fastapi_postgres.txt` from the Claude Code Agent Farm.

## Distributed Coordination Protocol

This protocol allows multiple agents to work on the same codebase simultaneously without conflicts using a lock-based system in a `/coordination/` directory.

### Coordination Structure
```
/coordination/
├── active_work_registry.json     # Central registry of all active work
├── completed_work_log.json       # Log of completed tasks  
├── agent_locks/                  # Directory for individual agent locks
│   └── {agent_id}_{timestamp}.lock
└── planned_work_queue.json       # Queue of planned but not started work
```

### Protocol Steps

1. **Unique Agent Identity**: Generate a unique ID (`agent_{timestamp}_{random_4_chars}`).
2. **Work Claiming Process**:
   - Check `active_work_registry.json` for conflicts.
   - Create a lock file in `agent_locks/` claiming specific files and features.
   - Register the work plan with detailed scope information in `active_work_registry.json`.
3. **Conflict Prevention**: 
   - NEVER modify a file locked by another agent.
   - If a file you need is locked, wait or select different work.
   - Handle stale locks (>2 hours old) by checking if the agent process is still active.
4. **Completion**:
   - Log completed tasks in `completed_work_log.json`.
   - Remove the lock file and entry from `active_work_registry.json`.
