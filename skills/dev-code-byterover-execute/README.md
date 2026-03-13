# ByteRover Phase Execution

Execute implementation plans task by task with verification, atomic commits, and persistent progress tracking.

## What it does

Guides an AI agent through a 4-phase execution workflow:

1. **Load Phase Context** — Queries the knowledge base for the plan, completed tasks, success criteria, and conventions
2. **Execute Tasks** — Implements each task sequentially: describe, implement, verify, commit, and record progress
3. **Verify Phase Goal** — Checks every success criterion (PASS / FAIL / NEEDS HUMAN TESTING) before closing the phase
4. **Phase Summary and Transition** — Stores accomplishments, updates project status, and prepares for the next phase

## When to use

- After creating a plan with `byterover-plan` and ready to implement
- When `byterover-progress` routes you to execute a planned phase
- To resume execution of a partially completed phase

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)
- A plan in the knowledge base (created via `byterover-plan`)

## Dependencies

- `byterover-plan` — plans must exist before execution

## Key principles

- **One task at a time** — complete and verify before moving on
- **Atomic commits** — one commit per task with a descriptive message
- **Verify against criteria** — check success criteria, not just task completion
- **Record everything** — curate completions, summaries, and decisions
- **Follow the plan** — raise concerns before deviating

## Output

A structured phase completion report including accomplishments, verification results for each success criterion, next phase recommendation, and overall milestone progress.

## License

MIT
