---
name: biz-money-maker-hand
description: Autonomous assistant for finding and evaluating income opportunities across platforms like Zhihu, Xiaohongshu, Upwork, and ClawHub.
tags: [business, automation, income, research]
version: 1.0.0
---

# Money Maker Hand - Autonomous Earning Assistant

## 🎯 Core Features

Runs autonomously to help you find and evaluate money-making opportunities:
- Market research (Zhihu/Xiaohongshu/Upwork).
- Opportunity discovery.
- Competitor analysis.
- Income tracking.
- Generating actionable recommendations.

---

## 🔄 Execution Flow (7 Phases)

### Phase 1: State Recovery
```
1. memory_recall check `money_maker_state`.
2. Read existing income database `income_database.json`.
3. Load historical reports.
```

### Phase 2: Income Source Configuration
```
Target Income: 10,000 RMB/month
Current Income: 0 RMB
Gap: 10,000 RMB
Priority Directions: Novels + Skills + Outsourcing
```

### Phase 3: Opportunity Discovery
```
Perform multi-platform research:
1. Zhihu Selection - Hot topics/submission rates/fee standards.
2. Xiaohongshu - Monetization methods/advertising quotes.
3. Upwork/Freelancer - AI-related outsourcing needs.
4. ClawHub - Trending Skills/pricing strategies.
```

### Phase 4: Opportunity Assessment
```
Score each opportunity (0-100):
- Market Demand: +30 (Search volume/competition).
- Monetization Potential: +30 (Unit price × quantity).
- Barrier to Entry: +20 (Skill match).
- Time Investment: +20 (ROI).
```

### Phase 5: Competitor Analysis
```
In-depth analysis of Top 3 competitors:
- Product/service details.
- Pricing strategy.
- Marketing channels.
- SWOT comparison.
```

### Phase 6: Report Generation
```
Output Format: Markdown Report
Contains:
1. Weekly income progress.
2. Top 5 opportunities (sorted by score).
3. Detailed action plan.
4. Risk alerts.
```

### Phase 7: State Persistence
```
1. Update `income_database.json`.
2. memory_store `money_maker_state`.
3. Update dashboard metrics.
```

... (rest of content)
