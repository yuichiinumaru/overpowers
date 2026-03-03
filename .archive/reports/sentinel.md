## 2026-02-23 - Hardcoded Secrets in Backup Files
**Vulnerability:** A backup environment file (`.env.bak`) containing live API keys was committed to the repository because `.gitignore` only excluded `.env`. Additionally, documentation dump files contained hardcoded secrets.
**Learning:** Standard `.gitignore` patterns like `.env` are insufficient if developers create backup files with different extensions (e.g., `.env.bak`, `.env.old`) that contain the same sensitive data.
**Prevention:** Explicitly ignore backup patterns for sensitive files (e.g., `.env*`, `*.bak`) in `.gitignore`. Regularly scan the codebase for high-entropy strings and known secret patterns, including in `docs/` and backup files.
