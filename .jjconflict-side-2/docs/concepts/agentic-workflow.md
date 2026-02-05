# Agentic Workflow & Thoughts System

Extracted from [Agentic](https://github.com/Cluster444/agentic), this workflow emphasizes a structured, phase-based approach to software development and a persistent knowledge base called "Thoughts".

## The Thoughts Directory

The `thoughts/` directory is your project's knowledge base, serving as persistent memory for both human developers and AI agents.

### Structure

```
thoughts/
├── architecture/     # System design and decisions (Source of Truth)
├── tickets/          # Work items and feature requests
├── research/         # Analysis and findings (Timestamped)
├── plans/            # Implementation specifications
├── reviews/          # Post-implementation validation
└── archive/          # Outdated documents (excluded from searches)
```

### Key Components

*   **Architecture**: Foundational design documents (e.g., `overview.md`, `system-architecture.md`).
*   **Research**: Timestamped findings from codebase analysis (`YYYY-MM-DD_topic.md`).
*   **Plans**: Detailed implementation specs with checkmarks (`descriptive-name.md`).
*   **Reviews**: Post-implementation validation (`YYYY-MM-DD_review.md`).

## Workflow Phases

### 1. Research Phase
*   **Purpose**: Understand the codebase and gather context.
*   **Process**: Analyzes ticket requirements, explores codebase, searches existing thoughts.
*   **Output**: `thoughts/research/YYYY-MM-DD_topic.md`.

### 2. Planning Phase
*   **Purpose**: Create detailed implementation specifications.
*   **Process**: Develops phased implementation approach, defines success criteria.
*   **Output**: `thoughts/plans/descriptive-name.md`.

### 3. Implementation Phase
*   **Purpose**: Execute the plan with code changes.
*   **Process**: Implements phases sequentially, verifies work at natural stopping points.
*   **Key**: Follows the plan while adapting to reality.

### 4. Commit Phase
*   **Purpose**: Create atomic, well-documented git commits.
*   **Process**: Reviews changes, drafts meaningful commit messages focusing on "why".

### 5. Review Phase
*   **Purpose**: Validate implementation against plan.
*   **Process**: Compares implementation to plan, identifies drift, validates criteria.
*   **Output**: `thoughts/reviews/YYYY-MM-DD_review.md`.

## Integration with Agents

*   **codebase-analyzer**: Spawns specialized subagents to analyze specific parts of the codebase.
*   **thoughts-locator**: Finds relevant documents in the thoughts directory.
*   **web-search-researcher**: Gathers external context when needed.
