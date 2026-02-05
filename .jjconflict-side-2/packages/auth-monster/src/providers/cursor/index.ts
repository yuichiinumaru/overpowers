import { randomUUID } from 'node:crypto';
import { AuthProvider, ManagedAccount, OAuthTokens } from '../../core/types';
import { generateChecksum } from './proto';
import { TokenExtractor } from '../../utils/extractor';
import { proxyFetch } from '../../core/proxy';

const CURSOR_API_BASE_URL = "https://api2.cursor.sh";
const REFRESH_ENDPOINT = "/auth/refresh";

export class CursorProvider {
  /**
   * Get request headers for Cursor API
   */
  getHeaders(account: ManagedAccount): Record<string, string> {
    const accessToken = account.tokens.accessToken;
    const checksum = generateChecksum(accessToken);
    
    return {
      "authorization": `Bearer ${accessToken}`,
      "content-type": "application/grpc-web+proto",
      "user-agent": "connect-es/1.4.0",
      "x-cursor-checksum": checksum,
      "x-cursor-client-version": "cli-2025.11.25-d5b3271",
      "x-cursor-client-type": "cli",
      "x-cursor-timezone": Intl.DateTimeFormat().resolvedOptions().timeZone,
      "x-ghost-mode": "true",
      "x-request-id": randomUUID(),
      "host": new URL(CURSOR_API_BASE_URL).host,
    };
  }

  getUrl(model: string, account: ManagedAccount): string {
    return `${CURSOR_API_BASE_URL}/aiserver.v1.AiService/StreamChat`;
  }

  /**
   * Refresh the access token using the refresh token
   */
  async refreshTokens(refreshToken: string): Promise<OAuthTokens | null> {
    try {
      const response = await proxyFetch(`${CURSOR_API_BASE_URL}${REFRESH_ENDPOINT}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${refreshToken}`,
        },
        body: JSON.stringify({}),
      });

      if (!response.ok) {
        return null;
      }

      const result = await response.json() as any;

      if (
        typeof result === "object" &&
        result !== null &&
        "accessToken" in result &&
        "refreshToken" in result
      ) {
        return {
          accessToken: result.accessToken,
          refreshToken: result.refreshToken,
          // Cursor tokens are JWTs, but we don't parse them here to get expiry.
          // The consumer can parse the JWT if needed.
          tokenType: 'Bearer'
        };
      }
    } catch (error) {
      console.error("Failed to refresh Cursor tokens:", error);
    }

    return null;
  }

  /**
   * Automatically discover local Cursor accounts
   */
  async discover(): Promise<ManagedAccount | null> {
    const data = TokenExtractor.extractCursorFromKeychain() || TokenExtractor.extractCursorFromSQLite();
    if (!data) return null;

    // data is string (accessToken)
    return {
      id: `cursor-local-${Date.now()}`,
      email: 'local@cursor',
      provider: AuthProvider.Cursor,
      tokens: {
        accessToken: data,
      },
      isHealthy: true,
      metadata: {
        discoveredAt: Date.now(),
        method: 'local'
      }
    };
  }
}

export const cursorProvider = new CursorProvider();
