---
name: content-news-newsnow-reader
description: Elegant real-time news reader for multiple Chinese platforms (Weibo, Zhihu, Baidu, Douyin, WallStreetCN, etc.). Uses standard Python libraries to fetch and format news without external dependencies.
tags: content, news, reader, rss, aggregator
version: 1.0.0
---

# NewsNow Reader Skill

Fetch and display real-time trending news from multiple platforms.

## Functions

- **Multi-Platform Support**: Weibo, Zhihu, Baidu, Douyin, WallStreetCN, Toutiao, and ThePaper.
- **Zero Dependencies**: Built with Python standard libraries (`urllib`, `json`, `re`).
- **Flexible Formatting**: Elegant (emoji + borders), compact, markdown, and summary styles.
- **Automated Auth**: Handles session cookies and API calls automatically.

## Usage

### Fetch News
```bash
# Fetch Weibo hot search (default)
python scripts/fetch_news.py

# Fetch Zhihu hot list
python scripts/fetch_news.py zhihu
```

### Format Output
```bash
# Display news in elegant format
python scripts/format_news.py news.json elegant
```

## Source Identifiers
| Source | ID |
|------|------|
| Weibo | `weibo` |
| Zhihu | `zhihu` |
| Baidu | `baidu` |
| Douyin | `douyin` |
| WallStreetCN | `wallstreetcn` |
| Toutiao | `toutiao` |
| ThePaper | `thepaper` |
