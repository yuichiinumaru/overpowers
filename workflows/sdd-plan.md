---
description: Plan the feature development based on the feature specification. 
argument-hint: Plan specifics suggestions
---

# Plan Feature Development

Guided feature development with codebase understanding and architecture focus.

You are helping a developer implement a new feature based on SDD: Specification Driven Development. Follow a systematic approach: understand the codebase deeply, identify and ask about all underspecified details, design elegant architectures.

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Core Principles

- **Ask clarifying questions**: Identify all ambiguities, edge cases, and underspecified behaviors. Ask specific, concrete questions rather than making assumptions. Wait for user answers before proceeding with implementation. Ask questions early (after understanding the codebase, before designing architecture).
- **Understand before acting**: Read and comprehend existing code patterns first
- **Read files identified by agents**: When launching agents, ask them to return lists of the most important files to read. After agents complete, read those files to build detailed context before proceeding.
- **Simple and elegant**: Prioritize readable, maintainable, architecturally sound code
- **Use TodoWrite**: Track all progress throughout

## Outline

1. **Setup**: Get the current git branch, if it written in format `feature/<number-padded-to-3-digits>-<kebab-case-title>`, part after `feature/` is defined as FEATURE_NAME. Consuquently, FEATURE_DIR is defined as `specs/FEATURE_NAME`, FEATURE_SPEC is defined as `specs/FEATURE_NAME/spec.md`, IMPL_PLAN is defined as `specs/FEATURE_NAME/plan.md`, SPECS_DIR is defined as `specs/`. 

2. **Load context**: Read FEATURE_SPEC and `specs/constitution.md`.
3. Copy `specs/templates/plan-template.md` to `FEATURE_DIR/plan.md` using `cp` command, in future refered as `PLAN_FILE`.
4. Continue with stage 2

## Stage 2: Research & Codebase Exploration

**Goal**: Understand relevant existing code and patterns at both high and low levels. Research unknown areas, libraries, frameworks, and missing dependencies.

Follow the structure in {PLAN_FILE} template to:

- Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
- Fill Constitution Check section from constitution
- Evaluate gates (ERROR if violations unjustified)

### Actions

**Technical Context**:

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task
2. **Launch `researcher` agent to perform created tasks**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Codebase Exploration**:

1. For code explaration launch 2-3 `code-explorer` agents in parallel. Each agent should:
   - Trace through the code comprehensively and focus on getting a comprehensive understanding of abstractions, architecture and flow of control
   - Target a different aspect of the codebase (eg. similar features, high level understanding, architectural understanding, user experience, etc)
   - Include a list of 5-10 key files to read

   **Example agent prompts**:
   - "Find features similar to [feature] and trace through their implementation comprehensively"
   - "Map the architecture and abstractions for [feature area], tracing through the code comprehensively"
   - "Analyze the current implementation of [existing feature/area], tracing through the code comprehensively"
   - "Identify UI patterns, testing approaches, or extension points relevant to [feature]"

2. Once the agents return, please read all files identified by agents to build deep understanding
3. Update research report in `FEATURE_DIR/research.md` file with all findings and set links to relevant files.
4. Present comprehensive summary of findings and patterns discovered to user.

---

## Stage 3: Clarifying Questions

**Goal**: Fill in gaps and resolve all ambiguities before designing

**CRITICAL**: This is one of the most important stages. DO NOT SKIP.

**Actions**:

1. Review the codebase findings and original feature request
2. Identify underspecified aspects: edge cases, error handling, integration points, scope boundaries, design preferences, backward compatibility, performance needs
3. **Present all questions to the user in a clear, organized list**
4. **Wait for answers before proceeding to architecture design**

If the user says "whatever you think is best", provide your recommendation and set it as a assumed decision in `research.md` file.

### Output

`research.md` with all NEEDS CLARIFICATION resolved and links to relevant files.

---

## Stage 4: Architecture Design

**Prerequisites:** `research.md` complete

**Goal**: Design multiple implementation approaches with different trade-offs.

### Actions

1. Launch 2-3 `software-architect` agents in parallel with different focuses: minimal changes (smallest change, maximum reuse), clean architecture (maintainability, elegant abstractions), or pragmatic balance (speed + quality). Use provided prompt exactly, while prefiling required variables:

   ```markdown
   Perform software architecture plan design.
   


   **CRITICAL**: Do not write code during this stage, use only high level planing and architecture diagrams.

   User Input: {provide user input here if it exists}

   ## Steps

   - **Load context**: Read `specs/constitution.md`, {FEATURE_SPEC}, {FEATURE_DIR}/research.md.
   - Write the architecture design to {FEATURE_DIR}/design.{focus-name}.md file, while focusing on following aspect: {focus description}. 
   ```

2. Review all approaches and form your opinion on which fits best for this specific task (consider: small fix vs large feature, urgency, complexity, team context)
3. Present to user: brief summary of each approach, trade-offs comparison, **your recommendation with reasoning**, concrete implementation differences.
4. **Ask user which approach they prefer**

## Stage 5: Plan

Launch new `software-architect` agent to make final design doc, based on appraoch choosen by user in previous stage. Use provided prompt exactly, while prefiling required variables:

   ```markdown
   Perform software architecture plan design.
   
   **Goal**: Plan the implementation based on approach choosen by the user and clarify all unclear or uncertain areas.

   **CRITICAL**: Do not write code during this stage, use only high level planing and architecture diagrams.

   User Input: {provide user input here}

   ## Steps

   1. **Load context**: Read `specs/constitution.md`, {FEATURE_SPEC}, {FEATURE_DIR}/research.md.
   2. Read design files: {list of design files generated by previous agents}.

   3. Write the final design doc to {FEATURE_DIR}/design.md file, based on appraoch choosen by the user.
   4. Write implementation plan by filling `FEATURE_DIR/plan.md` template.
   5. **Extract entities from feature spec** → `FEATURE_DIR/data-model.md`:
      - Entity name, fields, relationships
      - Validation rules from requirements
      - State transitions if applicable
   6. **Generate API contracts** from functional requirements if it applicable:
      - For each user action → endpoint
      - Use standard REST/GraphQL patterns
      - Output OpenAPI/GraphQL schema to `FEATURE_DIR/contract.md`
   7. Output implementation plan summary.
   ```

## Stage 6: Review Implementation Plan

### Actions

1. Once Stage 5 is complete, launch new `software-architect` agent to review implementation plan. Use provided prompt exactly, while prefiling required variables:

   ```markdown
   Review implementation plan.
   
   **Goal**: Review implementation plan and present unclear or unceartan areas to the user for clarification.
   
   **CRITICAL**: Do not write code during this stage, use only high level planing and architecture diagrams.
   
   User Input: {provide user input here}

   ## Steps

   1. **Load context**: Read `specs/constitution.md`, {FEATURE_SPEC}, {FEATURE_DIR}/research.md.
   2. Review implementation plan in {FEATURE_DIR}/plan.md file, identify unclear or unceartan areas.
   3. Resolve high confidence issues by yourself.
   4. Output areas that still not resolved or unclear to the user for clarification.
   ```

2. If agent returns areas that still not resolved or unclear, present them to the user for clarification, then repeat step 1.

3. Once all areas are resolved or unclear, report branch and generated artifacts, including: data-model.md, contract.md, plan.md, etc.

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications
