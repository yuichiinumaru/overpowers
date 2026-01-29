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
*   **Hooks** (`hooks/`): Event-driven triggers (pre/post action) to enforce rules or notifications.
*   **Configuration** (`opencode.json`): The runtime configuration where all agents and settings are injected.

## 4. Architecture Diagram

```mermaid
graph TD
    User[User Request] --> CEO[CEO Orchestrator Agent]

    subgraph Local_Orchestration
        CEO -->|Decompose| Planner[Task Decomposition Expert]
        Planner -->|Assign| Specialist1[Specialist Agent (e.g., Python Expert)]
        Planner -->|Assign| Specialist2[Specialist Agent (e.g., Security Auditor)]
    end

    subgraph Execution_Layer
        Specialist1 -->|Execute| LocalSkills[Local Skills/Scripts]
        Specialist2 -->|Execute| LocalSkills

        CEO -->|Delegate Heavy Load| JulesDispatch[Skill: Jules Dispatch]
    end

    subgraph Jules_Swarm_Cloud
        JulesDispatch -->|Prompt| CloudTask1[Google Jules Account 1]
        JulesDispatch -->|Prompt| CloudTask2[Google Jules Account 2]
        CloudTask1 -->|Branch| GitBranch1[Feature Branch]
        CloudTask2 -->|Branch| GitBranch2[Feature Branch]
    end

    subgraph Integration
        GitBranch1 --> JulesHarvest[Skill: Jules Harvest]
        GitBranch2 --> JulesHarvest
        JulesHarvest --> JulesTriage[Skill: Jules Triage]
        JulesTriage -->|Merge| MainCodebase[Main Codebase]
    end
```

## 5. Critical Paths

### A. The "CEO" Orchestration Loop
1.  **Input**: User provides a high-level goal (e.g., "Refactor auth system").
2.  **Decomposition**: The CEO agent uses the `task_decomposition_expert` to break this into atomic tasks.
3.  **Delegation**:
    *   Small tasks -> Executed locally by specialized agents (e.g., `security_auditor`).
    *   Large/Parallel tasks -> Dispatched to Jules Swarm.
4.  **Review**: The CEO synthesizes the results and presents them to the user.

### B. The Jules Swarm Workflow (4-Stage)
1.  **Dispatch (`jules-dispatch`)**:
    *   Generates optimized, modular prompts.
    *   Creates a dispatch record in `.jules/pending/`.
    *   Assigns tasks to available Google Jules accounts (round-robin).
2.  **Harvest (`jules-harvest`)**:
    *   Polls for completed tasks.
    *   Fetches remote branches created by the swarm.
3.  **Triage (`jules-triage`)**:
    *   Enables parallel review of the harvested branches.
    *   Rates solutions.
4.  **Integrate (`jules-integrate`)**:
    *   Merges the approved branches into the main codebase.

## 6. Style Guide

*   **Naming Convention**: `kebab-case` for all files (agents, skills, scripts).
*   **Agent Frontmatter**:
    ```yaml
    ---
    name: agent-name
    description: Brief description
    category: category-name
    model: optional-model-override
    ---
    ```
*   **Changelog Law**:
    *   **MUST** update `CHANGELOG.md` for *every* modification.
    *   Newest entries at the top.
    *   Never delete history.
*   **Continuity**:
    *   Update `continuity.md` at the end of every session to track state.

## 7. Operational Instructions

### Deploying the Agent Army
To regenerate and inject all agent configurations into the local OpenCode environment:
```bash
./deploy-agent-army.sh
```
*   **Logic**: Runs `generate-agent-configs.py` (parse markdown -> json) then `inject-agents-to-config.py` (update `opencode.json`).

### Adding a New Agent
1.  Create `agents/new-agent-name.md`.
2.  Add frontmatter and prompt.
3.  Run `./deploy-agent-army.sh`.
4.  Verify with `opencode agent list`.

## 8. Technical Debt & Observations

*   **Scale Complexity**: With 390+ agents, there is significant overlap in capabilities. Finding the "right" agent can be difficult for a human, necessitating the "CEO" agent pattern.
*   **Maintenance**: Keeping 960+ components updated and compatible with the underlying OpenCode platform is a high-effort task.
*   **Dependency**: The system is heavily dependent on the external OpenCode/Claude Code CLI environment and its plugin architecture.
*   **Manual Steps**: The "Jules Swarm" still has manual triggers (dispatch/harvest), though heavily automated via scripts.
