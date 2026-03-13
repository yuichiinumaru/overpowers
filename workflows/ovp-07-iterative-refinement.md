---
description: Refine a document through 10 high-density reasoning iterations using specialized skills.
argument-hint: Path to the document or previous work to refine
---

# /07-iterative-refinement (Iterative Refinement & Heavy Reasoning)

**Goal**: Systematically enhance a document's depth and quality by applying a sequence of specialized reasoning skills over 10 iterations, followed by a total structural reorganization with zero information loss.

## Actions

1. **Skill Inventory & Filtering**: List all available skills and filter those most relevant to the document's specific subject matter. Always include the following core reasoning/planning skills as primary options:
   - `reasoning` / `firstprinciples` / `brainstorming` / `openspec-explore`
   - `ensemble-solving` / `council` / `scientific-critical-thinking`
   - `knowledge-synthesis` / `recall-reasoning` / `decision-helper`
   - `plan-writing` / `planning-with-files` / `concise-planning`
   - `feature-planning` / `prd` / `gepetto` / `task-coordination-strategies`
   - `conductor-new-track` / `writing-plans` / `workflow-orchestration-patterns`
   - `codebase_investigator` / `senior-architect`

2. **Iterative Expansion (10 Rounds)**: Execute 10 separate refinement iterations. For each iteration:
   - Select a unique skill from the filtered list that hasn't been used in previous rounds.
   - Apply the skill to expand upon the document's core concepts, edge cases, and implications.
   - **Append Only**: Do not overwrite existing content. Add a new section at the bottom titled `## Iteration [n] - [Skill Name]`.
   - **Minimum Density**: Each iteration block must consist of at least 50 lines of substantive new information.
   - **Trust, but verify**: Review, analyze and check codebase, documentation, and memories when necessary. 
   - **Count**: Use the script `scripts/utils/count_lines.py` to count the number of lines in the document before and after the iteration. The difference should be **at least 50 lines**, but not limited to it. Write what you think is necessary to answer completely each aspect possible.

3. **Non-Destructive Reorganization**: Once all 10 iterations are complete, perform a master reorganization of the document.
   - Distribute the information added during the iterations into the original structure or a new, more logical hierarchy.
   - **Information Preservation**: Ensure no information is lost, simplified, or synthesized away. Every detail added must be preserved. Do not worry about the limits to file or length.
   - **Clarity & Cohesion**: Improve the logical flow, terminology consistency, and overall readability of the final consolidated version.
