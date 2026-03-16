---
name: 'v2ray-proxy'
description: 'V2Ray proxy management - automatic proxy switching and system proxy configuration based on network status. Use case: OpenClaw automatically enables proxy when accessing external networks.'
tags: [proxy, v2ray, network, system-config, automation]
version: "1.0.0"
---
# V2Ray Proxy Management

Manages V2Ray proxy automatic switching and configures system proxy based on network status.

## Features

- 🚀 Start/Stop V2Ray
- 🌐 Auto configure/clear system proxy
- 🔄 Auto mode (automatic switching based on network status)
- 📊 Status view and connection test

## Configuration

V2Ray Location: `/media/felix/d/v2rayN-linux-64/`
Proxy Port: `10808`

## Usage

```bash
# Full proxy on
bash <skill>/scripts/v2ray-proxy.sh on

# Full proxy off
bash <skill>/scripts/v2ray-proxy.sh off

# Auto mode (automatic switching based on network status)
bash <skill>/scripts/v2ray-proxy.sh auto

# Check status
bash <skill>/scripts/v2ray-proxy.sh status

# Test proxy
bash <skill>/scripts/v2ray-proxy.sh test
```

## Command Reference

| Command | Description |
|------|------|
| `start` | Start V2Ray only |
| `stop` | Stop V2Ray only |
| `on` | Start + Set system proxy |
| `off` | Clear proxy + Stop |
| `auto` | Auto mode |
| `status` | Check status |
| `test` | Test connection |

## Auto Proxy Workflow

1. When OpenClaw needs to access external network (e.g., search, API calls)
2. Execute `auto` or `on` to enable proxy
3. Execute `off` to disable proxy after access is complete

## Auto-start on Boot

V2Ray can be set to auto-start on boot, but proxy switching is controlled by this script:

```bash
# Add to boot startup (optional)
# Edit /etc/rc.local or use systemd
```
