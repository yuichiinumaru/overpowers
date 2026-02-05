---
name: x-search
description: X（旧Twitter）上の投稿を検索してSNSでの反応やトレンドを調べる。ツイート、SNS、トレンド、炎上、話題、反応などのキーワードが含まれる質問に使用。
---

# X (Twitter) 検索スキル

X（旧Twitter）上の投稿やトレンドを検索し、SNS上の反応を収集するスキル。

## いつ使うか

以下のような質問やタスクに対して使用:
- 「〇〇についてのSNSでの反応」
- 「〇〇のトレンド」
- 「〇〇についてツイートされていること」
- 「〇〇が話題になっているか」
- 「〇〇の炎上情報」
- 「みんなの〇〇への反応」

## トリガーキーワード

以下のキーワードが含まれる場合に発動:
- ツイート
- X / Twitter
- SNS
- バズ / トレンド
- 炎上
- 話題
- 反応
- みんなの / 世間

## 使用方法

### 検索の実行

```python
from duckduckgo_search import DDGS

def search_x(query: str, max_results: int = 5) -> list[dict]:
    """X (Twitter) を検索"""
    search_query = f"site:x.com OR site:twitter.com {query}"
    with DDGS() as ddgs:
        results = list(ddgs.text(search_query, max_results=max_results))
        return [
            {
                "title": r.get("title", ""),
                "snippet": r.get("body", ""),
                "url": r.get("href", ""),
                "source": "X"
            }
            for r in results
        ]
```

### 結果の活用

1. 検索結果から主要な意見やトレンドを抽出
2. ポジティブ/ネガティブな反応を分類
3. 影響力のあるアカウントの意見を優先
4. 最新の投稿を重視

## 制限事項

- DuckDuckGoを経由するため、リアルタイム性に限界あり
- X APIを直接使用していないため、一部の投稿は取得できない
- 検索結果は公開投稿のみ

## 関連スキル

- `web-search`: 一般的なWeb検索
- `news-search`: ニュース記事の検索
