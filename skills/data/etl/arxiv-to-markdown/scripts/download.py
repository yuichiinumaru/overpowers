#!/usr/bin/env python3
"""
Batch download arXiv papers as markdown via ar5iv HTML conversion.

Usage:
    uv run --with html2text download.py --input <urls-file> --output <output-dir>

The input file should contain one arXiv URL per line (arxiv.org/html/ or arxiv.org/abs/).
Papers are fetched from ar5iv.labs.arxiv.org (HTML rendering of LaTeX papers)
and converted to clean markdown using html2text.
"""

import argparse
import os
import re
import sys
import time
import urllib.request
import urllib.error

import html2text


def extract_paper_id(url: str) -> str | None:
    """Extract arxiv paper ID from URL."""
    m = re.search(r'(?:html|abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)', url)
    if m:
        return m.group(1)
    return None


def fetch_html(paper_id: str, timeout: int = 30, max_retries: int = 2) -> str | None:
    """Fetch HTML from ar5iv."""
    url = f"https://ar5iv.labs.arxiv.org/html/{paper_id}"
    for attempt in range(max_retries + 1):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (ArXiv-to-MD pipeline; research use)'
            })
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode('utf-8', errors='replace')
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if attempt < max_retries:
                time.sleep(2 ** attempt)
            else:
                print(f"  HTTP {e.code} after {max_retries + 1} attempts", file=sys.stderr)
                return None
        except Exception as e:
            if attempt < max_retries:
                time.sleep(2 ** attempt)
            else:
                print(f"  Error: {e}", file=sys.stderr)
                return None
    return None


def html_to_markdown(html_content: str) -> str:
    """Convert HTML to markdown."""
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = True
    h.ignore_links = False
    h.protect_links = True
    h.unicode_snob = True
    return h.handle(html_content)


def extract_title(md: str) -> str:
    """Extract paper title from markdown using multiple strategies."""
    lines = md.split('\n')

    # Strategy 1: Look for '# Title:...' pattern (arxiv abstract page)
    for line in lines[:80]:
        m = re.match(r'^#\s+Title:\s*(.+)', line.strip())
        if m:
            return m.group(1).strip()

    # Strategy 2: First '# ' heading that is not navigation/category
    skip_patterns = ['quick links', 'skip', 'navigate', 'computer science',
                     'mathematics', 'physics', 'statistics', 'electrical',
                     'quantitative', 'economics']
    for line in lines[:80]:
        l = line.strip()
        if l.startswith('# ') and len(l) > 8:
            title_text = l[2:].strip()
            if not any(p in title_text.lower() for p in skip_patterns):
                return title_text

    # Strategy 3: First '## ' heading after line 10 that looks like a title
    for line in lines[5:60]:
        l = line.strip()
        if l.startswith('## ') and len(l) > 10:
            title_text = l[3:].strip()
            if not any(p in title_text.lower() for p in skip_patterns + ['submission history', 'acknowledgements', 'references', 'abstract']):
                return title_text

    return "Unknown"


def main():
    parser = argparse.ArgumentParser(description="Download arXiv papers as markdown")
    parser.add_argument("--input", "-i", required=True, help="File with arXiv URLs (one per line)")
    parser.add_argument("--output", "-o", required=True, help="Output directory for markdown files")
    parser.add_argument("--delay", "-d", type=float, default=1.5, help="Delay between requests in seconds (default: 1.5)")
    parser.add_argument("--timeout", "-t", type=int, default=30, help="Request timeout in seconds (default: 30)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be downloaded without fetching")
    args = parser.parse_args()

    # Read URLs
    with open(args.input) as f:
        urls = [line.strip() for line in f if line.strip()]

    # Extract valid paper IDs
    papers = []
    skipped = []
    for url in urls:
        pid = extract_paper_id(url)
        if pid:
            papers.append(pid)
        else:
            skipped.append(url)

    # Deduplicate versioned entries
    seen_base = {}
    unique_papers = []
    for pid in papers:
        base = re.sub(r'v\d+$', '', pid)
        if base not in seen_base:
            seen_base[base] = pid
            unique_papers.append(pid)
    papers = unique_papers

    print(f"=== ArXiv Batch Download ===")
    print(f"Total URLs: {len(urls)}")
    print(f"Valid IDs: {len(papers)} (after dedup)")
    print(f"Skipped: {len(skipped)}")

    # Create output dir and check existing
    os.makedirs(args.output, exist_ok=True)
    existing = {f.replace('.md', '') for f in os.listdir(args.output) if f.endswith('.md')}
    to_download = [p for p in papers if re.sub(r'v\d+$', '', p) not in existing and p not in existing]

    print(f"Already downloaded: {len(existing)}")
    print(f"Remaining: {len(to_download)}")

    if args.dry_run:
        print("\n[DRY RUN] Would download:")
        for pid in to_download[:20]:
            print(f"  {pid}")
        if len(to_download) > 20:
            print(f"  ... and {len(to_download) - 20} more")
        return

    if not to_download:
        print("\nNothing to download!")
        return

    # Download loop
    success = failed = not_available = 0
    total_bytes = 0

    for i, pid in enumerate(to_download):
        base_pid = re.sub(r'v\d+$', '', pid)
        out_path = os.path.join(args.output, f"{base_pid}.md")

        if os.path.exists(out_path):
            continue

        print(f"[{i+1}/{len(to_download)}] {pid}...", end=" ", flush=True)

        html = fetch_html(pid, timeout=args.timeout)
        if html is None:
            print("NOT AVAILABLE")
            not_available += 1
            continue

        md = html_to_markdown(html)
        title = extract_title(md)

        frontmatter = f"""---
arxiv_id: '{base_pid}'
source_url: 'https://ar5iv.labs.arxiv.org/html/{pid}'
title: '{title.replace("'", "")}'
downloaded: '{time.strftime("%Y-%m-%d %H:%M:%S")}'
---

"""
        content = frontmatter + md

        with open(out_path, 'w') as f:
            f.write(content)

        size = len(content)
        total_bytes += size
        success += 1
        print(f"OK ({size//1024}KB) - {title[:60]}")

        if (i + 1) % 50 == 0:
            print(f"\n--- Progress: {success}/{i+1} ok, {not_available} unavailable, {total_bytes//1024//1024}MB ---\n")

        time.sleep(args.delay)

    print(f"\n=== DONE ===")
    print(f"Success: {success}")
    print(f"Not available (404/fatal): {not_available}")
    print(f"Total size: {total_bytes / 1024 / 1024:.1f} MB")
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()
