import { AuthMonster } from '../index';
import { AuthProvider } from '../core/types';
import path from 'path';
import fs from 'fs';

async function test() {
  const testStorage = path.join(__dirname, '../../test-storage');
  if (fs.existsSync(testStorage)) {
    fs.rmSync(testStorage, { recursive: true });
  }

  const monster = new AuthMonster({
    config: {
      active: AuthProvider.Gemini,
      fallback: [],
      method: 'sticky',
      modelPriorities: {},
      fallbackDirection: 'down',
      providers: {}
    },
    storagePath: testStorage
  });

  await monster.init();
  console.log('Initialized AuthMonster');

  const testAccount = {
    id: 'test-gemini',
    email: 'test@example.com',
    provider: AuthProvider.Gemini,
    tokens: { accessToken: 'fake-token' },
    apiKey: 'fake-api-key',
    isHealthy: true
  };

  await monster.addAccount(testAccount);
  console.log('Added test account');

  const auth = await monster.getAuthDetails();
  if (auth && auth.headers['x-goog-api-key'] === 'fake-api-key') {
    console.log('SUCCESS: Gemini auth details retrieved correctly');
  } else {
    console.log('FAILURE: Could not retrieve Gemini auth details', auth);
    process.exit(1);
  }
}

test().catch(err => {
  console.error(err);
  process.exit(1);
});
