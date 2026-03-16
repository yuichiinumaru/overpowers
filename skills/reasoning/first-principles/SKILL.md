---
name: first-principles
description: First-principles reasoning and decomposition. Use when analyzing constraints, challenging assumptions, or rebuilding solutions from fundamental truths.
tags:
  - reasoning
  - analysis
version: 1.0.0
category: reasoning
---

# First-Principles Reasoning

Foundational reasoning methodology that deconstructs problems to fundamental truths rather than reasoning by analogy. Breaks inherited assumptions and rebuilds solutions from irreducible facts.

## When to Use

- **Architecture decisions**: Challenge "is this actually a constraint or just how we've always done it?"
- **Problem decomposition**: Break complex problems into constituent parts
- **Cost/value analysis**: Identify what is actually necessary vs. what is convention
- **Adversarial analysis**: Deconstruct assumptions in security models, designs, specifications
- **When stuck**: Rebuild understanding from fundamentals when inherited approaches fail

## The 3-Step Framework

```
┌─────────────────────────────────────────────────────────┐
│  STEP 1: DECONSTRUCT                                    │
│  "What is this really made of?"                         │
│  Break down to constituent parts and fundamental truths │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  STEP 2: CHALLENGE                                      │
│  "Is this a real constraint or an assumption?"          │
│  Classify each element as hard/soft constraint          │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  STEP 3: RECONSTRUCT                                    │
│  "Given only the truths, what's optimal?"               │
│  Build new solution from fundamentals, ignoring form    │
└─────────────────────────────────────────────────────────┘
```

## Instructions

### Step 1: Deconstruct
Ask these questions about the subject:
- What is this actually made of?
- What are the constituent parts?
- What is the actual cost/value of each part?
- What would a physicist say about this?

### Step 2: Challenge (Constraint Classification)
Classify every constraint using this table:

| Type | Definition | Example | Can Change? |
|------|------------|---------|-------------|
| **Hard** | Physics/reality | "Data can't travel faster than light" | No |
| **Soft** | Policy/choice | "We always use REST APIs" | Yes |
| **Assumption** | Unvalidated belief | "Users won't accept that UX" | Maybe false |

**Rule**: Only hard constraints are truly immutable. Soft constraints and assumptions must be challenged.

### Step 3: Reconstruct
- If we started from scratch with only the fundamental truths, what would we build?
- What field has solved an analogous problem differently?
- Are we optimizing function or form?
- What is the simplest solution that satisfies only the hard constraints?

## Output Format

```markdown
## First Principles Analysis: [Topic]

### Deconstruction
- **Constituent Parts**: [List fundamental elements]
- **Actual Values**: [Real costs/metrics, not market prices]

### Constraint Classification
| Constraint | Type | Evidence | Challenge |
|------------|------|----------|-----------|
| [X] | Hard/Soft/Assumption | [Why] | [What if removed?] |

### Reconstruction
- **Fundamental Truths**: [Only the hard constraints]
- **Optimal Solution**: [Built from fundamentals]
- **Form vs Function**: [Are we optimizing the right thing?]

### Key Insight
[One sentence: what assumption was limiting us?]
```

## Principles

1. **Physics First** — Real constraints come from physics/reality, not convention
2. **Function Over Form** — Optimize what you're trying to accomplish, not how it's traditionally done
3. **Question Everything** — Every assumption is guilty until proven innocent
4. **Cross-Domain Synthesis** — Solutions from unrelated fields often apply
5. **Rebuild, Don't Patch** — When assumptions are wrong, start fresh rather than fixing

## Anti-Patterns to Avoid

- **Reasoning by Analogy**: "Company X does it this way, so should we"
- **Accepting Market Prices**: "$600/kWh" without checking material costs
- **Form Fixation**: Improving the suitcase instead of inventing wheels
- **Soft Constraint Worship**: Treating policies as physics
- **Premature Optimization**: Optimizing before understanding fundamentals

## Integration

Works well with:
- **`skills/research/experiments/scientific-critical-thinking`** — Scientific method after decomposition
- **`skills/coding/testing/reasoning`** — Structured reasoning for reconstruction phase
- **`skills/tools/math/ensemble-solving`** — Multi-perspective challenge phase
