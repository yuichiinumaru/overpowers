---
name: communication-bot-qqbot
description: QQ 官方机器人 (QQ Bot) 配置与接入指南。包含从创建机器人到接入 OpenClaw AI 的全过程，以及常见问题排查。
tags: [qq, bot, communication, configuration, ai-integration]
version: 1.0.0
---

# QQ 官方机器人配置指南 (communication-bot-qqbot)

## 前置条件

- QQ 号（建议使用小号）
- 可访问公网 IP（家庭宽带需处理动态 IP）
- 服务器或本地机器
- OpenClaw 已安装

---

## 配置步骤

### 步骤 1: 创建 QQ 机器人

1. 访问 [QQ 机器人平台](https://bot.q.qq.com/wiki)
2. 点击「登录」，使用 QQ 扫码登录
3. 进入「开发者注册」页面，完成实名认证
4. 点击「创建机器人」，填写基本信息
5. 记录关键信息：
   - AppID (如: 102842119)
   - AppSecret (点击显示，只显示一次，务必保存！)

⚠️ **重要**: AppSecret 只显示一次，立即保存！

---

### 步骤 2: 配置 IP 白名单

**家庭宽带需要公网 IP，并配置到 QQ 开放平台。**

#### 获取公网 IP

```bash
curl https://api.ipify.org
```

#### 配置白名单

1. 进入 [QQ 机器人控制台](https://bot.q.qq.com/console/)
2. 选择你的机器人
3. 点击「开发设置」→「IP 白名单」
4. 添加获取到的公网 IP
5. 保存

---

### 步骤 3: 配置 OpenClaw

在 `openclaw.json` 中添加 QQ 频道配置：

```json
{
  "channels": {
    "qq": {
      "enabled": true,
      "appId": "你的AppID",
      "appSecret": "你的AppSecret"
    }
  }
}
```

---

### 步骤 4: 部署 QQ Bot 程序

复制 `qq_official_bot.py` 到工作区：

```bash
cp qq_official_bot.py ~/.openclaw/workspace/
```

编辑配置文件：

```python
APP_ID = "你的AppID"
APP_SECRET = "你的AppSecret"
```

---

### 步骤 5: 启动机器人

```bash
# 启动 QQ Bot
~/.openclaw/workspace/qq_bot_daemon.sh start

# 查看状态
~/.openclaw/workspace/qq_bot_daemon.sh status
```

---

## 常见问题与解决方案

### 问题 1: 错误 11298 - IP 不在白名单
- 获取当前公网 IP 并更新白名单。

### 问题 2: 无法收到消息
- 检查 Intents 权限是否开启（GUILDS, GROUP_AND_C2C_EVENT, AT_MESSAGES）。
- 确认选择「使用长连接接收事件」。

### 问题 3: ModuleNotFoundError
- 执行 `pip3 install requests aiohttp websockets --user`。

---

## 管理命令

```bash
~/.openclaw/workspace/qq_bot_daemon.sh {start|stop|restart|status}
```
