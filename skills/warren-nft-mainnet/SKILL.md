---
name: warren-nft
description: Deploy NFT collections permanently on MegaETH mainnet. Images are stored on-chain via SSTORE2, then published through WarrenContainer and WarrenLaunchedNFT.
metadata: {"openclaw":{"emoji":"🖼️","homepage":"https://thewarren.app","requires":{"anyBins":["node"]}}}
user-invocable: true
---

# Warren NFT - On-Chain NFT Collection Deployment

Deploy complete NFT collections with permanent on-chain image storage on MegaETH mainnet.

**Network**: MegaETH Mainnet (Chain ID: 4326)
**RPC**: `https://mainnet.megaeth.com/rpc`
**Explorer**: https://megaeth.blockscout.com

## How It Works

```
Your Images → SSTORE2 (on-chain) → WarrenContainer → WarrenLaunchedNFT
                                     /images/1.png     tokenURI renders
                                     /images/2.png     images on-chain
                                     ...
```

1. Each image is deployed as a Page contract (fractal tree for larger files).
2. All images are stored in a WarrenContainer NFT at `/images/1.png`, `/images/2.png`, etc.
3. A WarrenLaunchedNFT contract is deployed referencing the container.
4. Collection is registered for management and mint pages.

## Setup (One Time)

```bash
cd {baseDir}
bash setup.sh
```

## Prerequisites

### 1. Wallet + MegaETH ETH

Bridge ETH from Ethereum to MegaETH mainnet for gas.

Approximate cost:

- ~0.03 ETH for a small collection (around 10 images)

### 2. Genesis Access Requirement

The script checks in this order:

1. Human Genesis Key (0xRabbitNeo)
2. 0xRabbit.agent Key
3. Auto-mint 0xRabbit.agent Key (free)

Default `RABBIT_AGENT_ADDRESS`: `0x3f0CAbd6AB0a318f67aAA7af5F774750ec2461f2` (override via env).
If you override or unset it, mint a human key:

- https://thewarren.app/mint

## Contract Addresses (Mainnet)

| Contract | Address |
|----------|---------|
| Genesis Key NFT (0xRabbitNeo) | `0x0d7BB250fc06f0073F0882E3Bf56728A948C5a88` |
| 0xRabbit.agent Key NFT | `0x3f0CAbd6AB0a318f67aAA7af5F774750ec2461f2` |
| WarrenContainer | `0xF70B6082d0309E93Cc4C83eeA562Fa1E985Ea21f` |
| WarrenContainerRenderer | `0x9b1f966491F1dBf734DECadaAA2aaA65cdF8B923` |
| Treasury/Relayer | `0xcea9d92ddb052e914ab665c6aaf1ff598d18c550` |

## Deploy NFT Collection

### Option 1: From Image Folder

```bash
cd {baseDir}
PRIVATE_KEY=0x... node deploy-nft.js \
  --images-folder ./my-art/ \
  --name "Cool Robots" \
  --symbol "ROBOT" \
  --description "100 unique robot NFTs on-chain" \
  --max-supply 100
```

### Option 2: Auto-Generate SVG Art

```bash
cd {baseDir}
PRIVATE_KEY=0x... node deploy-nft.js \
  --generate-svg 10 \
  --name "Generative Art" \
  --symbol "GART" \
  --description "AI-generated on-chain art"
```

### Full Configuration

```bash
PRIVATE_KEY=0x... node deploy-nft.js \
  --images-folder ./collection/ \
  --name "Cyber Punks" \
  --symbol "CPUNK" \
  --description "On-chain cyberpunk collection" \
  --max-supply 1000 \
  --whitelist-price 0.01 \
  --public-price 0.02 \
  --max-per-wallet 5 \
  --royalty-bps 500
```

## CLI Options

| Option | Required | Default | Description |
|--------|----------|---------|-------------|
| `--images-folder <path>` | * | - | Folder with image files |
| `--generate-svg <count>` | * | - | Generate random SVG art (1-256) |
| `--name <string>` | Yes | - | Collection name |
| `--symbol <string>` | Yes | - | Collection symbol (3-5 chars) |
| `--description <text>` | No | Auto | Collection description |
| `--max-supply <number>` | No | Image count | Maximum mintable NFTs |
| `--whitelist-price <eth>` | No | 0 | Whitelist mint price in ETH |
| `--public-price <eth>` | No | 0 | Public mint price in ETH |
| `--max-per-wallet <number>` | No | 10 | Mint limit per wallet |
| `--royalty-bps <number>` | No | 500 | Royalty (500 = 5%, max 1000 = 10%) |

\* Either `--images-folder` or `--generate-svg` is required.

## Output

```
🎉 NFT Collection Deployed!
============================================================
NFT Contract:  0xABC...
Container ID:  15
Image Count:   10
Max Supply:    100
Public Price:  0 ETH (Free)

📋 Management: https://thewarren.app/launchpad/0xABC.../
🎨 Mint Page:  https://thewarren.app/launchpad/0xABC.../mint
============================================================
```

## Image Requirements

- Formats: PNG, JPG, JPEG, SVG, GIF, WebP
- Size: up to 500KB per image
- Count: 1-256 images per collection
- Naming: sequential or alphabetical

## Example Workflows

### Quick Test (3 SVGs)

```bash
cd {baseDir}
PRIVATE_KEY=0x... node deploy-nft.js --generate-svg 3 --name "Quick Test" --symbol "QT"
```

### Medium Test (20 SVGs)

```bash
cd {baseDir}
PRIVATE_KEY=0x... node deploy-nft.js --generate-svg 20 --name "Art Collection" --symbol "ART" --public-price 0.001
```

### Full Collection (100 SVGs)

```bash
cd {baseDir}
PRIVATE_KEY=0x... node deploy-nft.js --generate-svg 100 --name "Century" --symbol "C100" --max-per-wallet 3
```

## Troubleshooting

**"No ETH balance"**
- Bridge ETH to MegaETH mainnet.

**"No Genesis Key found and RABBIT_AGENT_ADDRESS is not configured"**
- Set `RABBIT_AGENT_ADDRESS=0x3f0CAbd6AB0a318f67aAA7af5F774750ec2461f2`, or mint human key at `https://thewarren.app/mint`.

**"Image exceeds 500KB"**
- Resize or compress images.

**"Too many images"**
- Maximum 256 images per container.

**DB registration warning**
- Non-critical. Collection is still deployed on-chain.

## Notes

- Mainnet content is permanent and immutable.
- You pay gas from your own wallet.
