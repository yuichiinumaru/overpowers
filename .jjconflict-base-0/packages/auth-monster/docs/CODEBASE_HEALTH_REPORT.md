# Codebase Health & Analysis Report

**Date:** 2023-10-27
**Subject:** OpenCode Auth Monster - Deep Architectural Analysis

## 1. Architectural Alignment
The codebase exhibits a high degree of alignment with the documented architecture in `README.md` and `AGENTS.md`.
- **Core Loop:** The `UnifiedModelHub` -> `AccountRotator` -> `Provider` flow is implemented exactly as described.
- **Conventions:** `AGENTS.md` conventions (Port 1455, mcp_ prefix, etc.) are strictly enforced in the code (e.g., `src/providers/anthropic/transform.ts`).
- **Modularity:** Providers are well-isolated in `src/providers/`, sharing a common interface implicitly (though strict TypeScript interface enforcement could be tighter).

## 2. Key Components Analysis

### Core Logic
- **UnifiedModelHub (`src/core/hub.ts`)**: Acts as an effective router. The "Mark VI" models are hardcoded, which might require frequent updates. *Recommendation: Move mappings to an external JSON config.*
- **AccountRotator (`src/core/rotation.ts`)**: robust implementation of `sticky`, `round-robin`, and `hybrid` strategies. The PID-offset logic is a clever solution for stateless parallelism.
- **QuotaManager (`src/core/quota-manager.ts`)**: Implements necessary pre-flight checks. However, it relies heavily on local state and explicit `account.quota` updates. It lacks a centralized/shared state store (like Redis), meaning quota awareness is process-local unless persisted to disk frequently.

### Security
- **SecretStorage (`src/core/secret-storage.ts`)**:
    - **Strength**: Uses macOS Keychain (`security` CLI) when available.
    - **Weakness**: Fallback mechanism is a simple JSON file with Base64 obfuscation (`auth-monster-secrets.json`). This is not encryption and offers minimal protection on non-macOS systems (Linux/Windows). *Critical Technical Debt.*

### Resilience
- **Rate Limit Handling**: The "parking" mechanism (waiting up to 60s) and deduplication of 429 errors are proactive stability features.
- **Fallbacks**: The `resolveModelChain` logic provides a robust safety net.

## 3. Discrepancies & Technical Debt

| Area | Discrepancy / Debt | Severity | Suggestion |
| :--- | :--- | :--- | :--- |
| **Windsurf Integration** | `AuthMonster.handleWindsurfRequest` is a special case in the main request loop, bypassing the standard `proxyFetch` pattern. | Medium | Refactor Windsurf into a standard `Provider` that handles its own transport logic internally. |
| **Proxy Support** | `src/core/proxy.ts` notes complexity with Node's native `fetch` vs. `node-fetch` agents. SOCKS support might be flaky on native `fetch`. | Low | Standardize on `undici` or `node-fetch` explicitly to ensure consistent proxy behavior. |
| **Model Hardcoding** | `UnifiedModelHub` contains a large list of hardcoded model mappings. | Low | Extract to `models.json` or `config.ts` for easier updates without code changes. |
| **Tests** | Tests in `src/test/` seem minimal for such a complex routing system. | Medium | Increase unit coverage for `AccountRotator` edge cases. |

## 4. Conclusion
The system is well-structured for its purpose: a high-availability, multi-tenant authentication proxy. The core logic is sound, but the persistence layer (secrets) on non-macOS platforms needs immediate attention for a production environment. The "Cognitive Context" is now fully captured in `docs/SYSTEM_KNOWLEDGE_GRAPH.md`.
