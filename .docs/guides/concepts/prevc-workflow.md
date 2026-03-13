# PREVC Workflow

The PREVC workflow is a universal 5-phase process designed to improve AI output quality through structured, spec-driven development. It stands for **Planning, Review, Execution, Validation, and Confirmation**.

## Phases

| Phase | Name | Purpose |
|-------|------|---------|
| **P** | Planning | Define what to build. Gather requirements, write specs, identify scope. No code yet. |
| **R** | Review | Validate the approach. Architecture decisions, technical design, risk assessment. |
| **E** | Execution | Build it. Implementation follows the approved specs and design. |
| **V** | Validation | Verify it works. Tests, QA, code review against original specs. |
| **C** | Confirmation | Ship it. Documentation, deployment, stakeholder handoff. |

## Why PREVC?

LLMs produce better results when they follow a structured process instead of generating code blindly. PREVC ensures:

- **Specifications before code**: AI understands what to build before building it.
- **Context awareness**: Each phase has the right documentation and agent.
- **Human checkpoints**: Review and validate at each step, not just at the end.
- **Reproducible quality**: Same process, consistent results across projects.

## Scale-Adaptive Routing

The system can automatically detect project scale and adjust the workflow:

| Scale | Phases | Use Case |
|-------|--------|----------|
| QUICK | E → V | Bug fixes, small tweaks |
| SMALL | P → E → V | Simple features |
| MEDIUM | P → R → E → V | Regular features |
| LARGE | P → R → E → V → C | Complex systems, compliance |

## Example Flow

**Task**: "Add authentication"

1.  **Planning**: Determine auth type (OAuth, JWT), providers, scope.
2.  **Review**: Propose architecture, dependencies, identify risks. User approves.
3.  **Execution**: Implement the approved design.
4.  **Validation**: Run tests, security audit.
5.  **Confirmation**: Deploy, update docs.

## Agents & Skills

The PREVC workflow is supported by specialized agents (e.g., `prevc-architect-specialist`, `prevc-feature-developer`) and skills (e.g., `prevc-api-design`, `prevc-code-review`).
