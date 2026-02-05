# Memory: Final Round Integration - Deep Dive Analysis

This document synthesizes findings from the final deep dive into the following repositories:
- `cursor-opencode-auth`
- `opencode-auth-sync`
- `opencode-gemini-auth-swap`
- `yet-another-opencode-cursor-auth`
- `Indosaram-opencode-kiro-auth`

## 1. Token Extraction Logic

### macOS Keychain (Native Zero-Dependency)
Found in `cursor-opencode-auth`, this approach avoids heavy dependencies like `keytar`.
```javascript
import { execSync } from "child_process";

function getCursorToken() {
  try {
    return execSync('security find-generic-password -s "cursor-access-token" -w', {
      encoding: "utf8",
      stdio: ["pipe", "pipe", "pipe"],
    }).trim();
  } catch (e) {
    throw new Error("Could not retrieve token from macOS Keychain");
  }
}
```

### SQLite Extraction (Windsurf/Cursor)
Extraction from local application state databases.
```javascript
// Windsurf SQLite extraction
const statePath = "~/Library/Application Support/Windsurf/User/globalStorage/state.vscdb";
const query = "SELECT value FROM ItemTable WHERE key = 'windsurfAuthStatus';";
const cmd = `sqlite3 "${statePath}" "${query}"`;
const token = execSync(cmd, { encoding: 'utf8' }).trim();
```

## 2. Profile Promotion (Index 0 Manipulation)
Strategy for maintaining compatibility with tools that default to the first entry in an accounts list. Found in `opencode-gemini-auth-swap`.

```typescript
/**
 * Promotes a specific account to index 0 to ensure compatibility
 */
function promoteAccount(refreshToken: string, storagePath: string) {
    const data = JSON.parse(readFileSync(storagePath, 'utf8'));
    
    // Find account
    const idx = data.accounts.findIndex(a => a.refreshToken === refreshToken);
    let account;
    
    if (idx !== -1) {
        // Remove from current position
        [account] = data.accounts.splice(idx, 1);
    } else {
        // Create new if missing
        account = { refreshToken, addedAt: Date.now() };
    }
    
    // Unshift to position 0
    account.lastUsed = Date.now();
    data.accounts.unshift(account);
    data.activeIndex = 0;
    
    // Update family-specific indices if they exist
    if (data.activeIndexByFamily) {
        Object.keys(data.activeIndexByFamily).forEach(f => {
            data.activeIndexByFamily[f] = 0;
        });
    }
    
    writeFileSync(storagePath, JSON.stringify(data, null, 2));
}
```

## 3. Multi-instance Lock Strategy
Beyond basic file locking, using `proper-lockfile` to handle concurrency and stale locks.

```typescript
import lockfile from "proper-lockfile";

const LOCK_OPTIONS = {
  stale: 10000,     // Consider lock stale after 10s
  retries: {
    retries: 5,     // Retry 5 times
    minTimeout: 100,
    maxTimeout: 1000,
    factor: 2,
  },
};

async function safeAtomicUpdate(path: string, updateFn: (data: any) => any) {
  // Ensure file exists for lockfile to work
  if (!existsSync(path)) writeFileSync(path, '{}');
  
  let release;
  try {
    release = await lockfile.lock(path, LOCK_OPTIONS);
    const data = JSON.parse(readFileSync(path, 'utf8'));
    const updated = await updateFn(data);
    
    // Atomic write via rename
    const tempPath = `${path}.${randomBytes(4).toString('hex')}.tmp`;
    writeFileSync(tempPath, JSON.stringify(updated, null, 2));
    renameSync(tempPath, path);
  } finally {
    if (release) await release();
  }
}
```

## 4. Multi-Instance PID Offset
Used to prevent parallel collisions by initializing cursors based on the process ID.

```javascript
function getRotationCursor(accountCount, strategy = 'round-robin') {
    if (process.env.OPENCODE_MONSTER_PID_OFFSET === 'true') {
        // Start from a different point based on PID
        return process.pid % accountCount;
    }
    return 0;
}
```

## 5. Summary Table

| Feature | Best Reference Repo | Key Technique |
| :--- | :--- | :--- |
| **Keychain** | `cursor-opencode-auth` | Native `security` CLI wrapper |
| **SQLite** | `opencode-windsurf-auth` | Direct SQL query on `ItemTable` |
| **Promotion** | `opencode-gemini-auth-swap` | `unshift` + `activeIndex = 0` |
| **Locking** | `opencode-antigravity-auth` | `proper-lockfile` + Atomic Rename |
| **Sync** | `opencode-auth-sync` | `chokidar` + `gh secret set` |
