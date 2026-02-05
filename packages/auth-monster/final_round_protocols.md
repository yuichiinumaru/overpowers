# FINAL ROUND PROTOCOLS: AUTH FEDERATION & RPC DEEP DIVE

This memory serves as a technical reference for manual Protobuf encoding, Device Flow state machines, and provider-specific OAuth edge cases.

---

## 1. MANUAL PROTOBUF & CONNECT-RPC (Binary Protocol)

When interacting with restrictive backends (e.g., Cursor, Windsurf) without heavy libraries, use this manual encoding strategy.

### Connect-RPC Envelope (5-byte Header)
Connect-RPC (and gRPC-Web) wraps Protobuf messages in a framed stream.
- **Byte 0**: Compression flag (0x00 = none, 0x01 = gzip).
- **Bytes 1-4**: Payload length (Big-Endian UInt32).

```javascript
/**
 * Create a Connect-RPC frame for a Protobuf payload
 */
function createConnectFrame(payload) {
  const frame = Buffer.alloc(5 + payload.length);
  frame[0] = 0; // No compression
  frame.writeUInt32BE(payload.length, 1);
  payload.copy(frame, 5);
  return frame;
}
```

### Manual Protobuf Writer (Varints & Strings)
```javascript
class ProtoWriter {
  constructor() { this.parts = []; }
  
  writeVarint(v) {
    const b = [];
    while (v > 127) { b.push((v & 0x7f) | 0x80); v >>>= 7; }
    b.push(v & 0x7f);
    this.parts.push(Buffer.from(b));
  }
  
  writeString(field, value) {
    const buf = Buffer.from(value, 'utf8');
    this.writeVarint((field << 3) | 2); // WireType 2 = Length-delimited
    this.writeVarint(buf.length);
    this.parts.push(buf);
  }
  
  writeMessage(field, writer) {
    const buf = writer.toBuffer();
    this.writeVarint((field << 3) | 2);
    this.writeVarint(buf.length);
    this.parts.push(buf);
  }
  
  toBuffer() { return Buffer.concat(this.parts); }
}
```

---

## 2. DEVICE FLOW STATE MACHINE (RFC 8628)

Qwen and other CLI-first providers utilize the Device Flow for browserless authentication.

### Polling Logic & Error Handling
```javascript
async function pollDeviceToken(deviceCode, interval, expiresAt) {
  while (Date.now() < expiresAt) {
    const res = await fetch(TOKEN_ENDPOINT, {
      method: 'POST',
      body: new URLSearchParams({
        grant_type: 'urn:ietf:params:oauth:grant-type:device_code',
        device_code: deviceCode,
        client_id: CLIENT_ID
      })
    });

    const data = await res.json();
    if (res.ok) return data.access_token;

    // RFC 8628 Specific Error Codes
    switch (data.error) {
      case 'authorization_pending':
        await sleep(interval * 1000);
        break;
      case 'slow_down':
        interval += 5; // Increase poll interval
        await sleep(interval * 1000);
        break;
      case 'expired_token':
        throw new Error('Device code expired. Please restart login.');
      default:
        throw new Error(data.error_description || 'Auth failed');
    }
  }
}
```

---

## 3. PUTER.COM 'USER-PAYS' LOGIC

Puter.com uses a credit-based system where tokens are attached to individual user accounts.

### Credit Check Protocol
Always verify credits before switching accounts in a `round-robin` or `hybrid` strategy.
```javascript
async function getPuterCredits(token) {
  const res = await fetch('https://api.puter.com/auth/get-monthly-usage', {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const data = await res.json();
  // Puter uses 'allowanceInfo.remaining' (values in micro-credits, scale by 10^8)
  return data.allowanceInfo.remaining;
}
```

### Request Transformation (Google/OpenAI Bridge)
Puter acts as a multi-model router. Key interface: `puter-chat-completion`.
```javascript
const puterRequest = {
  interface: 'puter-chat-completion',
  service: 'ai-chat',
  method: 'complete',
  args: {
    messages: transformedMessages,
    model: 'claude-opus-4-5', // Stripped of 'puter-' prefix
    stream: true
  },
  auth_token: token
};
```

---

## 4. CHINESE PROVIDER MODEL MAPPING

Standardize model IDs across Qwen, iFlow, and DeepSeek for federation.

| Provider | OpenCode ID | Native ID | Strategy |
| :--- | :--- | :--- | :--- |
| **Qwen** | `qwen-3-coder` | `qwen3-coder-plus` | Multi-Modal (Vision + Thinking) |
| **DeepSeek** | `deepseek-r1` | `deepseek-r1` | Native Reasoning (CFA L3) |
| **GLM** | `glm-4-6` | `glm-4.6` | Auto-Thinking Mode |
| **iFlow** | `iflow-rome` | `iflow-rome-30ba3b` | Proprietary High-Context |

### Reasoning Model Detection
```javascript
const THINKING_MODELS = ['glm-4.6', 'deepseek-r1', 'qwen3-235b-thinking'];
const isReasoning = (model) => THINKING_MODELS.some(m => model.includes(m));
```

