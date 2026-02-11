---
name: x402-wach
description: DeFi risk analysis toolkit powered by WACH.AI via x402 payments. Currently supports ERC-20 and Solana SPL token asset risk analysis. Use when the user asks to check if a token is safe, assess DeFi risk, detect honeypots, analyze liquidity, holder distribution, or smart contract vulnerabilities for tokens on Ethereum, Polygon, Base, BSC, or Solana. Costs 0.01 USDC per query on Base.
license: MIT
compatibility: Requires Node.js 18+, npm, network access, and a funded EVM wallet (USDC on Base).
metadata:
  author: quillai-network
  version: "1.0"
  endpoint: https://x402.wach.ai/verify-token
  payment: 0.01 USDC on Base (automatic via x402)
---

# x402-wach — DeFi Risk Analysis

A DeFi risk analysis toolkit powered by WACH.AI, using the x402 HTTP payment protocol. Payment is handled automatically (0.01 USDC per request on Base).

**Currently supported features:**

- **Asset Risk Analysis** — ERC-20 tokens (Ethereum, Polygon, Base, BSC) and Solana SPL tokens

## When to Use This Skill

Use this skill when the user wants to:

- **Assess DeFi risk** for a specific token or asset
- **Check if a token is safe** or a potential scam/honeypot
- **Get token risk scores** (overall, code, market)
- **Analyze holder distribution** (whale concentration, top holders, exchange wallets)
- **Review liquidity health** (total liquidity, trading pairs, DEXes)
- **Inspect smart contract security** (ownership, mint authority, freeze authority, blacklists, pausability)
- **Look up token market data** (price, market cap, 24h volume, supply)

## Installation

Install the CLI globally via npm:

```bash
npm install -g @quillai-network/x402-wach
```

Or install locally in a project:

```bash
npm install @quillai-network/x402-wach
```

Verify the installation:

```bash
x402-wach --version
```

## Setup

After installation, follow these steps to get ready for token analysis:

### 1. Create or Import a Wallet

You need an EVM wallet to sign x402 payments.

```bash
# Option A — Generate a brand new wallet
x402-wach wallet create

# Option B — Import an existing wallet by private key
x402-wach wallet import
```

The wallet is stored securely at `~/.x402-wach/wallet.json` with restricted file permissions (owner read/write only).

### 2. Fund the Wallet

Each token analysis costs **0.01 USDC on Base**. Send USDC (Base network) to your wallet address.

```bash
# Check your wallet address
x402-wach wallet info
```

You can bridge USDC from Ethereum or other chains using https://bridge.base.org.

### 3. You're Ready

Run the setup guide anytime:

```bash
x402-wach guide
```

## Supported Chains

| Short Name | Chain               | Token Standard | Use For                          |
| ---------- | ------------------- | -------------- | -------------------------------- |
| `eth`      | Ethereum            | ERC-20         | Tokens on Ethereum mainnet       |
| `pol`      | Polygon             | ERC-20         | Tokens on Polygon                |
| `base`     | Base                | ERC-20         | Tokens on Base                   |
| `bsc`      | Binance Smart Chain | BEP-20         | Tokens on BSC                    |
| `sol`      | Solana              | SPL            | Tokens on Solana                 |

## Commands

### Analyze Token Risk

```bash
x402-wach verify-risk <TOKEN_ADDRESS> <CHAIN_SHORT_NAME>
```

**Parameters:**

- `TOKEN_ADDRESS` — The token's contract address
  - EVM chains: `0x` followed by 40 hex characters (e.g., `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`)
  - Solana: Base58 string, 32–44 characters (e.g., `6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN`)
- `CHAIN_SHORT_NAME` — One of: `eth`, `pol`, `base`, `bsc`, `sol`

**Examples:**

```bash
# Analyze USDC on Ethereum
x402-wach verify-risk 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 eth

# Analyze TRUMP on Solana
x402-wach verify-risk 6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN sol

# Analyze USDC on Base
x402-wach verify-risk 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 base
```

### Wallet Management

```bash
# Create a new wallet
x402-wach wallet create

# Import an existing wallet by private key
x402-wach wallet import

# View wallet address and file location
x402-wach wallet info
```

### Other Commands

```bash
# List all supported chains
x402-wach chains

# Step-by-step setup guide
x402-wach guide

# Help
x402-wach --help
```

## Programmatic Usage

The SDK can also be used as a Node.js/TypeScript library:

```typescript
import { verifyTokenRisk, validateTokenAddress } from "@quillai-network/x402-wach";

// Always validate before calling (avoids wasting USDC on invalid inputs)
const validation = validateTokenAddress("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "eth");
if (!validation.valid) {
  console.error(validation.error);
} else {
  const report = await verifyTokenRisk("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "eth");
  console.log(report);
}
```

## Output Structure

The risk analysis report includes (when available):

- **Market Data**: Price, market cap, 24h volume, price change, total supply
- **Risk Scores**: Overall score, code score, market score (0–100%)
- **Honeypot Analysis**: Whether the token is a honeypot, buy/sell/transfer taxes
- **Holders**: Total count, top holders with labels (e.g., exchange wallets), supply concentration
- **Liquidity**: Total liquidity in USD, number of trading pairs, top DEX pairs
- **Code Analysis**: Ownership checks, mint/freeze authority, blacklist mechanisms, pausability
- **Social & Community**: Twitter, Discord, Telegram, website links

## Edge Cases and Error Handling

- **Invalid address format**: The CLI validates addresses client-side before making the request (and before any payment). EVM addresses must be `0x` + 40 hex chars. Solana addresses must be 32–44 base58 chars.
- **Wrong chain for address**: The CLI detects mismatches (e.g., a Solana address used with `eth`) and suggests the correct chain.
- **Token not found**: If no token exists at the given address on the selected chain, a clear error message is shown instead of an empty report.
- **Insufficient USDC**: If the wallet lacks funds, the x402 payment will fail with a 402 error prompting the user to fund their wallet.
- **No wallet configured**: The CLI will prompt the user to run `x402-wach wallet create` or `x402-wach wallet import`.

## Important Notes

- Each analysis costs **0.01 USDC on Base** — deducted automatically via the x402 payment protocol.
- The **payment always happens on Base**, regardless of which chain the token being analyzed is on.
- The wallet is stored at `~/.x402-wach/wallet.json` with restricted file permissions (owner-only).
- Always validate the token address and chain before calling `verify-risk` to avoid paying for invalid queries.
- This is a **DeFi risk analysis toolkit** — ERC-20/SPL asset risk analysis is the first supported feature, with more analysis types planned.