---
name: auth-setup
description: Interactive TUI wizard for configuring multi-provider authentication. Auto-discovers existing tokens, sets up OAuth flows, and configures quota management for optimal model rotation.
category: setup
---

# Auth Setup Wizard

This skill provides an interactive Terminal User Interface (TUI) for setting up multi-provider authentication across Gemini, Anthropic, OpenAI, Cursor, Windsurf, and more.

## Usage

```bash
# Run the TUI wizard
cd ~/.config/opencode/overpowers
npx ts-node skills/auth-setup/tui-wizard.ts
```

## Features

1. **Auto-Discovery** – Scans for existing tokens:
   - Cursor (macOS Keychain / SQLite)
   - Windsurf (SQLite)
   - Qwen (`~/.qwen/oauth_creds.json`)
   - Kiro (AWS SSO Cache)
   - Claude Code (macOS Keychain)

2. **OAuth Flows** – Interactive login for:
   - Google (Gemini API)
   - Anthropic (Console)

3. **API Key Entry** – Manual entry for:
   - OpenAI
   - Any generic provider

4. **Quota Strategy Configuration** – Set priorities:
   - Primary model (e.g., Claude 4.5 Opus)
   - Fallback chain
   - Bulk work model (e.g., Gemini 3 Flash)

5. **Account Verification** – Tests each account before saving

## Output

Saves to `~/.config/opencode/auth-monster-accounts.json` with:
- Encrypted tokens via SecretStorage
- Rate limit tracking per model
- Health scores for rotation

## Integration

After setup, the auth engine is automatically available to:
- OpenCode sessions
- Jules Swarm tasks
- Overpowers personas
