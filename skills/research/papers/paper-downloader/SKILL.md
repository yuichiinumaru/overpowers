---
name: sci-academic-paper-downloader
description: Batch downloader for academic paper PDFs from multiple sources (arXiv, PubMed, PMC, Semantic Scholar). Prioritizes official free channels and provides manual download guides for paid articles.
tags: [academic-papers, pdf-downloader, arxiv, pubmed, research-tools, metadata-extraction]
version: 1.0.0
---

# Scholar Paper Downloader

## Overview

A skill for downloading academic paper PDFs, helping users batch-download papers from various public academic repositories, automatically extracting metadata, and generating bibliography index lists.

**Design Principles**:
- Prioritize downloading from official free channels (arXiv, PMC, PubMed Central).
- Provide detailed manual download guidance for paid articles.
- Avoid automatic download methods that may infringe on copyrights.

## When to Use This Skill

Trigger this skill when the user needs to:
- Download PDF versions of academic papers.
- Batch-acquire multiple papers.
- Download preprints from sites like arXiv.
- Download open-access literature from PubMed Central.
- Search and download papers by keywords.
- Batch-download papers by ID.
- Generate bibliography index lists.

## Usage Scenarios

### 1. Search and Download by Keyword

```bash
python scripts/batch_downloader.py -q "machine learning"
```

### 2. Download by arXiv ID

```bash
python scripts/batch_downloader.py --ids 2103.00001 2103.00002
```

### 3. Query Information by DOI

```bash
python scripts/doi_query.py 10.1056/NEJMoa1915872
```

### 4. Download from PubMed/PDF URL

```bash
python scripts/batch_downloader.py --urls "https://arxiv.org/pdf/2103.00001.pdf"
```

### 5. Custom Configuration

```bash
python scripts/batch_downloader.py -q "deep learning" -o ./my_papers -m 20 -w 5
```

## Features

### Core Capabilities

1.  **Multi-source Search**: Supports multiple academic sources including arXiv, PubMed, PMC, Semantic Scholar, etc.
2.  **Batch Downloading**: Concurrent downloading with progress tracking.
3.  **Automatic Renaming**: Automatically renames files based on metadata.
4.  **Metadata Extraction**: Extracts titles, authors, dates, etc.
5.  **Index Generation**: Generates indexes in Markdown and JSON formats.
6.  **Legal Priority**: Only automatically downloads from official free channels.
7.  **Manual Guidance**: Provides detailed manual download guides for paid articles.

### Download Strategy

The skill adopts a priority strategy for different types of literature:

1.  **First Priority**: Official Free Channels
    *   arXiv (Preprint server)
    *   PubMed Central (PMC, Open access)
    *   Open-access articles on official journal websites
    *   Institutional repositories
2.  **Second Priority**: Query and Indexing
    *   PubMed (Metadata query)
    *   Semantic Scholar (Information retrieval)
    *   CrossRef (DOI resolution)
3.  **When Automatic Download Fails**: Provide manual download guidance
    *   Sci-Hub manual download instructions
    *   Institutional access suggestions
    *   Contact author templates
    *   Document delivery services

### Supported Official Channels

| Channel | Type | Status | Description |
| :--- | :--- | :--- | :--- |
| arXiv | Preprint | ✅ Fully Supported | Free download |
| PubMed Central | Open Access | ✅ Fully Supported | Free download |
| PubMed | Metadata | ✅ Fully Supported | Information query |
| arXiv API | Data Source | ✅ Fully Supported | Paper search |
| Semantic Scholar| Metadata | ✅ Fully Supported | Information retrieval|

## Directory Structure

```
scholar-paper-downloader/
├── SKILL.md                    # Main documentation
├── scripts/
│   ├── __init__.py
│   ├── config.py              # Configuration management
│   ├── paper_search.py        # Paper retrieval
│   ├── pdf_downloader.py      # PDF downloader (official channels only)
│   ├── metadata_extractor.py  # Metadata extraction
│   ├── file_manager.py        # File management
│   ├── index_generator.py     # Index generation
│   ├── batch_downloader.py    # Main batch download program
│   ├── pubmed_downloader.py   # PubMed/PMC downloader
│   ├── doi_query.py           # DOI info query tool
│   └── requirements.txt       # Python dependencies
└── references/
    ├── arxiv_api_guide.md     # arXiv API guide
    ├── best_practices.md      # Best practices
    └── manual_download_guide.md  # Manual download guide
```

## Technical Implementation

### Download Workflow

1.  Input query (Keyword/DOI/ID/URL)
    ↓
2.  Search papers (arXiv + PubMed + Semantic Scholar)
    ↓
3.  Check if automatic download is possible
    ├─ arXiv papers → Direct download
    ├─ PMC open access → Direct download
    └─ Paid journals → Generate manual download guide
    ↓
4.  Extract metadata
    ↓
5.  Save files
    ├─ PDF → Save to specified directory
    └─ Guide → Save download guide
    ↓
6.  Generate index

### Configuration Options

```python
# Key configurations in config.py
MAX_WORKERS = 5              # Concurrent download threads
TIMEOUT = 30                 # Request timeout (seconds)
RETRY_TIMES = 3              # Retry times
OUTPUT_DIR = "./downloads"   # Default output directory
```

## Output Format

### PDF File Naming

```
[FirstAuthor]_[Year]_[JournalAbbreviation].pdf
Example:
Wickramasinghe_2022_CellStemCell.pdf
Schweitzer_2020_NEJM.pdf
```

### Index Files

Generates indexes in two formats:

1.  **Markdown Index** (`index.md`)
```markdown
# Paper Index

## 2022-03-11

1. PPARdelta activation induces metabolic...
   - DOI: 10.1016/j.stem.2022.02.011
   - Journal: Cell Stem Cell
   - Status: Manual download required
   - Guide: PPAR_DELTA_DOWNLOAD.md
```

2.  **JSON Index** (`index.json`)
```json
[
  {
    "title": "...",
    "doi": "10.1016/j.stem.2022.02.011",
    "journal": "Cell Stem Cell",
    "status": "manual",
    "guide": "PPAR_DELTA_DOWNLOAD.md",
    "timestamp": "2026-03-11"
  }
]
```

### Manual Download Guide Template

For papers that cannot be automatically downloaded, a detailed guide is generated:

```markdown
# Paper Download Guide

## Paper Information
- Title: ...
- DOI: ...
- Journal: ...

## Quick Download Methods
1. Visit Sci-Hub: https://sci-hub.tw
2. Enter DOI: ...
3. Click Download

## Alternative Methods
- Institutional access
- Contact the author
- Document delivery
```

## Best Practices

### 1. Batch Downloading Advice

```bash
# Recommended configuration
python scripts/batch_downloader.py \
  -q "your topic" \
  -o ./my_papers \
  -m 20 \
  -w 5
```

Parameter descriptions:
- `-o`: Specify output directory.
- `-m`: Maximum number of papers to download.
- `-w`: Number of concurrent threads (keep small to avoid being blocked).

### 2. Handling Paid Literature

For paid journal papers:
1. Check if there's an open-access version on PMC.
2. If not, generate a detailed manual download guide.
3. Provide various suggestions for obtaining the article.
4. Retain paper metadata for subsequent tracking.

### 3. Index Management

Regularly check index files:
```bash
# View all undownloaded papers
grep "Manual download required" index.md

# Update manual download status
# Edit index.json, change status to "downloaded"
```

## Notes

### ⚠️ Important Reminders

1.  **Copyright Respect**:
    *   Only automatically download from official free channels.
    *   Paid literature only provides download guides, no automatic downloading.
    *   Downloaded papers are for personal academic research only.
2.  **Usage Restrictions**:
    *   Comply with website terms of service.
    *   Do not over-request (limit concurrency).
    *   Respect rate limits.
3.  **Recommended Use**:
    *   ✅ Academic research
    *   ✅ Personal learning
    *   ✅ Literature surveys
    *   ❌ Commercial applications
    *   ❌ Large-scale mass downloading
    *   ❌ Public sharing of paid content

### Manual Download Guide Description

The generated guides include:
1.  **Sci-Hub Manual Download**: Available Sci-Hub mirror links, detailed steps, and common problem solving.
2.  **Legal Acquisition Channels**: Institutional access guides, contact author templates, and document delivery services.
3.  **Alternative Resources**: Open-access checks, links to other databases, and academic forum help.

## Troubleshooting

### FAQ

**Q: Cannot download a certain paper?**
A:
1. Check if it's a paid journal.
2. Check the download guide in `papers/*.md`.
3. Try manually visiting official channels.

**Q: Downloaded PDF cannot be opened?**
A:
1. Check file size (should be >1KB).
2. Re-download.
3. Try other download sources.

**Q: Cannot find relevant papers?**
A:
1. Try different keywords.
2. Use a more precise title.
3. Enter DOI directly.

## Example Workflow

### Example 1: Download arXiv Papers

```bash
# Search and download 5 arXiv papers related to machine learning
python scripts/batch_downloader.py -q "machine learning" -m 5
```

Output:
```
✅ Downloaded: arxiv_2103.00001.pdf
✅ Downloaded: arxiv_2103.00002.pdf
...
📄 Generated: index.md, index.json
```

### Example 2: Query DOI Information

```bash
python scripts/doi_query.py 10.1016/j.stem.2022.02.011
```

Output:
```
Title: PPARdelta activation induces metabolic...
Authors: Nadeera M. Wickramasinghe, ...
Journal: Cell Stem Cell
DOI: 10.1016/j.stem.2022.02.011
```

### Example 3: Handling Paid Literature

```bash
python scripts/batch_downloader.py --doi 10.1056/NEJMoa1915872
```

Output:
```
ℹ️ Paper not available for auto-download
📄 Generated manual download guide: NEJM_DOWNLOAD.md
📄 Added to index with status: manual
```
