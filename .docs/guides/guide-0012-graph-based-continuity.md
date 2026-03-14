# Guide 0012: Graph-based Continuity

## Overview
Graph-based Continuity integrates agent session logs (`continuity-*.md`) directly into the Overpowers Knowledge Graph. This allows agents to understand not just *what* code exists, but *who* changed it, *why*, and *when* during active development cycles.

## How it Works
The `overpowers-graph-ext` indexer scans the `.agents/` directory for files matching `continuity-*.md`. If these files contain valid YAML frontmatter, they are added as nodes to the knowledge graph.

## Frontmatter Standard
To ensure your session is indexed, include the following frontmatter at the top of your `continuity-[name].md` file (located in `.agents/`):

```yaml
---
name: continuity-[your-name]
type: continuity
domain: Session
description: Brief summary of your current focus.
requires:
  - [skill-id-1]
  - [skill-id-2]
related_to:
  - [file-path-1]
  - [task-file-path-1]
---
```

## Benefits for Agents
- **Contextual Awareness**: Agents can search the graph for "recent changes to [skill]" and find the continuity node of the agent who last worked on it.
- **Dependency Tracking**: By listing `requires`, the graph can show which skills are being actively tested or utilized in current sessions.
- **Improved Handoffs**: When a new agent starts, they can traverse the graph from the last continuity node to understand the full context of the work in progress.

## Rebuilding the Graph
After updating your continuity file, you can trigger a graph rebuild to make your session searchable:

```bash
npm run build:graph
```
