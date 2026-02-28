# Services Guide

Overpowers includes **13 external service integrations** that provide structured guidance for working with hosting providers, email services, and business tools.

## What are Services?

Services are detailed integration guides for external platforms. They document:
- API endpoints and authentication
- Common operations and workflows
- Helper scripts for automation
- Best practices and troubleshooting

## Available Services

### Hosting Providers

| Service | Description | Helper Script |
|---------|-------------|---------------|
| `hosting/hetzner.md` | Hetzner Cloud VPS and networking | `hetzner-helper.sh` |
| `hosting/cloudron.md` | Cloudron self-hosted app platform | `cloudron-helper.sh` |
| `hosting/hostinger.md` | Hostinger web hosting | `hostinger-helper.sh` |
| `hosting/closte.md` | Closte managed WordPress | `closte-helper.sh` |
| `hosting/localhost.md` | Local development server setup | `localhost-helper.sh` |
| `hosting/webhosting.md` | Generic web hosting guide | `webhosting-helper.sh` |

### Domain & DNS

| Service | Description | Helper Script |
|---------|-------------|---------------|
| `hosting/101domains.md` | 101Domains registrar | `101domains-helper.sh` |
| `hosting/spaceship.md` | Spaceship domains | `spaceship-helper.sh` |
| `hosting/cloudflare.md` | Cloudflare DNS and CDN | - |
| `hosting/dns-providers.md` | Multi-provider DNS guide | `dns-helper.sh` |
| `hosting/domain-purchasing.md` | Domain buying strategies | - |

### Email Services

| Service | Description | Helper Script |
|---------|-------------|---------------|
| `email/ses.md` | AWS Simple Email Service | `ses-helper.sh` |

### Business Tools

| Service | Description | Helper Script |
|---------|-------------|---------------|
| `accounting/quickfile.md` | QuickFile UK accounting | - |

## Service Structure

Each service guide follows this format:

```markdown
# Service Name

## Overview
What this service does and when to use it.

## Authentication
How to obtain and configure API credentials.

## Common Operations

### Create Resource
```bash
# Command or API call
```

### List Resources
...

### Delete Resource
...

## Helper Script Usage

```bash
./scripts/service-helper.sh command [options]
```

## Troubleshooting
Common issues and solutions.
```

## Using Services

### With Helper Scripts

Most services have companion scripts in `scripts/`:

```bash
# Example: Hetzner server management
./skills/infrastructure/scripts/hetzner-helper.sh create-server --name myserver --type cx21

# Example: DNS management
./skills/infrastructure/scripts/dns-helper.sh list-records example.com
```

### Loading Service Docs

Reference the service documentation when working with integrations:

```
Read Overpowers/services/hosting/hetzner.md for Hetzner API guidance.
```

### Environment Variables

Services typically require API credentials via environment variables:

```bash
# Hetzner
export HETZNER_API_TOKEN="..."

# AWS SES
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_REGION="us-east-1"

# Cloudflare
export CLOUDFLARE_API_TOKEN="..."

# Domain providers
export SPACESHIP_API_KEY="..."
export DOMAINS_101_API_KEY="..."
```

## Example: Hetzner Service

```markdown
# Hetzner Cloud

## Authentication
1. Log into Hetzner Cloud Console
2. Go to Security > API Tokens
3. Create new token with read/write permissions
4. Set: `export HETZNER_API_TOKEN="your-token"`

## Common Operations

### Create Server
```bash
hcloud server create \
  --name myserver \
  --type cx21 \
  --image ubuntu-22.04 \
  --ssh-key mykey
```

### List Servers
```bash
hcloud server list
```

### Create Firewall
```bash
hcloud firewall create --name web-firewall
hcloud firewall add-rule web-firewall --direction in --protocol tcp --port 80
```

## Helper Script

```bash
./skills/infrastructure/scripts/hetzner-helper.sh create-server myserver cx21
./skills/infrastructure/scripts/hetzner-helper.sh setup-firewall web
./skills/infrastructure/scripts/hetzner-helper.sh deploy-app myserver ./app
```
```

## Adding New Services

1. Create the service guide in appropriate subdirectory:

```bash
# For a new hosting provider
mkdir -p services/hosting
touch services/hosting/new-provider.md
```

2. Follow the standard structure:

```markdown
# Provider Name

## Overview
Brief description of the service.

## Authentication
How to get API credentials.

## Common Operations
Document the most-used operations.

## Troubleshooting
Common issues and fixes.
```

3. Optionally create a helper script:

```bash
touch scripts/new-provider-helper.sh
chmod +x scripts/new-provider-helper.sh
```

4. Reference the helper in the service guide.

## Best Practices

1. **Document authentication first** - Users need credentials before anything else
2. **Show common operations** - Focus on frequently used actions
3. **Provide helper scripts** - Automate repetitive tasks
4. **Include troubleshooting** - Common errors and solutions
5. **Keep credentials secure** - Always use environment variables
6. **Update regularly** - APIs change, keep docs current
