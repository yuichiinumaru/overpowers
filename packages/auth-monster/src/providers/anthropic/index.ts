import { AuthProvider, ManagedAccount, OAuthTokens } from '../../core/types';
import { transformRequest, transformResponseText } from './transform';
import { listenForCode } from '../../utils/oauth-server';
import { proxyFetch } from '../../core/proxy';

const CLIENT_ID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e";

export class AnthropicProvider {
  static readonly provider = AuthProvider.Anthropic;

  static getHeaders(account: ManagedAccount): Record<string, string> {
    const headers: Record<string, string> = {
      'content-type': 'application/json',
    };

    if (account.apiKey) {
      headers['x-api-key'] = account.apiKey;
      headers['anthropic-version'] = '2023-06-01';
    } else if (account.tokens.accessToken) {
      headers['authorization'] = `Bearer ${account.tokens.accessToken}`;
      
      // Beta headers logic from reference
      const betas = [
        "oauth-2025-04-20",
        "interleaved-thinking-2025-05-14",
        "claude-code-20250219" // Always include for now as per reference logic implying it's needed for Claude Code features
      ];
      
      headers['anthropic-beta'] = betas.join(',');
      headers['user-agent'] = 'claude-cli/2.1.2 (external, cli)';
    }

    return headers;
  }

  static getUrl(model: string, account: ManagedAccount): string {
    return "https://api.anthropic.com/v1/messages";
  }

  static async refreshTokens(account: ManagedAccount): Promise<ManagedAccount> {
    if (!account.tokens.refreshToken) {
      return account;
    }

    try {
      const response = await proxyFetch("https://console.anthropic.com/v1/oauth/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          grant_type: "refresh_token",
          refresh_token: account.tokens.refreshToken,
          client_id: CLIENT_ID,
        }),
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
          refreshToken: json.refresh_token || account.tokens.refreshToken, // Use new refresh token if provided
          expiryDate: Date.now() + json.expires_in * 1000,
          tokenType: json.token_type || 'Bearer',
        },
        lastUsed: Date.now(),
      };
    } catch (error) {
      console.error('Failed to refresh Anthropic tokens:', error);
      // Return account as is, or maybe mark as unhealthy? 
      // For now, returning as is but the caller might check expiry.
      return {
        ...account,
        isHealthy: false
      };
    }
  }

  /**
   * Performs interactive OAuth login using the standardized local callback server.
   */
  static async login(): Promise<OAuthTokens> {
    const port = 1455;
    const redirectUri = `http://localhost:${port}/callback`;
    const authUrl = `https://console.anthropic.com/v1/oauth/authorize?response_type=code&client_id=${CLIENT_ID}&redirect_uri=${encodeURIComponent(redirectUri)}&scope=offline_access`;

    console.log(`\nTo authenticate with Anthropic, please open your browser and visit:`);
    console.log(`\x1b[36m${authUrl}\x1b[0m\n`);
    console.log(`Waiting for callback on port ${port}...`);
    
    const code = await listenForCode(port);
    
    console.log('Code received, exchanging for tokens...');
    
    const response = await proxyFetch("https://console.anthropic.com/v1/oauth/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        grant_type: "authorization_code",
        code,
        client_id: CLIENT_ID,
        redirect_uri: redirectUri,
      }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Failed to exchange code for tokens: ${response.status} ${errorText}`);
    }

    const json = await response.json() as any;
    return {
      accessToken: json.access_token,
      refreshToken: json.refresh_token,
      expiryDate: Date.now() + (json.expires_in * 1000),
      tokenType: json.token_type || 'Bearer',
    };
  }
}

export { transformRequest, transformResponseText };
