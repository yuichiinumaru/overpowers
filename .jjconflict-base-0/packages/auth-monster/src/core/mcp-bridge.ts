import { spawn, ChildProcess } from 'child_process';
import * as path from 'path';
import * as os from 'os';
import * as fs from 'fs';
import { AuthProvider, ManagedAccount } from './types';

export class MCPBridge {
  private child: ChildProcess | null = null;
  private tokenPath: string;

  constructor(tokenPath?: string) {
    this.tokenPath = tokenPath || path.join(os.homedir(), '.auth-mcp-token.json');
  }

  /**
   * Starts the auth-mcp server process.
   * Assumes `auth-mcp` is in the PATH or references/auth-mcp/auth-mcp exists.
   */
  start(): void {
    const binPath = path.resolve(__dirname, '../../references/auth-mcp/auth-mcp');

    // In a real scenario, we might prefer a configured path
    // For now, we spawn it as a node process directly if possible, or use the wrapper

    // Check if bin exists, else fallback
    const cmd = fs.existsSync(binPath) ? binPath : 'auth-mcp';

    this.child = spawn(cmd, [], {
      stdio: ['pipe', 'pipe', 'pipe'],
      env: process.env
    });

    this.child.stderr?.on('data', (data) => {
      // Log MCP debug output
      // console.error(`[MCP] ${data.toString()}`);
    });

    this.child.on('close', (code) => {
      // console.log(`[MCP] exited with code ${code}`);
      this.child = null;
    });
  }

  /**
   * Performs the JSON-RPC handshake to initialize the session.
   */
  async initialize(): Promise<void> {
    return new Promise((resolve, reject) => {
      if (!this.child || !this.child.stdin || !this.child.stdout) {
        return reject(new Error('MCP server not running'));
      }

      const initMsg = {
        jsonrpc: '2.0',
        id: 1,
        method: 'initialize',
        params: {
          protocolVersion: '2024-11-05',
          capabilities: {},
          clientInfo: { name: 'opencode-monster', version: '1.0.0' }
        }
      };

      const handler = (chunk: Buffer) => {
        const msg = chunk.toString();
        try {
          const json = JSON.parse(msg);
          if (json.id === 1 && json.result) {
            this.child?.stdout?.off('data', handler);
            resolve();
          }
        } catch (e) {
          // Ignore partial chunks for this simple MVP
        }
      };

      this.child.stdout.on('data', handler);
      this.child.stdin.write(JSON.stringify(initMsg) + '\n');

      // Timeout
      setTimeout(() => {
        this.child?.stdout?.off('data', handler);
        reject(new Error('MCP handshake timeout'));
      }, 5000);
    });
  }

  /**
   * Reads the token generated/stored by the MCP server.
   */
  getToken(): string | null {
    if (!fs.existsSync(this.tokenPath)) return null;
    try {
      const data = JSON.parse(fs.readFileSync(this.tokenPath, 'utf8'));
      return data.token || null;
    } catch {
      return null;
    }
  }

  stop() {
    this.child?.kill();
  }
}
