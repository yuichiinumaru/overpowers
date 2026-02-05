import { AuthProvider, ManagedAccount } from '../../core/types';

export class DeepSeekProvider {
  static readonly provider = AuthProvider.DeepSeek;

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
    return "https://api.deepseek.com/chat/completions";
  }
}
