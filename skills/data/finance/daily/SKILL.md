---
name: fund-news-daily
description: "基金新闻日报。从证券时报、中国证券报、证券日报抓取公募基金新闻，支持今日/过去七天/指定日期/指定日期范围查询，过去七天和日期范围查询支持生成Word文档。严格过滤私募/ETF龙虎榜/资金净流入等内容。"
metadata:
  openclaw:
    category: "news"
    tags: ['news', 'media', 'content']
    version: "1.0.0"
---

# 基金新闻日报

从三大权威财经平台抓取公募基金/基金行业政策新闻。

## 数据源（严格按此顺序输出）

1. **证券时报**：http://www.stcn.com/article/list/fund.html
2. **中国证券报**：https://www.cs.com.cn/tzjj/jjdt/
3. **证券日报**：http://www.zqrb.cn/fund/

## 内容筛选规则（严格执行）

### ✅ 必须抓取
- 公募基金相关所有新闻
- 基金行业监管/政策类新闻
- ETF 相关新闻

### ❌ 绝对过滤
- 私募基金相关内容
- 基金经理/机构人士访谈/专访内容
- 纯市场评论/分析类内容
- 非基金领域无关财经新闻
- 「x只ETF获融资净买入」类表述
- 「x月x日资金净流入」类表述
- 包含「ETF龙虎榜」关键词的内容

## 时间查询规则

| 查询类型 | 触发词 | 时间范围 |
|---------|--------|---------|
| 今日新闻 | "今日"、"今天"、默认 | 当日 00:00 - 当前 |
| 过去七天 | "过去七天"、"最近一周" | 当日向前推7天 |
| 指定日期 | "YYYY年MM月DD日" | 指定日期 00:00-24:00 |
| 指定日期范围 | "YYYY年MM月DD日至..." | 初始日 00:00 到 截止日 23:59 |

## 执行流程

1. **解析查询类型** → 确定时间范围
2. **抓取三大平台** → 使用 Agent Browser CLI
3. **过滤与排序** → 应用筛选规则
4. **格式化输出** → 结构化文本 或 Word文档

## 抓取命令

```bash
# 证券时报
agent-browser open "http://www.stcn.com/article/list/fund.html" --timeout 30000
agent-browser snapshot -c --timeout 20000

# 中国证券报
agent-browser open "https://www.cs.com.cn/tzjj/jjdt/" --timeout 30000
agent-browser snapshot -c --timeout 20000

# 证券日报
agent-browser open "http://www.zqrb.cn/fund/" --timeout 30000
agent-browser snapshot -c --timeout 20000

# 完成后关闭
agent-browser close
```

## 输出格式

```
【基金新闻专属汇总】
查询类型：□今日 □过去七天 □指定日期 □指定日期范围
汇总时间：YYYY年MM月DD日 HH:MM

1. 证券时报
├── 发布时间：MM月DD日 HH:MM
│   新闻标题：{原文标题}
│   内容概要：{摘抄原文核心内容}
│   新闻链接：{官方原文链接}
└── （无内容则标注「本平台当日无符合规则新闻」）

2. 中国证券报
...

3. 证券日报
...
```

## Word文档生成

**适用范围**：过去七天、指定日期范围查询

**执行方式**：调用 `scripts/fund_news_word.py`

**详细格式规范**：参见 `references/word_format.md`

## 调用示例

| 用户输入 | 行为 |
|---------|------|
| "查今日基金新闻" | 今日新闻 |
| "基金新闻日报" | 今日新闻（默认） |
| "查过去七天基金新闻" | 过去七天新闻 + Word |
| "查2026年03月10日基金新闻" | 指定日期新闻 |
| "查2026年3月1日至3月10日基金新闻" | 指定日期范围 + Word |

## 文件结构

```
fund-news-daily/
├── SKILL.md                    # 本文件
├── scripts/
│   └── fund_news_word.py       # Word文档生成脚本
└── references/
    └── word_format.md          # Word格式规范参考
```
