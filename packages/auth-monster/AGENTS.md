# AGENTS.md — WORKSPACE FEDERATION CONSTITUTION

This workspace contains multiple repositories in which our team is working in.
- You must focus only on one project at a time, depending on the user request. 
- However, since most of them are designed to work together, you must carefully assess the tech stack of each before commiting to changes. Do not refrain from askin the user about this.
- Use standard organization and filename convention defaults across all repos, as best as possible, using Forge methodology. 
- Write down to this file (this AGENTS.md) all conventions stablished across all repos, in the end of the file.
- Each project has it's own documentation and AGENTS.md - which refer to that project's specific particularities.

---

## 7. ESTABLISHED WORKSPACE CONVENTIONS (Federated)

| Category | Convention | Description |
| :--- | :--- | :--- |
| **OAuth** | Port `1455` | Default port for local OAuth callback servers across all auth plugins. |
| **Spoofing** | String Replacement | Replace `OpenCode` with `Claude Code` in system prompts for Anthropic providers to bypass server-side blocks. |
| **Tooling** | Prefixing | Use `mcp_` or `oc_` prefixes for tool names when interacting with restrictive backends. |
| **Config** | `auth-monster-config.json` | Global configuration stored in `~/.config/opencode/auth-monster-config.json`. |
| **Rotation** | Strategy Selection | Standard rotation strategies: `sticky`, `round-robin`, `hybrid` (Score + Tokens). |
| **Rotation** | PID Offset | Use `process.pid` to initialize rotation cursors to prevent parallel collision. |
| **Stability** | Rate Limit Dedup | 2s deduplication window for concurrent 429 errors. |
| **Stability** | Thinking Warmup | Lightweight background request to "wake up" reasoning models when switching accounts. |
| **Load Balancing** | Unified Model Hub | Routes generic model names to the best (Provider, Account) pair based on health and quota. |
| **Security** | Keychain/Secret Service | Prefer OS-level secret storage over plain-text files when possible. |
| **Sync** | GitHub Secrets | `opencode-monster sync` uploads accounts to `OPENCODE_MONSTER_ACCOUNTS` GH secret. |
| **Discovery** | `TokenExtractor` | Unified mechanism for extracting local tokens from Cursor (Keychain) and Windsurf (SQLite). |
| **Proxy** | `ProxyManager` | Global proxy support via `proxyFetch`, respecting `HTTP_PROXY` env and global config. |
| **Fallback** | Model Chain | Ordered fallback list for models, configurable via `opencode-monster fallback`. |
