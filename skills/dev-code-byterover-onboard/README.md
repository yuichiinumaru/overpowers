# ByteRover Project Onboarding

Interactive knowledge-driven project onboarding. Get up to speed quickly using ByteRover's accumulated knowledge.

## What it does

Guides an AI agent through a 5-phase onboarding workflow:

1. **Knowledge Retrieval** — Queries all six major domains (stack, architecture, conventions, testing, integrations, concerns)
2. **Assess Completeness** — Rates each domain as Comprehensive / Partial / Missing
3. **Structured Overview** — Synthesizes knowledge into a scannable onboarding guide covering project summary, architecture, development guide, testing, key concerns, and getting started
4. **Gap Identification** — Highlights missing or incomplete domains with actionable next steps
5. **Curate Discoveries** — Stores any new insights that emerge during the onboarding session

## When to use

- Starting work on an unfamiliar project
- New team member needs to ramp up quickly
- Returning to a project after a long break
- Need a quick overview of project state and conventions

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)
- Ideally an existing knowledge base from a prior `byterover-explore` run (if empty, the skill recommends running explore first)

## Key principles

- **Knowledge-only** — presents what's in the knowledge base, never fabricates information
- **Honest about gaps** — if a domain has no knowledge, says so and suggests explore
- **Practical first** — prioritizes "how to run/test/deploy" over theoretical architecture
- **Curate discoveries** — stores new insights found during onboarding for future sessions

## Output

A structured onboarding guide with coverage ratings per domain, practical getting-started information, identified knowledge gaps, and suggested next steps.

## License

MIT
