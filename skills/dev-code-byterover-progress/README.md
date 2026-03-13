# ByteRover Project Progress

Check project progress, resume paused work, and get routed to the next action.

## What it does

Guides an AI agent through a 5-phase progress check:

1. **Load Project State** — Queries the knowledge base for milestone, roadmap, phase status, paused work, and pending items
2. **Assess Current Position** — Determines active phase, completion status, blockers, and last activity
3. **Present Status Report** — Formats a clear summary with completed phases, current phase status, and pending items
4. **Route to Next Action** — Recommends the most logical next workflow based on project state (e.g., resume paused work, execute a plan, plan the next phase, ship the milestone)
5. **Update Status** — Curates session state so the next session can resume seamlessly

## Routing logic

| State | Recommendation |
|-------|---------------|
| Paused work exists | Resume from handoff context |
| Phase planned, not executed | Run `byterover-execute` |
| Phase needs a plan | Run `byterover-plan` |
| Phase complete, more remain | Plan the next phase |
| All phases complete | Run `byterover-ship` |
| No project defined | Run `byterover-milestone` |

## When to use

- Starting a new session and need to pick up where you left off
- After being away from a project
- When unsure what to work on next
- To check overall milestone and phase progress

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)

## Output

A formatted progress report with milestone status, phase completion, pending items, and a prioritized recommendation for the next action to take.

## License

MIT
