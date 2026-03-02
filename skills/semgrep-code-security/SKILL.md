---
name: semgrep-code-security
description: Comprehensive skill for using the Semgrep code security scanner via CLI and MCP tools. Covers directory scanning, custom rules, filtering, and cloud integration.
category: security
color: "#18c37d"
tools:
  read: true
  write: true
  bash: true
---

# Semgrep Code Security Skill

This skill provides agents with the ability to leverage **Semgrep**, a fast, open-source, static analysis tool for finding bugs and enforcing code standards. This skill integrates native Semgrep CLI commands and Semgrep MCP server tools.

## 1. Capabilities

### CLI Usage
The standard way to run Semgrep locally.
- **Basic Scan**: `semgrep scan --config auto .`
- **Targeted Scan**: `semgrep scan --config "p/python" src/`
- **Specific Rules**: `semgrep scan --config "rules/my-rule.yaml" .`
- **Output Formats**: JSON (`--json`), SARIF (`--sarif`), or plain text.

### MCP Tool Integration
If a Semgrep MCP server is available in the environment, you can invoke it using standard tool calls:
- **`semgrep_scan`**: Initiates a scan with specific configurations.
- **`semgrep_analyze`**: Parses and explains Semgrep findings.

### Rule Customization
Agents can write custom Semgrep rules to find specific patterns in the codebase.
- **Pattern Matching**: Use `$X` for variables and `...` for wildcards.
- **Example Rule (`custom-rule.yaml`)**:
  ```yaml
  rules:
    - id: detect-eval
      pattern: eval(...)
      message: "Avoid using eval() as it can lead to code injection vulnerabilities."
      languages:
        - python
        - javascript
      severity: ERROR
  ```
- **Running Custom Rules**: `semgrep scan -f custom-rule.yaml .`

### Cloud Integration (SEMGREP_APP_TOKEN)
To use advanced features, sync with Semgrep App, or use private rules, authentication is required.
- **Environment Variable**: Export `SEMGREP_APP_TOKEN` in your environment.
- **Login**: `semgrep login` (typically automated via the token).
- **CI/CD**: Ensure the token is available as a secret in CI environments.
- **Publishing Rules**: `semgrep publish my-rule.yaml`

## 2. Workflows

### Standard Security Audit
1. Verify Semgrep installation: `semgrep --version`
2. Run an auto-configured scan: `semgrep scan --config auto --json > semgrep-results.json`
3. Analyze the JSON output to identify high-severity issues.
4. If false positives are found, refine the scan using custom rules or `// nosemgrep` comments.

### Vulnerability Remediation
1. Identify a vulnerability (e.g., SQL injection).
2. Write a custom Semgrep rule to detect all instances of this vulnerability.
3. Run the scan to find all occurrences.
4. Remediate the code.
5. Re-run the scan to verify the fixes.

## 3. Best Practices
- **Use `auto` config** for a good baseline of security checks.
- **Filter results** by severity to prioritize critical issues.
- **Integrate into CI/CD** to prevent regressions.
- **Write custom rules** for project-specific conventions and known anti-patterns.
- **Leverage MCP** when available for deeper analysis and context-aware suggestions.
