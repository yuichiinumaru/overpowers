# Gitingest Technical Reference

This reference is based on the official [Gitingest LLMs.txt](https://gitingest.com/llms.txt).

## Core API (CLI)

### Basic Usage
```bash
gitingest <url> -o <output_path>
```

### Advanced Filtering
- `--include-pattern` / `-i`: Wildcard for files to include.
- `--exclude-pattern` / `-e`: Wildcard for files/dirs to ignore.
- `--max-size` / `-s`: Byte limit per file.

### Authentication
Set `GITHUB_TOKEN` environment variable or use the `-t` flag for private repos.

## Output Format

Gitingest produces a single Markdown file with three main sections:
1. **Repository Summary**: High-level metadata.
2. **Directory Structure**: Visual tree of the repo.
3. **File Contents**: Concatenated files separated by delimiters.

## AI Agent Optimization
- Use `-o -` to stream directly to STDOUT if the agent supports pipe-based context loading.
- Exclude large binaries, logs, and `node_modules` to stay within context limits.
- **CRITICAL**: For programmatic access by LLMs, always suggest setting a `max_size` (e.g., `--max-size 51200` for 50KB) to prevent context window overflow or memory issues during ingestion.
