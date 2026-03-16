# ai-llm-gitingest

A skill for the Overpowers toolkit that integrates `gitingest` to allow seamless repository context ingestion for AI agents.

## Features

- **GitHub to Markdown**: Convert any repo into a structured digest.
- **Pattern Filtering**: Include/exclude specific files using Unix shell-style wildcards.
- **Size Control**: Limit maximum file sizes to avoid context window overflow.
- **Private Repo Support**: Uses GitHub tokens for authenticated access.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Agents can trigger this skill whenever they need to analyze a repository that isn't currently in their active workspace.

```bash
python scripts/run.py <repo_url> [options]
```

## Credits

Based on [GitIngest](https://gitingest.com).
