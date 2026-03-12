---
name: osint
description: Open source intelligence gathering for people, companies, and threat intelligence. Use for due diligence, background checks, and investigations.
tags:
- safety
- sec
---
# OSINT (Open Source Intelligence)

Open Source Intelligence gathering for authorized investigations and data collection.

## When to Use

- **People lookup**: "research [person]", "who is [person]", "background check on [person]".
- **Company lookup**: "do OSINT on [company]", "company intelligence", "investigate [company]".
- **Due Diligence**: "is [company] legitimate", "assess [company]", "should we work with [company]".
- **Threat Intel**: "is this domain malicious", "analyze [entity]", "research this threat actor".

## Prerequisites

- Access to web search tools (Perplexity, Brave, Google).
- Authorization for the investigation (MUST verify explicit permission).
- Awareness of legal and ethical boundaries (Public sources only).

## Instructions

### Step 1: Authorization & Scoping
1. Verify explicit authorization from the client/user.
2. Define the scope of the investigation (target, goals, timeframe).
3. Confirm legal compliance for the target jurisdiction.

### Step 2: Collection
Use parallel agent deployment for comprehensive results:
- **Perplexity/Brave**: Current web data, social media, and company updates.
- **Academic Tools**: Deep professional backgrounds and published works.
- **Technical Tools**: DNS, WHOIS, and infrastructure reconnaissance.

### Step 3: Verification & Reporting
1. Cross-reference findings across multiple sources.
2. Verify the credibility of the sources.
3. Generate a structured report with findings, confidence levels, and citations.

## Ethical Guardrails

- **ALLOWED**: Publicly available websites, social media, public records, search engines, archived content.
- **PROHIBITED**: Private data, unauthorized access, social engineering, purchasing breached data, ToS violations.

## Examples

```bash
# Example goal: Investigate a domain for potential malicious activity
# 1. Search for domain history in Wayback Machine
# 2. Check current DNS records and WHOIS data
# 3. Search for mentions of the domain in security forums
```

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| Limited results | Use alternative search engines or targeted queries (e.g., site:linkedin.com) |
| Contradictory data | Cross-verify with original primary sources (official registries) |
| Blocked access | Respect robots.txt and site terms; do not use automated scraping without permission |
