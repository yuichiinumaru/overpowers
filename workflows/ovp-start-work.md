---
name: start-work
description: "Start Sisyphus work session from Prometheus plan. Looks for plans in .sisyphus/plans/, updates boulder.json state, and begins execution."
---

You are starting a Sisyphus work session.

## WHAT TO DO

1. **Context Initialization (Explicit Memory Read)**: 
   - Read `.agents/continuity-<agent-name>.md` and check `.agents/memories/` for the current strategic focus.

2. **Find available plans**: Search for Prometheus-generated plan files at `.sisyphus/plans/`

3. **Check for active boulder state**: Read `.sisyphus/boulder.json` if it exists

4. **Decision logic**:
   - If \`.sisyphus/boulder.json\` exists AND plan is NOT complete (has unchecked boxes):
     - **APPEND** current session to session_ids
     - Continue work on existing plan
   - If no active plan OR plan is complete:
     - List available plan files
     - If ONE plan: auto-select it
     - If MULTIPLE plans: show list with timestamps, ask user to select

5. **Create/Update boulder.json & Memory**:
   - **Explicit Memory Update**: Sync the selected plan as the "Current Focus" in `.agents/continuity-<agent-name>.md`.
   \`\`\`json
   {
     "active_plan": "/absolute/path/to/plan.md",
     "started_at": "ISO_TIMESTAMP",
     "session_ids": ["session_id_1", "session_id_2"],
     "plan_name": "plan-name"
   }
   \`\`\`

6. **Read the plan file** and start executing tasks according to Orchestrator Sisyphus workflow

## CRITICAL

- Always update boulder.json BEFORE starting work
- Read the FULL plan file before delegating any tasks
- Follow Orchestrator Sisyphus delegation protocols (7-section format)
