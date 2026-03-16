---
name: openclaw-behavior-plan
description: "Generates structured behavior plans for OpenClaw agents based on user requirements. Use when the user asks to create a plan, design agent behavior, plan multi-step tasks for OpenClaw, or when they ..."
metadata:
  openclaw:
    category: "openclaw"
    tags: ['openclaw', 'agent', 'automation']
    version: "1.0.0"
---

# OpenClaw Behavior Plan Generation (openclaw-behavior-plan)

**On Trigger**: Output "Triggering openclaw-behavior-plan skill".

Generates a structured behavior plan suitable for an OpenClaw Agent to execute, based on the user's described goal or need. The plan should be mappable to tools and skills in TOOLS.md/SKILLS.md, supporting a multi-step reasoning loop (Load → Call → Parse → Execute → Append → Loop).

## 1. Plan Structure Template

Use the following structure when generating a plan:

```markdown
# Behavior Plan: [Task Title]

## Goal
[One-sentence description of the desired final outcome]

## Prerequisites
- [ ] Are required tools/skills available?
- [ ] Has necessary information been acquired?

## Execution Steps

### Step 1: [Step Name]
- **Objective**: [What this step aims to achieve]
- **Tool/Skill**: [execute_shell | search_web | read_file | action of a specific skill]
- **Input**: [Parameters or dependencies]
- **Expected Output**: [What will be obtained upon completion of this step]

### Step 2: [Step Name]
...

### Step N: [Step Name]
...

## Exceptions and Fallbacks
- If [a specific step] fails → [Alternative solution or retry strategy]

## Completion Criteria
- [ ] [Verifiable completion condition 1]
- [ ] [Verifiable completion condition 2]
```

## 2. Generation Principles

1.  **Executable Steps**: Each step should correspond to a specific capability in TOOLS.md or SKILLS.md, avoiding abstract descriptions.
2.  **Dependency Order**: When a later step depends on the output of an earlier step, clearly state "Depends on [Output] from Step N".
3.  **Tool Selection**:
    *   Requires current information → `search_web`
    *   Requires reading/writing files → `read_file` / `write_file`
    *   Requires script execution → `execute_shell`
    *   Requires third-party services → Corresponding skill (e.g., calendar, email, slack)
4.  **Reasonable Granularity**: A single step should not be too large (making failure localization difficult) nor too small (increasing loop iterations).
5.  **Exception Handling**: Provide fallback or retry instructions for steps that might fail (network issues, permissions, format errors).

## 3. Mapping to OpenClaw Reasoning Loop

| Plan Step | Manifestation in Reasoning Loop |
|-----------|---------------------------------|
| Step Execution | Load → Call → Parse(tool_call) → Execute → Append |
| Step 2 Execution | Next Loop iteration, continuing based on Step 1 results |
| Completion Criteria | LLM outputs final text, stops when no pending tool_calls |

## 4. Output Format

*   Output the complete plan directly (Markdown), without additional packaging.
*   If user requirements are ambiguous, first list 1-2 clarifying questions, then generate the plan.
*   If sensitive operations are involved (e.g., `execute_shell` for deletion, system modification), mark it in the plan as "Requires User Confirmation".

## 5. More Examples

See [examples.md](examples.md) for details.
