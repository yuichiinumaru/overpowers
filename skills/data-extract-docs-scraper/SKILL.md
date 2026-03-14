---
name: docs-scraper
description: A robust web crawler and scraper utilizing Playwright to extract full documentation sites into structured Markdown directories.
tags:
- data
- extract
- ai
- llm
version: 1.0.0
category: general
---
# Documentation Scraper Skill

This skill is designed to crawl and download complex documentation sites that rely on JavaScript rendering or dynamic sidebars (such as Docusaurus, Nextra, or Fumadocs sites where the raw source isn't easily accessible).

**Important:** Before using this crawler, check if the documentation can be obtained more efficiently via the `read-docs` skill (Fumadocs `llms.txt`) or by simply cloning the original GitHub repository. This scraper is a comprehensive fallback.

## Usage

```bash
uv run python -m playwright install --with-deps chromium
uv run python skills/data-extract-docs-scraper/scripts/scrape_docs.py <start_url> <output_dir> [options]
```

### Required Arguments
- `<start_url>`: The root URL of the documentation (e.g., `https://docs.agno.com`). The crawler will not follow links that leave this base path.
- `<output_dir>`: The local directory where the structured markdown files will be saved.

### Options
- `--max-depth`: The maximum depth to crawl from the start URL (default: 5).
- `--max-pages`: The maximum number of pages to scrape globally to prevent infinite loops (default: 500).
- `--selector`: A CSS selector to specifically extract content from (e.g., `article`, `main`, `#content`). If omitted, it will try common semantic main tags before falling back to the body.
- `--headless`: Run the browser in headless mode (default: true). Use `--no-headless` to debug.

## How it works

1. It initializes a Playwright Chromium instance.
2. Starts at the provided root URL.
3. Extracts links from the page, prioritizing links within navigation sidebars and the main content.
4. Filters out external links and links outside the base URL path.
5. Converts the HTML of the main content area to Markdown using `markdownify`.
6. Saves the Markdown file, mirroring the URL's path structure inside the `<output_dir>`.
7. Recursively visits discovered links up to the specified maximum depth or page limit.

## Integration with NotebookLM Workflow

This skill is heavily utilized by the `ovp-documentation-retrieval` workflow to provide a fallback data source for the `ai-llm-gitingest-chunker` and NotebookLM pipelines.
