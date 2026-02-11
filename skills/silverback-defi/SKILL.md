---
name: silverback-defi
description: DeFi intelligence powered by Silverback — market data, swap quotes, technical analysis, yield opportunities, token audits, whale tracking, and AI chat via 26 x402 endpoints on Base chain. Pays per request with USDC.
homepage: https://silverbackdefi.app
user-invocable: true
disable-model-invocation: true
metadata: {"clawdbot":{"requires":{"bins":["node"],"env":["SILVERBACK_PRIVATE_KEY"]},"emoji":"🦍","category":"Finance & Crypto","tags":["defi","trading","crypto","yield","swap","analysis","base-chain","x402"]}}
---

# Silverback DeFi Intelligence

Silverback provides real-time DeFi intelligence via 26 x402-paid endpoints on Base chain. Every request pays with USDC — no API keys, no subscriptions. Your wallet pays per call automatically via the x402 protocol.

## Security

- This skill signs x402 USDC micropayments (max $0.05 per call for chat).
- The x402 protocol only signs EIP-3009 `transferWithAuthorization` for the exact amount in the server's 402 response. It cannot sign arbitrary transactions.
- The script ONLY calls `x402.silverbackdefi.app/api/v1/chat`. No other endpoints or domains.
- Model invocation is disabled — only you can trigger this skill.
- **Use a dedicated wallet with minimal USDC. Do NOT use your main wallet.**

## Setup

1. Install dependencies:
```bash
cd silverback-defi && npm install
```

2. Set your wallet private key as an environment variable (recommended):
```bash
export SILVERBACK_PRIVATE_KEY=0xYOUR_DEDICATED_WALLET_KEY
```

Or as a fallback, create `config.json` in the skill root:
```json
{
  "private_key": "0x_YOUR_WALLET_PRIVATE_KEY_HERE"
}
```

Your wallet needs USDC on Base. The chat endpoint costs $0.05 per call.

## Usage

```bash
node scripts/silverback.mjs "What are the top coins right now?"
node scripts/silverback.mjs "Analyze ETH technically"
node scripts/silverback.mjs "Where can I earn yield on USDC?"
node scripts/silverback.mjs "Is 0x558881c4959e9cf961a7E1815FCD6586906babd2 safe?"
node scripts/silverback.mjs "Show me whale activity on VIRTUAL"
```

## What This Skill Can Do

The script calls Silverback's `/api/v1/chat` endpoint ($0.05 USDC per call). The AI agent has access to 26 tools:

### DeFi Services
| Tool | Description |
|------|-------------|
| **swap** | Non-custodial Permit2 swap — returns EIP-712 data for client signing |
| **swap-quote** | Optimal swap routing with price impact on Base chain |
| **pool-analysis** | Liquidity pool health — TVL, volume, fees, IL risk |
| **technical-analysis** | RSI, MACD, Bollinger Bands, trend detection, trading signals |
| **defi-yield** | Yield opportunities across lending, LP, and staking protocols |
| **backtest** | Backtest a trading strategy |

### Market Data
| Tool | Description |
|------|-------------|
| **top-coins** | Top cryptocurrencies by market cap with prices and 24h changes |
| **top-pools** | Best yielding liquidity pools on Base DEXes |
| **top-protocols** | Top DeFi protocols ranked by TVL |
| **trending-tokens** | Trending tokens on CoinGecko |
| **gas-price** | Current Base chain gas prices |
| **dex-metrics** | DEX trading volume and metrics |
| **token-metadata** | Token details and contract info |
| **correlation-matrix** | Token price correlation analysis |

### Intelligence
| Tool | Description |
|------|-------------|
| **token-audit** | Smart contract security audit — honeypot detection, ownership, taxes |
| **whale-moves** | Large wallet movement tracking |
| **arbitrage-scanner** | Cross-DEX arbitrage opportunities |
| **agent-reputation** | ERC-8004 on-chain reputation scores for AI agents |
| **agent-discover** | Discover trusted AI agents by capability |

### Chat
| Tool | Description |
|------|-------------|
| **chat** | AI chat with all intelligence tools — ask anything |

## How x402 Payment Works

1. Script calls `x402.silverbackdefi.app/api/v1/chat`
2. Server returns HTTP 402 with exact USDC amount ($0.05)
3. `@x402/fetch` signs an EIP-3009 `transferWithAuthorization` for that amount
4. Request retries with the signed payment in the `X-Payment` header
5. Server verifies on-chain, returns data

The signing is scoped to the exact amount and recipient specified by the server. The x402 library does not sign arbitrary transactions.

## MCP Server

For Claude Desktop, Cursor, or Claude Code integration, use the MCP package:
```bash
npm install -g silverback-x402-mcp
```
See: https://www.npmjs.com/package/silverback-x402-mcp

## Links

- **Website**: https://silverbackdefi.app
- **x402 Docs**: https://silverbackdefi.app/x402
- **API Base**: https://x402.silverbackdefi.app
- **Source**: https://github.com/RidingLiquid/silverback-skill
