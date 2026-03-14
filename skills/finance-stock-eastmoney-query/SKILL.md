---
name: finance-stock-eastmoney-query
description: Queries real-time stock market data from EastMoney (东方财富), including prices, rankings, and indices for A-shares, HK, and US markets.
tags: [finance, stock, eastmoney, market-data, trading]
version: 1.0.0
---

# 东方财富股票查询

使用东方财富API获取股票数据。

## 支持的查询类型

- **个股行情**：股票代码、现价、涨跌、成交量、成交额
- **涨跌幅排行**：当日涨跌幅排名
- **自选股查询**：用户关注的股票信息

## 使用方式

直接问我股票相关问题，例如：
- "600519现在多少钱？"（查询茅台股价）
- "今天涨幅最高的股票"
- "帮我查一下腾讯的股票"
- "A股今天怎么样？"

## 注意事项

- 支持A股、港股、美股
- 港股代码加.HK，美股代码加.N
- 数据有几分钟延迟
