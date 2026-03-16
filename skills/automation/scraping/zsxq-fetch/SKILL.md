---
name: zsxq-fetch
description: 知识星球帖子抓取助手，自动抓取指定星球的最新帖子，支持全部/仅精华两种筛选模式，支持通过帖子链接或 ID 获取单条帖子详情，支持多星球配置。
tags: [zsxq, knowledge-star, content-fetch, social-media]
version: 1.0.0
category: utility
---

# 知识星球帖子抓取助手

从指定知识星球抓取最新帖子内容，支持全部帖子与仅精华两种筛选模式，支持通过帖子链接或 ID 查看单条帖子详情，支持多星球配置。

## 认证与环境

### 必需环境变量

```bash
export ZSXQ_TOKEN="你的 token 值"
```

**执行前必须检查 `$ZSXQ_TOKEN` 是否已设置。**

获取方式：浏览器打开 wx.zsxq.com → 登录 → F12 → Application → Cookies → 复制 `zsxq_access_token` 的值。

### 依赖安装

无第三方依赖，仅需 Node.js >= 18。

## 配置文件

### `{baseDir}/groups.json` — 多星球配置

```json
[
  {
    "group_id": "YOUR_GROUP_ID",
    "name": "星球名称",
    "scope": "digests",
    "max_topics": 20
  }
]
```

字段说明：
- `group_id`：从星球 URL `wx.zsxq.com/group/{group_id}` 获取
- `name`：星球名称（展示用）
- `scope`：`digests`（仅精华）| `all`（全部），推荐 `digests`
- `max_topics`：每个星球最多抓取的帖子数

## 子命令

### 1. 获取帖子列表
```bash
node {baseDir}/fetch_topics.js topics <group_id> [count] [scope]
```

### 2. 获取精华帖（快捷方式）
```bash
node {baseDir}/fetch_topics.js digests <group_id> [count]
```

### 3. 获取指定帖子详情
```bash
node {baseDir}/fetch_topics.js topic <group_id> <topic_id_or_url>
```

### 4. 列出已加入的星球
```bash
node {baseDir}/fetch_topics.js groups
```

## 错误处理

| 错误场景 | 检测方式 | 处理 |
|---------|---------|------|
| Token 未设置 | `$ZSXQ_TOKEN` 为空 | 提示用户设置并说明获取方法 |
| Token 过期 | HTTP 401 | 提示重新获取 token |
| 未加入星球 | HTTP 403 | 提示用户需先加入该星球 |
| API 限流 | HTTP 429 | 自动重试（指数退避 2s/4s/8s） |
| 星球不存在 | API 返回 `succeeded=false` | 跳过该星球，报告中标注 |
