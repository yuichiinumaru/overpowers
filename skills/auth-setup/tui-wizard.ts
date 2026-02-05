#!/usr/bin/env npx ts-node
/**
 * Auth Setup TUI Wizard
 * 
 * Interactive terminal interface for configuring multi-provider authentication.
 * Uses Blessed for TUI and integrates with auth-monster's core engine.
 */

import * as blessed from 'blessed';
import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';
import { execSync, spawn } from 'child_process';

// ============================================================================
// TYPES
// ============================================================================

interface DiscoveredAccount {
    provider: string;
    email: string;
    source: string;
    token?: string;
    healthy: boolean;
}

interface AuthConfig {
    accounts: DiscoveredAccount[];
    primaryModel: string;
    fallbackChain: string[];
    bulkModel: string;
}

// ============================================================================
// AUTO-DISCOVERY (Adapted from auth-monster/extractor.ts)
// ============================================================================

async function autoDiscover(): Promise<DiscoveredAccount[]> {
    const accounts: DiscoveredAccount[] = [];

    // 1. Qwen (File)
    const qwenPath = path.join(os.homedir(), '.qwen', 'oauth_creds.json');
    if (fs.existsSync(qwenPath)) {
        try {
            const data = JSON.parse(fs.readFileSync(qwenPath, 'utf8'));
            if (data.access_token) {
                accounts.push({
                    provider: 'qwen',
                    email: 'qwen-local@device',
                    source: 'file (~/.qwen/oauth_creds.json)',
                    token: data.access_token,
                    healthy: true
                });
            }
        } catch { }
    }

    // 2. Cursor (SQLite on Linux)
    const cursorDbPath = path.join(os.homedir(), '.config', 'Cursor', 'User', 'globalStorage', 'state.vscdb');
    if (fs.existsSync(cursorDbPath)) {
        try {
            const result = execSync(
                `sqlite3 "${cursorDbPath}" "SELECT value FROM ItemTable WHERE key = 'cursorAuth/accessToken';"`,
                { encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] }
            ).trim();
            if (result) {
                accounts.push({
                    provider: 'cursor',
                    email: 'cursor-local@device',
                    source: 'sqlite (Cursor)',
                    token: result,
                    healthy: true
                });
            }
        } catch { }
    }

    // 3. Windsurf (SQLite)
    const windsurfDbPath = path.join(os.homedir(), '.config', 'Windsurf', 'User', 'globalStorage', 'state.vscdb');
    if (fs.existsSync(windsurfDbPath)) {
        try {
            const result = execSync(
                `sqlite3 "${windsurfDbPath}" "SELECT value FROM ItemTable WHERE key = 'windsurfAuthStatus';"`,
                { encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] }
            ).trim();
            if (result) {
                const json = JSON.parse(result);
                if (json.accessToken) {
                    accounts.push({
                        provider: 'windsurf',
                        email: json.email || 'windsurf-local@device',
                        source: 'sqlite (Windsurf)',
                        token: json.accessToken,
                        healthy: true
                    });
                }
            }
        } catch { }
    }

    // 4. AWS SSO (Kiro)
    const ssoCachePath = path.join(os.homedir(), '.aws', 'sso', 'cache');
    if (fs.existsSync(ssoCachePath)) {
        try {
            const files = fs.readdirSync(ssoCachePath);
            for (const file of files) {
                if (!file.endsWith('.json')) continue;
                const content = JSON.parse(fs.readFileSync(path.join(ssoCachePath, file), 'utf8'));
                if (content.accessToken && content.expiresAt) {
                    const expiresAt = new Date(content.expiresAt).getTime();
                    if (expiresAt > Date.now()) {
                        accounts.push({
                            provider: 'kiro',
                            email: content.email || 'kiro-local@aws',
                            source: 'aws-sso',
                            token: content.accessToken,
                            healthy: true
                        });
                        break;
                    }
                }
            }
        } catch { }
    }

    // 5. Antigravity accounts (already configured)
    const antigravityPath = path.join(os.homedir(), '.config', 'opencode', 'antigravity-accounts.json');
    if (fs.existsSync(antigravityPath)) {
        try {
            const data = JSON.parse(fs.readFileSync(antigravityPath, 'utf8'));
            if (data.accounts && Array.isArray(data.accounts)) {
                for (const acc of data.accounts) {
                    accounts.push({
                        provider: 'gemini-antigravity',
                        email: acc.email,
                        source: 'antigravity-accounts.json',
                        token: acc.refreshToken ? '***' : undefined,
                        healthy: true
                    });
                }
            }
        } catch { }
    }

    return accounts;
}

// ============================================================================
// TUI COMPONENTS
// ============================================================================

function createScreen(): blessed.Widgets.Screen {
    return blessed.screen({
        smartCSR: true,
        title: '👹 Auth Monster Setup Wizard',
        cursor: { artificial: true, shape: 'underline', blink: true, color: 'cyan' }
    });
}

function createHeader(screen: blessed.Widgets.Screen): blessed.Widgets.BoxElement {
    return blessed.box({
        parent: screen,
        top: 0,
        left: 0,
        width: '100%',
        height: 3,
        content: '{center}{bold}👹 Auth Monster Setup Wizard{/bold}{/center}',
        tags: true,
        style: { fg: 'white', bg: 'blue' }
    });
}

function createMainBox(screen: blessed.Widgets.Screen): blessed.Widgets.BoxElement {
    return blessed.box({
        parent: screen,
        top: 3,
        left: 0,
        width: '100%',
        height: '100%-6',
        border: { type: 'line' },
        style: { border: { fg: 'cyan' } },
        scrollable: true,
        keys: true,
        vi: true
    });
}

function createFooter(screen: blessed.Widgets.Screen): blessed.Widgets.BoxElement {
    return blessed.box({
        parent: screen,
        bottom: 0,
        left: 0,
        width: '100%',
        height: 3,
        content: '{center}Press {bold}q{/bold} to quit | {bold}Enter{/bold} to select | {bold}↑↓{/bold} to navigate{/center}',
        tags: true,
        style: { fg: 'gray', bg: 'black' }
    });
}

// ============================================================================
// WIZARD STEPS
// ============================================================================

async function runWizard() {
    const screen = createScreen();
    createHeader(screen);
    const mainBox = createMainBox(screen);
    createFooter(screen);

    // Bind quit key
    screen.key(['q', 'C-c'], () => {
        screen.destroy();
        process.exit(0);
    });

    // Step 1: Welcome
    mainBox.setContent(`
{bold}Welcome to Auth Monster!{/bold}

This wizard will help you configure multi-provider authentication for:
  • Gemini (Google)
  • Claude (Anthropic)
  • GPT (OpenAI)
  • Cursor, Windsurf, Qwen, Kiro...

{yellow-fg}Press Enter to continue...{/yellow-fg}
  `);
    screen.render();

    await waitForKey(screen, 'enter');

    // Step 2: Auto-Discovery
    mainBox.setContent(`
{bold}Step 1: Auto-Discovery{/bold}

Scanning your system for existing tokens...
  `);
    screen.render();

    const discovered = await autoDiscover();

    let discoveryReport = `
{bold}Step 1: Auto-Discovery{/bold}

Found {green-fg}${discovered.length}{/green-fg} existing accounts:

`;

    for (const acc of discovered) {
        discoveryReport += `  {cyan-fg}${acc.provider}{/cyan-fg} - ${acc.email} (${acc.source})\n`;
    }

    discoveryReport += `
{yellow-fg}Press Enter to continue to provider setup...{/yellow-fg}
  `;

    mainBox.setContent(discoveryReport);
    screen.render();

    await waitForKey(screen, 'enter');

    // Step 3: Quota Strategy
    mainBox.setContent(`
{bold}Step 2: Quota Strategy{/bold}

Default configuration (recommended for power users):

{bold}Primary Model (Orchestration/Review):{/bold}
  → Claude 4.5 Opus (Thinking)

{bold}Fallback Chain:{/bold}
  1. GPT-5.2 Codex
  2. Claude 4.5 Sonnet
  3. Gemini 3 Pro (Preview)

{bold}Bulk Work Model:{/bold}
  → Gemini 3 Flash

{yellow-fg}Press Enter to save this configuration...{/yellow-fg}
  `);
    screen.render();

    await waitForKey(screen, 'enter');

    // Step 4: Save
    const config: AuthConfig = {
        accounts: discovered,
        primaryModel: 'claude-4.5-opus-thinking',
        fallbackChain: ['gpt-5.2-codex', 'claude-4.5-sonnet', 'gemini-3-pro-preview'],
        bulkModel: 'gemini-3-flash-preview'
    };

    const configPath = path.join(os.homedir(), '.config', 'opencode', 'auth-monster-config.json');
    fs.writeFileSync(configPath, JSON.stringify(config, null, 2));

    mainBox.setContent(`
{bold}Setup Complete!{/bold}

{green-fg}✓{/green-fg} Configuration saved to:
  ${configPath}

{green-fg}✓{/green-fg} Discovered ${discovered.length} accounts

{bold}Next Steps:{/bold}
  • Run {cyan-fg}opencode{/cyan-fg} to start using the unified auth
  • Use {cyan-fg}/skill jules-dispatch{/cyan-fg} for parallel task execution
  • Quota will be managed automatically based on your strategy

{yellow-fg}Press q to exit...{/yellow-fg}
  `);
    screen.render();

    await waitForKey(screen, 'q');
    screen.destroy();
    process.exit(0);
}

function waitForKey(screen: blessed.Widgets.Screen, key: string): Promise<void> {
    return new Promise(resolve => {
        const handler = () => {
            screen.unkey([key], handler);
            resolve();
        };
        screen.key([key], handler);
    });
}

// ============================================================================
// MAIN
// ============================================================================

runWizard().catch(err => {
    console.error('Wizard error:', err);
    process.exit(1);
});
