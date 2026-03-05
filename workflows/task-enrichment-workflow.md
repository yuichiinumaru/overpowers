---
description: Enrich an existing task by conducting supplementary research and refining ambiguous specifications.
argument-hint: Task file name or ID (e.g., 0039-ops-sdd-workflows)
---

# /task-enrichment-workflow

**Goal**: Proactively enrich an existing task by conducting supplementary external research, reviewing codebase context, and expanding its specifications to meet strict minimum execution conditions.

## Actions

1. **Task Retrieval & Validation**:
   - Read the target task file in `docs/tasks/`.
   - Ensure the task contains an Objective and Subtasks.
   - Identify ambiguities, vague descriptions, or lack of technical context ("minimum conditions check").

2. **Requirement Clarification**:
   - Identify the core domain, tool, or framework mentioned in the task.
   - Determine what external context or internal codebase locations are necessary to fully specify the "how-to".

3. **Context Gathering (Research)**:
   - **Internal**: Use semantic search (`grep_search` or Serena MCP) to find related files, dependencies, or architectural constraints.
   - **External**: Use web search (`tavily-web`, documentation sites) to acquire best practices, API updates, or external integration steps relevant to the task.

4. **Task Refining & Expansion**:
   - In the target task file, append a new section: `## Enriched Context & Research`.
   - Document the gathered internal constraints and external best practices concisely.
   - Expand the `## Subtasks` section by converting ambiguous bullets into concrete, actionable steps with specific file names, commands, and expected outputs.

5. **Synchronization**:
   - Ensure the updated task aligns with the `AGENTS.md` constitution (e.g., preventing the use of forbidden tools or anti-patterns).
   - Save the enriched file and commit the changes via Jujutsu, indicating the task has been formally structured and readied for execution.
