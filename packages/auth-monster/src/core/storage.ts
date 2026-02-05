import fs from 'fs';
import path from 'path';
import { xdgConfig } from 'xdg-basedir';
import { lock } from 'proper-lockfile';
import { ManagedAccount, AuthProvider } from './types';
import { SecretStorage } from './secret-storage';

export class StorageManager {
  private storagePath: string;
  private secretStorage: SecretStorage;

  constructor(customPath?: string) {
    const configDir = customPath || path.join(xdgConfig || '', 'opencode');
    if (!fs.existsSync(configDir)) {
      fs.mkdirSync(configDir, { recursive: true });
    }
    this.storagePath = path.join(configDir, 'auth-monster-accounts.json');
    this.secretStorage = new SecretStorage(configDir);
  }

  async loadAccounts(): Promise<ManagedAccount[]> {
    if (!fs.existsSync(this.storagePath)) {
      return [];
    }

    try {
      const release = await lock(this.storagePath, { retries: 5 });
      let accounts: ManagedAccount[] = [];
      try {
        const data = fs.readFileSync(this.storagePath, 'utf8');
        accounts = JSON.parse(data);
      } finally {
        await release();
      }

      // Rehydrate tokens from secret storage
      const hydratedAccounts = await Promise.all(accounts.map(async (acc) => {
          // Fallback to what's in JSON if not in secret storage (for legacy data)
          const accessToken = await this.secretStorage.getSecret('accessToken', acc.id);
          const refreshToken = await this.secretStorage.getSecret('refreshToken', acc.id);
          const apiKey = await this.secretStorage.getSecret('apiKey', acc.id);

          if (accessToken) acc.tokens.accessToken = accessToken;
          if (refreshToken) acc.tokens.refreshToken = refreshToken;
          if (apiKey) acc.apiKey = apiKey;

          return acc;
      }));

      return hydratedAccounts;

    } catch (error) {
      console.error('Failed to load accounts:', error);
      return [];
    }
  }

  async saveAccounts(accounts: ManagedAccount[]): Promise<void> {
    const dir = path.dirname(this.storagePath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    // Ensure file exists for locking
    if (!fs.existsSync(this.storagePath)) {
      fs.writeFileSync(this.storagePath, '[]', 'utf8');
    }

    try {
      // 1. Save secrets first
      await Promise.all(accounts.map(async (acc) => {
          if (acc.tokens.accessToken) {
              await this.secretStorage.saveSecret('accessToken', acc.id, acc.tokens.accessToken);
          }
          if (acc.tokens.refreshToken) {
              await this.secretStorage.saveSecret('refreshToken', acc.id, acc.tokens.refreshToken);
          }
          if (acc.apiKey) {
              await this.secretStorage.saveSecret('apiKey', acc.id, acc.apiKey);
          }
      }));

      // 2. Prepare accounts for JSON storage (strip sensitive data)
      const sanitizedAccounts = accounts.map(acc => {
          const clone = { ...acc, tokens: { ...acc.tokens } };
          // Remove sensitive data from the clone that will be saved to disk
          clone.tokens.accessToken = '';
          clone.tokens.refreshToken = '';
          clone.apiKey = '';
          return clone;
      });

      const release = await lock(this.storagePath, { retries: 5 });
      try {
        fs.writeFileSync(this.storagePath, JSON.stringify(sanitizedAccounts, null, 2), 'utf8');
      } finally {
        await release();
      }
    } catch (error) {
      console.error('Failed to save accounts:', error);
      throw error;
    }
  }

  async addAccount(account: ManagedAccount): Promise<void> {
    const accounts = await this.loadAccounts();
    const index = accounts.findIndex(a => a.id === account.id || (a.email === account.email && a.provider === account.provider));
    
    if (index >= 0) {
      accounts[index] = { ...accounts[index], ...account };
    } else {
      accounts.push(account);
    }
    
    await this.saveAccounts(accounts);
  }

  async deleteAccount(id: string): Promise<void> {
    const accounts = await this.loadAccounts();
    const filtered = accounts.filter(a => a.id !== id);
    if (accounts.length !== filtered.length) {
      await this.saveAccounts(filtered);
      // Cleanup secrets
      await this.secretStorage.deleteSecret('accessToken', id);
      await this.secretStorage.deleteSecret('refreshToken', id);
      await this.secretStorage.deleteSecret('apiKey', id);
    }
  }

  async getAccountsByProvider(provider: AuthProvider): Promise<ManagedAccount[]> {
    const accounts = await this.loadAccounts();
    return accounts.filter(a => a.provider === provider);
  }
}
