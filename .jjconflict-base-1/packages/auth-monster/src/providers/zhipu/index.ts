import { AuthProvider, ManagedAccount } from '../../core/types';

export class ZhipuProvider {
  static readonly provider = AuthProvider.Zhipu;

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
    // Simple prompt simulation, in real CLI this would be passed
    const { Password } = require('enquirer');
    const prompt = new Password({
        name: 'apiKey',
        message: 'Enter your Zhipu AI API Key'
    });

    const apiKey = await prompt.run();
    return { apiKey };
  }
}
