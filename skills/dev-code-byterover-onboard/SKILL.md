---
name: byterover-onboard
description: "Interactive knowledge-driven project onboarding. Queries comprehensive knowledge across all domains, presents a structured project overview, identifies knowledge gaps, and suggests running explore to fill them."
---

# ByteRover Project Onboarding

A structured workflow for getting up to speed on a project using ByteRover's accumulated knowledge. Presents a comprehensive overview and identifies areas needing further exploration.

## When to Use

- Starting work on an unfamiliar project
- When a new team member needs to get up to speed quickly
- When returning to a project after a long break
- When you need a quick overview of project state and conventions

## Prerequisites

Run `brv status` first. If errors occur, instruct the user to resolve them in the brv terminal. See the byterover skill's TROUBLESHOOTING.md for details.

The project should ideally have existing knowledge from a prior `byterover-explore` run. If the knowledge base is empty, recommend running `byterover-explore` first for best results.

## Process

### Phase 1: Comprehensive Knowledge Retrieval

Query every major knowledge domain to build a complete picture:

```bash
brv query "What is the technology stack — languages, frameworks, and key dependencies?"
brv query "What is the architecture — directory structure, layers, data flow, and entry points?"
brv query "What coding conventions and patterns are used — naming, imports, error handling?"
brv query "What testing approach is used — framework, patterns, organization?"
brv query "What external integrations exist — APIs, databases, auth providers, services?"
brv query "What concerns exist — tech debt, known issues, fragile areas, security risks?"
```

Save the responses for synthesis in Phase 3.

### Phase 2: Assess Knowledge Completeness

For each domain, rate coverage:

| Domain | Rating | Criteria |
|--------|--------|----------|
| Technology Stack | Comprehensive / Partial / Missing | Lists specific deps, versions, runtime |
| Architecture | Comprehensive / Partial / Missing | Describes layers, data flow, entry points |
| Conventions | Comprehensive / Partial / Missing | Specifies naming, imports, error handling |
| Testing | Comprehensive / Partial / Missing | Names framework, patterns, organization |
| Integrations | Comprehensive / Partial / Missing | Lists specific services, configs |
| Concerns | Comprehensive / Partial / Missing | References specific files, issues |

- **Comprehensive** — Detailed, specific, references file paths
- **Partial** — Some knowledge exists but lacks specificity or is incomplete
- **Missing** — No knowledge returned or only vague generalities

### Phase 3: Present Structured Overview

Synthesize retrieved knowledge into a structured onboarding guide:

#### Project Summary
- What the project does (purpose and scope)
- Technology stack (languages, runtime, key frameworks)
- Key dependencies and their roles

#### Architecture
- Directory structure and what lives where
- Architectural layers and their responsibilities
- Data flow (how requests/data move through the system)
- Entry points (where execution begins)

#### Development Guide
- Coding conventions (naming, imports, code style)
- Common patterns to follow (with examples from knowledge base)
- Error handling approach
- How to add new features (where to put code, what patterns to use)

#### Testing
- Test framework and runner
- Where tests live and naming conventions
- How to write tests (mocking, fixtures, assertions)
- How to run tests

#### Key Concerns
- Known tech debt and its location
- Fragile areas to be careful with
- Known issues and workarounds
- Security considerations

#### Getting Started
- How to set up the development environment
- How to run the project locally
- How to run tests
- Key configuration files

Present each section only if knowledge exists for it. Skip sections where the knowledge base returned nothing — don't fabricate information.

### Phase 4: Identify Gaps and Suggest Next Steps

For domains rated as **Partial** or **Missing**:

```
Knowledge gaps found:
- [Domain]: [What's missing]
  → Run byterover-explore to map this area
  → Or curate manually: brv curate "[domain]: [description]" -f [files]
```

If the user has specific questions about the project:
1. Query the knowledge base for an answer
2. If the answer is comprehensive, present it
3. If the answer is incomplete, note the gap and suggest exploring that area

### Phase 5: Curate Onboarding Notes

If the onboarding process reveals new insights — for example, the user asks a question that leads to reading code and discovering undocumented behavior:

```bash
brv curate "[domain]: [new insight discovered during onboarding]" -f [relevant files]
```

This builds the knowledge base for future onboarding sessions.

### Completion

Present the full onboarding summary to the user:

1. **Overview completeness** — How much of the project is documented (X/6 domains covered)
2. **Key takeaways** — The most important things to know before starting work
3. **Gaps found** — What's missing and how to fill it
4. **Suggested next steps:**
   - Run `byterover-explore` for missing domains
   - Start with a specific area based on the user's goals
   - Review specific files for hands-on understanding

## Important Rules

1. **Never read secrets** — Skip `.env`, credential files, and similar
2. **Knowledge-only** — Present what's in the knowledge base; do not fabricate information
3. **Be honest about gaps** — If a domain has no knowledge, say so and suggest explore
4. **Practical first** — Prioritize "how to run/test/deploy" over theoretical architecture
5. **Structured presentation** — Use clear sections and tables for scanability
6. **Suggest explore, not manual investigation** — When gaps exist, recommend `byterover-explore` rather than asking the agent to manually explore
7. **Curate discoveries** — If new insights emerge during onboarding, store them
8. **Max 5 files per curate** — Break down large curate operations if needed
9. **Verify curations** — After storing critical context, run `brv curate view <logId>` to confirm what was stored (logId is printed by `brv curate` on completion). Run `brv curate view --help` to see all options.
