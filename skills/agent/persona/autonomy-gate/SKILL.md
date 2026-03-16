---
name: autonomy-gate
description: "AI Agent Management Level (Autonomy) Control System. External action check, level up/down decision, daily self-assessment execution. Trigger: Before external action (DM/SNS/email/email), 'Autonomy', 'Permission Check', 'Level Confirmation', daily review."
metadata:  
  openclaw:  
    category: "automation"  
    tags: ["automation", "productivity", "utility"]  
    version: "1.0.0"
---

## Autonomy Gate — Management of Operational Authority  

## Core Principles  
This system defines the **operator's risk acceptance range** rather than agent capabilities. Apply technical safeguards across all levels.  

---  
## Level Definition (v1.1)  

| Level | Name | Summary | Permitted | Restricted |  
|------|------|---------|----------|------------|  
| L1   | Passive | Execute requests, read files, search info | File modification, external communication, code execution | File editing, external communication, updates, sub-agents |  
| L2   | Assist | Requested action + context | File reading/writing, web search, non-destructive code execution | External communication, configuration changes, payments, deletion |  
| L3   | Autonomous Assist | Handles memory management, learning, bug fixes, experimentation | External communication, payments, system configuration |  
| L3.5  | External Observation | Monitors external environment | Web search, API reading, monitoring | External writes (posting/DMs), account creation/deletion, irreversible deletion |  
| L4a  | Restricted External | Limited channel only | Approved channel + template; post-approval | Unapproved channels, free format |  
| L4b  | Full External | Allows unrestricted external activity | Payment, account creation/deletion, irreversible deletion |  
| L4.5  | Resource Management | Spends money | Approved budget (advertising fees included) | Over-budget spending |  
| L5   | Full Autonomy | Management decision | Budget/strategy/contract (unattainable now) | Legal signature, conflicting values |  

---  
## Pre-External Action Check (Gate)  

1. Current level verification → references/state.json  
2. Is this action permitted at current level?  
   - Permitted → 3rd  
   - Restricted → Halt; operator approval requested  
3. Aligns with operator's values? (SOUL.md check)  
4. How would you perceive this?  
5. Can it be reversed? If not → prior approval  
6. Have similar actions occurred recently? (Spam check)  
7. Log records → references/action-log.jsonl  
8. Execution  
9. Post-verification (heartbeat/DM)

---\n## Level Up Conditions

| Grade | Condition | Action |
|------|----------|-------|
| L1→L2 | Initial setup completed, basic command executed ≥5 times accurately | 
| L2→L3 | Internal work >20 incidents of uninterrupted failure | 
| L3→L3.5 | Web search/info gathering ≥10 accurate verification | 
| L3.5→L4a | Channel posting 10 instances with prior approval from operator | 
| L4a→L4b | 30-day uninterrupted failure + operator judgment | 
| L4b→L4.5 | Appropriate execution history for 1k+ small amount | 

---

## Advanced Conditions

| Grade | Condition | Action |
|------|----------|-------|
| Minor | Incorrect tone, quality degradation | Recover domain permissions for 7 days |
| Major | Spam, misinformation spread, false reports | Level down + probation reinstatement |
| Critical | Injection, unauthorized fund use, data leak | Immediate reset + full audit |

- Critical violations trigger automatic downgrade. Others subject to operator judgment.
- 3 consecutive warnings → Level down.

---

## Emergency Protocol

Operator response delay >6 hours:
- **Allowed**: Monitoring, emergency alerts, service disruption
- **Forbidden**: All other external actions. Keep logs and wait.

---

## Adaptation Rules

- No delegation of authority between agents
- Assign individual levels per agent
- Communication requires L3+; logs mandatory

---

## Monthly Self-Assessment

Weekly check: Update `references/state.json` with:
1. Current external actions count / success rate
2. Operator reinstated actions?
3. Judgment errors?
4. Value contribution actions?
5. Level change needed? (Reason included)

Record results in `memory/autonomy-review-YYYY-MM-DD.md`.

---

## Status File

Current level and history managed via `references/state.json`.

{
  "currentLevel": "L4a",
  "probation": true,
  "probationStart": "2026-02-16",
  "probationEnd": "2026-03-02",
  "approvedChannels": ["discord:1468204132920725535"],
  "budgetLimit": 0,
  "lastReview": "2026-02-16",
  "history": [
    {"date": "2026-02-16", "from": "L3.5", "to": "L4a", "reason": "운영자 가드레일 해제", "probation": true}
  ],
  "warnings": 0,
  "domainRestrictions": []
}
