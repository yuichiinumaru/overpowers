import { execSync } from 'child_process';
import { ManagedAccount } from '../core/types';

/**
 * Syncs accounts to GitHub secrets for a target repository.
 * Standardizes the secret name as OPENCODE_MONSTER_ACCOUNTS.
 * 
 * @param repo Repository in 'owner/repo' format.
 * @param accounts List of managed accounts to sync.
 * @param token Optional GitHub PAT to use for authentication.
 */
export async function syncToGitHub(repo: string, accounts: ManagedAccount[], token?: string): Promise<void> {
  try {
    // Check if gh CLI is installed
    try {
      execSync('gh --version', { stdio: 'ignore' });
    } catch (e) {
      throw new Error('GitHub CLI (gh) is not installed or not in PATH. Please install it from https://cli.github.com/');
    }

    const secretName = 'OPENCODE_MONSTER_ACCOUNTS';
    // Clean accounts for storage: remove transient health/rotation fields to keep it clean
    const accountsToSync = accounts.map(acc => ({
      id: acc.id,
      email: acc.email,
      provider: acc.provider,
      tokens: acc.tokens,
      apiKey: acc.apiKey,
      metadata: acc.metadata,
      isHealthy: true, // Reset health on sync
      healthScore: 100
    }));

    const jsonData = JSON.stringify(accountsToSync, null, 2);

    // Use gh secret set with stdin to handle potentially large data safely
    const command = `gh secret set ${secretName} --repo ${repo}`;
    
    console.log(`Syncing ${accounts.length} accounts to GitHub secret ${secretName} in ${repo}...`);
    
    const env = { ...process.env };
    if (token) {
        env.GITHUB_TOKEN = token;
    }

    execSync(command, { 
      input: jsonData, 
      stdio: ['pipe', 'inherit', 'inherit'],
      encoding: 'utf8',
      env
    });
    
    console.log(`Successfully synced!`);
  } catch (error: any) {
    if (error.message.includes('gh --version')) {
        // Handled above but just in case
    }
    throw error;
  }
}
