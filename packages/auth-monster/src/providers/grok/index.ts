import { AuthProvider, ManagedAccount } from '../../core/types';

export class GrokProvider {
  static readonly provider = AuthProvider.Grok;

  static getHeaders(account: ManagedAccount): Record<string, string> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (account.apiKey) {
      headers['Authorization'] = `Bearer ${account.apiKey}`;
    } else if (account.tokens.accessToken) {
        headers['Authorization'] = `Bearer ${account.tokens.accessToken}`;
    }

    return headers;
  }

  static getUrl(model: string, account: ManagedAccount): string {
    return "https://api.x.ai/v1/chat/completions";
  }
}
