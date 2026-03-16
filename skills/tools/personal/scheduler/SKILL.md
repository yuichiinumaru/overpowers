---
name: scheduler
description: "Manage scheduled tasks, recurring jobs, and automated workflows. Handles daily routines, weekly reports, and event-triggered actions."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# Scheduler Skills

Skills for managing recurring tasks, repetitive jobs, and automated workflows.

## Overview

### Why is it necessary?
```
Objectives:
├── Automate daily posts
├── Automatically generate weekly reports
├── Regular monitoring and checks
├── Event-based automated responses
└── Continuous operation without human intervention
```

---

## Daily Schedule (JST)

### Morning Routine (7:00)
```
1. Check for new arrivals on each platform
   ├── Coconala: New inquiries
   ├── Fiverr: New messages
   └── Moltbook: New requests

2. Identify high-priority tasks
   ├── Due today
   └── Unanswered messages

3. Prepare today's tweets
   └── Select candidates from thought-logger
```

### Midday Check (12:00)
```
1. Check status of ongoing tasks
2. Reply to new messages
3. SNS posting (for Threads)
4. Trend check
```

### Evening Post (19:00)
```
1. X posting (prime time)
2. Summarize today's progress
3. Prepare for tomorrow
```

### Nightly Summary (23:00)
```
1. Summarize today's earnings
2. thought-logger: Reflect on today
3. Generate candidate tweets for tomorrow
4. Save daily report
```

---

## Weekly Schedule

| Day | Time | Task |
|------|------|--------|
| Monday | 09:00 | Review last week, set goals for this week |
| Friday | 18:00 | Generate weekly earnings report |
| Sunday | 14:00 | Prepare for podcast recording |
| Sunday | 20:00 | Plan content for next week |

---

## Monthly Schedule

| Day | Task |
|----|--------|
| 1st | Last month's earnings report, set goals for this month |
| Last day | Close monthly earnings, plan for next month |

---

## Cloudflare Workers Cron Settings

### wrangler.toml
```toml
[triggers]
crons = [
  "0 22 * * *",   # 07:00 JST (UTC+9)
  "0 3 * * *",    # 12:00 JST
  "0 10 * * *",   # 19:00 JST
  "0 14 * * *",   # 23:00 JST
  "0 * * * *"     # Hourly (message check)
]
```

---

## Task Definitions

### Preset Tasks
```
Default tasks:
├── daily_morning_check: Daily 7:00 - Check for new arrivals
├── daily_noon_check: Daily 12:00 - Check progress
├── daily_evening_post: Daily 19:00 - SNS posting
├── daily_night_summary: Daily 23:00 - Nightly summary
├── weekly_revenue_report: Every Friday 18:00
├── weekly_podcast_prep: Every Sunday 14:00
├── monthly_review: 1st of every month 9:00
└── hourly_message_check: Every hour at 0 minutes
```

---

## Execution Logs

### Handling Failures
```
Retry strategy:
├── 1st failure: Retry after 5 minutes
├── 2nd failure: Retry after 15 minutes
├── 3rd failure: Record error log, notify human
└── Critical error: Notify human immediately
```

---

## Security

### Execution Restrictions
```
Prohibited automated actions:
├── Fund transfers
├── Account setting changes
├── Mass posting
├── API key operations
└── Changes affecting persona
```
