---
name: x-knowledge-base
description: 自動收集 X 書籤並轉化為 Obsidian 知識庫，配備 AI 濃縮與交叉連結功能，支援自我進化趨勢分析
tags: [X, Twitter, 书签管理，Obsidian, 知识库，AI 浓缩]
version: 1.0.2
category: knowledge
---

# X Knowledge Base

自動將 X (Twitter) 書籤轉化為 Obsidian Markdown 格式，建立個人知識庫。支援自我進化，根據書籤傾向動態調整關鍵字和趨勢分析。

## 功能

### 基礎功能
- **抓取書籤**：從 X/Twitter 抓書籤內容
- **完整原文**：使用 Jina AI 擷取完整文章內容
- **AI 濃縮**：自動產生一句話摘要、三個重點、應用場景
- **交叉連結**：根據標籤自動建立 wiki-link
- **Obsidian 格式**：YAML frontmatter + wiki-link

### 自我進化功能 ⭐
- **興趣趨勢追蹤**：每次存書籤，自動記錄標籤並統計頻率
- **動態關鍵字調整**：根據趨勢自動調整每日情報關鍵字
- **新興標籤偵測**：發現突然增加的標籤，自動加入追蹤
- **自適應推薦**：根據書籤傾向推薦相關內容

## 使用方式

### 檢查書籤
```
"檢查我的書籤" - 抓取並儲存新書籤
```

### 自我進化
```
"今天的趨勢是什麼" - 興趣趨勢報告（含動態調整）
"我的興趣變化了嗎" - 偵測興趣轉變
```

## 檔案結構

```
x-knowledge-base/
├── SKILL.md
├── scripts/
│   ├── fetch_bookmarks.sh      # 抓書籤
│   ├── fetch_article.sh        # Jina AI 抓全文
│   └── save_obsidian.sh        # 存 Obsidian
├── tools/
│   ├── bookmark_enhancer.py    # AI 濃縮 + 交叉連結
│   └── trend_analyzer.py       # 自我進化趨勢分析
└── config/
    ├── interests.yaml           # 興趣標籤配置
    └── trends.json             # 趨勢數據（自動產生）
```

## 技術細節

### Jina AI 擷取
```bash
https://r.jina.ai/http://x.com/用戶名/status/ID
```

### MiniMax API
- endpoint: https://api.minimax.io/anthropic/v1/messages
- model: MiniMax-M2.5
