import { TokenExtractor } from '../src/utils/extractor';
import { AuthProvider } from '../src/core/types';
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import assert from 'assert';

// Mock execSync
const child_process = require('child_process');
const originalExecSync = child_process.execSync;

console.log('Testing Scavenger Pipeline...');

// Test 1: Cursor Extraction (Mock Keychain)
child_process.execSync = (cmd: string) => {
  if (cmd.includes('security')) {
    return 'cursor-secret-token-123\n';
  }
  return '';
};

// Mock process.platform
const originalPlatform = process.platform;
Object.defineProperty(process, 'platform', { value: 'darwin' });

(async () => {
  // Use the class method directly, but we need to make sure the import is correct
  // and the class is compiled. The error suggests it might be an issue with how
  // ts-node handles static methods or the import itself.
  // Let's try instantiation if static fails, or check the import.

  const accounts = await TokenExtractor.discoverAll();
  const cursor = accounts.find(a => a.provider === AuthProvider.Cursor);

  assert.ok(cursor, 'Cursor account not discovered');
  assert.strictEqual(cursor?.tokens.accessToken, 'cursor-secret-token-123', 'Cursor token mismatch');
  console.log('✓ Cursor extraction passed');

  // Test 2: Qwen Extraction (Mock File)
  const qwenDir = path.join(os.homedir(), '.qwen');
  const qwenFile = path.join(qwenDir, 'oauth_creds.json');

  if (!fs.existsSync(qwenDir)) fs.mkdirSync(qwenDir, { recursive: true });
  fs.writeFileSync(qwenFile, JSON.stringify({ access_token: 'qwen-secret-token-456' }));

  const accounts2 = await TokenExtractor.discoverAll();
  const qwen = accounts2.find(a => a.provider === AuthProvider.Qwen);

  assert.ok(qwen, 'Qwen account not discovered');
  assert.strictEqual(qwen?.tokens.accessToken, 'qwen-secret-token-456', 'Qwen token mismatch');
  console.log('✓ Qwen extraction passed');

  // Cleanup
  fs.unlinkSync(qwenFile);
  fs.rmdirSync(qwenDir);

  // Restore mocks
  child_process.execSync = originalExecSync;
  Object.defineProperty(process, 'platform', { value: originalPlatform });
})();
