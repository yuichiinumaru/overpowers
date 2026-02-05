import fs from 'fs';
import path from 'path';
import { xdgConfig } from 'xdg-basedir';
import { AuthMonsterConfig, AuthMonsterConfigSchema, AuthProvider } from './types';

export class ConfigManager {
  private configPath: string;
  private configDir: string;

  constructor(customPath?: string) {
    this.configDir = customPath || path.join(xdgConfig || '', 'opencode');
    if (!fs.existsSync(this.configDir)) {
      fs.mkdirSync(this.configDir, { recursive: true });
    }
    this.configPath = path.join(this.configDir, 'auth-monster-config.json');
  }

  getConfigDir(): string {
    return this.configDir;
  }

  loadConfig(): AuthMonsterConfig {
    if (!fs.existsSync(this.configPath)) {
      return AuthMonsterConfigSchema.parse({});
    }

    try {
      const data = fs.readFileSync(this.configPath, 'utf8');
      const parsed = JSON.parse(data);
      return AuthMonsterConfigSchema.parse(parsed);
    } catch (error) {
      console.error('Failed to load config, using defaults:', error);
      return AuthMonsterConfigSchema.parse({});
    }
  }

  saveConfig(config: AuthMonsterConfig): void {
    const dir = path.dirname(this.configPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    fs.writeFileSync(this.configPath, JSON.stringify(config, null, 2), 'utf8');
  }

  setActiveProvider(provider: AuthProvider): void {
    const config = this.loadConfig();
    config.active = provider;
    this.saveConfig(config);
  }
}
