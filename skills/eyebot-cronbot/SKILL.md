---
name: eyebot-cronbot
description: Task scheduler and blockchain automation engine
version: 1.2.0
author: ILL4NE
metadata:
  chains: [base, ethereum, polygon, arbitrum]
  category: automation
---

# CronBot ⏰

**Blockchain Task Automation**

Schedule and automate recurring blockchain operations. Set triggers, create workflows, and execute transactions on schedule.

## Features

- **Scheduled Tasks**: Cron-style timing
- **Event Triggers**: React to on-chain events
- **Price Triggers**: Execute at target prices
- **Workflow Chains**: Multi-step automations
- **Retry Logic**: Handle failed transactions

## Trigger Types

| Trigger | Example |
|---------|---------|
| Time | Every hour, daily at 9am |
| Price | When ETH > $3000 |
| Event | On token transfer |
| Balance | When wallet < 0.1 ETH |
| Gas | When gas < 20 gwei |

## Use Cases

- Auto-claim rewards
- Scheduled DCA buys
- Gas-optimized transactions
- Alert on conditions
- Portfolio rebalancing

## Usage

```bash
# Schedule a task
eyebot cronbot schedule "swap ETH USDC 0.1" --cron "0 9 * * *"

# Set price trigger
eyebot cronbot trigger "buy ETH 1000" --when "ETH < 2000"

# List active jobs
eyebot cronbot list
```

## Support
Telegram: @ILL4NE
