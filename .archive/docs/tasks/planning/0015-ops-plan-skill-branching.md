# Future Research: Skill Branching / Decision Trees

> Status: CONCEPT
> Priority: MEDIUM
> Created: 2026-01-19

## The Idea

Skills should have **branches** or **trees** that guide selection based on context:

```
START with skill X
├── IF condition_A → use skill Y
├── IF condition_B → use skill Z
│   ├── IF sub_condition → use skill Z1
│   └── ELSE → use skill Z2
└── ELSE → use skill X (default)
```

## Why This Matters

### Problem: One-Size-Fits-All Skills

Current skills are monolithic. But:
- Different models respond better to different instruction styles
- Different task complexities need different depths
- Different user preferences exist

### Solution: Skill Decision Trees

Instead of picking a single skill, the system could:
1. Evaluate the context (model, task type, user preferences)
2. Traverse a decision tree
3. Select the optimal skill variant

## Example: Code Review

```yaml
skill: code-review
branches:
  - condition: "model.supports_long_context AND diff.lines > 500"
    use: code-review-comprehensive
  - condition: "task.is_security_focused"
    use: code-review-security
  - condition: "user.prefers_brief"
    use: code-review-quick
  - default: code-review-standard
```

## Implementation Ideas

### Option 1: Skill Metadata
Add `branches` field to skill frontmatter:
```yaml
---
name: code-review
branches:
  security: code-review-security
  comprehensive: code-review-comprehensive
  quick: code-review-quick
triggers:
  security: ["security", "vulnerability", "CVE"]
  comprehensive: ["thorough", "full review", "audit"]
---
```

### Option 2: Skill Orchestrator
A meta-skill that selects the appropriate variant:
```
/use skill-selector --task="review this PR for security issues"
→ Selects: code-review-security
```

### Option 3: Progressive Disclosure Extension
Extend the existing progressive disclosure pattern:
- Level 1: Metadata + branch conditions
- Level 2: Selected branch's instructions
- Level 3: Resources for that branch

## Research Questions

1. How do we measure which branch is "better" for a given context?
2. Should branching be automatic or user-controlled?
3. How do we prevent branch explosion (too many variants)?
4. Can we learn optimal branching from usage patterns?

## Merge Strategy Connection

This concept emerged from the question: "Should we merge aggressively or conservatively when integrating new skills?"

The answer might be: **Neither. Create branches.**

- Conservative branch: Keeps original behavior
- Aggressive branch: Uses new integrated patterns
- Let the system (or user) choose based on context

## Dependencies

- Testing infrastructure to measure skill effectiveness
- Usage analytics to understand which variants work best
- Clear branch condition syntax

---

*This document created during Phase 2 integration when discussing merge strategies.*
