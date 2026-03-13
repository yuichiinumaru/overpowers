# ByteRover Knowledge Audit

Audit the health of your ByteRover knowledge base. Finds stale entries, missing coverage, and provides actionable remediation commands.

## What it does

Guides an AI agent through a 5-phase audit process:

1. **Inventory** — Queries all major knowledge domains to understand current coverage
2. **Cross-Reference** — Verifies documented knowledge against the actual codebase (deps, architecture, conventions, tests, integrations)
3. **Staleness Detection** — Flags entries where referenced files, functions, or patterns no longer match reality
4. **Gap Analysis** — Identifies undocumented modules, config, endpoints, and patterns
5. **Coverage Report** — Produces a structured summary table with prioritized `brv curate` commands to fix every finding

## When to use

- After major refactors or dependency upgrades
- Periodically (monthly or per sprint) to maintain knowledge quality
- When suspecting knowledge drift
- Before starting work in an area with existing documentation

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)
- An existing knowledge base (run `byterover-explore` first if starting from scratch)

## Output

A structured coverage report with:

- Domain-level status table (Current / Stale / Missing)
- Stale entries with severity ratings and exact `brv curate` fix commands
- Gap entries with exact `brv curate` fill commands

## License

MIT
