- **Phase: MCP Edge Cases Resolution (Memcord, NotebookLM & Playwright)**
  - Replaced `"uvx"` with `"uv"` and explicitly used `"command": "{env:UV_PATH}"` or `"command": "uv"` alongside args like `["--directory", "~/.config/opencode/mcp/memcord", "run", "memcord", "server"]` across `mcp-*.json`, `opencode-example.json`, and `mcp-codex.toml`.
  - Investigated `packages/memcord` to understand proper run setups, confirming UV was required since Memcord MCP runs as a local Python script instead of an NPX global.
  - Ran a batch script to remove the `"run"` CLI parameter for `notebooklm` configs inside `scripts/templates/`, as `notebooklm-mcp` does not recognize it.
  - Handled the `playwright_browser` limit of 100 tools issue in Antigravity: removed it from Antigravity's template since Antigravity has native browser subagent integration.
- **Phase: API Key Rotation and Verification**
  - Prompted to write a testing script (`scripts/test-api-keys.py`) to systematically validate and ping keys from `.env` across integrated LLM and MCP providers.
  - User instructed purging revoked unused tokens (OpenAI, Anthropic, xAI, Groq, OpenRouter, Cerebras) from both `.env` and `userenv`.
  - Upgraded the test scripts (`scripts/install-mcps.sh` and `scripts/test-mcps.sh`) to enforce API key and AI MCP integration tests as a final initialization validation step.
- **Phase: Post-installation Testing & Cleanup**
  - Manually validated execution and connectivity with CLI tests (`opencode mcp list`, `kilo mcp list`, `gemini mcp list`).
  - Executed a successful series of single-tool tests on surviving Antigravity MCPs:
    * `Serena` tested correctly (prompted for project context).
    * `Memcord` responded with ping/pong successfully.
    * `Context7` fetched React documentation accurately.
    * `Stitch` resolved projects array (empty array since none existed on the account).
    * `Genkit` fetched list successfully (no local runtime found).
    * `Hyperbrowser` / `Vibe Check` still needed minor troubleshooting or API key fixes.
- **Phase: Exploring NotebookLM Use Cases**
  - Removed outdated `nlm-skill` and focused on the surviving `notebooklm` skill.
  - The AI generated 5 powerful tactical strategies and brainstormed 3 new sub-workflows leveraging CLI functionality (`nlm notebook create`, `nlm source add`) to overcome the context limits, including using `gitingest` for codebase mapping and building a Youtube-to-skill pipeline.
