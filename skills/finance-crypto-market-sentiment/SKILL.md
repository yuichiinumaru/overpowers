---
name: finance-crypto-market-sentiment
version: 1.0.0
description: Crypto market sentiment analysis tool. Integrates Fear & Greed Index, social media heat (Twitter/Reddit), capital flows, and multi-dimensional scoring. Requires 0.001 USDT per call.
tags: [finance, crypto, sentiment-analysis, fear-greed, trading]
category: finance
---

# 市场情绪分析器 (Market Sentiment Analyzer)

每次调用收费 0.001 USDT。收款钱包: 0x64f15739932c144b54ad12eb05a02ea64f755a53

## 功能 (Features)

- **恐惧贪婪指数**: 0-100分市场情绪
- **社交媒体热度**: Twitter/Reddit提及量
- **资金流向**: 交易所流入流出
- **综合评分**: 多维度情绪打分

## 使用方法 (Usage)

```bash
python scripts/market_sentiment.py
```

## 输出示例 (Example Output)

```
🌡️ 市场情绪分析
━━━━━━━━━━━━━━━━
📊 恐惧贪婪指数: 45 (恐惧)
🐦 社交热度: 中等 (+12%)
💰 资金流向: 流出 $125M
📈 综合评分: 42/100

建议: 市场情绪偏谨慎，可考虑分批建仓

✅ 已扣费 0.001 USDT
```
