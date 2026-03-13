# ByteRover Systematic Debugging

Investigate bugs using the scientific method, powered by ByteRover's persistent knowledge of past issues and project patterns.

## What it does

Guides an AI agent through a 6-phase hypothesis-driven debugging process:

1. **Query Known Issues** — Checks ByteRover for past fixes and similar symptoms before investigating from scratch
2. **Gather Evidence** — Records precise symptoms, error messages, reproduction steps, and scope
3. **Form Hypotheses** — Creates 2-3 specific, falsifiable hypotheses ranked by likelihood
4. **Test Hypotheses** — Tests one variable at a time, documenting confirmations and eliminations
5. **Root Cause and Fix** — Applies the minimal fix targeting the root cause, then verifies with tests
6. **Curate** — Stores the root cause, fix, and general pattern via `brv curate` for future sessions

## When to use

- When encountering a bug or unexpected behavior
- When a test fails unexpectedly
- When behavior doesn't match documented expectations
- When debugging a regression

## Prerequisites

- ByteRover CLI installed and configured (`brv status` should succeed)
- A clear symptom description from the user (what happened vs. what was expected)

## Key principles

- **Never guess** — form hypotheses and test them
- **One variable at a time** — change one thing, observe, document
- **Fix the cause, not the symptom** — a swallowed error is not a fix
- **Always curate** — store findings to build institutional memory

## Output

A structured debugging report including root cause with evidence, fix applied, test verification results, eliminated hypotheses, and knowledge stored for future reference.

## License

MIT
