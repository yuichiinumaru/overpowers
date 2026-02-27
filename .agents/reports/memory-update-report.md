# Memory Update Report

**Date:** 2026-02-27
**Agent:** Jules (Senior PRD Engineer)

## Summary
A comprehensive analysis of the Mothership codebase was conducted to update the project's "memories" (knowledge base). The file structure, core components, and new additions were verified against existing documentation.

## Key Findings

### 1. Structure Confirmation
The project follows a monorepo structure with distinct zones:
-   **`packages/`**: Shared libraries (Khala, Ivisa UI, Scrapling).
-   **`services/`**: Backend services (Golden Armada, Deep Research, LLM Gateway).
-   **`apps/`**: Frontend applications (Nexus Web, Vivi Web, Deep Research App).
-   **`src/`**: Home to Sentinel components (Host, Dashboard, Scout) and shared source.

### 2. Component Analysis
-   **Khala**: Confirmed as the memory engine utilizing SurrealDB. Includes a comprehensive README detailing 170+ strategies.
-   **Golden Armada**: Confirmed as the agent swarm. README identifies it as a "Massive Agentic Swarm" with 222+ agents using Gemini 3.0.
-   **Deep Research**: Two components found:
    -   `services/deep_research`: Python-based autonomous agent using LangGraph.
    -   `apps/deep-research`: Next.js frontend application.
-   **Sentinel**: Significant presence found in `src/` (Host in C#, Dashboard in React, Scout as browser extension). `services/sentinel` contains only a placeholder README.
-   **Legion KMS**: Hybrid Next.js/Python project.
-   **LLM Gateway**: FastAPI service wrapping LiteLLM.

### 3. Documentation Gaps Identified
-   **Missing READMEs**: Several key directories (`services/legion_kms`, `services/nexus_backend`, `services/vivi_agent_os`, `apps/nexus-web`, `apps/vivi-web`) lack README files, making immediate understanding of their specific internal workings more difficult without code inspection.
-   **Duplication**: `docker-compose.yml` contained a duplicate entry for `deep-research`.

### 4. Updates Made
-   **`docs/knowledge/00-project-context-and-state.md`**: Updated to reflect the current component list (Sentinel, LLM Gateway, Deep Research split), tech stack details (C#, LangGraph), and current phase challenges.
-   **`docs/architecture/project-structure.md`**: Rewritten to provide an accurate map of the `apps/`, `packages/`, `services/`, and `src/` directories.

## Recommendations for Next Steps
1.  **Consolidate Documentation**: Create READMEs for the undocumented services identified above.
2.  **Sentinel Integration**: Formulate a plan to fully integrate Sentinel components from `src/` into the `services/` architecture if that is the intended end state, or clarify the `src/` vs `services/` separation.
3.  **Docker Cleanup**: Fix the duplicate `deep-research` entry in `docker-compose.yml`.
