# claude-md-enhancer

System for scoring and improving the quality of CLAUDE.md files.

## Scoring Criteria
- **Completeness**: Are all required sections present (Build, Lint, Test, Conventions)?
- **Accuracy**: Do the commands actually work in the current environment?
- **Clarity**: Are the instructions easy for an agent to follow?
- **Conventions**: Are project-specific style rules clearly documented?

## Improvement Workflow
1. Analyze existing `CLAUDE.md`.
2. Generate a quality score.
3. Suggest specific additions or corrections.
4. Update the file while preserving useful existing content.
