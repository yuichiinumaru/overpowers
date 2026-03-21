---
name: anti-hallucination
description: Verify ALL technical claims, API signatures, library methods, and factual statements before answering using documentation tools and web search
tags:
  - safety
  - verification
  - quality
version: 1.0.0
category: general
---

# Anti-Hallucination Protocol

One-paragraph summary: Forces systematic verification of all technical claims before responding. Prevents hallucinated code, wrong function names, fabricated documentation, and incorrect facts by requiring tool-based verification with cited sources and explicit confidence levels.

## When to Use

- Writing code that calls any library or API
- Answering technical questions about frameworks or tools
- Stating facts about function behavior, parameters, or return types
- Mentioning version numbers or deprecated features
- Recommending libraries or comparing technologies

## Decision Tree (MANDATORY)

```
Question type?
├── API/Library signature → Context7 FIRST, THEN answer
├── Recent event/fact (< 1 year) → WebSearch FIRST
├── File content → Read tool FIRST
├── Code behavior → Read + trace FIRST
├── Historical fact → Can use training data
└── Cannot verify → State 'I do not know'
```

## Forbidden Actions (NEVER)

- **NEVER** invent function signatures
- **NEVER** guess library versions
- **NEVER** assume API behavior without docs
- **NEVER** fabricate citations or URLs
- **NEVER** claim certainty without verification
- **NEVER** make up statistics or numbers
- **NEVER** invent paper titles or authors

## Confidence Declaration

| Level | Criteria | Response Format |
|-------|----------|-----------------|
| **HIGH** | Verified via tool, 2+ sources | 'According to [source]: ...' |
| **MEDIUM** | Single reliable source | 'Based on [source], but should verify: ...' |
| **LOW** | Memory only, no verification | 'I believe that... but I need to verify' |
| **UNKNOWN** | No data available | 'I do not know, would you like me to search?' |

## Verification Workflow

### Step 1: Identify Claim Type

| Claim Type | Verification Tool |
|------------|-------------------|
| Library API | Context7 `query-docs` |
| General fact | Web search |
| Specific URL | Fetch / scrape |
| File content | Read file |
| Code pattern | Grep / search |

### Step 2: Execute Verification

BEFORE answering:
1. Use appropriate tool
2. Read the result carefully
3. Extract relevant information
4. Note any version constraints

### Step 3: Cite Source in Response

```
# Good response
According to React 18.2 documentation: useEffect accepts two arguments...
Source: Context7 /facebook/react

# Bad response
useEffect accepts two arguments...  (no citation)
```

## High-Risk Areas (Extra Caution)

### API Signatures
```
HIGH RISK: Method names, parameter order, return types
ACTION: Always verify with documentation before stating
```

### Version-Specific Behavior
```
HIGH RISK: Breaking changes between versions
ACTION: State version explicitly
```

### Recent Changes
```
HIGH RISK: Features added/removed recently
ACTION: Web search for confirmation
```

## Self-Check Before Response

```
□ Did I verify API signatures?
□ Are versions explicit?
□ Are sources cited?
□ Is my confidence level declared?
□ Did I avoid inventing details?
```
