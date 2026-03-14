---
name: crypto-auto-progression
description: Enable and maintain "real execution driven" auto-progression (cron) for crypto-hedge-backtest. Use when user requests automatic progression every N minutes, automatic phase result reporting, troubleshooting persistent cron errors, or solidifying automation workflows into reusable solutions.
tags: [crypto, automation, cron, backtest, progression]
version: "1.0.0"
---

# Crypto Auto Progression

Provides a reusable auto-progression workflow for `projects/crypto-hedge-backtest`.

## Objective
- Use cron to drive periodic progression, not empty reminders.
- Each trigger must perform at least one real execution: `run script / modify code / produce file`.
- Report only when there are phase results, avoiding repetitive status spam.

## Standard Task Templates

### 1) 5-minute Progression Task (Main Task)
- schedule: `every 5m`
- sessionTarget: `main`
- payload.kind: `systemEvent`
- payload.text must emphasize "real execution + phase result reporting + no duplicate reminders without results"

### 2) 30-minute Health Check (Guardian Task)
- schedule: `every 30m`
- Check if there are real outputs in the last 30 minutes (new files/new commits/new reports)
- Alert and explain blockers if no output

### 3) Daily Report (Optional)
- schedule: `cron 30 21 * * *` + `Asia/Manila`
- Summary: completed items, key results, risks, next day plan

## Creation & Validation (Mandatory Order)
1. First create **1** 5-minute main task.
2. Immediately `cron run --force` to manually trigger once.
3. Use `cron runs` to confirm `status=ok`.
4. Then create 30-minute health check and daily report.
5. Use `cron list` to verify `enabled=true` and `nextRunAtMs`.

## Troubleshooting (High-Frequency Issues)
- `invalid cron.add params ... required property 'name/schedule/sessionTarget/payload'`
  - Cause: job body missing fields or empty `job:{}`.
  - Fix: Resend with complete job structure, do not blindly retry same bad request.

- `openclaw-cn cron disable ... --json` reports `unknown option '--json'`
  - Cause: `cron disable` does not support `--json`.
  - Fix: Remove `--json`.

- Binance data pull occasionally fails with `SSL: UNEXPECTED_EOF_WHILE_READING`
  - Fix: Add network retry + exponential backoff in data layer; retry before continuing scan link.

## Reporting Standards (This Project)
- Report when there are substantive results:
  - New/updated files
  - Key metrics/conclusions
  - Next steps
- Status statement binary choice:
  - `继续推进中（无需你回复）` (Continuing progression, no reply needed)
  - `我已暂停推进，等待你决策` (I've paused progression, awaiting your decision)
