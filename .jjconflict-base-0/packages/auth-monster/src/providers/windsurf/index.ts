import { AuthProvider, ManagedAccount } from '../../core/types';
import { getCredentials, WindsurfCredentials } from './auth';
import { TokenExtractor } from '../../utils/extractor';

export class WindsurfProvider {
  static readonly provider = AuthProvider.Windsurf;

  static getHeaders(account: ManagedAccount): Record<string, string> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/grpc',
    };

    if (account.metadata?.csrfToken) {
      headers['x-codeium-csrf-token'] = account.metadata.csrfToken;
    }

    return headers;
  }

  static getUrl(model: string, account: ManagedAccount): string {
    const port = account.metadata?.port || 0;
    return `http://localhost:${port}/exa.language_server_pb.LanguageServerService/RawGetChatMessage`;
  }

  static async refreshTokens(account: ManagedAccount): Promise<ManagedAccount> {
    try {
      // Re-discover credentials
      const credentials = getCredentials();
      
      // Update account with new credentials
      return {
        ...account,
        apiKey: credentials.apiKey,
        metadata: {
          ...account.metadata,
          csrfToken: credentials.csrfToken,
          port: credentials.port,
          version: credentials.version,
          lastRefreshed: Date.now()
        },
        isHealthy: true
      };
    } catch (error) {
      console.error('Failed to refresh Windsurf credentials:', error);
      return {
        ...account,
        isHealthy: false,
        lastSwitchReason: error instanceof Error ? error.message : 'Unknown error during refresh'
      };
    }
  }
  
  /**
   * Automatically discover local Windsurf accounts
   */
  static async discover(): Promise<ManagedAccount | null> {
      try {
          const credentials = getCredentials();
          return {
              id: `windsurf-local-${Date.now()}`,
              email: 'local@windsurf',
              provider: AuthProvider.Windsurf,
              tokens: { accessToken: credentials.apiKey },
              apiKey: credentials.apiKey,
              metadata: {
                  csrfToken: credentials.csrfToken,
                  port: credentials.port,
                  version: credentials.version,
                  discoveredAt: Date.now()
              },
              isHealthy: true
          };
      } catch (error) {
          // If process not running, try direct SQLite extraction via TokenExtractor
          const apiKey = TokenExtractor.extractWindsurfFromSQLite();
          if (apiKey) {
              return {
                  id: `windsurf-local-${Date.now()}`,
                  email: 'local@windsurf',
                  provider: AuthProvider.Windsurf,
                  tokens: { accessToken: apiKey },
                  apiKey: apiKey,
                  isHealthy: true,
                  metadata: {
                      discoveredAt: Date.now(),
                      method: 'sqlite'
                  }
              };
          }
          return null;
      }
  }

  // Helper to initialize a new account from environment
  static async discoverAccount(): Promise<ManagedAccount> {
      const account = await this.discover();
      if (!account) {
          throw new Error('Could not discover local Windsurf account');
      }
      return account;
  }
}

export * from './grpc-client';
export * from './auth';
export * from './types';
export * from './models';
