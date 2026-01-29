# Jules Architectural Digest: Overpowers Toolkit

## 1. Project Overview

**Overpowers** is a massive, opinionated toolkit for OpenCode/Claude Code, forked from [Superpowers](https://github.com/obra/superpowers). It serves as a comprehensive "agent army" and automation framework, significantly expanding the original capabilities with over 960 components.

The system is designed to transform a single developer into an orchestrator of hundreds of specialized AI agents. It emphasizes **delegation over execution**, utilizing a hierarchy where a "CEO" agent coordinates specialized sub-agents and external swarms.

## 2. Tech Stack & Versions

*   **Core Platform**: OpenCode / Claude Code (Proprietary/External CLI environment)
*   **Definition Language**: Markdown (`.md`) with YAML Frontmatter
    *   Used for defining Agents, Hooks, and documenting Skills.
*   **Scripting & Tooling**:
    *   **Python 3**: Used for configuration generation (`generate-agent-configs.py`) and complex logic.
    *   **Bash Shell**: Used for deployment scripts (`deploy-agent-army.sh`) and skill execution wrappers.
*   **Infrastructure**:
    *   **Jules Swarm**: A submodule (`packages/jules-swarm`) for distributed task execution across multiple Google accounts.
    *   **JSON**: Used for final configuration injection into OpenCode.

## 3. Entity Relationship Map

*   **Agents** (`agents/*.md`): The core units of work. Defined by a prompt, description, and metadata.
    *   *Types*: Primary (Orchestrators), Subagents (Specialists).
    *   *Relations*: Orchestrators (like CEO) call Subagents.
*   **Skills** (`skills/*/SKILL.md`): Capabilities that agents can invoke.
    *   *Structure*: A directory containing a definition (`SKILL.md`) and executable scripts.
    *   *Relations*: Agents use Skills to perform actions (e.g., "dispatch to swarm").
*   **Commands** (`commands/`): Shorthand operations for common tasks.
*   **Workflows** (`workflows/*.md`): Documented processes that guide agents through complex multi-step objectives.
*   **Hooks** (`hooks/`): Event-driven triggers.
    *   **Safety Layer**: `hooks/safety/destructive-command-blocker.ts` prevents dangerous ops.
*   **Knowledge Graph** (`docs/knowledge/`): Domain-specific knowledge fragments (e.g., Testing patterns) loaded by agents.
*   **Configuration** (`opencode.json`): The runtime configuration where all agents and settings are injected.

## 4. Architecture Diagram

```mermaid
graph TD
    User[User Request] --> CEO[CEO Orchestrator Agent]

    subgraph Local_Orchestration
        CEO -->|Decompose| Planner[Task Decomposition Expert]
        Planner -->|Assign| Specialist1[Specialist Agent]
        Planner -->|Assign| Specialist2[Specialist Agent]
    end

    subgraph Safety_Layer
        Specialist1 -.->|Command| SafetyHook[Destructive Command Blocker]
        SafetyHook --|Block| Specialist1
        SafetyHook --|Allow| Execution_Layer
    end

    subgraph Execution_Layer
        Specialist1 -->|Execute| LocalSkills[Local Skills/Scripts]
        Specialist2 -->|Execute| LocalSkills
    end
```

## 5. Critical Paths

### A. The "CEO" Orchestration Loop
1.  **Input**: User provides a high-level goal.
2.  **Decomposition**: The CEO agent uses the `task_decomposition_expert`.
3.  **Delegation**: Tasks dispatched to specialists.
4.  **Review**: Synthesis of results.

### B. The Compound Product Cycle (Report -> Code)
1.  **Input**: Report markdown file in `reports/`.
2.  **Analysis**: `auto-compound.sh` prioritizes one feature.
3.  **Cycle**: Generates PRD, executes loop, verifies.
4.  **Output**: Feature Branch ready for PR.

## 6. Core Agents (Oh My OpenCode Integration)
The system logic is driven by 5 core agents:
*   **Sisyphus (Orchestrator)**: Plans obsessively, delegates to specialists.
*   **Metis (Consultant)**: Classifies intent and consults *before* planning.
*   **Librarian (Researcher)**: Finds documentation and examples from external sources.
*   **Oracle (Architect)**: High-IQ reasoning for complex architecture and debugging.
*   **Explorer (Recon)**: Internal codebase exploration via grep/AST search.

## 7. Style Guide

*   **Naming Convention**: `kebab-case` for all files.
*   **Agent Frontmatter**:
    ```yaml
    ---
    name: agent-name
    description: Brief description
    category: category-name
    model: optional-model-override
    ---
    ```
*   **Changelog Law**: **MUST** update `CHANGELOG.md` for *every* modification.
*   **Continuity**: Update `continuity.md` at session end.

## 8. Operational Instructions

### Deploying the Agent Army
To regenerate and inject all agent configurations:
```bash
./deploy-agent-army.sh
```

### Adding a New Agent
1.  Create `agents/new-agent-name.md`.
2.  Add frontmatter and prompt.
3.  Run `./deploy-agent-army.sh`.
