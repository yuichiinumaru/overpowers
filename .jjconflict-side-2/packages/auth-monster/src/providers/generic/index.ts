import { ManagedAccount } from '../../core/types';
import { CookieManager } from '../../integrations/codexbar/cookie-manager';

export class GenericProvider {
  /**
   * Generates headers for Generic OpenAI-compatible providers.
   * Typically expects an API Key in the Authorization header.
   */
  static async getHeaders(account: ManagedAccount): Promise<Record<string, string>> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (account.apiKey) {
      headers['Authorization'] = `Bearer ${account.apiKey}`;
    }

    // Add any custom headers from metadata
    if (account.metadata?.headers) {
        Object.assign(headers, account.metadata.headers);
    }

    // Check for cookie extraction request
    if (account.metadata?.cookieDomain) {
        const domain = account.metadata.cookieDomain;
        const browser = account.metadata.cookieBrowser; // optional
        const cookieHeader = await CookieManager.getCookiesForDomain(domain, browser);
        if (cookieHeader) {
            headers['Cookie'] = cookieHeader;
        }
    }

    return headers;
  }

  /**
   * Resolves the request URL.
   * For Generic providers, the baseUrl MUST be provided in account metadata
   * or config options.
   */
  static getUrl(model: string, account: ManagedAccount): string {
    let baseUrl = account.metadata?.baseUrl;

    if (!baseUrl) {
       // Fallback to localhost for convenience if nothing specified (e.g. Ollama default)
       baseUrl = "http://localhost:11434/v1";
    }

    // Ensure clean slash handling
    baseUrl = baseUrl.replace(/\/$/, '');

    // Check if the user already provided the full path in baseUrl
    if (baseUrl.endsWith('/chat/completions')) {
        return baseUrl;
    }

    return `${baseUrl}/chat/completions`;
  }
}
