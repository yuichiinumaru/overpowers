import { AuthMonster } from '../index';
import { AuthProvider } from '../core/types';
import path from 'path';
import fs from 'fs';

async function testStability() {
  const testStorage = path.join(__dirname, '../../test-stability-storage');
  if (fs.existsSync(testStorage)) {
    fs.rmSync(testStorage, { recursive: true });
  }

  const monster = new AuthMonster({
    config: {
      active: AuthProvider.Anthropic,
      fallback: [],
      method: 'round-robin',
      modelPriorities: {},
      fallbackDirection: 'down',
      providers: {}
    },
    storagePath: testStorage
  });

  await monster.init();

  const account1 = {
    id: 'acc1',
    email: 'acc1@example.com',
    provider: AuthProvider.Anthropic,
    tokens: { accessToken: 'token1' },
    isHealthy: true,
    healthScore: 100,
    metadata: { model: 'claude-3-5-sonnet-20241022' }
  };

  const account2 = {
    id: 'acc2',
    email: 'acc2@example.com',
    provider: AuthProvider.Anthropic,
    tokens: { accessToken: 'token2' },
    isHealthy: true,
    healthScore: 100,
    metadata: { model: 'claude-3-5-sonnet-20241022' }
  };

  await monster.addAccount(account1);
  await monster.addAccount(account2);

  console.log('--- Testing Rate Limit Deduplication ---');
  // Report rate limit twice quickly
  await monster.reportRateLimit('acc1', 10000, 'RATE_LIMIT_EXCEEDED');
  const status1 = monster.getAllAccountsStatus().find(a => a.id === 'acc1');
  console.log(`First report: score=${status1?.healthScore}, failures=${status1?.consecutiveFailures}`);

  await monster.reportRateLimit('acc1', 10000, 'RATE_LIMIT_EXCEEDED');
  const status2 = monster.getAllAccountsStatus().find(a => a.id === 'acc1');
  console.log(`Second report (immediate): score=${status2?.healthScore}, failures=${status2?.consecutiveFailures}`);

  if (status1?.consecutiveFailures === status2?.consecutiveFailures) {
    console.log('SUCCESS: Rate limit deduplicated!');
  } else {
    console.log('FAILURE: Rate limit NOT deduplicated!');
    process.exit(1);
  }

  console.log('--- Testing Thinking Warmup Trigger ---');
  // We can't easily test the actual fetch without mocking, but we can verify it doesn't crash
  const details1 = await monster.getAuthDetails();
  console.log(`Selected: ${details1?.account.email}`);

  const details2 = await monster.getAuthDetails();
  console.log(`Selected (round-robin): ${details2?.account.email}`);

  console.log('Stability test completed successfully.');
}

testStability().catch(err => {
  console.error(err);
  process.exit(1);
});
