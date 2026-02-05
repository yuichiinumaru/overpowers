import { exec } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';
import * as crypto from 'crypto';
import { promisify } from 'util';

const execAsync = promisify(exec);

export class SecretStorage {
  private useKeychain: boolean;
  private storagePath: string;
  private encryptionKey: Buffer;

  constructor(storageDir: string) {
    this.storagePath = path.join(storageDir, 'auth-monster-secrets.json');
    this.useKeychain = os.platform() === 'darwin';
    this.encryptionKey = this.deriveKey();
  }

  // Derive a stable, machine-specific key without requiring user input.
  // This isn't perfect security (root can read it), but it prevents
  // casual theft of the file from being useful on another machine.
  private deriveKey(): Buffer {
    const salt = 'auth-monster-salt-v1';
    let machineId = '';

    try {
        // Try to get a stable machine ID
        const networkInterfaces = os.networkInterfaces();
        const mac = Object.values(networkInterfaces)
            .flat()
            .find(i => i && !i.internal && i.mac !== '00:00:00:00:00:00')
            ?.mac;

        machineId = mac || os.hostname() + os.userInfo().username;
    } catch (e) {
        machineId = 'fallback-id';
    }

    return crypto.scryptSync(machineId, salt, 32);
  }

  private encrypt(text: string): string {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv('aes-256-cbc', this.encryptionKey, iv);
    let encrypted = cipher.update(text, 'utf8', 'hex');
    encrypted += cipher.final('hex');
    return iv.toString('hex') + ':' + encrypted;
  }

  private decrypt(text: string): string {
    const textParts = text.split(':');
    const iv = Buffer.from(textParts.shift()!, 'hex');
    const encryptedText = textParts.join(':');
    const decipher = crypto.createDecipheriv('aes-256-cbc', this.encryptionKey, iv);
    let decrypted = decipher.update(encryptedText, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    return decrypted;
  }

  async saveSecret(service: string, account: string, secret: string): Promise<void> {
    if (this.useKeychain) {
      try {
        await execAsync(`security add-generic-password -a "${account}" -s "${service}" -w "${secret}" -U`);
        return;
      } catch (e) {
        console.warn('Failed to save to keychain, falling back to encrypted file:', e);
      }
    }

    await this.saveToFile(service, account, secret);
  }

  async getSecret(service: string, account: string): Promise<string | null> {
    if (this.useKeychain) {
      try {
        const { stdout } = await execAsync(`security find-generic-password -a "${account}" -s "${service}" -w`);
        return stdout.trim();
      } catch (e) {
        // Not found or error
      }
    }

    return this.getFromFile(service, account);
  }

  async deleteSecret(service: string, account: string): Promise<void> {
    if (this.useKeychain) {
      try {
        await execAsync(`security delete-generic-password -a "${account}" -s "${service}"`);
      } catch (e) {}
    }
    await this.deleteFromFile(service, account);
  }

  private async saveToFile(service: string, account: string, secret: string) {
    let data: Record<string, string> = {};
    if (fs.existsSync(this.storagePath)) {
      try {
          data = JSON.parse(fs.readFileSync(this.storagePath, 'utf8'));
      } catch(e) {}
    }
    const key = `${service}:${account}`;
    data[key] = this.encrypt(secret);
    fs.writeFileSync(this.storagePath, JSON.stringify(data, null, 2), { mode: 0o600 });
  }

  private async getFromFile(service: string, account: string): Promise<string | null> {
    if (!fs.existsSync(this.storagePath)) return null;
    try {
        const data = JSON.parse(fs.readFileSync(this.storagePath, 'utf8'));
        const key = `${service}:${account}`;
        if (data[key]) {
            try {
                return this.decrypt(data[key]);
            } catch (e) {
                // Return null if decryption fails (e.g. machine ID changed)
                console.warn(`Failed to decrypt secret for ${account}. Machine ID may have changed.`);
                return null;
            }
        }
    } catch (e) {}
    return null;
  }

  private async deleteFromFile(service: string, account: string) {
    if (!fs.existsSync(this.storagePath)) return;
    try {
        const data = JSON.parse(fs.readFileSync(this.storagePath, 'utf8'));
        const key = `${service}:${account}`;
        if (data[key]) {
          delete data[key];
          fs.writeFileSync(this.storagePath, JSON.stringify(data, null, 2), { mode: 0o600 });
        }
    } catch (e) {}
  }
}
