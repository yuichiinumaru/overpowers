# Overpowers Memory Management Strategy

Based on the recent parsing of `.agents/antigravity-session.md` and the existing memory states in `Serena MCP`, `Memcord MCP`, and the `Knowledge (AgentDB)` module, here is a consolidated overview and strategy for maintaining shared agent consciousness.

## Current State of Memory Systems

**1. Serena MCP (File-based, Project-scoped)**
*   **Current Memories:** 
    *   `overpowers_core_identity`
    *   `overpowers_infrastructure_fallback`
    *   `overpowers_orchestration_system`
    *   `overpowers_protocols_and_conventions`
    *   `overpowers_timeline_and_changes`
*   **Purpose:** Strong for foundational, slowly changing project contexts (rules, identity, overarching architecture). It handles literal/regex edits well.

**2. Memcord MCP (Vector/Search-based, Cross-session)**
*   **Current Slots & Entries:**
    *   `megazord-architecture-blueprint` (2 entries)
    *   `overpowers_main` (2 entries)
    *   `khala-exhaustive-mapping` (1 entry)
    *   `gemini-cli-megazord-integration` (1 entry)
    *   `gemini-cli-arch-audit` (1 entry)
    *   `khala-agentmemory` (1 entry)
*   **Purpose:** Excellent for semantic search, dynamic tracking of active sub-projects (like Khala and Megazord), and offloading context from long-running agent threads. It allows natural language semantic queries (`memcord_query`).

**3. Knowledge (AgentDB / File System KBs)**
*   **Current KBs:** Extensive JSON-based schemas (`kb_cognitive_fusion_architecture_cfa`, `kb_problem_solving_network`, etc.) and Markdown artifacts.
*   **Purpose:** The ultimate "Source of Truth" for complex, interconnected protocols (CFA, Synergy, Guardian Security). Highly structured but harder to quickly mutate dynamically compared to Serena/Memcord.

## Identified "Cagada" (Mistake) in Session
During the final phase of the analyzed session, the agent lost track of the Version Control System boundary. The Overpowers repo uses **Jujutsu (jj)** extensively for safe multi-agent concurrency. 
*   **The Mistake:** The agent executed standard Git commands (`git push origin --delete <branch>`) which manipulated the underlying git state without updating Jujutsu's concurrent working copy logs properly. This resulted in `jj resolve` conflicts and diverged states when trying to manage sub-trees (like `auth-monster`).
*   **The Fix Required:** The agent had to forcefully squash changes (`jj squash`) and manually reset bookmarks (`jj bookmark set`) to recover.
*   **Memory Action:** This incident highlights the need to strictly enforce the `.agents/rules/vcs-workflow.md` rule across all memory systems.

## Proposed Memory Synthesis Strategy

To avoid fragmentation ("Memória de Peixe") and align with the `knowledge-update.md` guidelines:

1.  **Tier 1: Fast Context Offloading (Memcord)**
    *   *When to use:* During active problem-solving, debugging complex errors, or building out a new feature slice (e.g., updating `gemini-cli-megazord-integration`). 
    *   *Action:* Use `memcord_save_progress` at the end of heavy reasoning blocks.

2.  **Tier 2: Project Milestones & State (Serena)**
    *   *When to use:* When architectural decisions are made, dependencies are added, or major workflows are validated.
    *   *Action:* Update `overpowers_timeline_and_changes` and architecture files via `edit_memory` or `write_memory`.

3.  **Tier 3: Permanent Knowledge Base (Knowledge / AgentDB / NotebookLM)**
    *   *When to use:* When completing a major epic, deriving a new operational rule, or generating comprehensive documentation (like the CFA modules).
    *   *Action:* Compile Memcord slots and Serena summaries into structured `kb_*.json` or Markdown artifacts in the Knowledge system. Delegate ingestion runs to NotebookLM via the `nlm` CLI for RAG querying on massive files (300+ limit handling).

## Next Steps
We must continually run the `knowledge-update.md` protocol:
1. List what changed since last update.
2. Read existing memories.
3. Update Memcord -> Serena -> Knowledge.
