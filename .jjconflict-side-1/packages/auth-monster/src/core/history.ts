import fs from 'fs';
import path from 'path';
import { Redactor } from './redactor';

export interface HistoryEntry {
  timestamp: number;
  model: string;
  provider: string;
  accountId: string;
  tokens?: {
    input: number;
    output: number;
  };
  cost?: number;
  request: any;
  response: any;
  durationMs: number;
  success: boolean;
  error?: string;
}

export class HistoryManager {
  private filePath: string;

  constructor(storagePath: string) {
    this.filePath = path.join(storagePath, 'history.jsonl');
  }

  async addEntry(entry: Omit<HistoryEntry, 'timestamp'>): Promise<void> {
    const fullEntry: HistoryEntry = {
      timestamp: Date.now(),
      ...entry
    };

    const redactedEntry = Redactor.redact(fullEntry);
    const line = JSON.stringify(redactedEntry) + '\n';

    try {
      // Ensure directory exists
      const dir = path.dirname(this.filePath);
      if (!fs.existsSync(dir)) {
        await fs.promises.mkdir(dir, { recursive: true });
      }

      await fs.promises.appendFile(this.filePath, line, 'utf8');
    } catch (error) {
      console.error('[HistoryManager] Failed to write history:', error);
    }
  }

  // Basic query support (e.g. for replay)
  async getRecentEntries(limit: number = 50): Promise<HistoryEntry[]> {
    try {
        if (!fs.existsSync(this.filePath)) return [];
        const content = await fs.promises.readFile(this.filePath, 'utf8');
        const lines = content.trim().split('\n');
        return lines
            .slice(-limit)
            .map(line => {
                try {
                    return JSON.parse(line);
                } catch {
                    return null;
                }
            })
            .filter((e): e is HistoryEntry => e !== null)
            .reverse(); // Newest first
    } catch (error) {
        console.error('[HistoryManager] Failed to read history:', error);
        return [];
    }
  }
}
