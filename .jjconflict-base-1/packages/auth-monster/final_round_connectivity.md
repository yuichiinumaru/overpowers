# FINAL ROUND CONNECTIVITY MEMORY

This document summarizes the deep dive into connectivity, performance, and security patterns across the referenced repositories.

## 1. HTTP/2 and gRPC Performance Tweaks
Manual gRPC implementation over HTTP/2 is preferred for low-latency streaming and better control over the protocol.

### Actionable Snippets:
**Manual gRPC Framing (Node.js)**
```javascript
function buildGrpcFrame(payload) {
    const frame = Buffer.alloc(5 + payload.length);
    frame[0] = 0; // Compression flag: 0 = none
    frame.writeUInt32BE(payload.length, 1); // 4-byte big-endian length
    payload.copy(frame, 5);
    return frame;
}

// HTTP/2 Request with Trailers
const client = http2.connect(\`http://localhost:\${port}\`);
const req = client.request({
    ':method': 'POST',
    ':path': '/service/Method',
    'content-type': 'application/grpc',
    'te': 'trailers', // Required for gRPC status
});

req.on('trailers', (trailers) => {
    const status = trailers['grpc-status'];
    if (status !== '0') {
        const message = trailers['grpc-message'];
        console.error(\`gRPC Error \${status}: \${decodeURIComponent(message)}\`);
    }
});
```

**Upstream HTTP/2 Enforcement (Rust/Pingora)**
```rust
async fn upstream_peer(&self, _session: &mut Session, _ctx: &mut Self::CTX) -> Result<Box<HttpPeer>> {
    let mut peer = HttpPeer::new(addr, true, host);
    peer.options.set_http_version(2, 1); // Force HTTP/2, fallback to 1.1
    Ok(Box::new(peer))
}
```

## 2. VPN/SOCKS5 Proxy Support
Implement proxy support by leveraging environment variable standards that most HTTP clients honor automatically.

### Actionable Snippets:
**Proxy Environment Setup (Python)**
```python
def setup_vpn_proxy(vpn_url):
    if vpn_url:
        proxy_url = vpn_url if "://" in vpn_url else f"http://{vpn_url}"
        os.environ['HTTP_PROXY'] = proxy_url
        os.environ['HTTPS_PROXY'] = proxy_url
        os.environ['ALL_PROXY'] = proxy_url
        
        # Ensure local connections bypass the proxy
        no_proxy = os.environ.get("NO_PROXY", "")
        local_hosts = "127.0.0.1,localhost"
        os.environ["NO_PROXY"] = f"{no_proxy},{local_hosts}" if no_proxy else local_hosts
```

## 3. Header Spoofing for 'backend-api'
To bypass server-side blocks or simulate official clients, use strict header remapping and internal originator tags.

### Actionable Snippets:
**Codex/Internal Header Spoofing**
```javascript
function createInternalHeaders(accountId, accessToken, isCodex = true) {
    const headers = new Headers();
    headers.set("Authorization", \`Bearer \${accessToken}\`);
    headers.set("Openai-Account-Id", accountId);
    
    if (isCodex) {
        headers.set("Openai-Internal-Beta", "responses-v1");
        headers.set("X-Openai-Originator", "codex");
    }
    
    headers.set("accept", "text/event-stream");
    return headers;
}
```

**Strict Header Filtering (Rust/Pingora)**
```rust
async fn upstream_request_filter(&self, _session: &mut Session, upstream_request: &mut RequestHeader, _ctx: &mut Self::CTX) -> Result<()> {
    // 1. Collect required client headers
    let content_type = upstream_request.headers.get("content-type").map(|v| v.to_str().unwrap().to_string());
    
    // 2. Clear ALL client headers to remove fingerprints
    let keys: Vec<String> = upstream_request.headers.keys().map(|k| k.as_str().to_string()).collect();
    for key in keys { upstream_request.remove_header(&key); }
    
    // 3. Re-inject sanitized/spoofed headers
    upstream_request.insert_header("User-Agent", "opencode/1.0")?;
    upstream_request.insert_header("Openai-Intent", "conversation-edits")?;
    if let Some(ct) = content_type { upstream_request.insert_header("Content-Type", ct)?; }
    
    Ok(())
}
```

## 4. SSE Streaming Error Handling
Use `TransformStream` (Node.js/Web) for efficient, real-time transformation and error detection in SSE streams.

### Actionable Snippets:
**FSM-based SSE Parser & Thinking Cache**
```javascript
export function createStreamingTransformer(signatureStore, sessionId) {
    let buffer = '';
    return new TransformStream({
        transform(chunk, controller) {
            buffer += new TextDecoder().decode(chunk, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop() || '';

            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    try {
                        const json = JSON.parse(line.slice(5));
                        // Detect thinking blocks and cache signatures
                        if (json.response?.thoughtSignature) {
                             signatureStore.set(sessionId, {
                                 text: json.response.thinking,
                                 signature: json.response.thoughtSignature
                             });
                        }
                        controller.enqueue(new TextEncoder().encode(line + '\n'));
                    } catch (e) {
                        // Handle partial JSON or SSE error events
                        if (line.includes('"error":')) controller.enqueue(new TextEncoder().encode(line + '\n'));
                    }
                }
            }
        }
    });
}
```
