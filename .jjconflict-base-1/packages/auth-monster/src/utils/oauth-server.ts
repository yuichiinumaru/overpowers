import http from 'http';
import { URL } from 'url';
import crypto from 'crypto';

/**
 * Standard port for local OAuth callback server.
 */
export const OAUTH_CALLBACK_PORT = 1455;

/**
 * Encodes a buffer to base64url format.
 */
function base64UrlEncode(buffer: Buffer): string {
  return buffer.toString('base64')
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=/g, '');
}

/**
 * Generates PKCE verifier and challenge.
 */
export async function generatePKCE() {
  const verifier = base64UrlEncode(crypto.randomBytes(32));
  const challenge = base64UrlEncode(
    crypto.createHash('sha256').update(verifier).digest()
  );
  return { verifier, challenge };
}

/**
 * Listens for an OAuth callback code or token on the specified port.
 * Returns a promise that resolves with the captured code/token.
 */
export async function listenForCode(port: number = OAUTH_CALLBACK_PORT): Promise<string> {
  return new Promise((resolve, reject) => {
    const server = http.createServer((req, res) => {
      const url = new URL(req.url || '', `http://${req.headers.host}`);
      
      // Handle favicon or other noise
      if (url.pathname !== '/callback' && url.pathname !== '/oauth2callback') {
        res.writeHead(404);
        res.end();
        return;
      }

      // Capture 'code' (OAuth2 code) or 'token' (implicit/custom)
      // Also capture 'state' if needed by the caller, but here we return the code.
      const code = url.searchParams.get('code') || url.searchParams.get('token');
      const state = url.searchParams.get('state');
      
      if (code) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(`
          <html>
            <head>
              <title>Authentication Successful</title>
              <style>
                body {
                  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                  display: flex;
                  align-items: center;
                  justify-content: center;
                  height: 100vh;
                  margin: 0;
                  background: #f7fafc;
                }
                .card {
                  background: white;
                  padding: 2.5rem;
                  border-radius: 12px;
                  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
                  text-align: center;
                  max-width: 400px;
                }
                h1 {
                  color: #2d3748;
                  margin-top: 0;
                  font-size: 1.5rem;
                }
                p {
                  color: #4a5568;
                  line-height: 1.5;
                }
                .icon {
                  color: #48bb78;
                  font-size: 3rem;
                  margin-bottom: 1rem;
                }
              </style>
            </head>
            <body>
              <div class="card">
                <div class="icon">✓</div>
                <h1>Authentication Successful!</h1>
                <p>OpenCode Auth Monster has captured your credentials.</p>
                <p>You can now close this window and return to your terminal.</p>
              </div>
            </body>
          </html>
        `);
        
        // Use a small delay before closing to ensure the response is sent
        setTimeout(() => {
          server.close();
          // If we have state, we might want to return both, but for simplicity 
          // let's just return the code. If the caller needs state, they can parse it.
          // Actually, return code + (state ? '#' + state : '') for compatibility with some references
          resolve(state ? `${code}#${state}` : code);
        }, 100);
      } else {
        res.writeHead(400, { 'Content-Type': 'text/plain' });
        res.end('Missing code or token in query parameters.');
      }
    });

    server.on('error', (err) => {
      reject(err);
    });

    server.listen(port, () => {
      // Server started
    });
  });
}
