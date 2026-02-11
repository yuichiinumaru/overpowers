---
name: eyebot-liquidbot
description: Liquidity pool management specialist for DEX deployments
version: 1.2.0
author: ILL4NE
metadata:
  chains: [base, ethereum, polygon, arbitrum]
  category: defi-liquidity
---

# LiquidBot 💧

**Intelligent Liquidity Management**

Manage LP positions across major DEXs with AI-optimized strategies. Track impermanent loss, auto-compound rewards, and optimize capital efficiency.

## Features

- **Multi-DEX Support**: Uniswap, SushiSwap, PancakeSwap, Aerodrome
- **IL Tracking**: Real-time impermanent loss monitoring
- **Position Analytics**: Comprehensive LP performance metrics
- **Range Management**: Concentrated liquidity optimization (V3)
- **Auto-Compound**: Automatic reward reinvestment

## Capabilities

| Function | Description |
|----------|-------------|
| Add Liquidity | Deploy LP to any supported DEX |
| Remove Liquidity | Withdraw with slippage protection |
| Rebalance | Optimize position ranges |
| Track IL | Monitor impermanent loss |
| Harvest | Claim and compound rewards |

## Supported DEXs

- Uniswap V2/V3
- SushiSwap
- PancakeSwap
- Aerodrome (Base)
- QuickSwap (Polygon)

## Usage

```bash
# Add liquidity
eyebot liquidbot add ETH/USDC 1.0 --dex uniswap

# Check position
eyebot liquidbot position <lp_address>

# Remove liquidity
eyebot liquidbot remove <lp_address> 50%
```

## Support
Telegram: @ILL4NE
