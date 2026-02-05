# Analysis Findings

## ProxyPilot
*   **Kiro (AWS CodeWhisperer) Support**: Found extensive support for "Kiro" (AWS CodeWhisperer) in `internal/auth/kiro`.
    *   It supports `LoginWithBuilderID` (AWS Builder ID) and `LoginWithGoogle`/`LoginWithGitHub` (via Kiro's social auth).
    *   Endpoints: `https://prod.us-east-1.auth.desktop.kiro.dev`, `https://codewhisperer.us-east-1.amazonaws.com`.
    *   Use of `~/.aws/sso/cache/kiro-auth-token.json`.
*   **Minimax & Zhipu AI**: API Key based.
*   **Antigravity**: Google OAuth with specific scopes + onboarding dance.
*   **Amazon Q CLI**: "Import from CLI" (`q login` first).
*   **Prompt Caching**: Implements prompt caching logic (`internal/cache`).
*   **System Tray**: Has a system tray app (Golang).

## ZeroLimit
*   Seems to be a frontend/Tauri app.
*   Likely relies on `CLIProxyAPI` or similar for the backend logic.

## Desktop Apps (CodMate, Quotio, ProxyPal, VibeProxy)
*   **CodMate**: Uses macOS Keychain for Claude Code credentials.
    *   Service Name: `Claude Code-credentials-<hash>` where hash is first 8 chars of SHA256 of `~/.claude`.
    *   Account Name: `NSUserName()` (current user).
*   **VibeProxy**: Native macOS app.

## Proposed Integrations
1.  **Kiro Provider**: DONE.
2.  **Amazon Q / Kiro Import**: DONE.
3.  **Zhipu Provider**: Implement simple API Key provider.
4.  **Claude Keychain Extraction**: Implement logic to find `Claude Code-credentials-*` in Keychain.
5.  **Minimax Provider**: Implement simple API Key provider.
6.  **Antigravity**: Add enum and stub, maybe full impl later.
