---
name: office-docs
description: Extract text and tables from .docx and .xlsx using local scripts (no external deps).
allowed-tools: Bash(python:*)
---

# Office Docs (docx + xlsx)

This skill provides lightweight, dependency-free extraction for Office documents using the scripts in `tools/`.

## DOCX

Extract paragraphs and tables from a `.docx` file:

```bash
python tools/docx_extract.py "/path/to/file.docx" --output "/path/to/output.txt"
```

## XLSX

Extract sheet data from a `.xlsx` file:

```bash
python tools/xlsx_extract.py "/path/to/file.xlsx" --output "/path/to/output.txt" --format csv
```

### Notes

- If `--output` points to a directory, each sheet is written to its own file.
- If `--output` is a file and there are multiple sheets, the script prefixes each sheet with `# Sheet: <name>`.
