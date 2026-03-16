---
name: social-zhihu-pyzhihu-cli
description: CLI tool for browsing and interacting with Zhihu content. Supports search, hot lists, questions, answers, user profiles, and content publishing.
tags: [zhihu, cli, social, python]
version: 1.0.0
---

# Zhihu-CLI Skill

## What is zhihu-cli

zhihu-cli (PyPI package name `pyzhihu-cli`) is a Python command-line tool for browsing Zhihu content in the terminal. It supports 23 subcommands including search, hot lists, questions, answers, users, voting, following, posting questions, posting ideas, and posting articles.

- **PyPI Package Name**: `pyzhihu-cli`
- **CLI Command Name**: `zhihu`
- **Python Requirement**: >= 3.10

---

## Installation

### User Installation (from PyPI)

```bash
# Recommended: using uv (global CLI tool)
uv tool install pyzhihu-cli

# Or using pipx
pipx install pyzhihu-cli

# Or using pip
pip install pyzhihu-cli
```

### Development Installation (from source)

```bash
# Clone the repository
git clone https://github.com/BAIGUANGMEI/zhihu-cli.git
cd zhihu-cli

# Create a virtual environment and install
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -e .
```

QR code login is handled via the Zhihu API (`POST /api/v3/account/api/login/qrcode`) to obtain a token and link. The terminal uses the `qrcode` library to render the QR code and polls `scan_info` until confirmation, **without requiring Playwright**.

---

## Usage

### 1. Login (Required for first use)

```bash
# Method 1: QR code login (Recommended, requires requests + qrcode, no Playwright needed)
zhihu login --qrcode

# Method 2: Manually provide Cookie string (must include z_c0)
zhihu login --cookie "z_c0=xxx; _xsrf=yyy; d_c0=zzz"
```

Cookie retrieval: Log in to Zhihu in a browser → F12 → Network → Any request → Headers → Cookie, and copy the full value.


## ***Note for data retrieval commands: Using --json is recommended for raw JSON output to get more detailed information.***

... (rest of content)
