# Research to Product Workflow

Transform research and ideas into implemented features using our **research → analysis → implementation** agent pipeline.

## When to Use

- Starting a new feature from scratch
- Exploring technology options before implementation
- Analyzing competitors before building
- Learning new frameworks/libraries

## Research Phase Agents

| Agent | Role |
|-------|------|
| `comprehensive-researcher` | Broad topic exploration |
| `academic-researcher` | Academic papers & best practices |
| `technical-researcher` | Technical docs & tutorials |
| `trend-researcher` | Industry trends & patterns |
| `market-research-analyst` | Market & competitive analysis |

## Workflow Steps

### 1. Initial Research

```
/invoke comprehensive-researcher

Topic: "[Your feature/technology]"
Output: 
- Key concepts
- Top resources
- Common approaches
- Trade-offs
```

### 2. Competitive Analysis (if applicable)

```
/invoke market-research-analyst

Questions:
- Who else has built this?
- What approaches work?
- What are the pitfalls?
```

**Use Skills:**
- `competitive-ads-extractor` - Analyze competitor messaging
- `tailored-resume-generator` - Position features for users

### 3. Technical Deep Dive

```
/invoke technical-researcher

Focus:
- Implementation patterns
- Library comparisons
- Performance benchmarks
- Security considerations
```

### 4. Synthesis & Planning

```
/invoke feedback-synthesizer

Input: All research findings
Output: 
- Recommended approach
- Risk assessment
- Implementation plan
```

### 5. Handoff to Development

```
/invoke rapid-prototyper

With research insights:
- Build proof of concept
- Validate assumptions
- Identify blockers early
```

## Research → Development Bridge

| Research Output | Development Input |
|-----------------|-------------------|
| Best practices | Coding standards |
| Trade-offs | Architecture decisions |
| Competitive intel | Feature differentiation |
| Risk analysis | Mitigation strategy |

## Related Skills

- `langsmith-fetch` - Debug LLM implementations
- `arxiv-search` - Academic paper search
- `web-research` - Structured web research

## Success Metrics

| Phase | Deliverable |
|-------|-------------|
| Research | Summary document |
| Analysis | Decision matrix |
| Planning | Implementation spec |
| Prototype | Working demo |
