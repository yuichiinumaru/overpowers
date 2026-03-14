---
name: ai-llm-gitingest
description: Converts GitHub repositories into a single, AI-friendly Markdown file for deep context ingestion.
---

# Gitingest Skill

This skill enables agents to ingest entire GitHub repositories (public or private) and convert them into a structured Markdown digest. This is ideal for providing an LLM with full codebase context in a single prompt.

## When to Use

- "Ingest the repository [URL]"
- "Convert this repo into a markdown digest"
- "Give me the full context of the [URL] codebase"

## Prerequisites

- Python 3.10+
- `gitingest` package (installed via `pip install gitingest`)
- GitHub Token (optional, for private repositories)

## Instructions

### Step 1: Setup
Ensure dependencies are installed and `GITHUB_TOKEN` is set if accessing private repos.

### Step 2: Execution
Run the `scripts/run.py` with the repository URL and optional filtering patterns.

### Step 3: Verification
Check the generated Markdown file (default: `digest.md`) for the summary, directory tree, and file contents.

## Examples

```bash
python scripts/run.py https://github.com/octocat/Hello-World --output context.md
```

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| Rate limit | Use a `GITHUB_TOKEN` via `-t` or environment variable. |
| File too large | Use `--max-size` or `--include-pattern` to filter files. |
| Private repo error | Check your token permissions and visibility settings. |
