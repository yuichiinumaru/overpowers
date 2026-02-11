---
name: eyebot-yieldbot
description: Yield farming optimizer for maximum DeFi returns
version: 1.2.0
author: ILL4NE
metadata:
  chains: [base, ethereum, polygon, arbitrum]
  category: defi-yield
---

# YieldBot 🌾

**AI Yield Optimization**

Find and farm the best yields across DeFi. Auto-compound rewards, track APY changes, and optimize capital allocation.

## Features

- **Yield Discovery**: Find best APY opportunities
- **Auto-Compound**: Automatic reward reinvestment
- **Risk Assessment**: Protocol safety ratings
- **Position Tracking**: Monitor all farm positions
- **Rebalancing**: Optimize allocations over time

## Yield Sources

| Source | Type |
|--------|------|
| DEX LP | Trading fees + rewards |
| Lending | Supply APY |
| Staking | Protocol rewards |
| Vaults | Automated strategies |
| Points | Airdrop farming |

## Supported Protocols

- Aave, Compound (Lending)
- Uniswap, Aerodrome (LP)
- Lido, RocketPool (Staking)
- Yearn, Beefy (Vaults)

## Usage

```bash
# Find best yields
eyebot yieldbot scan --chain base --min-apy 10

# Deposit to farm
eyebot yieldbot farm <protocol> <pool> 1000 USDC

# Auto-compound position
eyebot yieldbot compound <position_id>
```

## Support
Telegram: @ILL4NE
