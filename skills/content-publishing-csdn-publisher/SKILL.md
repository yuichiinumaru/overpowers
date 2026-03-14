---
name: content-publishing-csdn-publisher
description: 写文章并发布到 CSDN。使用浏览器自动化 + 扫码登录。集成 blog-writer 写作方法论，产出高质量、有个人风格的技术文章。
tags: [csdn, publishing, content-creation, automation, playwright]
version: 2.3.0
---

# CSDN Publisher (content-publishing-csdn-publisher)

通过浏览器自动化发布文章到 CSDN。支持扫码登录，二维码可通过 Telegram 发送。集成了 blog-writer 写作方法论。

## 🎯 核心工作流

1. **内容创作**：调用 blog-writer 写作方法论，产出高质量初稿。
2. **状态检查**：验证 CSDN 登录状态。
3. **扫码登录**：若未登录，启动登录流程并获取二维码。
4. **文章注入**：使用 CDP (Chrome DevTools Protocol) 注入标题与正文。
5. **发布验证**：添加标签、设置原创、点击发布并获取链接。

## 🔧 技术发布流程

### 前置条件
- 安装 Chrome 浏览器。
- 安装依赖：`pip install playwright`。
- 配置 Playwright 浏览器环境。

### 扫码登录流程
1. 启动 `scripts/login.py`。
2. 捕获二维码并发送至用户（支持 Telegram）。
3. 自动保存 Cookie 至 `credentials/csdn-cookie.json`。

### 文章注入方案
- 使用 `scripts/inject-content.js` 通过 CDP 直接操作编辑器 DOM，绕过长字符串限制。

## 📝 写作风格指南
- **开头**：强有力的个人经历或观点开场。
- **结构**：清晰的小标题，短段落。
- **语言**：直接、口语化，避免陈词滥调。

## 📁 目录结构
```
csdn-publisher/
├── SKILL.md              # 本文档
├── scripts/
│   ├── login.py          # 扫码登录脚本
│   └── inject-content.js # CDP 内容注入脚本
└── examples/             # 示例文章库
```
