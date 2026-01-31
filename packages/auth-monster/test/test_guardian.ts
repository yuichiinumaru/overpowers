import * as sanitizer from '../src/utils/sanitizer';
import assert from 'assert';

console.log('Testing Guardian Module...');

// Test 1: Sanitization
const dirtyPayload = {
  model: 'gpt-4',
  messages: [
    {
      role: 'assistant',
      content: 'Hello',
      thoughtSignature: 'bad-signature-123'
    }
  ],
  thoughtSignature: 'bad-top-level-sig'
};

const clean = sanitizer.sanitizeCrossModelRequest(dirtyPayload);
assert.strictEqual(clean.thoughtSignature, undefined, 'Top-level signature not stripped');
assert.strictEqual(clean.messages[0].thoughtSignature, undefined, 'Message-level signature not stripped');
console.log('✓ Sanitization passed');

// Test 2: Header Spoofing
const headers = {
  'Content-Type': 'application/json',
  'User-Agent': 'node-fetch/1.0',
  'x-stainless-lang': 'js'
};

const spoofed = sanitizer.applyHeaderSpoofing(headers, 'acc-123', 'openai');

assert.strictEqual(spoofed['x-stainless-lang'], undefined, 'Leaky header not removed');
assert.ok(spoofed['User-Agent'].includes('Mozilla'), 'User-Agent not spoofed');
assert.strictEqual(spoofed['Openai-Account-Id'], 'acc-123', 'Account ID not injected');
console.log('✓ Header spoofing passed');
