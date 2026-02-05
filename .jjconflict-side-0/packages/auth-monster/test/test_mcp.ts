import { MCPBridge } from '../src/core/mcp-bridge';
import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';
import assert from 'assert';
import { EventEmitter } from 'events';

// Mock child_process
const child_process = require('child_process');
const originalSpawn = child_process.spawn;

console.log('Testing MCP Integration...');

// Mock Spawn
const mockChild = new EventEmitter() as any;
mockChild.stdin = { write: (data: string) => {} };
mockChild.stdout = new EventEmitter();
mockChild.stderr = new EventEmitter();
mockChild.kill = () => {};

child_process.spawn = () => {
  // Simulate MCP Server Response behavior
  setTimeout(() => {
    // Send success response to 'initialize'
    const response = JSON.stringify({
      jsonrpc: '2.0',
      id: 1,
      result: { protocolVersion: '2024-11-05', capabilities: {} }
    });
    mockChild.stdout.emit('data', Buffer.from(response));
  }, 100);

  return mockChild;
};

(async () => {
  const bridge = new MCPBridge();

  // 1. Start Bridge
  bridge.start();

  // 2. Test Handshake
  try {
    await bridge.initialize();
    console.log('✓ MCP Handshake passed');
  } catch (e) {
    console.error('MCP Handshake failed:', e);
    process.exit(1);
  }

  // 3. Test Token Reading
  const mockTokenPath = path.join(os.tmpdir(), '.auth-mcp-token-test.json');
  fs.writeFileSync(mockTokenPath, JSON.stringify({ token: 'mcp-test-token-789' }));

  // Hackily inject the path since it's private/protected in class but we passed it in constructor in real usage
  // Re-instantiate with explicit path
  const bridge2 = new MCPBridge(mockTokenPath);
  const token = bridge2.getToken();

  assert.strictEqual(token, 'mcp-test-token-789', 'Token reading failed');
  console.log('✓ MCP Token reading passed');

  // Cleanup
  fs.unlinkSync(mockTokenPath);
  child_process.spawn = originalSpawn;
})();
