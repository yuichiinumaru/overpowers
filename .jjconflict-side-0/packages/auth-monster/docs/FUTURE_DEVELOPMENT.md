# Future Development Roadmap

This roadmap is derived from a deep analysis of reference repositories (`CLIProxyAPI`, `ProxyPilot`, `CCS`, `Quotio`, `CodMate`, etc.) and aims to elevate `opencode-auth-monster` to a best-in-class authentication and proxy solution.

## Phase 1: Foundation Hardening & Security (High Priority)

These tasks address core stability and security gaps identified when comparing against `CLIProxyAPI` and `ProxyPilot`.

- [ ] **Secure Secret Storage**: Move away from plain JSON files for token storage. Implement OS-level keychain integration (Keytar or similar) like `ProxyPilot` and `CCS` do for production environments.
- [ ] **Encryption at Rest**: If file storage must be used, encrypt the `auth-monster-accounts.json` file using a user-provided passphrase or machine-specific key.
- [ ] **Token Refresh Robustness**: Implement a dedicated `TokenRefresher` service that runs in the background (or on-demand with mutex locks) to prevent race conditions during parallel requests. `CLIProxyAPI` has a sophisticated `refresh_registry`.
- [ ] **Socket/Pipe Transport**: Support named pipes (Windows) or Unix domain sockets for local communication to avoid TCP port conflicts and improve security (seen in `ProxyPilot`).

## Phase 2: Provider Expansion & Protocol Support

Expand the ecosystem to support more AI providers and communication protocols, matching the breadth of `CLIProxyAPI`.

- [ ] **Azure OpenAI / Foundry Support**: Add an `AzureProvider` to support enterprise deployments (seen in `CCS`).
- [ ] **Grok / xAI Support**: Add `GrokProvider`.
- [ ] **DeepSeek Native**: Support DeepSeek API directly (not just via Qwen proxy).
- [ ] **SSE & gRPC Handling**: Ensure the core proxy (`https-tunnel-proxy`) can gracefully handle Server-Sent Events (SSE) and potentially gRPC for newer model protocols (Windsurf uses gRPC).
- [ ] **Custom Provider Config**: Allow users to define "Generic OpenAI-compatible" providers via config, so they can add local LLMs (Ollama, LM Studio) without code changes.

## Phase 3: Advanced Traffic Management

Implement sophisticated traffic shaping and analysis features found in `CCS` and `ProxyPilot`.

- [ ] **Cost Tracking & Estimation**: Implement a `CostEstimator` that tracks input/output tokens and calculates estimated spend based on known model pricing (seen in `CodMate` and `CCS`).
- [ ] **Request/Response Redaction**: Add a middleware layer to redact sensitive information (API keys, PII) from logs and debug outputs.
- [ ] **Session Replay/History**: Store request history (metadata only or full content option) to allow users to review past interactions or "replay" failed requests.
- [ ] **Rate Limit "Parking"**: Instead of just failing or rotating, implement a "parking" queue that holds requests until a specific account's rate limit resets (if it's the only one available).

## Phase 4: UI/UX & Management Interfaces

Improve the user experience beyond the CLI, taking inspiration from `Quotio` and `Proxypal`.

- [ ] **TUI Dashboard**: Expand the `quota` command into a full-screen TUI (using `ink` or `blessed`) that shows real-time request logs, health status, and active connections.
- [ ] **System Tray Utility**: Create a lightweight system tray app (Electron/Tauri) that shows current active provider and allows quick switching (like `Quotio`).
- [ ] **Web Admin Panel**: Embed a small web server (like `CLIProxyAPI Management Center`) to visualize configuration and logs in a browser.

## Phase 5: Specialized Workflows

Integrate "agentic" features found in `Splitrail` and `CCS`.

- [ ] **"Dialectics" Mode**: A mode where the proxy splits a prompt into two, sends it to different models (e.g., Claude and Gemini), and then synthesizes the result (inspired by `CodMate`).
- [ ] **Git Integration**: Add a `pre-commit` hook generator that uses the configured AI to generate commit messages automatically.
- [ ] **Project Review Agent**: A dedicated workflow that ingests `git diff` and provides a code review summary using the best available reasoning model.
- [ ] **Reasoning Enforcer**: Middleware that forcibly injects "thinking" instructions into prompts for models that support it, ensuring better output quality.

## Optimal Development Order

1.  **Secure Storage**: Critical for user trust.
2.  **Custom Provider Config**: High value for flexibility (Ollama support).
3.  **Cost Tracking**: Essential for users managing multiple paid accounts.
4.  **TUI Dashboard**: "Wow" factor and immediate usability improvement.
5.  **Azure/Enterprise Support**: Expands user base to corporate environments.
