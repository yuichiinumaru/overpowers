import { AuthProvider, ManagedAccount, OAuthTokens } from '../../core/types';
import { listenForCode, generatePKCE } from '../../utils/oauth-server';
import { proxyFetch } from '../../core/proxy';

const GEMINI_CLIENT_ID = process.env.GEMINI_CLIENT_ID || "";
const GEMINI_CLIENT_SECRET = process.env.GEMINI_CLIENT_SECRET || "";
const GEMINI_SCOPES = [
  "https://www.googleapis.com/auth/cloud-platform",
  "https://www.googleapis.com/auth/userinfo.email", 
  "https://www.googleapis.com/auth/userinfo.profile"
];

export class GeminiProvider {
  static readonly provider = AuthProvider.Gemini;

  static getHeaders(account: ManagedAccount): Record<string, string> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (account.apiKey) {
      headers['x-goog-api-key'] = account.apiKey;
    } else if (account.tokens.accessToken) {
      headers['Authorization'] = `Bearer ${account.tokens.accessToken}`;
    }

    // Ported from vibe-open-auth: Multi-account metadata headers if needed
    if (account.metadata?.projectId) {
      headers['x-goog-user-project'] = account.metadata.projectId;
    }

    return headers;
  }

  static getUrl(model: string, account: ManagedAccount): string {
    return `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`;
  }

  static async refreshTokens(account: ManagedAccount): Promise<ManagedAccount> {
    if (!account.tokens.refreshToken) {
      return account;
    }

    try {
      // Parse project ID from refresh token if it was stored that way (ref: shantur-opencode-gemini-auth)
      const [refreshToken, projectId = ""] = account.tokens.refreshToken.split('|');

      const response = await proxyFetch("https://oauth2.googleapis.com/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          grant_type: "refresh_token",
          refresh_token: refreshToken,
          client_id: GEMINI_CLIENT_ID,
          client_secret: GEMINI_CLIENT_SECRET,
        }),
      });

      if (!response.ok) {
        throw new Error(`Token refresh failed: ${response.status}`);
      }

      const json = await response.json() as any;
      
      return {
        ...account,
        tokens: {
          ...account.tokens,
          accessToken: json.access_token,
          refreshToken: json.refresh_token ? `${json.refresh_token}|${projectId}` : account.tokens.refreshToken,
          expiryDate: Date.now() + (json.expires_in * 1000),
          tokenType: json.token_type || 'Bearer',
        },
        lastUsed: Date.now(),
        isHealthy: true
      };
    } catch (error) {
      console.error('Failed to refresh Gemini tokens:', error);
      return {
        ...account,
        isHealthy: false
      };
    }
  }

  /**
   * Performs interactive OAuth login using the standardized local callback server.
   */
  static async login(): Promise<OAuthTokens & { email: string, metadata?: any }> {
    const port = 1455;
    const redirectUri = `http://localhost:${port}/callback`;
    const pkce = await generatePKCE();
    
    // Optional: Ask for project ID
    console.log("\n=== Google Gemini OAuth Setup ===");
    console.log("If you have a specific Google Cloud Project ID, you can use it.");
    console.log("Otherwise, the system will attempt to use/create a managed project.");
    
    // In a real CLI we would use readline, but here we'll just proceed with default/empty
    const projectId = ""; 

    const url = new URL("https://accounts.google.com/o/oauth2/v2/auth");
    url.searchParams.set("client_id", GEMINI_CLIENT_ID);
    url.searchParams.set("response_type", "code");
    url.searchParams.set("redirect_uri", redirectUri);
    url.searchParams.set("scope", GEMINI_SCOPES.join(" "));
    url.searchParams.set("code_challenge", pkce.challenge);
    url.searchParams.set("code_challenge_method", "S256");
    url.searchParams.set("state", Buffer.from(JSON.stringify({ verifier: pkce.verifier, projectId })).toString('base64'));
    url.searchParams.set("access_type", "offline");
    url.searchParams.set("prompt", "consent");

    console.log(`\nPlease visit the following URL to authorize Gemini:\n`);
    console.log(`\x1b[36m${url.toString()}\x1b[0m\n`);
    console.log(`Waiting for callback on port ${port}...`);

    const codeWithState = await listenForCode(port);
    const [code, state] = codeWithState.split('#');

    console.log('Code received, exchanging for tokens...');
    
    const { verifier, projectId: stateProjectId } = JSON.parse(Buffer.from(state, 'base64').toString());

    const response = await proxyFetch("https://oauth2.googleapis.com/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
        client_id: GEMINI_CLIENT_ID,
        client_secret: GEMINI_CLIENT_SECRET,
        code: code,
        grant_type: "authorization_code",
        redirect_uri: redirectUri,
        code_verifier: verifier,
      }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Failed to exchange Gemini code: ${response.status} ${errorText}`);
    }

    const json = await response.json() as any;
    
    // Get user info to get email
    const userInfoResponse = await proxyFetch("https://www.googleapis.com/oauth2/v1/userinfo?alt=json", {
      headers: {
        "Authorization": `Bearer ${json.access_token}`
      }
    });
    
    const userInfo = userInfoResponse.ok ? await userInfoResponse.json() as any : { email: 'unknown@google.com' };

    return {
      accessToken: json.access_token,
      refreshToken: `${json.refresh_token}|${stateProjectId || ""}`,
      expiryDate: Date.now() + (json.expires_in * 1000),
      tokenType: json.token_type || 'Bearer',
      email: userInfo.email,
      metadata: {
        projectId: stateProjectId
      }
    };
  }

  /**
   * Transforms standardized OpenAI-like request to Gemini's format.
   */
  static transformRequest(body: any): any {
    if (body.contents) return body; // Already in Gemini format

    const transformed: any = {
      contents: []
    };

    if (body.messages && Array.isArray(body.messages)) {
      transformed.contents = body.messages.map((msg: any) => {
        // Convert roles
        let role = msg.role;
        if (role === 'assistant') role = 'model';
        if (role === 'system') role = 'user'; // Gemini system instruction is handled differently but for simple cases we can map to user

        // Convert content to parts
        let parts = [];
        if (typeof msg.content === 'string') {
          parts = [{ text: msg.content }];
        } else if (Array.isArray(msg.content)) {
          parts = msg.content.map((part: any) => {
            if (part.type === 'text') return { text: part.text };
            if (part.type === 'image_url') {
               // Handle image mapping if needed
               return { text: '[Image]' };
            }
            return part;
          });
        }

        return { role, parts };
      });
    }

    // Move model
    if (body.model) {
      // In Gemini API, the model is often in the URL, but some clients expect it in body
      transformed.model = body.model;
    }

    // Safety settings, generation config, etc.
    transformed.generationConfig = {
      temperature: body.temperature,
      maxOutputTokens: body.max_tokens,
      topP: body.top_p,
      topK: body.top_k,
      stopSequences: body.stop
    };

    return transformed;
  }
}
