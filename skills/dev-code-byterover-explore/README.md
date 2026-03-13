# ByteRover Explore

Systematically explore a codebase and curate findings into ByteRover's context tree.

## What it does

Guides an AI agent through a 3-phase exploration workflow:

1. **Check Existing Knowledge** — Queries ByteRover to avoid duplicate work and identify areas to refresh
2. **Codebase Mapping** — Explores six domains and curates findings via `brv curate`:
   - Technology stack (languages, frameworks, dependencies)
   - Architecture and structure (directories, layers, entry points)
   - Conventions and patterns (naming, style, error handling)
   - Testing patterns (framework, organization, mocking)
   - Integrations (APIs, databases, auth, third-party services)
   - Concerns and technical debt (TODOs, fragile areas, security risks)
3. **Documentation and Knowledge Gaps** — Assesses existing documentation quality and identifies areas still missing coverage

## When to use

- Starting work on an unfamiliar codebase
- Onboarding to a new project
- Building a comprehensive knowledge base from scratch
- Refreshing knowledge after major changes

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)

## Key principles

- **Never read secrets** — skip `.env`, credential files, and similar
- **File paths required** — every finding references specific files
- **Be prescriptive** — concrete patterns, not vague observations
- **Let ByteRover read files** — use `-f` flags (max 5 per command)

## Output

A comprehensive knowledge base covering all six domains, plus a report of key findings, remaining gaps, and suggested next steps.

## License

MIT
