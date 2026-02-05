# Most Valuable Project Management (MVPM)

Extracted from [Pew Pew Workspace](https://github.com/pew-pew-prompts/pew-pew-workspace), MVPM is a flexible organizational system for AI-assisted development.

## Core Philosophy

*   **Prioritize Value**: Start with what delivers the most value first (MVM → MVS).
*   **Parallel Execution**: Structure only what enables parallel work.
*   **Traceability**: Maintain connection between all document types for a single issue.

## Concepts

### MVM (Most Valuable Milestone)
The largest meaningful chunk of value to deliver.

### MVS (Most Valuable Step)
The smallest increment of work that moves the project forward.

### Organization Structure
Flexible structure based on parallel work:
```
{company-concept}/{most-valuable-milestone}/{most-valuable-step}.md
```

### Traceability Principle
The same issue can have multiple document types with the **SAME number**:
```
AUTH-042-oauth-integration-story.md    # User story
AUTH-042-oauth-integration-plan.md     # Technical plan
AUTH-042-oauth-integration-bug.md      # Bug report
AUTH-042-oauth-integration-pr.md       # Pull request
```

## Structure Flow

1.  **Backlog**: Everything starts in `000-backlog/`.
2.  **Milestone**: Promoted to `001-most-valuable-milestone/`.
3.  **Step**: Broken down into `001-most-valuable-step/`.
4.  **Files**: Concrete artifacts (stories, plans, PRs) created.

## Workflow Decision Tree

1.  **What needs to be done?** → Define MVS (e.g., `set-up-flutter-app`).
2.  **What concept?** → `essentials`.
3.  **Which department?** → `tech department`.
4.  **Build hierarchy** → `tech/essentials/001-initial-setup/001-set-up-flutter-app`.
5.  **Teams needed?**
    *   **Yes**: Create team folders (`team-app/`, `team-backend/`).
    *   **No**: Create MVS files directly.

## Directory Structure

```
issues/
└── {company-concept}/
    ├── 000-backlog/
    └── {001-most-valuable-milestone}/
        ├── 000-backlog/
        └── {001-most-valuable-step}/
            ├── 000-backlog/
            ├── CONC-001-feature-story.md
            ├── CONC-001-feature-plan.md
            └── CONC-001-feature-pr.md
```

## Agents

Extracted agents supporting this workflow:
*   `pew-lead-developer`: Orchestrates development tasks.
*   `pew-feature-workflow-orchestrator`: Manages feature lifecycle.
*   `pew-roadmap-agent`: Manages high-level planning.
*   `pew-bug-workflow-orchestrator`: Manages bug fix lifecycle.
