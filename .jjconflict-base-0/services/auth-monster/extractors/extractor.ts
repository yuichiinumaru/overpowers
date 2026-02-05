import { execSync } from 'child_process';
import * as path from 'path';
import * as os from 'os';
import * as fs from 'fs';
import * as crypto from 'crypto';
import { AuthProvider, ManagedAccount } from '../core/types';

export interface ExtractedToken {
  provider: AuthProvider;
  token: string;
  email?: string;
}

export class TokenExtractor {

  /**
   * Auto-discover accounts from local environment (Cursor, Windsurf, Env Vars).
   */
  static async discoverAll(): Promise<ManagedAccount[]> {
    const accounts: ManagedAccount[] = [];

    // 1. Cursor (Keychain)
    try {
      const cursorToken = this.getCursorToken();
      if (cursorToken) {
        accounts.push({
          id: 'cursor-local',
          email: 'local-cursor@device',
          provider: AuthProvider.Cursor,
          tokens: { accessToken: cursorToken },
          isHealthy: true,
          healthScore: 100,
          metadata: { source: 'keychain' }
        });
      }
    } catch (e) {
      // Ignore missing cursor
    }

    // 2. Windsurf (SQLite)
    try {
      const windsurfAuth = this.getWindsurfAuth();
      if (windsurfAuth) {
        accounts.push({
          id: 'windsurf-local',
          email: 'local-windsurf@device',
          provider: AuthProvider.Windsurf,
          tokens: { accessToken: windsurfAuth },
          isHealthy: true,
          healthScore: 100,
          metadata: { source: 'sqlite' }
        });
      }
    } catch (e) {
      // Ignore missing windsurf
    }

    // 3. Qwen (File)
    try {
        const qwenToken = this.getQwenToken();
        if (qwenToken) {
            accounts.push({
                id: 'qwen-local',
                email: 'local-qwen@device',
                provider: AuthProvider.Qwen,
                tokens: { accessToken: qwenToken },
                isHealthy: true,
                healthScore: 100,
                metadata: { source: 'file' }
            });
        }
    } catch (e) {
        // Ignore missing qwen
    }

    // 4. Kiro/AWS SSO (File)
    try {
        const kiroToken = await this.extractKiroFromSSOCache();
        if (kiroToken) {
            accounts.push({
                id: 'kiro-local',
                email: kiroToken.email || 'local-kiro@aws',
                provider: AuthProvider.Kiro,
                tokens: { accessToken: kiroToken.token },
                isHealthy: true,
                healthScore: 100,
                metadata: { source: 'aws-sso' }
            });
        }
    } catch (e) {
        // Ignore missing kiro
    }

    // 5. Claude (Keychain)
    try {
        const claudeToken = this.extractClaudeFromKeychain();
        if (claudeToken) {
            accounts.push({
                id: 'claude-local',
                email: 'local-claude@device',
                provider: AuthProvider.Anthropic,
                tokens: { accessToken: claudeToken },
                isHealthy: true,
                healthScore: 100,
                metadata: { source: 'keychain', model: 'claude-3-opus-20240229' }
            });
        }
    } catch (e) {
        // Ignore missing claude
    }

    return accounts;
  }

  public static async extractKiroFromSSOCache(): Promise<ExtractedToken | null> {
    const home = os.homedir();
    const ssoCachePath = path.join(home, '.aws', 'sso', 'cache');

    if (!fs.existsSync(ssoCachePath)) return null;

    try {
        const files = fs.readdirSync(ssoCachePath);
        for (const file of files) {
            if (!file.endsWith('.json')) continue;

            try {
                const content = fs.readFileSync(path.join(ssoCachePath, file), 'utf8');
                const json = JSON.parse(content);

                // Look for standard AWS SSO token format
                if (json.accessToken && json.expiresAt) {
                     // Check expiry
                     const expiresAt = new Date(json.expiresAt).getTime();
                     if (expiresAt > Date.now()) {
                         // Found valid token
                         return {
                             provider: AuthProvider.Kiro,
                             token: json.accessToken,
                             email: json.email // Sometimes present?
                         };
                     }
                }
            } catch (e) {
                continue;
            }
        }
    } catch (e) {
        return null;
    }
    return null;
  }

  public static extractCursorFromKeychain(): string | null {
    return this.getCursorToken();
  }

  public static extractClaudeFromKeychain(): string | null {
    if (process.platform !== 'darwin') return null;

    // Logic from CodMate:
    // Service Name: "Claude Code-credentials-<hash>"
    // Hash is first 8 chars of SHA256 of expanded path "~/.claude"

    const home = os.homedir();
    const configPath = path.join(home, '.claude');

    // Hash path
    const hash = crypto.createHash('sha256').update(configPath).digest('hex').substring(0, 8);
    const serviceName = `Claude Code-credentials-${hash}`;

    try {
        // We use 'security find-generic-password' with service name
        // The account name is usually the OS username, but 'security' can find by service alone if unique enough
        // or we can iterate.

        const result = execSync(`security find-generic-password -s "${serviceName}" -w`, {
            encoding: 'utf8',
            stdio: ['pipe', 'pipe', 'pipe']
        }).trim();

        // Result is likely a JSON envelope
        if (result) {
            try {
                // Sometimes it returns the raw password (token) if -w is used,
                // but CodMate implies it stores a JSON "CredentialEnvelope".
                // However, `security -w` returns the password item.
                // If CodMate stores the JSON *as* the password, this works.
                // If it stores it as attribute, we might need different flags.
                // Assuming it stores the JSON string as the keychain item 'password' (data).

                // Let's try to parse as JSON
                const json = JSON.parse(result);
                if (json.claudeAiOauth && json.claudeAiOauth.accessToken) {
                    return json.claudeAiOauth.accessToken;
                }
            } catch (e) {
                // If not JSON, maybe it's the token directly?
                if (result.startsWith('sk-')) return result;
            }
        }
    } catch (e) {
        // Try fallback service name without hash or "Claude Code"
    }

    return null;
  }

  public static extractCursorFromSQLite(): string | null {
    const home = os.homedir();
    let dbPath = '';

    switch (process.platform) {
        case 'darwin':
            dbPath = path.join(home, 'Library/Application Support/Cursor/User/globalStorage/state.vscdb');
            break;
        case 'win32':
            dbPath = path.join(process.env.APPDATA || path.join(home, 'AppData', 'Roaming'), 'Cursor/User/globalStorage/state.vscdb');
            break;
        case 'linux':
            dbPath = path.join(home, '.config/Cursor/User/globalStorage/state.vscdb');
            break;
        default:
            return null;
    }

    if (!fs.existsSync(dbPath)) return null;

    try {
        const query = "SELECT value FROM ItemTable WHERE key = 'cursorAuth/accessToken';";

        const result = execSync(`sqlite3 "${dbPath}" "${query}"`, {
            encoding: 'utf8',
            stdio: ['pipe', 'pipe', 'pipe']
        }).trim();

        if (!result) return null;

        return result;
    } catch (e) {
        return null;
    }
  }

  public static extractWindsurfFromSQLite(): string | null {
    return this.getWindsurfAuth();
  }

  /**
   * Extract Cursor token from macOS Keychain.
   */
  private static getCursorToken(): string | null {
    if (process.platform !== 'darwin') return null;
    try {
      return execSync('security find-generic-password -s "cursor-access-token" -w', {
        encoding: 'utf8',
        stdio: ['pipe', 'pipe', 'pipe'],
      }).trim();
    } catch (e) {
      return null;
    }
  }

  /**
   * Extract Windsurf auth status from SQLite DB.
   */
  private static getWindsurfAuth(): string | null {
    const home = os.homedir();
    // Common path on macOS/Linux
    const dbPath = path.join(home, 'Library/Application Support/Windsurf/User/globalStorage/state.vscdb');
    
    if (!fs.existsSync(dbPath)) return null;

    try {
      // Query SQLite directly
      const query = "SELECT value FROM ItemTable WHERE key = 'windsurfAuthStatus';";
      const result = execSync(`sqlite3 "${dbPath}" "${query}"`, {
        encoding: 'utf8',
        stdio: ['pipe', 'pipe', 'pipe']
      }).trim();

      if (!result) return null;

      // Parse JSON result to get access token
      const json = JSON.parse(result);
      return json.accessToken || null;
    } catch (e) {
      return null;
    }
  }

  /**
   * Extract Qwen token from local creds file.
   */
  private static getQwenToken(): string | null {
      const home = os.homedir();
      const credsPath = path.join(home, '.qwen/oauth_creds.json');

      if (!fs.existsSync(credsPath)) return null;

      try {
          const data = fs.readFileSync(credsPath, 'utf8');
          const json = JSON.parse(data);
          return json.access_token || null;
      } catch (e) {
          return null;
      }
  }
}

// Export for direct usage
export const autoDiscoverAccounts = () => TokenExtractor.discoverAll();
