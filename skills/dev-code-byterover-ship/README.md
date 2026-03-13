# ByteRover Ship & Handoff

Complete milestones with retrospective and archival, or pause work with resumable handoff context.

## What it does

Serves two purposes depending on intent:

### Ship (milestone completion)
1. **Pre-Flight Audit** — Verifies all phases are complete, requirements covered, tests pass
2. **Retrospective and Stats** — Gathers commit counts, files changed, and key accomplishments from phase summaries
3. **Project Evolution** — Migrates requirements to Validated, updates project record, notes carried tech debt, optionally creates a git tag

### Pause (work handoff)
1. **Capture State** — Records current phase/task position, completed work, remaining items, decisions, and blockers
2. **Store Handoff** — Compresses everything into a resumable handoff via `brv curate` so a future session can pick up seamlessly

## When to use

- All phases in a milestone are complete and ready to ship
- When `byterover-progress` indicates the milestone is ready
- When you need to pause work mid-phase and resume later
- At the end of a sprint or development cycle

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)

## Key principles

- **Verify before shipping** — all phases complete, tests should pass
- **Accomplishments are specific** — concrete outcomes, not vague summaries
- **Handoffs must be resumable** — enough context for a fresh agent to continue
- **Git tags are optional** — always asks the user first

## Output

**Ship:** Retrospective with stats, validated requirements, optional git tag, and recommendation to run `byterover-milestone` for the next cycle.

**Pause:** Stored handoff context with resume instructions via `byterover-progress`.

## License

MIT
