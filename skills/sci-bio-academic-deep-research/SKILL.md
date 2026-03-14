---
name: academic-deep-research
description: Transparent, rigorous research methodology using 2-cycle investigation
  per theme, APA 7th citations, and evidence hierarchy. Use for literature reviews,
  competitive intelligence, and high-stakes claim verification.
tags:
- bio
- sci
version: 1.0.0
category: general
---
# Academic Deep Research

A methodical research system designed for exhaustive investigation, building comprehensive understanding through systematic cycles and rigorous evidence standards.

## When to Use

- User asks for "deep research" or "exhaustive analysis".
- Complex topics requiring multi-source investigation and verification.
- Literature reviews, competitive analysis, or trend reports.
- Claims that need verification from multiple high-quality sources.

## Prerequisites

- Access to web search tools (Perplexity, Brave, Google).
- Access to academic databases or primary sources if possible.
- Sufficient token budget for multi-cycle analysis and parallel agent spawning.

## Instructions

### Phase 1: Engagement & Scoping
1. Ask 2-3 essential clarifying questions (Goal, Depth, Constraints).
2. Reflect understanding back to the user and wait for confirmation.

### Phase 2: Research Planning
Present a complete plan with:
1. Major themes identified (3-5 themes).
2. Execution steps (Action, Tool, Expected Output).
3. Deliverable format and citation style.
**WAIT for explicit user approval before proceeding.**

### Phase 3: Mandated Research Cycles
Execute two full cycles per theme:
- **Cycle 1 (Landscape)**: Broad search (count=20), synthesize patterns, identify gaps.
- **Cycle 2 (Deep Dive)**: Targeted search on gaps, fetch primary sources, refine hypotheses.
- **Between tool calls**: You MUST show your work, connecting new findings to previous results and noting contradictions.

### Phase 4: Final Report
Present a cohesive research paper in narrative prose:
1. **Executive Summary**: Core question and primary findings.
2. **Knowledge Development**: Evolution of understanding through the cycles.
3. **Comprehensive Analysis**: Primary findings, patterns, and contradictions.
4. **Practical Implications**: Immediate applications and future directions.
5. **References**: Full APA 7th edition formatted list.

## Research Standards

- **Evidence Hierarchy**: Prioritize systematic reviews and RCTs over media reports.
- **Citation Density**: 1-2 citations per paragraph (Author, Year).
- **Conflict Resolution**: Address contradictory sources fairly, assessing evidence quality.
- **Transparency**: Acknowledge uncertainties and limitations [HIGH/MEDIUM/LOW confidence labels].

## Examples

```markdown
/* APA 7th Citation Example */
Multiple meta-analyses have confirmed that resistance training combined 
with adequate protein intake is more effective for preserving muscle mass 
than either intervention alone (Smith, 2020; Garcia et al., 2022).
```

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| Insufficient results | Broaden query terms, use synonyms, or search adjacent terminology |
| Unresolved contradiction | Present both claims with context and assess evidence quality |
| Outdated information | Assess if still relevant; prioritize current scientific consensus |
