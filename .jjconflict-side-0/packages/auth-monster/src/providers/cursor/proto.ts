import { createHash, randomUUID } from 'node:crypto';

// --- Checksum Generation ---

/**
 * Generate checksum for Cursor API requests
 * Based on OpenCursor's implementation
 */
export function generateChecksum(token: string): string {
  const salt = token.split(".");
  
  // XOR-based obfuscation
  const calc = (data: Buffer): void => {
    let t = 165;
    for (let i = 0; i < data.length; i++) {
      data[i] = ((data[i]! ^ t) + i) & 0xff;
      t = data[i]!;
    }
  };
  
  // Timestamp rounded to 30-minute intervals
  const now = new Date();
  now.setMinutes(30 * Math.floor(now.getMinutes() / 30), 0, 0);
  const timestamp = Math.floor(now.getTime() / 1e6);
  
  // Create timestamp buffer
  const timestampBuffer = Buffer.alloc(6);
  let temp = timestamp;
  for (let i = 5; i >= 0; i--) {
    timestampBuffer[i] = temp & 0xff;
    temp = Math.floor(temp / 256);
  }
  calc(timestampBuffer);
  
  // SHA-256 hashes
  const calcHex = (input: string): string => {
    return createHash("sha256").update(input).digest("hex").slice(0, 8);
  };
  
  const hex1 = salt[1] ? calcHex(salt[1]) : "00000000";
  const hex2 = calcHex(token);
  
  return `${timestampBuffer.toString("base64url")}${hex1}/${hex2}`;
}

// --- Connect-RPC / Protobuf Helpers ---

/**
 * Add Connect-RPC envelope (5-byte header)
 * Format: [flags: 1 byte][length: 4 bytes big-endian][payload]
 */
export function addConnectEnvelope(data: Uint8Array, flags: number = 0): Uint8Array {
  const result = new Uint8Array(5 + data.length);
  result[0] = flags;
  result[1] = (data.length >> 24) & 0xff;
  result[2] = (data.length >> 16) & 0xff;
  result[3] = (data.length >> 8) & 0xff;
  result[4] = data.length & 0xff;
  result.set(data, 5);
  return result;
}

/**
 * Encode a varint (variable-length integer)
 */
export function encodeVarint(value: number): Uint8Array {
  const bytes: number[] = [];
  while (value > 127) {
    bytes.push((value & 0x7f) | 0x80);
    value >>>= 7;
  }
  bytes.push(value);
  return new Uint8Array(bytes);
}

/**
 * Encode a string field in protobuf format
 * Field format: (field_number << 3) | wire_type
 * String wire type = 2
 */
export function encodeStringField(fieldNumber: number, value: string): Uint8Array {
  if (!value) return new Uint8Array(0);
  
  const fieldTag = (fieldNumber << 3) | 2; // wire type 2 = length-delimited
  const encoded = new TextEncoder().encode(value);
  const length = encodeVarint(encoded.length);
  
  const result = new Uint8Array(1 + length.length + encoded.length);
  result[0] = fieldTag;
  result.set(length, 1);
  result.set(encoded, 1 + length.length);
  
  return result;
}

/**
 * Encode an int32 field in protobuf format
 * Wire type = 0 (varint)
 */
export function encodeInt32Field(fieldNumber: number, value: number): Uint8Array {
  if (value === 0) return new Uint8Array(0);
  
  const fieldTag = (fieldNumber << 3) | 0; // wire type 0 = varint
  const encoded = encodeVarint(value);
  
  const result = new Uint8Array(1 + encoded.length);
  result[0] = fieldTag;
  result.set(encoded, 1);
  
  return result;
}

/**
 * Encode a nested message field
 */
export function encodeMessageField(fieldNumber: number, data: Uint8Array): Uint8Array {
  if (data.length === 0) return new Uint8Array(0);
  
  const fieldTag = (fieldNumber << 3) | 2; // wire type 2 = length-delimited
  const length = encodeVarint(data.length);
  
  const result = new Uint8Array(1 + length.length + data.length);
  result[0] = fieldTag;
  result.set(length, 1);
  result.set(data, 1 + length.length);
  
  return result;
}

/**
 * Concatenate multiple Uint8Arrays
 */
export function concatBytes(...arrays: Uint8Array[]): Uint8Array {
  const totalLength = arrays.reduce((sum, arr) => sum + arr.length, 0);
  const result = new Uint8Array(totalLength);
  let offset = 0;
  for (const arr of arrays) {
    result.set(arr, offset);
    offset += arr.length;
  }
  return result;
}
