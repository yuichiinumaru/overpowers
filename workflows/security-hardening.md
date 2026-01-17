# Security Hardening Workflow

Systematic security review and hardening using our **security-focused agents and scripts**.

## When to Use

- Before production deployment
- After major code changes
- Periodic security audits
- Before open-sourcing code

## Security Agent Team

| Agent | Focus |
|-------|-------|
| `security-auditor` | General security review |
| `api-security-audit` | API-specific vulnerabilities |
| `mcp-security-auditor` | MCP server security |
| `incident-responder` | Attack response planning |

## Workflow Steps

### 1. Automated Scanning

Run security scripts from `Overpowers/scripts/`:

```bash
# Snyk dependency scan
./scripts/snyk-helper.sh

# SonarCloud code analysis
./scripts/sonarcloud-cli.sh analyze

# Secret detection
./scripts/secretlint-helper.sh
```

### 2. Dependencies Audit

```
/invoke security-auditor

Focus: Dependency vulnerabilities
- Outdated packages
- Known CVEs
- Unused dependencies
- License compliance
```

### 3. Code Security Review

```
/invoke security-auditor

Check for:
- [ ] Input validation
- [ ] Output encoding
- [ ] Authentication/Authorization
- [ ] Injection vulnerabilities (SQL, XSS, Command)
- [ ] Sensitive data handling
- [ ] Error information leakage
```

### 4. API Security (if applicable)

```
/invoke api-security-audit

Review:
- [ ] Authentication mechanism
- [ ] Rate limiting
- [ ] Input validation on all endpoints
- [ ] Proper HTTP methods
- [ ] CORS configuration
- [ ] API versioning
```

### 5. Infrastructure Review

```
/invoke devops-troubleshooter

Check:
- [ ] Secrets management
- [ ] Environment configuration
- [ ] Network exposure
- [ ] Container security
- [ ] Access controls
```

### 6. Remediation Plan

```
/invoke incident-responder

Create:
- Vulnerability priority list
- Remediation steps per issue
- Timeline for fixes
- Verification plan
```

## Security Checklist

### Authentication
- [ ] Passwords hashed with bcrypt/argon2
- [ ] Session tokens are secure
- [ ] Multi-factor available (if applicable)
- [ ] Brute force protection

### Authorization
- [ ] Principle of least privilege
- [ ] Role-based access control
- [ ] Resource ownership verified

### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] TLS for data in transit
- [ ] PII handling compliant
- [ ] Backups encrypted

## Related Scripts

| Script | Purpose |
|--------|---------|
| `snyk-helper.sh` | Vulnerability scanning |
| `sonarcloud-cli.sh` | Code quality & security |
| `secretlint-helper.sh` | Secret detection |
| `codacy-cli.sh` | Automated review |

## Related Skills

- `github-workflow-automation` - CI/CD security gates
- `verification-quality` - Quality verification
