---
name: feishu-notes-bot
description: 通过飞书机器人创建、查询和管理笔记，支持飞书消息交互和云文档同步。
tags:
  - feishu
  - notes
  - bot
  - productivity
  - documentation
version: 1.0.0
category: productivity
---

# Feishu Notes Bot - 飞书笔记机器人

通过飞书机器人实现笔记的创建、查询和管理，支持飞书消息交互和云文档同步。

## 🎯 功能特性

### 核心功能
- 📝 **创建笔记** - 在飞书聊天中快速创建笔记
- 🔍 **搜索笔记** - 搜索本地和飞书云文档中的笔记
- 📊 **查看行动项** - 查询待办事项列表
- 📋 **会议记录** - 结构化会议笔记并同步到飞书文档
- 🔔 **消息通知** - 飞书消息提醒和推送

### 支持的笔记类型
| 类型 | 命令示例 | 存储位置 |
|------|---------|---------|
| 会议笔记 | "记录会议：项目进度会" | 飞书云文档 + 本地 |
| 快速笔记 | "记一下：明天买咖啡" | 本地 |
| 日记 | "写日记" | 本地 |
| 项目笔记 | "项目更新：A 项目进度" | 飞书云文档 |
| 行动项 | "待办：下周完成报告" | 本地 actions.md |

## ⚙️ 配置步骤

### 第 1 步：飞书应用配置

1. **访问飞书开放平台：** https://open.feishu.cn/
2. **创建企业自建应用** - 应用名称：Notes Bot
3. **配置应用权限** - 添加发送消息、文档读写、云空间访问等权限
4. **获取凭证** - App ID 和 App Secret
5. **配置机器人** - 启用机器人功能

### 第 2 步：配置到 OpenClaw

编辑 `~/.openclaw/openclaw.json` 或设置环境变量 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET`

### 第 3 步：配置笔记存储路径

编辑笔记配置文件，设置不同类型笔记的存储位置（飞书文档或本地）

## 💬 使用方式

### 私聊机器人
在飞书中私聊 Notes Bot，发送会议信息或笔记内容，机器人会自动创建结构化笔记并保存到飞书云文档。

### 群聊机器人
在飞书群聊中 @Notes Bot 创建会议笔记或查询信息。

### 快捷命令
- `/note <内容>` - 创建快速笔记
- `/meeting <主题>` - 创建会议笔记
- `/todo <任务>` - 添加行动项
- `/search <关键词>` - 搜索笔记
- `/actions` - 查看待办事项
- `/help` - 显示帮助

## 📁 文件结构

```
feishu-notes-bot/
├── SKILL.md
├── scripts/
│   ├── create_note.py
│   ├── sync_to_feishu.py
│   └── send_notification.py
├── templates/
│   ├── meeting.md
│   ├── decision.md
│   └── quick.md
└── config/
    ├── feishu_example.json
    └── routing_example.md
```

## ⚠️ 注意事项

1. **权限配置** - 确保飞书应用有文档读写权限
2. **网络访问** - 需要能访问飞书 API
3. **凭证安全** - App Secret 不要公开分享
4. **速率限制** - 飞书 API 有调用频率限制

## 🔗 相关资源

- 飞书开放平台：https://open.feishu.cn/
- 飞书 API 文档：https://open.feishu.cn/document/

---

*版本：1.0.0 | 更新时间：2026-03-16*
