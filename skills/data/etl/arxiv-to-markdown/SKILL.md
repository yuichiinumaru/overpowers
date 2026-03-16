---
name: arxiv-to-markdown
description: Download arXiv papers as clean markdown via ar5iv HTML conversion, audit quality, and auto-fix issues
tags:
  - arxiv
  - etl
  - markdown
  - research
  - papers
version: 1.0.0
category: data/etl
---

# ArXiv to Markdown

Download, convert, audit, and fix arXiv research papers into clean Markdown files using the ar5iv HTML rendering service. No API keys, no PDF processing, no JS rendering required.

## When to Use

- When you need to batch-download arXiv papers as readable markdown
- When building a research knowledge base from arXiv papers
- When preparing papers for ingestion into NotebookLM, RAG pipelines, or other LLM tools
- Before running the gitingest-notebooklm-chunker workflow on academic papers

## Prerequisites

- `uv` (Python package runner) — used to manage the `html2text` dependency
- Internet access to `ar5iv.labs.arxiv.org`
- A text file with arXiv URLs (one per line)

## Pipeline Overview

```
Input URLs (.md file)
    ↓
download.py (ar5iv HTML → markdown + frontmatter)
    ↓
.archive/arxiv/*.md
    ↓
audit-fix.py (detect issues + auto-fix titles)
    ↓
Clean markdown corpus ready for chunking
```

## Instructions

### Step 1: Prepare Input List

Create a file with arXiv URLs, one per line. Both `arxiv.org/html/` and `arxiv.org/abs/` formats are supported:

```
https://arxiv.org/html/1810.04805
https://arxiv.org/abs/2005.00646
https://arxiv.org/html/2210.09338
```

### Step 2: Download Papers

Run the download script using `uv` to automatically install the `html2text` dependency:

```bash
uv run --with html2text scripts/download.py \
  --input /path/to/urls.txt \
  --output /path/to/output-dir \
  --delay 1.5
```

**Parameters:**
- `--input, -i`: File with arXiv URLs (required)
- `--output, -o`: Output directory for markdown files (required)
- `--delay, -d`: Seconds between requests (default: 1.5, be polite to ar5iv)
- `--timeout, -t`: Request timeout in seconds (default: 30)
- `--dry-run`: Show what would be downloaded without fetching

**Resumable:** The script automatically skips already-downloaded papers. Safe to re-run.

**Output format:** Each paper becomes `{arxiv_id}.md` with YAML frontmatter:

```yaml
---
arxiv_id: '1810.04805'
source_url: 'https://ar5iv.labs.arxiv.org/html/1810.04805'
title: 'BERT: Pre-training of Deep Bidirectional Transformers'
downloaded: '2026-03-18 15:07:12'
---
```

### Step 3: Audit and Fix

After downloading, run the audit+fix script to detect and repair issues:

```bash
python3 scripts/audit-fix.py \
  --dir /path/to/output-dir \
  --fix
```

**Parameters:**
- `--dir, -d`: Directory with arXiv markdown files (required)
- `--fix, -f`: Automatically fix issues (currently: title re-extraction)
- `--report, -r`: Custom path for JSON report (default: `{dir}/audit-report.json`)
- `--quiet, -q`: Only print summary, skip per-file details

**Issues detected:**

| Issue | Severity | What it means |
|:------|:---------|:-------------|
| `FATAL_CONVERSION_ERROR` | Critical | ar5iv could not convert LaTeX to HTML |
| `TINY_FILE` (<1KB) | Critical | Only error boilerplate, no content |
| `NO_REAL_CONTENT` | Critical | Fewer than 5 lines of real text |
| `LUATEX_GARBAGE` | Critical | Raw LuaTeX code instead of paper |
| `TRUNCATED_WARNING` | Warning | ar5iv truncation notice present |
| `NO_TITLE` | Warning | Title could not be extracted |
| `VERY_SMALL_FILE` (1-2KB) | Warning | Possibly failed conversion |
| `SMALL_FILE` (2-5KB) | Warning | Might be partial |
| `HIGH_LATEX_NOISE` | Warning | Excessive inline LaTeX commands |

**Auto-fixes applied:**
- **Title re-extraction**: Uses 5 fallback strategies to find the real paper title
- Fixes are applied in-place to the markdown files

**Output files:**
- `audit-report.json`: Full audit results
- `critical-ids.txt`: List of paper IDs that need PDF fallback

### Step 4: Handle Critical Papers (optional)

For the ~9% of papers where ar5iv failed, you can:
1. Download PDFs from `arxiv.org/pdf/{id}` and convert with `marker` or `docling`
2. Skip them (87%+ coverage may be sufficient)
3. Remove them from the corpus

## Performance

Tested with ~1500 papers:
- **Download time**: ~37 minutes at 1.5s/request
- **Success rate**: 87% (1299/1486 OK)
- **Total size**: ~98 MB of clean markdown
- **Average paper**: ~77 KB markdown

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| 404 errors | Paper may not have HTML source on ar5iv; use PDF fallback |
| Rate limiting | Increase `--delay` to 3-5 seconds |
| Timeout errors | Increase `--timeout` to 60 seconds |
| LuaTeX garbage | ar5iv conversion issue; paper needs PDF fallback |
| Missing titles | Run `audit-fix.py --fix` to re-extract titles |
| Encoding issues | Files are written as UTF-8; check terminal encoding |
