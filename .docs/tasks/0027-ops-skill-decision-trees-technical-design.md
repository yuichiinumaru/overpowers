# Technical Design: Skill Decision Trees Standardization

## 1. Architecture Overview
This is a documentation-centric enhancement. It doesn't change the execution engine but rather the "software" (skills) running on it.

The standardization will follow the **Progressive Disclosure** principle:
1.  **Level 1**: Small, high-signal decision tables in `SKILL.md`.
2.  **Level 2**: Detailed flowcharts or complex logic in `references/decision_trees.md`.

## 2. Standard Formats

### Format A: The Quick Matrix (Table)
Best for simple choice between 2-3 options.

| If [Context/Constraint] | Then use [Action/Tool] | Why? |
| :--- | :--- | :--- |
| Simple fact lookup | `google_web_search` | Speed & Cost |
| Deep analysis | `research-lookup` (Reasoning) | Accuracy |

### Format B: The Logic Flow (Nested List)
Best for sequential decisions.

1.  **Check Task Complexity**:
    - If task has < 3 steps → **Fast Mode**
    - If task has 3+ steps → **Planning Mode**
2.  **Verify Permissions**:
    - If write access is required → **Direct Execution**
    - If read-only is preferred → **Subagent Research**

## 3. Core Heuristics (Overpowers Standard)

### Model Selection
- **Reasoning (Opus/Reasoning Pro)**: Logic bugs, complex refactors, new architecture, security PoC.
- **Pro (Gemini Pro)**: General implementation, documentation, standard bug fixes.
- **Fast (Flash/Haiku)**: Search, simple edits, validation, boilerplate.

### Task Strategy
- **Trivial**: Single file, zero ambiguity → **Act immediately**.
- **Complex**: Multi-file, architectural impact → **Plan first, validate often**.
- **High Fragility**: Binary formats, specific indentation → **Low freedom scripts**.

## 4. Implementation Plan
1.  Create `docs/guides/skill-decision-trees.md` with the above content.
2.  Create `templates/skill-decision-tree-template.md`.
3.  Update Task 0027 status to completed once reviewed.

## 5. Security & Performance
- **Performance**: Standardized trees help agents skip unnecessary tool calls or research steps, saving tokens and time.
- **Security**: Trees should include security-first logic (e.g., "If secret is detected -> STOP").
