---
name: data-sci-pdf-analyzer
description: Extract text from PDF files, summarize, and analyze the content. Useful when users upload PDFs or ask questions about PDF content.
tags:
  - pdf
  - data-extraction
  - analysis
version: 1.0.0
---

# PDF Analyzer スキル

PDFファイルの内容を解析し、情報を抽出・要約するためのスキル。

## いつ使うか

以下のような状況で使用:
- ユーザーがPDFファイルをアップロードしたとき
- 「このPDFの内容を説明して」と頼まれたとき
- PDF内の特定のデータ（表、テキスト）を探す必要があるとき
- PDFの内容に基づいた専門的なアドバイスが求められたとき

## ステップ

1. **テキスト抽出**: `scripts/extract_text.py` を使用してPDFの全ページからテキストを読み取る。
2. **チャンク分割**: テキストが長すぎる場合は、重要なセクションごとに分割して処理する。
3. **要約・分析**: 抽出されたテキストをChatGPTに渡し、ユーザーの質問に対する回答や要約を生成させる。
4. **統合**: 他の検索結果（Web、X）がある場合は、それらと組み合わせて最終回答を作成する。

## 使用例

### プロンプト例
- 「添付したPDFの要点をおしえて」
- 「この資料の中にある予算の数字を抽出して」
- 「PDFの内容をもとに、SNSのトレンドと照らし合わせて分析して」

## スクリプト

- `extract_text.py`: `pypdf` ライブラリを使用してPDFからテキストを抽出する。