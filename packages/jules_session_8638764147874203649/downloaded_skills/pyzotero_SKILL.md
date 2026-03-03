---
name: pyzotero-cli
version: 1.0.0
description: Command-line interface for Zotero - search your local Zotero library, list collections, and manage items from the terminal.
homepage: https://github.com/urschrei/pyzotero
metadata:
  {
    "openclaw":
      {
        "emoji": "📚",
        "requires": { "anyBins": ["pyzotero"], "bins": ["python3"] },
        "install":
          [
            {
              "id": "pipx_cli",
              "kind": "pipx",
              "package": "pyzotero[cli]",
              "label": "Install pyzotero CLI (pipx - recommended for PEP 668-compliant systems)",
              "platforms": ["linux-debian", "linux-ubuntu", "linux-arch", "linux-fedora", "linux-rhel"],
            },
            {
              "id": "pip_cli",
              "kind": "pip",
              "package": "pyzotero[cli]",
              "label": "Install pyzotero CLI (pip)",
            },
          ],
      },
  }
---

# Pyzotero CLI

Command-line interface for Zotero - search your local Zotero library, list collections, and manage items from the terminal.

## Quick Start

```bash
# Install (PEP 668 systems)
pipx install "pyzotero[cli]"

# Enable local API in Zotero 7
# Settings > Advanced > "Allow other applications on this computer to communicate with Zotero"

# List collections
pyzotero listcollections

# Search library
pyzotero search -q "machine learning"

# Full-text search (includes PDFs)
pyzotero search -q "attention mechanisms" --fulltext
```

📖 **Detailed guide:** [QUICKSTART.md](QUICKSTART.md)

## Installation

### pipx (Recommended for PEP 668 systems)
```bash
pipx install "pyzotero[cli]"
```

### pip (Generic)
```bash
pip install --user "pyzotero[cli]"
export PATH="$HOME/.local/bin:$PATH"
```

📖 **Complete installation guide:** [INSTALL.md](INSTALL.md)

## Prerequisites

### Enable Local Zotero Access

**Required for CLI usage:**

1. Open Zotero 7 (or newer)
2. Go to **Edit > Preferences > Advanced**
3. Check **"Allow other applications on this computer to communicate with Zotero"**
4. Restart Zotero

## Core Commands

| Command | Description |
|---------|-------------|
| `pyzotero search -q "topic"` | Search library |
| `pyzotero search --fulltext` | Search with full-text (PDFs) |
| `pyzotero search --collection ID` | Search in specific collection |
| `pyzotero listcollections` | List all collections |
| `pyzotero itemtypes` | List item types |

## Search Examples

### Basic Search
```bash
# Search titles and metadata
pyzotero search -q "machine learning"

# Phrase search
pyzotero search -q "\"deep learning\""
```

### Full-Text Search
```bash
# Search in PDFs and attachments
pyzotero search -q "neural networks" --fulltext
```

### Advanced Filtering
```bash
# Filter by item type
pyzotero search -q "methodology" --itemtype book --itemtype journalArticle

# Search within collection
pyzotero search --collection ABC123 -q "test"
```

## Output Formats

### Human-Readable
```bash
pyzotero search -q "python"
```

### JSON Output
```bash
pyzotero search -q "topic" --json

# Process with jq
pyzotero search -q "topic" --json | jq '.[] | .title'
```

## Documentation

| Document | Description |
|----------|-------------|
| [QUICKSTART.md](QUICKSTART.md) | 5-minute quick start guide |
| [INSTALL.md](INSTALL.md) | Comprehensive installation guide |
| [EXAMPLES.md](EXAMPLES.md) | Practical usage examples |
| [README.md](README.md) | Project overview |

## Troubleshooting

**Connection error (local Zotero):**
```
Make sure Zotero is running
Enable local API: Settings > Advanced > "Allow other applications on this computer to communicate with Zotero"
Restart Zotero
```

**Command not found:**
```bash
export PATH="$HOME/.local/bin:$PATH"
pipx ensurepath
```

**Permission denied (PEP 668 systems):**
```bash
pipx install "pyzotero[cli]"
```

📖 **Detailed troubleshooting:** [INSTALL.md](INSTALL.md)

## Quick Reference

```bash
# Search
pyzotero search -q "topic"
pyzotero search -q "topic" --fulltext
pyzotero search -q "topic" --json

# List
pyzotero listcollections
pyzotero itemtypes

# Filter
pyzotero search -q "topic" --itemtype journalArticle
pyzotero search --collection ABC123 -q "topic"
```

---

**For complete documentation:**
- [QUICKSTART.md](QUICKSTART.md) - Get started
- [INSTALL.md](INSTALL.md) - Installation details
- [EXAMPLES.md](EXAMPLES.md) - Usage examples
- [README.md](README.md) - Full overview
