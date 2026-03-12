# Skill Decision Trees (Model/Task/Context Guidance)

## 1. Introduction
The Overpowers Toolkit integrates hundreds of skills, agents, and tools. When selecting which skill or agent to employ, the decision process must consider three primary dimensions: **Model Capabilities**, **Task Specificity**, and **Contextual Constraints**. This document outlines the decision tree framework for navigating this complexity.

## 2. The Decision Dimensions

### 2.1 Model Governance
According to `AGENTS.md`, different LLMs serve specific operational roles:
*   **Complex Reasoning & Coding (High Freedom)**: `gemini-3.1-pro` / `claude-4.6-opus-thinking`
    *   *Use when*: Tasks involve major architectural decisions, SDD (Specification-Driven Development), or handling high variability.
*   **Fast Execution & Fallback (Medium Freedom)**: `gemini-3-flash` / `claude-4.6-sonnet`
    *   *Use when*: Tasks are well-defined, scripts exist, or the path is clear. Good for executing parameterized scripts.
*   **Testing & Verification (Low Freedom)**: `gemini-3.1-flash-lite`
    *   *Use when*: Tasks are fragile, error-prone, or require running specific test suites repeatedly.

### 2.2 Task Specificity & Degrees of Freedom
Skill selection correlates directly with the task's degree of freedom (as per `guide-0005-skill-creation.md`):
*   **High Freedom**: Use skills with text-based instructions. The model needs context (e.g., `references/`) to make heuristic-guided decisions.
*   **Medium Freedom**: Use skills with parameterized scripts or pseudocode. The model follows a preferred pattern but adapts configuration.
*   **Low Freedom**: Use skills with rigid, deterministic scripts (`scripts/`). The model acts as an executor, minimizing token usage and logic generation.

### 2.3 Contextual Constraints (Progressive Disclosure)
The context window is a scarce resource.
*   **Triggering**: The YAML frontmatter (`name`, `description`) of a skill determines if it should be loaded.
*   **Loading Context**: If the task is broad, load `SKILL.md`. If the task requires deep domain knowledge (e.g., AWS vs GCP), conditionally load specific reference files (e.g., `references/aws.md`).
*   **Execution vs. Loading**: If a deterministic script exists (e.g., `scripts/rotate_pdf.py`), execute it directly via the shell environment instead of reading its code into the context window, unless debugging is required.

## 3. The Decision Tree

### Step 1: Analyze the Request
1.  **What is the core objective?** (e.g., "Build a React component", "Rotate a PDF", "Audit security").
2.  **Is this a recognized domain?** Match the objective to the skill triggers (`description` in YAML frontmatter).

### Step 2: Determine the Degree of Freedom
1.  **Is it a deterministic, repeatable action?** -> **Low Freedom**.
    *   *Action*: Select a skill that provides a script in `scripts/`.
    *   *Model*: Fast Logic (`gemini-3-flash` or `claude-4.6-sonnet`).
2.  **Is it a standardized process with some variability?** -> **Medium Freedom**.
    *   *Action*: Select a skill with a clear `SKILL.md` workflow and parameterizable scripts.
    *   *Model*: Fast Logic or Reasoning depending on complexity.
3.  **Is it open-ended, creative, or architectural?** -> **High Freedom**.
    *   *Action*: Select a skill providing deep `references/` (e.g., `brand-guidelines`, `architecture-patterns`).
    *   *Model*: Complex Reasoning (`gemini-3.1-pro` or `claude-4.6-opus-thinking`).

### Step 3: Apply Progressive Disclosure
1.  **Load the Skill**: Read the `SKILL.md`.
2.  **Navigate References**: Based on the specific sub-task (e.g., "Use AWS"), read *only* the relevant reference file (`references/aws.md`). Do not load all references.
3.  **Utilize Assets**: If the skill provides templates (`assets/`), copy them to the working directory.

### Step 4: Execution & Verification
1.  **Execute**: Run the necessary scripts or write the code.
2.  **Verify**: Use the Testing model (`gemini-3.1-flash-lite`) or fast logic to run test suites and validate output.

## 4. Anti-Patterns to Avoid
*   **Context Bloat**: Loading all reference files of a skill when only one is needed.
*   **Model Mismatch**: Using `gemini-3.1-pro` to run a simple, deterministic Python script.
*   **Reinventing the Wheel**: Writing custom code when a skill already provides a validated script in its `scripts/` directory.

## 5. Summary
Effective agent operations in the Overpowers Toolkit require balancing the capabilities of the LLM with the structured constraints of the skills. By matching the task's required degree of freedom to the appropriate model tier and utilizing progressive disclosure, agents can operate efficiently and reliably.
