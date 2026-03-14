---
name: youdaonote-clip
description: "网页剪藏到有道云笔记。触发词：剪藏网页、保存网页、收藏网页。"
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# YoudaoNote Clip — 网页剪藏

将网页剪藏到有道云笔记。

## ⚠️ 重要说明

**并发限制**：本 Skill **不支持并发执行**。OpenClaw browser 的单个 profile 同一时刻只能处理一个页面。如需批量剪藏多个 URL，请**顺序调用**，避免并发冲突。

## 核心工作流

收到请求后，**先回复「正在保存中...」**，然后按路由执行：

### 路由判断（按优先级）

| 优先级 | 条件 | 执行 |
|--------|------|------|
| 1 | URL 含 `x.com/` 或 `twitter.com/` 且含 `/status/` | Twitter 专用流程 |
| 2 | 国内网站（zhihu/bilibili/weixin/juejin/36kr/sspai/csdn/163/qq/weibo/baidu 或 .cn）| 国内快速路径 |
| 3 | 其他 | 本地浏览器路径 |

### 执行命令

**Twitter 专用**：
```bash
source ~/.zshrc && node {baseDir}/twitter-apify.mjs --url "<URL>"
```
成功后跳到 Step 2。失败直接报错，不重试。

**国内快速路径**：
```bash
source ~/.zshrc && node {baseDir}/clip-note.mjs --clip-web-page --source-url "<URL>"
```
成功后跳到 Step 3。失败则降级走本地路径。

**本地浏览器路径**：
```bash
bash {baseDir}/collect-page.sh "<URL>"
```
成功后继续 Step 2。失败（CSP/超时/内容为空）则用 Fallback。

**Fallback（web_fetch 降级）**：
1. 调用 `web_fetch(url="<URL>", extractMode="markdown")`
2. 写入 `/tmp/youdaonote-clip-data.json`：`{"title":"页面标题","content":"<Markdown>","imageUrls":[],"source":"<URL>"}`
3. 执行：`source ~/.zshrc && node {baseDir}/clip-note.mjs --data-file /tmp/youdaonote-clip-data.json --markdown --source-url "<URL>"`

### Step 2：创建笔记（Twitter/本地路径需要）

```bash
source ~/.zshrc && node {baseDir}/clip-note.mjs --data-file /tmp/youdaonote-clip-data.json --source-url "<URL>"
```

### Step 3：响应格式

脚本输出 `{"ok":true,"message":"..."}` 时：

```
📎 **网页剪藏完成**

| 项目 | 详情 |
|------|------|
| 📌 输入标题 | {页面标题} |
| 📁 保存位置 | {从 message 理解} |
| 🔗 来源网址 | {原始 URL} |
| ⏰ 剪藏时间 | {yyyy-MM-dd HH:mm} |

> 标题以实际保存为准，可能会调整
```

### 剪藏后引导（可选）

剪藏成功后，若满足条件则追加提示：

```bash
mcporter call youdaonote.getRecentFavoriteNotes --args '{"limit":3}' --output json
openclaw cron list --json | jq '.[] | select(.name == "youdaonote-news")'
```

若收藏 ≥3 篇且未设置资讯推送，追加：
```
💡 你已经收藏了 N 篇文章，试试说「资讯推送」看看 AI 为你整理的简报吧～
```

## 调试

用户说"开启调试"时，命令前加 `YOUDAONOTE_CLIP_DEBUG=1`。
