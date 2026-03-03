---
description: Deep-scan the entire codebase in parallel using 10 subagents, producing architectural reports and syncing to memory systems.
argument-hint: Optional focus areas or exclusion patterns
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Objective

Divide the codebase into ~10 logical chunks and dispatch parallel subagents to scan each one. The goal is to build a deep, comprehensive understanding of the project architecture, patterns, tech stack, dependencies, and potential issues.

## Execution Flow

1. **Prepare the environment.**
   - Ensure `.agents/` directory exists.
   - Ensure `.agents/thoughts/` directory exists.
   - Create `.agents/thoughts/deep-scan/` for this scan's temporary reports.

2. **Analyze the codebase layout.**
   - List all top-level directories and measure their size.
   - Identify the ~10 largest or most meaningful chunks. Possible splitting strategies:
     - By top-level directory (e.g., `src/`, `lib/`, `api/`, `tests/`, `docs/`...)
     - By feature module if the project uses a modular architecture.
     - By language/stack if polyglot.
   - Create a `scan-plan.md` in `.agents/thoughts/deep-scan/` describing which chunk goes to which subagent.

3. **Dispatch 10 parallel subagents.**
   - Each subagent receives a specific directory/chunk to analyze.
   - Each subagent MUST write its findings to `.agents/thoughts/deep-scan/chunk-NN-report.md` where NN is its assigned number.
   - Each report should cover:
     - **Architecture patterns** found (MVC, event-driven, etc.)
     - **Key files and entry points** with brief descriptions.
     - **Dependencies** (imports, external packages).
     - **Code quality observations** (complexity, duplication, test coverage).
     - **Security concerns** (hardcoded secrets, unsafe patterns).
     - **TODOs and FIXMEs** found in the code.
     - **Tech debt** observations.

4. **Consolidate reports.**
   - After all subagents complete, read all chunk reports.
   - Create a unified `.agents/memories/codebase-architecture.md` that synthesizes key findings.
   - Highlight cross-cutting concerns (shared utilities, common patterns, inconsistencies).

5. **Sync to memory systems.**
   - Persist the consolidated report to available memory systems:
     - Serena MCP: `write_memory` with the architecture overview.
     - Memcord MCP: `memcord_save` with the project summary.
   - Tag memories appropriately (e.g., `architecture`, `deep-scan`, project name).
   - Update the centralized JSON Knowledge Graph (`docs/knowledge/SYSTEM_KNOWLEDGE_GRAPH.json` or equivalent) with new nodes and relationships discovered during the scan.

6. **Report to user.**
   - Summary of what was scanned.
   - Top 5 most important architectural observations.
   - Any critical issues or security concerns found.
   - Links to the detailed reports in `.agents/thoughts/deep-scan/`.
