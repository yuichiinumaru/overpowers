import { AuthProvider, ManagedAccount, OAuthTokens } from '../../core/types';
import { proxyFetch } from '../../core/proxy';
import * as crypto from 'crypto';

const CLIENT_ID = "f0304373b74a44d2b584a3fb70ca9e56";
const DEVICE_CODE_URL = "https://chat.qwen.ai/api/v1/oauth2/device/code";
const TOKEN_URL = "https://chat.qwen.ai/api/v1/oauth2/token";
const SCOPE = "openid profile email model.completion";
const GRANT_TYPE = "urn:ietf:params:oauth:grant-type:device_code";

function generateCodeVerifier(): string {
  return base64URLEncode(crypto.randomBytes(32));
}

function generateCodeChallenge(verifier: string): string {
  return base64URLEncode(crypto.createHash('sha256').update(verifier).digest());
}

function base64URLEncode(buffer: Buffer): string {
  return buffer.toString('base64')
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=/g, '');
}

export class QwenProvider {
  static readonly provider = AuthProvider.Qwen;

  static getHeaders(account: ManagedAccount): Record<string, string> {
    const headers: Record<string, string> = {
      'content-type': 'application/json',
    };

    if (account.tokens.accessToken) {
      headers['authorization'] = `Bearer ${account.tokens.accessToken}`;
    }

    return headers;
  }

  static getUrl(model: string, account: ManagedAccount): string {
    return "https://chat.qwen.ai/api/v1/chat/completions";
  }

  static async refreshTokens(account: ManagedAccount): Promise<ManagedAccount> {
    if (!account.tokens.refreshToken) {
      return account;
    }

    try {
      const response = await proxyFetch(TOKEN_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "Accept": "application/json"
        },
        body: new URLSearchParams({
            grant_type: "refresh_token",
            refresh_token: account.tokens.refreshToken,
            client_id: CLIENT_ID,
        }).toString()
      });

      if (!response.ok) {
        throw new Error(`Token refresh failed: ${response.status}`);
      }

      const json = await response.json();

      return {
        ...account,
        tokens: {
          ...account.tokens,
          accessToken: json.access_token,
          refreshToken: json.refresh_token || account.tokens.refreshToken,
          expiryDate: Date.now() + json.expires_in * 1000,
          tokenType: json.token_type || 'Bearer',
        },
        lastUsed: Date.now(),
      };
    } catch (error) {
      console.error('Failed to refresh Qwen tokens:', error);
      return {
        ...account,
        isHealthy: false
      };
    }
  }

  static async login(): Promise<OAuthTokens> {
    // 1. Generate PKCE
    const verifier = generateCodeVerifier();
    const challenge = generateCodeChallenge(verifier);

    // 2. Initiate Device Flow
    const deviceResp = await proxyFetch(DEVICE_CODE_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        },
        body: new URLSearchParams({
            client_id: CLIENT_ID,
            scope: SCOPE,
            code_challenge: challenge,
            code_challenge_method: 'S256'
        }).toString()
    });

    if (!deviceResp.ok) {
        throw new Error(`Device flow initiation failed: ${deviceResp.status} ${await deviceResp.text()}`);
    }

    const deviceData = await deviceResp.json();
    const deviceCode = deviceData.device_code;
    const userCode = deviceData.user_code;
    const verificationUri = deviceData.verification_uri_complete || deviceData.verification_uri;
    const interval = deviceData.interval || 5;

    console.log(`\nTo authenticate with Qwen, please visit:`);
    console.log(`\x1b[36m${verificationUri}\x1b[0m`);
    console.log(`And enter code: \x1b[1m${userCode}\x1b[0m\n`);
    console.log(`Waiting for confirmation...`);

    // 3. Poll for token
    while (true) {
        await new Promise(resolve => setTimeout(resolve, interval * 1000));

        const tokenResp = await proxyFetch(TOKEN_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                grant_type: GRANT_TYPE,
                client_id: CLIENT_ID,
                device_code: deviceCode,
                code_verifier: verifier
            }).toString()
        });

        if (tokenResp.ok) {
            const json = await tokenResp.json();
            return {
                accessToken: json.access_token,
                refreshToken: json.refresh_token,
                expiryDate: Date.now() + (json.expires_in * 1000),
                tokenType: json.token_type || 'Bearer'
            };
        }

        const errorText = await tokenResp.text();
        let errorData: any = {};
        try { errorData = JSON.parse(errorText); } catch {}

        if (errorData.error === 'authorization_pending') {
            continue;
        } else if (errorData.error === 'slow_down') {
            await new Promise(resolve => setTimeout(resolve, 5000));
            continue;
        } else {
             throw new Error(`Polling failed: ${tokenResp.status} ${errorText}`);
        }
    }
  }
}
