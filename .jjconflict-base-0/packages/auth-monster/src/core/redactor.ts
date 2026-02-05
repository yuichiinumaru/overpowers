export class Redactor {
  private static SENSITIVE_HEADERS = new Set([
    'authorization',
    'x-api-key',
    'x-auth-token',
    'cookie',
    'set-cookie',
    'openai-organization',
    'anthropic-version'
  ]);

  private static KEY_PATTERNS = [
    /sk-[a-zA-Z0-9]{20,}/g, // OpenAI / Anthropic style
    /AIza[a-zA-Z0-9_-]{35}/g, // Google
    /ey[a-zA-Z0-9_-]{20,}\.[a-zA-Z0-9_-]{20,}\.[a-zA-Z0-9_-]{20,}/g, // JWT-like
    /gh[pousr]-[a-zA-Z0-9]{36}/g // GitHub tokens
  ];

  /**
   * Redacts sensitive information from an object, array, or string.
   * Returns a deep copy with sensitive data replaced.
   */
  static redact(data: any): any {
    if (typeof data === 'string') {
        return this.redactString(data);
    }
    if (Array.isArray(data)) {
        return data.map(item => this.redact(item));
    }
    if (typeof data === 'object' && data !== null) {
        const copy: any = {};
        for (const key in data) {
            if (Object.prototype.hasOwnProperty.call(data, key)) {
                if (this.SENSITIVE_HEADERS.has(key.toLowerCase())) {
                    copy[key] = '[REDACTED]';
                } else {
                    copy[key] = this.redact(data[key]);
                }
            }
        }
        return copy;
    }
    return data;
  }

  private static redactString(str: string): string {
    let result = str;
    for (const pattern of this.KEY_PATTERNS) {
        result = result.replace(pattern, (match) => {
             // Keep first 3 and last 3 chars for debugging context, redact the rest
             if (match.length < 8) return '[REDACTED]';
             return match.substring(0, 3) + '...' + match.substring(match.length - 3);
        });
    }
    return result;
  }
}
