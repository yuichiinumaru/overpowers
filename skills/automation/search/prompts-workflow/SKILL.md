---
name: prompts-workflow
description: Automated workflow for collecting, converting, and publishing AI prompts to ClawdHub. Collects from multiple sources (Reddit, GitHub, Hacker News, SearXNG), converts prompts into Clawdbot Skills, and publishes them automatically.
tags: [automation, prompts, workflow, clawdhub, publishing]
version: 1.0.0
category: automation
---

# Prompts Workflow - AI 提示词自动化工作流

自动化收集、转换和发布 AI 提示词到 ClawdHub 的工作流技能。

## 功能

- **Collect**: 从多个来源（Reddit、GitHub、Hacker News、SearXNG）收集 AI 提示词
- **Convert**: 将收集到的提示词转换为 Clawdbot Skills
- **Publish**: 自动发布生成的技能到 ClawdHub

## 使用方式

### 自动模式（推荐）

```bash
cd /root/clawd/skills/prompts-workflow
node main.js auto
```

### 交互模式（断点恢复）

```bash
node main.js interactive
```

### 手动模式（指定步骤）

```bash
node main.js manual collect
node main.js manual collect convert
node main.js manual publish
```

### 查看状态

```bash
node main.js status
```

## 输出文件

- `output/state.json`: 工作流执行状态
- `output/workflow.log`: 详细日志
- `output/prompts/`: 收集到的原始提示词
- `output/skills/`: 转换后的技能

## Cron 集成

```bash
0 9 * * * cd /root/clawd && /usr/local/bin/clawdbot sessions_spawn --task "运行 prompts-workflow 技能" --cleanup delete
```

## 状态管理

支持状态：pending, running, completed, failed

失败时，`interactive` 模式会自动跳过已完成的步骤，从失败处恢复。
