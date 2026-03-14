---
name: knowledge-distill
version: 1.0.0
description: Knowledge distillation and archiving tool. Categorizes discussion results into five specific knowledge documents (Command Memory, Professional Work, General Knowledge, Research Logs, and Thought Distillation).
tags: [knowledge-management, archiving, documentation, distillation, research-logs]
category: knowledge
---

# 知识蒸馏 Skill (Knowledge Distillation)

将讨论成果分类写入对应的知识文档，支持便捷记录命令、知识结论、思维框架。

## 初始化 (Initialization)

首次使用时，检查 `~/knowledge-base/` 是否存在：
- 不存在则自动创建目录和5个空文档
- 用户可通过设置 `KNOWLEDGE_BASE_PATH` 环境变量自定义路径

```
~/knowledge-base/
├── 小龙虾命令记忆库.md     ← OpenClaw/CLI 命令速查
├── 专业知识蒸馏.md         ← 专业领域技术结论
├── 兴趣知识蒸馏.md         ← 工作以外的学习内容
├── 学习研究日志.md         ← 每次讨论的过程记录
└── 思维蒸馏.md             ← 方法论、认知模型、思考框架
```

## 五类文档分工 (Document Classification)

| 目标文档 | 写入条件 | 内容类型 |
|----------|---------|---------|
| 小龙虾命令记忆库.md | 用户说"记一下命令" | 命令格式、参数说明、使用场景 |
| 专业知识蒸馏.md | 专业领域的技术结论 | 技术参数、操作步骤、最佳实践 |
| 兴趣知识蒸馏.md | 工作以外的兴趣领域知识 | 与专业知识同等格式 |
| 学习研究日志.md | 每次讨论的过程记录 | 问题背景、结论、演变脉络 |
| 思维蒸馏.md | 非具体内容的思维结晶 | 思考方式、方法论、决策框架 |

## 执行流程 (Workflow)

1. **判断分类**：根据内容 and 触发词判断写入哪个文档
2. **整理内容**：提炼核心结论，去掉试错过程
3. **展示预览**：在对话框展示整理好的内容 and 计划写入位置
4. **等待确认**：用户确认后才执行写入
5. **写入日志**：同步在学习研究日志记录本次讨论过程

## 约束 (Constraints)

- 未经用户确认不可写入任何文档
- 蒸馏只保留最终正确结论，不保留试错过程
- 内容简洁，每条结论独立成块，便于检索
