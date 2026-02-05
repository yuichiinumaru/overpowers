#!/usr/bin/env node
import { Command } from 'commander';
import { createAuthMonster } from './index';
import { ConfigManager } from './core/config';
import { StorageManager } from './core/storage';
import { AuthProvider, ManagedAccount, OAuthTokens } from './core/types';
import { extractQuota, getCooldownStatus } from './core/quota-manager';
import * as fs from 'fs';
import * as path from 'path';
import { execSync } from 'child_process';

import { AnthropicProvider } from './providers/anthropic';
import { GeminiProvider } from './providers/gemini';
import { syncToGitHub } from './utils/github-sync';
import { runOnboardingWizard } from './utils/wizard';
import { startDashboard } from './ui/dashboard';
import { startServer } from './server/index';
import { DialecticsEngine } from './core/dialectics';
import { getProviderEndpoint } from './core/endpoints';

async function main() {

  const configManager = new ConfigManager();
  const config = configManager.loadConfig();
  const storageManager = new StorageManager(configManager.getConfigDir());

  const monster = createAuthMonster({
    config,
    storagePath: configManager.getConfigDir()
  });

  const program = new Command();

  program
    .name('auth-monster')
    .description('Premium CLI tool for managing AI provider authentication and stability.')
    .version('1.0.0');

  program.command('list')
    .description('List all managed accounts and their health status')
    .action(async () => {
      await monster.init();
      const status = monster.getAllAccountsStatus();
      console.table(status);
    });

  program.command('add')
    .description('Add a new provider account')
    .option('-p, --provider <provider>', 'Provider (gemini, anthropic, cursor, etc.)')
    .option('-e, --email <email>', 'Account email')
    .option('-k, --key <key>', 'API Key (if applicable)')
    .action(async (options) => {
      await monster.init();
      // Placeholder for interactive or direct add
      console.log('Adding account...', options);
      // Logic from Phase 2
    });

  program.command('status')
    .description('Show current system status and active provider')
    .action(async () => {
      await monster.init();
      console.log(`Active Provider: ${config.active}`);
      console.log(`Fallback Chain: ${config.fallback.join(' -> ')}`);
    });

  program.command('quota')
    .description('Check quota for an account')
    .argument('<email>', 'Account email')
    .action(async (email) => {
      await monster.init();
      const account = monster.getAccounts().find(a => a.email === email);
      if (account) {
        const status = getCooldownStatus(account.provider, account.id);
        console.log(`Quota Status for ${email}:`, status);
      } else {
        console.log('Account not found.');
      }
    });

  program.command('sync')
    .description('Sync accounts to GitHub Secrets')
    .action(async () => {
      await monster.init();
      // TODO: Implement repo selection or get from config
      console.log('Sync requires a target repository. Use: auth-monster sync <owner/repo>');
      // await syncToGitHub('owner/repo', monster.getAccounts());
      console.log('Sync placeholder.');
    });

  program.command('onboard')
    .description('Run the onboarding wizard to configure everything')
    .action(async () => {
      await monster.init();
      await runOnboardingWizard(monster);
    });

  program.command('proxy')
    .description('Start a local LLM proxy server')
    .option('-p, --port <number>', 'Port to listen on', '8080')
    .action(async (options) => {
      console.log(`Starting proxy on port ${options.port}...`);
      // Phase 4 Proxy logic
    });

  program.command('fallback')
    .description('Configure fallback strategy')
    .action(async () => {
      console.log('Configuring fallback...');
    });

  program.command('dashboard')
    .description('Launch the TUI Dashboard')
    .action(async () => {
      await monster.init();
      startDashboard(monster);
    });

  program.command('server')
    .description('Start the Web Admin Server')
    .option('-p, --port <number>', 'Port to listen on', '3000')
    .action(async (options) => {
      await monster.init();
      startServer(monster, parseInt(options.port));
    });

  program.command('dialectics')
    .description('Run a dialectics session: split prompt between two models and synthesize.')
    .argument('<prompt>', 'The prompt to process')
    .option('-a, --model-a <model>', 'First model', 'gemini-3-flash-preview')
    .option('-b, --model-b <model>', 'Second model', 'claude-3-7-sonnet-20250219')
    .option('-s, --synthesizer <model>', 'Synthesizer model', 'gemini-3-pro-preview')
    .action(async (prompt, options) => {
      await monster.init();
      const engine = new DialecticsEngine(monster);
      try {
        const result = await engine.synthesize(prompt, options.modelA, options.modelB, options.synthesizer);
        console.log('\n=== Synthesis Result ===\n');
        console.log(result);
      } catch (error) {
        console.error('Dialectics failed:', error);
        process.exit(1);
      }
    });

  program.command('install-hook')
    .description('Install the prepare-commit-msg git hook')
    .action(() => {
      const gitDir = path.resolve(process.cwd(), '.git');
      if (!fs.existsSync(gitDir)) {
        console.error('Error: .git directory not found. Are you in a git repository?');
        process.exit(1);
      }

      const hooksDir = path.join(gitDir, 'hooks');
      if (!fs.existsSync(hooksDir)) {
        fs.mkdirSync(hooksDir, { recursive: true });
      }

      const hookPath = path.join(hooksDir, 'prepare-commit-msg');

      // Determine path to the script
      const isTs = __filename.endsWith('.ts');
      let scriptPath;
      let runner;

      if (isTs) {
        scriptPath = path.resolve(__dirname, 'scripts/git-hook.ts');
        runner = 'npx ts-node';
      } else {
        scriptPath = path.resolve(__dirname, 'scripts/git-hook.js');
        runner = 'node';
      }

      const hookContent = `#!/bin/sh
# OpenCode Auth Monster Hook
${runner} "${scriptPath}" "$@"
`;

      fs.writeFileSync(hookPath, hookContent, { mode: 0o755 });
      console.log(`Hook installed at ${hookPath}`);
    });

  program.command('review')
    .description('Perform a code review on a file or git diff')
    .argument('[file]', 'File to review (if omitted, reviews staged git diff)')
    .option('-m, --model <model>', 'Model to use', 'claude-4.5-opus-thinking')
    .action(async (file, options) => {
      await monster.init();

      let content = '';
      if (file) {
        try {
          content = fs.readFileSync(file, 'utf-8');
        } catch (e) {
          console.error(`Could not read file: ${file}`);
          process.exit(1);
        }
      } else {
        try {
          content = execSync('git diff --cached').toString();
          if (!content.trim()) {
            console.log('No staged changes to review.');
            return;
          }
        } catch (e) {
          console.error('Error getting git diff. Are you in a git repo?');
          process.exit(1);
        }
      }

      const prompt = `Please review the following code changes.
          Focus on:
          1. Bugs and potential runtime errors.
          2. Security vulnerabilities.
          3. Code style and best practices.
          4. Performance improvements.

          Code/Diff:
          ${content.substring(0, 10000)}
          `;

      const details = await monster.getAuthDetails(options.model);
      if (!details) {
        console.error(`Could not resolve model: ${options.model}`);
        process.exit(1);
      }

      const url = getProviderEndpoint(details.provider, details.account, details.modelInProvider);

      console.log(`Reviewing with ${options.model}...`);
      try {
        const response = await monster.request(options.model, url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: {
            messages: [{ role: 'user', content: prompt }],
            model: details.modelInProvider,
            temperature: 0.2
          }
        });

        const json = await response.json() as any;
        let review = '';

        if (details.provider === AuthProvider.Gemini) {
          review = json.candidates?.[0]?.content?.parts?.[0]?.text;
        } else if (details.provider === AuthProvider.Anthropic) {
          review = json.content?.[0]?.text;
        } else {
          review = json.choices?.[0]?.message?.content;
        }

        console.log('\n=== Code Review ===\n');
        console.log(review || 'No review generated or error parsing response.');

      } catch (error) {
        console.error('Review failed:', error);
      }
    });

  await program.parseAsync(process.argv);

}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
