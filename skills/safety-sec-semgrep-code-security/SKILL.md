---
name: semgrep-code-security
description: ''
tags:
- safety
- sec
version: 1.0.0
category: general
---
# Semgrep Code Security

Fast, open-source, static analysis tool for searching code, finding bugs, and enforcing code standards.

## Overview

Semgrep is a lightweight static analysis tool that uses pattern matching to find bugs and security vulnerabilities. This skill covers scanning with curated rulesets, developing custom rules (including taint mode), and integrating with the Semgrep Cloud Platform.

## Installation

### CLI Installation
```bash
# Using pip (recommended)
pip install semgrep

# Using Homebrew (macOS)
brew install semgrep
```

### MCP Tool Configuration
The Semgrep MCP server is typically configured in `opencode.json` using the native `semgrep mcp` command:

```json
"semgrep": {
  "type": "local",
  "enabled": true,
  "command": ["semgrep", "mcp"]
}
```

---

# Part 1: Scanning with Semgrep

## CLI Scanning

### Basic Scans
```bash
semgrep --config auto .                    # Automatically detect relevant rulesets
semgrep --config p/security-audit .        # Run curated security-audit ruleset
semgrep --config p/owasp-top-ten .         # Scan for OWASP Top 10 vulnerabilities
```

### Advanced Scan Options
```bash
semgrep --config auto --sarif -o results.sarif .  # Output results in SARIF format
semgrep --config auto --json -o results.json .    # Output results in JSON format
semgrep --config auto --include="src/**" .        # Limit scan to specific directory
semgrep --config auto --exclude="tests/**" .      # Exclude specific directory
```

## MCP Tool Integration
When enabled, the Semgrep MCP server provides tools to automate scanning and context injection for AI assistants.

| Tool | Purpose |
|------|---------|
| `post-tool-cli-scan` | Runs a Semgrep scan automatically after a tool execution. |
| `stop-cli-scan` | Triggers a scan when a task is completed (stop hook). |
| `record-file-edit` | Records file modifications to focus scans on changed code. |
| `inject-secure-defaults` | Injects security-focused context into agent prompts. |

Agents can invoke these tools to ensure that any code generated or modified meets security standards before completion.

---

# Part 2: Custom Rule Development

## Rule Types

| Type | Use Case |
|------|----------|
| **Pattern Matching** | Simple syntactic patterns (e.g., finding `eval()` or hardcoded secrets). |
| **Taint Mode** | Tracking data flow from untrusted sources to dangerous sinks (e.g., SQLi, XSS). |

## Writing a Simple Pattern Rule
```yaml
rules:
  - id: avoid-eval
    languages: [python, javascript]
    message: "Avoid using eval() as it can lead to code injection."
    severity: WARNING
    pattern: eval(...)
```

## Writing a Taint Mode Rule
```yaml
rules:
  - id: sql-injection
    languages: [python]
    message: "Possible SQL injection detected."
    severity: ERROR
    mode: taint
    pattern-sources:
      - pattern: request.args.get(...)
    pattern-sinks:
      - pattern: cursor.execute(...)
    pattern-sanitizers:
      - pattern: int(...)
```

## Testing Rules
Always use test-driven development for Semgrep rules.

1. Create a test file (e.g., `rule_test.py`) with annotations:
```python
# ruleid: sql-injection
cursor.execute("SELECT * FROM users WHERE id = " + user_input)

# ok: sql-injection
cursor.execute("SELECT * FROM users WHERE id = %s", (user_input,))
```

2. Run the test:
```bash
semgrep --test --config your-rule.yaml rule_test.py
```

---

# Part 3: Cloud Integration & App Token

## Using SEMGREP_APP_TOKEN
To connect to the Semgrep Cloud Platform (for private rules, team collaboration, and managed scans), you must set the `SEMGREP_APP_TOKEN` environment variable.

```bash
export SEMGREP_APP_TOKEN=your_token_here
```

### Benefits of Cloud Integration
- **Private Rulesets:** Access rules shared within your organization.
- **Policies:** Automatically apply rulesets based on project type and environment.
- **Dashboard:** View and manage vulnerabilities across multiple repositories.

### Logging in via CLI
```bash
semgrep login
```
This will guide you through authenticating and automatically setting up your environment.

---

# Part 4: CI/CD Integration

## GitHub Actions Example
```yaml
# name: Semgrep Scan
on: [push, pull_request]
jobs:
  semgrep:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Semgrep CI
        run: semgrep ci
        env:
          SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}
```

## Suppression
To suppress a finding in code, use a comment:
```python
password = "123"  # nosemgrep: hardcoded-password
```

---

# Resources & References

- [Semgrep Registry](https://semgrep.dev/explore) - Browse thousands of curated rules.
- [Semgrep Editor](https://semgrep.dev/playground) - Test patterns and rules in your browser.
- [Official Documentation](https://semgrep.dev/docs) - Comprehensive guides and API references.
- [Rule Writing Guide](https://semgrep.dev/docs/writing-rules/overview) - Deep dive into custom rule creation.
