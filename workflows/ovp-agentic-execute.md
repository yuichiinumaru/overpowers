---
description: Execute a specific implementation plan. Provide a plan file as the argument to this command. It's very important this command runs in a new session.
---

# Implement Plan

You are tasked with implementing an approved technical plan from `thoughts/plans/`. These plans contain phases with specific changes and success criteria.

## Implementation Philosophy

Plans are carefully designed, but reality can be messy. Your job is to:
- Follow the plan's intent while adapting to what you find
- Implement each phase fully before moving to the next
- Verify your work makes sense in the broader codebase context
- Update checkboxes in the plan as you complete sections

When things don't match the plan exactly, think about why and communicate clearly. The plan is your guide, but your judgment matters too.

If you encounter a mismatch:
- STOP and think deeply about why the plan can't be followed
- Present the issue clearly:
  ```
  Issue in Phase [N]:
  Expected: [what the plan says]
  Found: [actual situation]
  Why this matters: [explanation]

  How should I proceed?
  ```
- **Document deviations in the plan**: If proceeding with a change, update the plan file with a clear record of the deviation using the Edit tool. Add or update a section at the end of the plan:

  ```markdown
  ## Deviations from Plan

  ### Phase [N]: [Phase Name]
  - **Original Plan**: [brief summary of what the plan specified]
  - **Actual Implementation**: [what was actually done]
  - **Reason for Deviation**: [why the change was necessary]
  - **Impact Assessment**: [effects on other phases, success criteria, or overall project]
  - **Date/Time**: [when the deviation was made]
  ```

## Verification Approach

After implementing a phase:
- Run the success criteria checks (usually `bun run check` covers everything)
- Fix any issues before proceeding
- Update your progress in both the plan and your todos
- Check off completed items in the plan file itself using Edit

Don't let verification interrupt your flow - batch it at natural stopping points.

## If You Get Stuck

When something isn't working as expected:
- First, make sure you've read and understood all the relevant code
- Consider if the codebase has evolved since the plan was written
- Present the mismatch clearly and ask for guidance

Use sub-tasks sparingly - mainly for targeted debugging or exploring unfamiliar territory.

## Resuming Work

If the plan has existing checkmarks:
- Trust that completed work is done
- Pick up from the first unchecked item
- Verify previous work only if something seems off

Remember: You're implementing a solution, not just checking boxes. Keep the end goal in mind and maintain forward momentum.

## Steps

1. **Context Initialization (Explicit Memory Read)**: Before starting, read `.agents/continuity-<agent-name>.md` and check `.agents/memories/` for the current strategic focus and architectural context.

2. **Read the plan completely** and check for any existing checkmarks (- [x]). Only read the plan file provided as an argument.

3. **Read the original ticket and all files mentioned in the plan**. Read files fully - never use limit/offset parameters, you need complete context. If you have trouble understanding the plan, refer to the research and ticket information.

4. **Consider the steps involved in the plan**. Think deeply about how the pieces fit together and derive a detailed todo list from the plan's phases and requirements.

5. **Implement each phase sequentially**, adapting to what you find while following the plan's intent.

6. **Verify each phase** using the success criteria checks (usually `bun run check` covers everything). Fix any issues before proceeding.

7. **Update the plan file** with checkmarks for completed items using the Edit tool.

8. **Handle any mismatches or issues** by presenting them clearly and asking for guidance if needed.

9. **Update ticket status & Memory (Explicit Memory Update)**: 
    - Update ticket status to 'implemented' by editing the ticket file's frontmatter.
    - Read and update `.agents/continuity-<agent-name>.md` to move the task to completed.
    - Suggest using `/11-sync-memory` to capture any major learnings during the execution.

Use the todowrite tool to create a structured task list for the 9 steps above, marking each as pending initially. Note that Step 4 may expand into multiple implementation subtasks derived from the plan.

**plan**

$ARGUMENTS
