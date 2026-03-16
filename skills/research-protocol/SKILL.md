---
name: research-protocol
description: Conduct rigorous research with proper citations, source triangulation, and confidence assessment for technical and academic queries
tags:
  - research
  - citations
  - quality
version: 1.0.0
category: general
---

# Research Protocol

One-paragraph summary: Systematic research workflow that ensures proper source attribution, cross-referencing, and confidence assessment. Covers academic papers, official documentation, and web sources with a clear hierarchy and citation formats.

## When to Use

- User asks about state of the art (SOTA)
- Recent developments in a field
- Comparing technologies or approaches
- Verifying scientific claims
- Finding academic papers or benchmark results
- Any query requiring cited, verified information

## Research Workflow

```
1. SCOPE    → Define question precisely
2. SEARCH   → Multiple sources, cross-reference
3. EVALUATE → Assess source reliability
4. SYNTHESIZE → Combine findings coherently
5. CITE     → Provide proper attribution
6. ASSESS   → State confidence level
```

## Source Hierarchy

| Priority | Source Type | Reliability | Citation Format |
|----------|-------------|-------------|-----------------|
| 1 | Peer-reviewed papers | Highest | [Author et al., Year] arXiv:XXXX |
| 2 | Official documentation | High | Docs [Library] vX.X |
| 3 | Conference proceedings | High | [Conf Year] Paper Title |
| 4 | Established tech blogs | Medium-High | [Org] Blog (Date) |
| 5 | GitHub repos with citations | Medium | GitHub [repo] |
| 6 | Stack Overflow (verified) | Medium | SO [answer-id] |
| 7 | General web content | Low | Mention skepticism |

## Search Strategy

### For SOTA (State of the Art)
```
1. WebSearch('[topic] SOTA 2025')
2. WebSearch('[topic] benchmark comparison')
3. Check arXiv for recent papers
4. Search HuggingFace if ML-related
```

### For Specific Papers
```
1. WebSearch('paper title arxiv')
2. Fetch arXiv page directly if ID known
```

### For Library/API Questions
```
1. Context7 resolve-library-id first
2. Then research protocol for broader context
```

## Citation Formats

### Academic Papers
```
[Author et al., Year] 'Title' - arXiv:XXXX.XXXXX
[Author et al., Year] 'Title' - DOI:10.XXXX/XXXXX
```

### Documentation
```
According to [Library] v[X.X] documentation: ...
According to [Framework] docs (2025): ...
```

### Web Sources
```
According to [Source Name] (Date): ...
Per [Organization] blog (Month Year): ...
```

## Confidence Assessment

| Confidence | Criteria | Response Style |
|------------|----------|----------------|
| **HIGH** | 3+ concordant sources, peer-reviewed | State as established fact |
| **MEDIUM** | 1-2 reliable sources | Add 'according to [source]' caveat |
| **LOW** | Conflicting sources | Present multiple views |
| **UNKNOWN** | No reliable sources | 'I do not know' |

## Handling Conflicts

When sources disagree:

```markdown
## Divergent Viewpoints

**Position A** (Source 1, Source 2):
[Description]

**Position B** (Source 3):
[Description]

**Assessment**: [Which seems more credible and why]
```

## Output Format

```markdown
## Summary
[Main findings - 3-5 lines max]

## Details
[Expanded information with inline citations]

## Sources
1. [Citation 1 with link/DOI]
2. [Citation 2 with link/DOI]

## Confidence Level: [HIGH/MEDIUM/LOW]
[1-2 sentence justification]

## Limitations
- [What could not be verified]
- [Potential biases in sources]
- [Recency concerns if applicable]
```

## Red Flags (Requires Extra Scrutiny)

- Single source only
- Source older than 2 years (for fast-moving fields)
- Preprint without peer review
- Corporate blog with potential bias
- No citations in the source itself
- Contradicts well-established knowledge
