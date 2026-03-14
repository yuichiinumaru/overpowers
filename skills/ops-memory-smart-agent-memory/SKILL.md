---
name: ops-memory-smart-agent-memory
version: 2.0.0
description: Advanced cross-platform long-term memory system for agents. Features layered context delivery, temperature modeling, skill experience tracking, structured storage (Markdown/JSON/SQLite), and automated archiving. Optimized for context efficiency and token savings.
tags: [memory, agent-memory, long-term-storage, context-management, knowledge-base]
category: ops
---

# Smart Agent Memory 🧠 v2.0

**跨平台 Agent 长期记忆系统 (Cross-Platform Long-Term Memory System)** — 分层上下文供给 + Skill经验记忆 + 温度模型 + 自动归档.

## ⚡ 核心原则：分层加载，按需供给 (Layered Loading, On-Demand Delivery)

> **绝对不要全量加载记忆！** 先读索引，再按需钻取。这是省 token 的关键。

### 记忆使用流程（每次需要记忆时）

```
1. index    → 读取精简索引（总览，<500 tokens）
2. 判断     → 根据当前任务决定需要哪部分记忆
3. context  → 按 tag/skill/时间 加载具体上下文
4. 行动     → 基于加载的上下文执行任务
```

### Skill 经验记忆流程（工具调用后）

```
工具调用成功/踩坑 → remember "经验总结" --skill <skill-name>
下次调用该工具前 → skill-mem <skill-name> 加载经验
```

## CLI Reference

```bash
CLI=~/.openclaw/skills/smart-agent-memory/scripts/memory-cli.js

# ★ 分层上下文（核心，优先使用）
node $CLI index                              # 精简记忆索引（先读这个！）
node $CLI context --tag <tag>                # 按标签加载上下文
node $CLI context --skill <skill-name>       # 按 Skill 加载经验+相关事实
node $CLI context --days 7                   # 最近 N 天的记忆
node $CLI context --entity-type person       # 按实体类型加载

# ★ Skill 经验记忆
node $CLI remember "该API时间参数必须用ISO格式" --skill api-tool
node $CLI skill-mem <skill-name>             # 读取某 Skill 的经验
node $CLI skill-list                         # 列出所有有经验记忆的 Skill

# 基础记忆操作
node $CLI remember <content> [--tags t1,t2] [--skill name] [--source conversation]
node $CLI recall <query> [--limit 10]
node $CLI forget <id>
node $CLI facts [--tags t1] [--limit 50]

# 教训与实体
node $CLI learn --action "..." --context "..." --outcome positive --insight "..."
node $CLI lessons [--context topic]
node $CLI entity "Alex" person --attr role=CTO
node $CLI entities [--type person]

# ★ 会话生命周期
node $CLI session-start                      # 对话开场：加载记忆概览+最近上下文
node $CLI session-end "本次讨论了XX，决定了YY"  # 对话结束：存会话摘要

# 维护
node $CLI gc [--days 30]                     # 归档冷数据
node $CLI reflect                            # 夜间反思
node $CLI stats                              # 记忆健康
node $CLI search <query>                     # 全文搜索 .md
node $CLI temperature                        # 温度报告
node $CLI extract <lesson-id> --skill-name x # 提炼 Skill
```

## Agent 行为规范

### 🔄 记忆召回 (Memory Recall)

**所有 agent 通过 `memory_search` 自动搜索 `memory/*.md`。**
双层存储确保每次写入都同步生成 Markdown，所以 `memory_search` 天然能搜到所有结构化数据。

需要深入某方向时，用 CLI 钻取：
```bash
node $CLI context --tag <tag>       # 按标签
node $CLI context --skill <name>    # 按 Skill 经验
node $CLI context --days 7          # 按时间
```

### 📝 记忆写入 (Memory Writing)

```bash
node $CLI remember "关键信息" --tags tag1,tag2    # 事实
node $CLI learn --action "..." --context "..." --outcome positive --insight "..."  # 教训
node $CLI session-end "本次讨论了XX，决定了YY"    # 会话摘要
```
> ⚠️ **不要攒到最后！** 有内容就写，中途断了也不丢。

### ✅ MUST DO
- **每次需要历史信息时**：先 `index`，看概览，再决定加载哪部分
- **工具调用踩坑后**：`remember "经验" --skill <name>` 沉淀经验
- **调用不熟悉的工具前**：`skill-mem <name>` 检查有没有历史经验
- **记录新信息时**：打好 tags，方便后续按需检索

### ❌ NEVER DO
- 不要一次性 `facts --limit 999` 全量加载
- 不要在每轮对话都加载全部记忆
- 不要忽略 `index` 直接 `recall`

## Storage Layout

```
~/.openclaw/workspace/memory/
├── YYYY-MM-DD.md           ← 每日日志
├── skills/                 ← ★ Skill 经验记忆
│   ├── api-tool.md
│   └── deploy.md
├── lessons/                ← 教训 Markdown
├── decisions/              ← 决策 Markdown
├── people/                 ← 人物档案
├── reflections/            ← 反思记录
├── .data/                  ← JSON 结构化数据
├── .archive/               ← 归档冷数据
└── .index.json             ← 温度索引 + 统计
```

## Recommended Cron Jobs

### 每晚反思 (Recommended)

```json
{
  "name": "memory-reflect",
  "schedule": { "kind": "cron", "expr": "45 23 * * *", "tz": "Asia/Shanghai" },
  "payload": {
    "kind": "agentTurn",
    "message": "运行记忆反思：node ~/.openclaw/skills/smart-agent-memory/scripts/memory-cli.js reflect，然后总结今天的记忆变化。"
  },
  "sessionTarget": "isolated",
  "delivery": { "mode": "none" }
}
```

### 每周日 GC 归档 (Recommended)

```json
{
  "name": "memory-gc",
  "schedule": { "kind": "cron", "expr": "0 2 * * 0", "tz": "Asia/Shanghai" },
  "payload": {
    "kind": "agentTurn",
    "message": "运行记忆GC：node ~/.openclaw/skills/smart-agent-memory/scripts/memory-cli.js gc --days 30，报告归档了多少条记忆。"
  },
  "sessionTarget": "isolated",
  "delivery": { "mode": "none" }
}
```
