# Scripts Guide

overpowers includes **89 DevOps and automation scripts** that extend your capabilities for infrastructure management, code quality, and service integration.

## Categories

### Code Quality & Linting

| Script | Description |
|--------|-------------|
| `quality-check.sh` | Comprehensive code quality analysis |
| `quality-fix.sh` | Auto-fix common quality issues |
| `quality-cli-manager.sh` | Manage multiple quality tools |
| `quality-feedback-helper.sh` | Process quality tool feedback |
| `linter-manager.sh` | Install and configure linters |
| `setup-linters-wizard.sh` | Interactive linter setup |
| `markdown-formatter.sh` | Format markdown files |
| `markdown-lint-fix.sh` | Fix markdown linting issues |
| `pre-commit-hook.sh` | Run quality checks before commits |

### Code Review Services

| Script | Description |
|--------|-------------|
| `codacy-cli.sh` | Codacy code review integration |
| `codacy-cli-chunked.sh` | Chunked analysis for large repos |
| `coderabbit-cli.sh` | CodeRabbit AI review |
| `coderabbit-pro-analysis.sh` | Advanced CodeRabbit analysis |
| `qlty-cli.sh` | Qlty code quality tool |
| `monitor-code-review.sh` | Monitor review status |
| `sonarcloud-cli.sh` | SonarCloud integration |
| `sonarcloud-autofix.sh` | Auto-fix SonarCloud issues |
| `sonarscanner-cli.sh` | Local SonarScanner |

### Security

| Script | Description |
|--------|-------------|
| `snyk-helper.sh` | Snyk vulnerability scanning |
| `secretlint-helper.sh` | Secret detection and prevention |

### Git & Version Control

| Script | Description |
|--------|-------------|
| `git-platforms-helper.sh` | Multi-platform git operations |
| `github-cli-helper.sh` | GitHub CLI automation |
| `gitlab-cli-helper.sh` | GitLab CLI automation |
| `gitea-cli-helper.sh` | Gitea self-hosted git |
| `auto-version-bump.sh` | Semantic versioning automation |
| `version-manager.sh` | Version consistency management |
| `validate-version-consistency.sh` | Check version across files |

### Hosting & Infrastructure

| Script | Description |
|--------|-------------|
| `hetzner-helper.sh` | Hetzner Cloud management |
| `vercel-cli-helper.sh` | Vercel deployment automation |
| `cloudron-helper.sh` | Cloudron app management |
| `coolify-helper.sh` | Coolify self-hosted PaaS |
| `coolify-cli-helper.sh` | Advanced Coolify operations |
| `hostinger-helper.sh` | Hostinger hosting management |
| `localhost-helper.sh` | Local development server |
| `servers-helper.sh` | Generic server management |
| `webhosting-helper.sh` | Web hosting automation |
| `webhosting-verify.sh` | Verify hosting configuration |

### DNS & Domains

| Script | Description |
|--------|-------------|
| `dns-helper.sh` | DNS management utilities |
| `101domains-helper.sh` | 101Domains management |
| `spaceship-helper.sh` | Spaceship domains |
| `pagespeed-helper.sh` | Google PageSpeed integration |

### Email Services

| Script | Description |
|--------|-------------|
| `ses-helper.sh` | AWS SES email management |

### AI & Automation

| Script | Description |
|--------|-------------|
| `ai-cli-config.sh` | AI tool configuration |
| `setup-ai-system-prompts.sh` | Configure AI system prompts |
| `ampcode-cli.sh` | AMPCode automation |
| `continue-cli.sh` | Continue.dev integration |
| `agno-setup.sh` | Agno AI setup |
| `generate-opencode-agents.sh` | Generate OpenCode agent configs |

### MCP Integrations

| Script | Description |
|--------|-------------|
| `setup-mcp-integrations.sh` | Configure MCP servers |
| `validate-mcp-integrations.sh` | Verify MCP configuration |
| `wordpress-mcp-helper.sh` | WordPress MCP integration |

### Browser Automation

| Script | Description |
|--------|-------------|
| `stagehand-helper.sh` | Stagehand browser automation (TS) |
| `stagehand-python-helper.sh` | Stagehand Python wrapper |
| `stagehand-setup.sh` | Setup Stagehand |
| `stagehand-python-setup.sh` | Setup Python Stagehand |
| `crawl4ai-helper.sh` | Crawl4AI web scraping |
| `crawl4ai-examples.sh` | Crawl4AI usage examples |

### Code Fixes

| Script | Description |
|--------|-------------|
| `fix-common-strings.sh` | Fix common string issues |
| `fix-error-messages.sh` | Standardize error messages |
| `fix-auth-headers.sh` | Fix authentication headers |
| `fix-return-statements.sh` | Fix return statement issues |
| `fix-shellcheck-critical.sh` | Fix critical shellcheck warnings |
| `comprehensive-quality-fix.sh` | Apply all quality fixes |

### Utilities

| Script | Description |
|--------|-------------|
| `system-cleanup.sh` | Clean up system resources |
| `context-builder-helper.sh` | Build context for AI tools |
| `setup-wizard-helper.sh` | Interactive setup wizards |
| `setup-local-api-keys.sh` | Configure API keys locally |
| `shared-constants.sh` | Shared constant definitions |
| `pandoc-helper.sh` | Pandoc document conversion |
| `toon-helper.sh` | Toon.io integration |
| `mainwp-helper.sh` | MainWP WordPress management |
| `vaultwarden-helper.sh` | Vaultwarden password manager |
| `updown-helper.sh` | Updown.io monitoring |
| `dspy-helper.sh` | DSPy framework helper |
| `dspyground-helper.sh` | DSPy playground |

## Using Scripts

### Direct Execution

```bash
# Make executable
chmod +x ~/.config/opencode/overpowers/scripts/quality-check.sh

# Run directly
~/.config/opencode/overpowers/scripts/quality-check.sh
```

### From OpenCode/Claude

```
Run the quality-check.sh script from overpowers/scripts/
```

### Environment Variables

Most scripts use environment variables for configuration. Set them in your shell profile or `.env` file:

```bash
export GITHUB_TOKEN="ghp_..."
export SNYK_TOKEN="..."
export SONAR_TOKEN="..."
```

## Creating New Scripts

1. Create a new `.sh` file in `scripts/`:

```bash
#!/bin/bash
set -euo pipefail

# Script description
# Usage: ./my-script.sh [options]

# Source shared constants if needed
source "$(dirname "$0")/shared-constants.sh"

# Your script logic here
```

2. Make it executable:

```bash
chmod +x scripts/my-script.sh
```

3. Document usage in a header comment.

## Best Practices

1. **Use `set -euo pipefail`** - Fail fast on errors
2. **Add usage documentation** - Comments at the top
3. **Support `--help` flag** - Show usage information
4. **Use environment variables** - For secrets and configuration
5. **Source shared-constants.sh** - For common definitions
6. **Test before committing** - Verify on fresh environment
