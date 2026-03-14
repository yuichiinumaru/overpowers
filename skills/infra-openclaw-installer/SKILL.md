---
name: infra-openclaw-installer
version: 1.0.0
description: Automated OpenClaw installation, configuration, and repair tool. Handles core installation, Claude API proxy configuration, Feishu plugin integration, and automated bug fixing.
tags: [infrastructure, installation, setup, configuration, openclaw, automation]
category: infra
---

# OpenClaw 全自动安装与配置 (OpenClaw Installer)

## 概述

本技能提供 OpenClaw 的一站式安装、配置 and 维护服务：

1. **全自动安装 OpenClaw** - 一键安装最新版本的 OpenClaw
2. **Claude API 中转站配置** - 接入用户的 AI 中转站
3. **飞书插件集成** - 安装并配置飞书消息通道
4. **Bug 自动修复** - 检测并修复 OpenClaw 的常见问题

## 依赖

确保已安装：
- Node.js 18+ 
- pnpm
- Python 3.8+

## 工作流程

### 阶段一：学习 OpenClaw 文档

首先阅读 OpenClaw 官方文档，成为 OpenClaw 专家：

```bash
# 阅读本地文档
ls ~/Library/pnpm/global/*/node_modules/openclaw/docs/

# 查看安装文档
cat ~/Library/pnpm/global/*/node_modules/openclaw/docs/install/*.md

# 查看网关配置文档
cat ~/Library/pnpm/global/*/node_modules/openclaw/docs/gateway/*.md
```

### 阶段二：检查 OpenClaw 安装状态

```bash
# 检查是否已安装
which openclaw
openclaw --version

# 检查网关状态
openclaw gateway status

# 查看日志
openclaw logs --tail 100
```

### 阶段三：全自动安装 OpenClaw

如果未安装 or 需要重新安装：

```bash
# 使用官方安装脚本
curl -fsSL https://openclaw.ai/install.sh | bash

# 或使用 pnpm 安装
pnpm add -g openclaw

# 验证安装
openclaw --version
```

### 阶段四：配置 Claude API 中转站

AI 中转站 URL：`https://ai.jiexi6.cn`

1. 编辑 OpenClaw 配置文件：
```bash
# 编辑模型配置
nano ~/.openclaw/config/models.json
```

2. 添加中转站配置：
```json
{
  "models": {
    "claude": {
      "provider": "openai-compatible",
      "baseUrl": "https://ai.jiexi6.cn/v1",
      "apiKey": "用户_API_Key",
      "models": ["claude-sonnet-4-5-20250929", "claude-opus-4-5-20250929"]
    }
  }
}
```

### 阶段五：安装飞书插件

1. 获取飞书应用凭证 (App ID, App Secret).
2. 安装飞书插件：
```bash
openclaw plugins install feishu
```

3. 配置飞书插件 in `~/.openclaw/config/feishu.json`.

### 阶段六：Bug 自动检测与修复

**常见问题及修复：**

1. **网关无法启动：**
```bash
# 清理并重启
openclaw gateway stop
openclaw gateway clean
openclaw gateway start
```

2. **模型连接失败：**
```bash
openclaw models refresh
```

### 阶段七：验证和测试

```bash
# 检查整体状态
openclaw status

# 测试消息发送
openclaw message send --channel feishu --to "测试用户" --message "测试消息"
```

## 自动化脚本

运行全自动安装脚本：

```bash
# 进入技能目录
cd ~/.openclaw/workspace/skills/install-openclaw

# 运行安装脚本
./scripts/install.sh
```

## 故障排查

### 查看日志

```bash
# 查看网关日志
tail -f ~/.openclaw/logs/gateway.log

# 使用 openclaw 命令查看
openclaw logs --follow
```

---

**参考文档：**
- OpenClaw 官方文档：https://docs.openclaw.ai/
- 飞书开放平台：https://open.feishu.cn/
