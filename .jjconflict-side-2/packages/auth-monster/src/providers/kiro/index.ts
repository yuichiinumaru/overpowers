import { AuthProvider, ManagedAccount } from '../../core/types';
import { TokenExtractor } from '../../utils/extractor';

export class KiroProvider {
  static readonly provider = AuthProvider.Kiro;

  static getHeaders(account: ManagedAccount): Record<string, string> {
    const headers: Record<string, string> = {
      'content-type': 'application/x-amz-json-1.0',
    };

    if (account.tokens.accessToken) {
      headers['Authorization'] = `Bearer ${account.tokens.accessToken}`;
    }

    return headers;
  }

  static async discoverAccount(): Promise<ManagedAccount | null> {
    const token = await TokenExtractor.extractKiroFromSSOCache();
    if (!token) return null;

    return {
      id: `kiro-local-${Date.now()}`,
      email: token.email || 'local-kiro@aws',
      provider: AuthProvider.Kiro,
      tokens: {
        accessToken: token.token,
      },
      isHealthy: true,
      healthScore: 100,
      metadata: {
        source: 'aws-sso-cache'
      }
    };
  }
}
