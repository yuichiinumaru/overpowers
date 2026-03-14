---
name: general-tool-notion-lifelog-system
description: "Automated life logging system integrated with Notion. Identifies dates in messages and records them to a Notion database with smart analysis."
tags: ["notion", "lifelog", "automation", "productivity", "personal"]
version: 1.0.0
---

# LifeLog 生活记录系统

自动将用户的日常生活记录到 Notion，支持智能日期识别和自动汇总分析。

## 核心功能

1. **实时记录** - 用户分享生活点滴时自动记录到 Notion
2. **智能日期识别** - 自动识别"昨天"、"前天"等日期，记录到对应日期
3. **补录标记** - 非当天记录的内容会标记为"🔁补录"
4. **自动汇总** - 每天凌晨自动运行 LLM 分析，生成情绪状态、主要事件、位置、人员

## Notion 数据库要求

创建 Notion Database，需包含：日期 (title), 原文 (rich_text), 情绪状态, 主要事件, 位置, 人员。

## 脚本说明

### 1. lifelog-append.sh
实时记录脚本，接收用户消息内容。支持日期表达如：今天、昨天、前天、具体日期。

### 2. lifelog-daily-summary-v5.sh
拉取指定日期的原文，用于 LLM 分析。

### 3. lifelog-update.sh
将 LLM 分析结果写回 Notion。

## 工作流
1. 用户发送生活记录 → 调用 `lifelog-append.sh` → 写入 Notion
2. 定时任务触发 → 调用 `lifelog-daily-summary-v5.sh`
3. LLM 分析原文 → 调用 `lifelog-update.sh` → 填充分析字段
