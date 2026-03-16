---
name: ops-memory-auto-memory-distiller
version: 1.0.0
description: Background skill for automated long-term memory distillation. Incrementally converts unstructured JSONL conversation logs into structured, categorized, and traceable Markdown memory cards with security redaction.
tags: [memory, distillation, archiving, background-task, knowledge-base]
category: ops
---

# Auto-Memory-Distiller (自动记忆提炼)

## 简介 (Introduction)
这是一个在后台静默运行的 OpenClaw 长期记忆自动提炼技能 (Skill)。
它负责将无序的超长对话流水账 (JSONL 记录)，增量转化为结构化、按主题分类 、可溯源的长期知识库 (Markdown 记忆卡片)。

## 特性 (Features)
1. **增量游标 (Incremental)**：通过 `state.json` 记录每个 Session 的已读行数，每次只处理新增对话。
2. **主题聚合 (Topic Merge)**：自动读取已有的主题目录，将新知识合并入旧主题。
3. **安全过滤 (Redaction)**：利用大模型清洗真实的 API Key and 无关痛痒的报错日志。
4. **溯源指针 (Pointers)**：生成的知识卡片永远带上原始对话的物理文件路径 and 行号。

## 依赖配置 (Prerequisites)
脚本默认使用 Gemini API，依赖以下 Python 库：
```bash
pip install google-genai python-dotenv
```

## 使用方法 (Usage)
建议把该脚本绑定到系统的 crontab or 通过 OpenClaw 的 heartbeat 在闲暇时自动触发：

```bash
# 手动运行
python ~/.openclaw/workspace/skills/auto-distiller/distiller.py
```

## 存储目录 (Directory Structure)
- 输出的记忆目录: `~/.openclaw/workspace/memory/topics/*.md`
