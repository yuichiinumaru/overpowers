import { createAuthMonster } from '../index';
import { ConfigManager } from '../core/config';
import { getProviderEndpoint } from '../core/endpoints';
import { AuthProvider } from '../core/types';
import { execSync } from 'child_process';
import * as fs from 'fs';

async function main() {
  const commitMsgFile = process.argv[2];
  const source = process.argv[3];

  if (source === 'message' || source === 'merge' || source === 'squash') {
    process.exit(0);
  }

  let diff = '';
  try {
    diff = execSync('git diff --cached').toString();
  } catch (e) {
    process.exit(0);
  }

  if (!diff.trim()) {
    process.exit(0);
  }

  const configManager = new ConfigManager();
  const config = configManager.loadConfig();
  const monster = createAuthMonster({
    config,
    storagePath: configManager.getConfigDir()
  });

  await monster.init();

  // Prefer a fast model, or fallback to config active
  const model = 'gemini-3-flash-preview';
  const details = await monster.getAuthDetails(model) || await monster.getAuthDetails(config.active);

  if (!details) {
      console.error('AuthMonster: No active account found for commit generation.');
      process.exit(0);
  }

  const url = getProviderEndpoint(details.provider, details.account, details.modelInProvider);

  const prompt = `Generate a concise and descriptive commit message for the following changes.
  Follow the conventional commits specification (e.g. feat: ..., fix: ...).
  Only output the commit message, no explanations.

  Diff:
  ${diff.substring(0, 8000)}`;

  try {
      console.log('AuthMonster: Generating commit message...');
      const response = await monster.request(model, url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: {
              messages: [{ role: 'user', content: prompt }],
              model: details.modelInProvider,
              temperature: 0.3
          }
      });

      const json = await response.json() as any;
      let message = '';

      if (details.provider === AuthProvider.Gemini) {
          message = json.candidates?.[0]?.content?.parts?.[0]?.text || '';
      } else if (details.provider === AuthProvider.Anthropic) {
          message = json.content?.[0]?.text || '';
      } else {
          message = json.choices?.[0]?.message?.content || '';
      }

      if (message) {
          const currentContent = fs.readFileSync(commitMsgFile, 'utf-8');
          fs.writeFileSync(commitMsgFile, `${message.trim()}\n\n${currentContent}`);
      }
  } catch (e) {
      console.error('AuthMonster: Failed to generate commit message.', e);
  }
}

main().catch(() => process.exit(0));
