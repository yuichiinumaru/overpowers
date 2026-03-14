---
name: calculator-chat
description: "OpenClaw skill: 用系统计算器数字回应用户。当用户发送 /calc-chat 或表达情感时，在系统计算器上显示对应数字（如 520=我爱你，88=再见）。支持中文谐音翻译。"
metadata:
  openclaw:
    category: "communication"
    tags: ['communication', 'chat', 'messaging']
    version: "1.0.0"
---

# Calculator Chat 🧮

OpenClaw skill - 用系统计算器数字回应用户

## 功能

- 💬 自然语言理解
- 🧮 系统计算器显示
- 🌐 中文谐音支持

## 触发方式

- `/calc-chat 我爱你`
- `/calc-chat 再见`
- 直接表达情感时自动触发

## 翻译示例

| 你说 | 计算器显示 | 含义 |
|-----|-----------|------|
| 我爱你 | 520 | 我爱你 |
| 一生一世 | 1314 | 一生一世 |
| 再见 / 拜拜 | 88 | 再见 |
| 好累 / 哭 | 555 | 呜呜呜 |
| 恭喜 / 发财 | 888 | 发发发 |
| 帮我 / 救命 | 995 | 救救我 |
| 想你 / 亲亲 | 777 | 亲亲亲 |
| 顺利 / 加油 | 66 | 顺顺 |

## 使用

```bash
calc-chat "我爱你"
calc-chat "恭喜发财"
```

## 依赖

- Python 3
- 系统计算器 (各平台自带)
