# ByteRover Code Review

Review code changes against stored conventions, patterns, architecture decisions, and security standards.

## What it does

Guides an AI agent through a 6-phase knowledge-driven code review:

1. **Load Project Context** — Queries the knowledge base for conventions, architecture patterns, testing standards, and security patterns
2. **Identify Changes** — Determines what to review (staged, unstaged, or specific files) and categorizes by type
3. **Convention Compliance** — Checks naming, imports, code style, and error handling against documented standards
4. **Architecture and Pattern Check** — Verifies layer boundaries, pattern compliance, dependency direction, and API consistency
5. **Test and Security Check** — Validates test coverage for changed files and scans for security concerns (hardcoded secrets, injection vectors, auth gaps)
6. **Curate New Patterns** — Stores newly discovered conventions or concerns back into the knowledge base

## When to use

- Before committing changes
- During pull request reviews
- After receiving code from other agents or developers
- When unsure if changes follow project conventions

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)
- Something to review: staged changes, unstaged changes, or specific file paths

## Key principles

- **Knowledge-first** — base reviews on documented standards, not personal preference
- **Distinguish severity** — clearly separate blocking issues from suggestions
- **Be specific** — reference file paths, line numbers, and the exact convention violated
- **No false positives** — only flag issues where a documented standard or clear security concern exists

## Output

A structured review report with blocking issues (must fix), suggestions (nice to have), newly curated patterns, and areas missing knowledge base coverage.

## License

MIT
