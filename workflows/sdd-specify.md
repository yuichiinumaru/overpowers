---
description: Create or update the feature specification from a natural language feature description.
argument-hint: Feature description
allowed-tools: ["Bash(cp:*)"]
---

# Specify Feature

Guided feature development with codebase understanding and architecture focus.

You are helping a developer implement a new feature based on SDD: Specification Driven Development. Follow a systematic approach: understand the codebase deeply, identify and ask about all underspecified details, design detailed specification.

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Stage 1: Discovery/Specification Design

**Goal**: Understand what needs to be built

**Actions**:

1. If feature unclear, **Ask clarifying questions**: Identify all ambiguities, edge cases, and underspecified behaviors. Ask specific, concrete questions rather than making assumptions. Wait for user answers before proceeding with next steps. Ask questions early.

2. Once feature is clear, summarize understanding by answering on this questions:
   - What problem are they solving?
   - What should the feature do?
   - Any constraints or requirements?

3. Write feature specification following #Outline section.

## Outline

The text the user typed after `/sdd:01-specify` in the triggering message **is** the feature description. Assume you always have it available in this conversation even if `{ARGS}` appears literally below. Do not ask the user to repeat it unless they provided an empty command.

Given that feature description, do this:

1. **Generate a concise short name** (2-4 words) for the branch:
   - Analyze the feature description and extract the most meaningful keywords
   - Create a 2-4 word short name that captures the essence of the feature
   - Use action-noun format when possible (e.g., "add-user-auth", "fix-payment-bug")
   - Preserve technical terms and acronyms (OAuth2, API, JWT, etc.)
   - Keep it concise but descriptive enough to understand the feature at a glance
   - Examples:
     - "I want to add user authentication" → "user-auth"
     - "Implement OAuth2 integration for the API" → "oauth2-api-integration"
     - "Create a dashboard for analytics" → "analytics-dashboard"
     - "Fix payment processing timeout bug" → "fix-payment-timeout"

2. **Check for existing branches before creating new one**:

   a. First, fetch all remote branches to ensure we have the latest information:

      ```bash
      git fetch --all --prune
      ```

   b. Find the highest feature number across all sources for the short-name:
      - Remote branches: `git ls-remote --heads origin | grep -E 'refs/heads/feature/[0-9]+-<short-name>$'`
      - Local branches: `git branch | grep -E '^[* ]*feature/[0-9]+-<short-name>$'`
      - Specs directories: Check for directories matching `specs/[0-9]+-<short-name>`

   c. Determine the next available number:
      - Extract all numbers from all three sources
      - Find the highest number N
      - Use N+1 for the new branch number

   d. Create new feature folder in `specs/` directory with the calculated number and short-name:
      - Create folder `specs/<number-padded-to-3-digits>-<short-name>`, in future refered as `FEATURE_DIR`
      - Create file `FEATURE_DIR/spec.md` by copying `specs/templates/spec-template.md` file, in future refered as `SPEC_FILE`.
      - Example: `cp specs/templates/spec-template.md specs/5-user-auth/spec.md`

   **IMPORTANT**:
   - Check all three sources (remote branches, local branches, specs directories) to find the highest number
   - Only match branches/directories with the exact short-name pattern
   - If no existing branches/directories found with this short-name, start with number 1
   - For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot")

3. Launch `business-analyst` agent with provided prompt exactly, while prefiling required variables:

      ```markdown
      Perform business analysis and requirements gathering.
      Write the specification to {SPEC_FILE} using the template structure, replacing placeholders with concrete details derived from the feature description (arguments) while preserving section order and headings, and expanding specification based on use case and feature information.
      
      User Input: {provide user input here}
      
      FEATURE_NAME: {FEATURE_NAME}
      FEATURE_DIR: {FEATURE_DIR}
      SPEC_FILE: {SPEC_FILE}

      ```

4. **Specification Quality Validation**: After writing the initial spec, validate it against quality criteria:

   a. **Create Spec Quality Checklist**: Copy `specs/templates/spec-checklist.md` file to `FEATURE_DIR/spec-checklist.md` using `cp` command, in future refered as `CHECKLIST_FILE`.

   b. Launch new `business-analyst` agent with provided prompt exactly, while prefiling required variables

      ```markdown
      Peform following steps:
      1. Fill in {CHECKLIST_FILE} file with based on user input.
      2. Review the specification in {SPEC_FILE} file against each checklist item in this checklist:
         - For each item, determine if it passes or fails
         - Document specific issues found (quote relevant spec sections)
      3. Reflect on specification and provide feedback on potential issues and missing areas, even if they not present in checklist.

      ---

      User Input: {provide user input here}
      
      FEATURE_NAME: {FEATURE_NAME}
      FEATURE_DIR: {FEATURE_DIR}
      SPEC_FILE: {SPEC_FILE}
      
      ```

   c. **Handle Validation Results**:

      - **If all items pass**: Mark checklist complete and proceed to step 6

      - **If items fail (excluding [NEEDS CLARIFICATION])**:
        1. List the failing items and specific issues
        2. Launch new `business-analyst` agent and ask it to analyze and update the spec to address each issue
        3. Re-run validation by launching new `business-analyst` agent until all items pass (max 3 iterations)
        4. If still failing after 3 iterations, document remaining issues in checklist notes and warn user

      - **If [NEEDS CLARIFICATION] markers remain**:
        1. Extract all [NEEDS CLARIFICATION: ...] markers from the spec:
        2. **LIMIT CHECK**: If more than 3 markers exist, keep only the 3 most critical (by scope/security/UX impact) and and launch new `business-analyst` agent to make informed guesses for the rest
        3. For each clarification needed (max 3), present options to user in this format:

           ```markdown
           ## Question [N]: [Topic]
           
           **Context**: [Quote relevant spec section]
           
           **What we need to know**: [Specific question from NEEDS CLARIFICATION marker]
           
           **Suggested Answers**:
           
           | Option | Answer | Implications |
           |--------|--------|--------------|
           | A      | [First suggested answer] | [What this means for the feature] |
           | B      | [Second suggested answer] | [What this means for the feature] |
           | C      | [Third suggested answer] | [What this means for the feature] |
           | Custom | Provide your own answer | [Explain how to provide custom input] |
           
           **Your choice**: _[Wait for user response]_
           ```

        4. **CRITICAL - Table Formatting**: Ensure markdown tables are properly formatted:
           - Use consistent spacing with pipes aligned
           - Each cell should have spaces around content: `| Content |` not `|Content|`
           - Header separator must have at least 3 dashes: `|--------|`
           - Test that the table renders correctly in markdown preview
        5. Number questions sequentially (Q1, Q2, Q3 - max 3 total)
        6. Present all questions together before waiting for responses
        7. Wait for user to respond with their choices for all questions (e.g., "Q1: A, Q2: Custom - [details], Q3: B")
        8. Launch new `business-analyst` agent to update the spec by replacing each [NEEDS CLARIFICATION] marker with the user's selected or provided answer
        9. Re-run validation by launching new `business-analyst` agent after all clarifications are resolved

   d. **Update Checklist**: After each validation iteration, update the checklist file with current pass/fail status

5. Report completion with branch name, spec file path, checklist results, and readiness for the next stage `/sdd:01-plan`.
