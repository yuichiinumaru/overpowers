# Evaluation-Driven Development (EvDD)

Evaluation-Driven Development is a quality assurance methodology that ensures agent skills perform reliably and accurately against predefined scenarios. It is a core requirement for all skills in the overpowers ecosystem.

## Core Principles

1. **Spec Before Skill**: Define the expected behavior (evaluation) before or alongside implementing the skill.
2. **100% Pass Requirement**: A skill is not considered "ready" until it passes all associated evaluation cases.
3. **Continuous Validation**: Evaluations run automatically during integration and updates to prevent regressions.

## The Evaluation Schema

Evaluations are stored as JSON files in the `evaluations/` directory, following the `schema.json`.

### Key Fields:
- **query**: The "input" to the agent.
- **expected_behavior**: Semantic actions the agent must take (e.g., "Explain the .body nesting").
- **expected_content**: Mandatory keywords or code snippets that must appear in the output.

## Workflow

### 1. Creation
Create a new evaluation for every major feature or common failure mode of a skill.
- Path: `evaluations/[skill-category]/[eval-id].json`

### 2. Testing
Test the agent's response to the `query` against the `expected_behavior` and `expected_content`.

### 3. Iteration
If the agent fails, refine the `SKILL.md` instructions until the evaluation passes consistently.

## Best Practices
- **Focus on Edge Cases**: Create evaluations for common "gotchas" or complex logic.
- **Keep it Atomic**: Each evaluation should test a specific behavior.
- **Use for Regressions**: If a bug is found in a skill, add an evaluation case to ensure it never returns.
