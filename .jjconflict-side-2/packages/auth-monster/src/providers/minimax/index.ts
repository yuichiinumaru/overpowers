import { AuthProvider, ManagedAccount } from '../../core/types';

export class MinimaxProvider {
  static readonly provider = AuthProvider.Minimax;

  static getHeaders(account: ManagedAccount): Record<string, string> {
    const headers: Record<string, string> = {
      'content-type': 'application/json',
    };

    if (account.apiKey) {
      headers['Authorization'] = `Bearer ${account.apiKey}`;
    }

    return headers;
  }

  static async login(): Promise<{ apiKey: string }> {
    const { Password } = require('enquirer');
    const prompt = new Password({
        name: 'apiKey',
        message: 'Enter your MiniMax API Key'
    });

    const apiKey = await prompt.run();
    return { apiKey };
  }
}
