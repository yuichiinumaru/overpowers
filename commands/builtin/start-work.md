---
name: start-work
description: "Start Sisyphus work session from Prometheus plan. Looks for plans in .sisyphus/plans/, updates boulder.json state, and begins execution."
---

You are starting a Sisyphus work session.

## WHAT TO DO

1. **Find available plans**: Search for Prometheus-generated plan files at \`.sisyphus/plans/\`

2. **Check for active boulder state**: Read \`.sisyphus/boulder.json\` if it exists

3. **Decision logic**:
   - If \`.sisyphus/boulder.json\` exists AND plan is NOT complete (has unchecked boxes):
     - **APPEND** current session to session_ids
     - Continue work on existing plan
   - If no active plan OR plan is complete:
     - List available plan files
     - If ONE plan: auto-select it
     - If MULTIPLE plans: show list with timestamps, ask user to select

4. **Create/Update boulder.json**:
   \`\`\`json
   {
     "active_plan": "/absolute/path/to/plan.md",
     "started_at": "ISO_TIMESTAMP",
     "session_ids": ["session_id_1", "session_id_2"],
     "plan_name": "plan-name"
   }
   \`\`\`

5. **Read the plan file** and start executing tasks according to Orchestrator Sisyphus workflow

## CRITICAL

- Always update boulder.json BEFORE starting work
- Read the FULL plan file before delegating any tasks
- Follow Orchestrator Sisyphus delegation protocols (7-section format)
