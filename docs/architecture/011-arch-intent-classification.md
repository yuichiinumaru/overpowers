# Protocol: Intent Classification & Pre-Planning

**Source**: Adapted from Metis Agent (Oh-My-OpenCode)
**Purpose**: To classify work intent before execution to determine the correct strategy and prevent "AI slop".

---

## 🛑 PHASE 0: INTENT CLASSIFICATION (MANDATORY FIRST STEP)

Before ANY planning or execution, the Orchestrator or Consultant must classify the work intent.

### Step 1: Identify Intent Type

| Intent | Signals | Primary Focus |
|:-------|:--------|:--------------|
| **Refactoring** | "refactor", "restructure", "clean up", changes to existing code | **SAFETY**: regression prevention, behavior preservation |
| **Build from Scratch** | "create new", "add feature", greenfield, new module | **DISCOVERY**: explore patterns first, informed questions |
| **Mid-sized Task** | Scoped feature, specific deliverable, bounded work | **GUARDRAILS**: exact deliverables, explicit exclusions |
| **Collaborative** | "help me plan", "let's figure out", wants dialogue | **INTERACTIVE**: incremental clarity through dialogue |
| **Architecture** | "how should we structure", system design, infrastructure | **STRATEGIC**: long-term impact, Oracle recommendation |
| **Research** | Investigation needed, goal exists but path unclear | **INVESTIGATION**: exit criteria, parallel probes |

### Step 2: Validate Classification

Confirm:
1. Is the intent type clear from request?
2. If ambiguous, **ASK** before proceeding.

---

## 🛡️ PHASE 1: INTENT-SPECIFIC STRATEGIES

### 1. IF REFACTORING
**Mission**: Ensure zero regressions, behavior preservation.
*   **Directives**:
    *   MUST: Define pre-refactor verification (exact test commands).
    *   MUST: Verify after EACH change.
    *   MUST NOT: Change behavior while restructuring.
    *   MUST NOT: Refactor adjacent code not in scope.

### 2. IF BUILD FROM SCRATCH
**Mission**: Discover patterns before asking, then surface hidden requirements.
*   **Directives**:
    *   MUST: Follow patterns from existing codebase.
    *   MUST: Define "Must NOT Have" section (AI over-engineering prevention).
    *   MUST NOT: Invent new patterns when existing ones work.

### 3. IF MID-SIZED TASK
**Mission**: Define exact boundaries. AI slop prevention is critical.
*   **Directives**:
    *   MUST: "Must Have" section with exact deliverables.
    *   MUST: "Must NOT Have" section with explicit exclusions.
    *   MUST NOT: Exceed defined scope.

### 4. IF COLLABORATIVE
**Mission**: Build understanding through dialogue.
*   **Directives**:
    *   MUST: Record all user decisions in "Key Decisions" section.
    *   MUST: Flag assumptions explicitly.
    *   MUST NOT: Proceed without user confirmation on major decisions.

### 5. IF ARCHITECTURE
**Mission**: Strategic analysis. Long-term impact assessment.
*   **Directives**:
    *   MUST: Consult `@oracle-consultant` before finalizing plan.
    *   MUST: Document architectural decisions with rationale.
    *   MUST: Define "minimum viable architecture".

### 6. IF RESEARCH
**Mission**: Define investigation boundaries and exit criteria.
*   **Directives**:
    *   MUST: Define clear exit criteria.
    *   MUST: Specify parallel investigation tracks.
    *   MUST NOT: Research indefinitely without convergence.

---

## 📝 OUTPUT FORMAT (For Agents)

When performing this analysis, produce an output block like this:

```markdown
## Intent Classification
**Type**: [Refactoring | Build | Mid-sized | Collaborative | Architecture | Research]
**Confidence**: [High | Medium | Low]
**Rationale**: [Why this classification]

## Identified Risks
- [Risk 1]: [Mitigation]

## Directives for Execution
- MUST: [Required action]
- MUST NOT: [Forbidden action]
- PATTERN: Follow `[file:lines]`
```
