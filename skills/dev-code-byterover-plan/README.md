# ByteRover Context-Aware Planning

Create structured implementation plans informed by existing knowledge using goal-backward analysis.

## What it does

Guides an AI agent through a 5-phase planning workflow:

1. **Gather Existing Context** — Queries the knowledge base for architecture, conventions, similar implementations, and known concerns in the affected area
2. **Goal-Backward Analysis** — States the desired outcome, derives observable truths that must hold, then identifies required artifacts for each
3. **Task Breakdown** — Decomposes into 3-7 concrete, sequenced tasks with file paths, actions, verification steps, and dependencies
4. **Risk and Concern Check** — Cross-references known issues and tech debt against the plan, adjusting tasks to mitigate risks
5. **Store the Plan** — Curates the complete plan via `brv curate` for future reference and execution

## When to use

- Before implementing a new feature
- When tackling a complex task that needs decomposition
- When planning a refactor across multiple files
- When scope is unclear and needs structured analysis

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)
- A description of what to build or change

## Key principles

- **Goal-backward, not forward** — derive tasks from outcomes, not the other way around
- **Every task needs file paths** — no vague descriptions, specify exactly which files
- **Reuse existing patterns** — reference patterns from the knowledge base
- **Right-size tasks** — 3-7 tasks per plan, each completable in 15-60 minutes
- **Plans must be executable** — specific enough for a different agent to implement without clarification

## Output

A sequenced implementation plan with goal statement, context used, ordered tasks (with files, actions, verification), dependency graph, identified risks, and estimated scope. Ready for execution with `byterover-execute`.

## License

MIT
