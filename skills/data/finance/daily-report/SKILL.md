---
name: social-crypto-daily-report
version: 1.0.0
description: Cryptocurrency daily report generator. Automatically collects market data (prices, funding, news, DeFi yields, Meme trends), dehydrates and formats the content into a structured three-part Telegram message.
tags: [crypto, daily-report, telegram, automation, finance, alpha]
category: social
---

# 加密货币日报 Skill (Crypto Daily Report)

## 触发词 (Triggers)
"出日报" / "生成日报" / "加密日报" / "日报" / "发日报"

## 输出目标 (Target)
Telegram 加密新闻 Topic (threadId: 182747, chatId: 680162114)
分三条消息发送.

## 静默执行原则 (Silent Execution)
- 执行过程中**不向用户输出任何中间状态文字**。
- 三条消息发送完毕后，主会话回复**仅用 NO_REPLY**。

---

## 执行流程 (Workflow)

### Step 1：并行数据采集
从 BlockBeats, Odaily, PANews, CoinDesk 获取快讯，使用 Python 脚本获取价格、Meme 趋势 and DeFi 收益。

### Step 2：融资信息补全
结合 RootData and BlockBeats 补全机构投资信息。

### Step 3：内容处理与脱水
去重、提炼核心信息 (1-2句话)，按重要性 and 时效过滤。

### Step 4：按板块组装
分为头条新闻、融资动态、重大更新、Alpha 前线、链上/DeFi、观点、交易数据 and 宏观政策。

### Step 5：排版与发送
分三条消息发送到指定 Telegram 频道。

---

## 全局规范 (Global Standards)

- **禁止表格**
- **禁止二级缩进**
- **每条内容只保留一个链接**
- **反幻觉**：所有数据必须来自本次会话实际查询。
- **字数控制**：每条消息建议不超过 3800 字符。
