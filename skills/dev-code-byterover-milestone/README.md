# ByteRover Milestone Planning

Define project milestones with goals, scoped requirements, phased roadmaps, and implementation decisions.

## What it does

Guides an AI agent through a 6-phase milestone planning workflow:

1. **Query Existing State** — Checks the knowledge base for project history, shipped milestones, and active requirements
2. **Goal Gathering** — Establishes project purpose, core value proposition, and 3-7 high-level capabilities through user conversation
3. **Requirements Scoping** — Breaks capabilities into testable requirements with REQ-IDs, scoped as MVP / Future / Out of Scope
4. **Phase Roadmap** — Derives 3-7 ordered phases from MVP requirements using goal-backward analysis, each with success criteria
5. **Gray Area Discussion** (optional) — Captures implementation decisions for ambiguous areas before planning begins
6. **Store Milestone** — Curates project definition, requirements, roadmap, and decisions via `brv curate`

## When to use

- Starting a new project or product initiative
- Beginning the next cycle of work after shipping a milestone
- When scope is unclear and needs structured analysis
- When multiple features need to be organized into phases

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)
- A description of what to build or what the next milestone should achieve

## Key principles

- **Requirements must be testable** — concrete outcomes, not vague descriptions
- **Every requirement gets a REQ-ID** — enables traceability across phases and milestones
- **Goal-backward** — derive phases from outcomes, not tasks
- **100% coverage** — every MVP requirement maps to exactly one phase
- **No scope creep** — defer new capabilities discovered during discussion

## Output

A complete milestone definition including named requirements with REQ-IDs, a phased roadmap with success criteria, and optionally captured implementation decisions. Next step: run `byterover-plan` for Phase 1.

## License

MIT
