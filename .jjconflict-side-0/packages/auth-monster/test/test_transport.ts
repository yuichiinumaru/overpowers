import { ProtoWriter, createConnectFrame } from '../src/core/transport';
import assert from 'assert';

console.log('Testing Transport Layer...');

// Test 1: ProtoWriter Varint
const writer = new ProtoWriter();
writer.writeVarint(150); // 150 = 10010110 -> [10010110 (0x96), 00000001 (0x01)]
const buf = writer.toBuffer();
assert.strictEqual(buf.toString('hex'), '9601', 'Varint encoding failed');
console.log('✓ Varint encoding passed');

// Test 2: String Field
const strWriter = new ProtoWriter();
strWriter.writeString(1, "testing");
// Field 1 (1 << 3 | 2) = 0x0A
// Length 7 = 0x07
// "testing" hex = 74657374696e67
const strBuf = strWriter.toBuffer();
assert.strictEqual(strBuf.toString('hex'), '0a0774657374696e67', 'String field encoding failed');
console.log('✓ String field encoding passed');

// Test 3: Connect Frame
const payload = Buffer.from('hello');
const frame = createConnectFrame(payload);
// Header: 00 (flag) + 00000005 (len) + payload
assert.strictEqual(frame.length, 10);
assert.strictEqual(frame[0], 0);
assert.strictEqual(frame.readUInt32BE(1), 5);
console.log('✓ Connect frame encoding passed');
