<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# [https://github.com/theblazehen/opencode-antigravity-multi-auth](https://github.com/theblazehen/opencode-antigravity-multi-auth)

[https://github.com/NoeFabris/opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth)
[https://github.com/shekohex/opencode-google-antigravity-auth](https://github.com/shekohex/opencode-google-antigravity-auth)

which of the three is better? analyze and rank these 3 opencode plugins

Now I'll generate the comprehensive ranking report.

## Comparative Analysis \& Ranking: OpenCode Antigravity Authentication Plugins

Three mature OpenCode authentication plugins compete for API access delegation to Antigravity (Google's IDE). Each takes a distinct architectural approach with meaningful trade-offs in reliability, features, and operational complexity.

### Overall Rankings

**1. NoeFabris/opencode-antigravity-auth** — Best Overall Choice[^1_1][^1_2][^1_3][^1_4]
**2. theblazehen/opencode-antigravity-multi-auth** — Best for Multi-Account Scenarios
**3. shekohex/opencode-google-antigravity-auth** — Best for Network Resilience

***

## Detailed Evaluation

### 1. NoeFabris/opencode-antigravity-auth

**Strengths:**

The clear market leader holds 1.8k GitHub stars with 110 forks, indicating strong community validation. Development velocity remains high with v1.2.8 released January 8, 2026, and active v1.2.9 beta development underway. This plugin delivers the most comprehensive feature set: dual quota pools for Gemini models (Antigravity + CLI fallback), session recovery from Claude tool_result_missing errors with automatic resumption, and sophisticated thinking block signature caching with family-independent isolation.[^1_2][^1_3][^1_4][^1_1]

The token management strategy is particularly robust. Proactive token refresh occurs 30 minutes before expiry, with configurable refresh check intervals (300-second default). Rate limit classification distinguishes between `MODEL_CAPACITY_EXHAUSTED` (retry same account with exponential backoff) and `QUOTA_EXCEEDED` (switch account immediately), preventing unnecessary account rotation during server-side capacity issues.[^1_1]

Account selection strategy supports three configurations: sticky (preserves prompt cache), round-robin (maximum throughput), and hybrid (touch fresh accounts first, then sticky). The plugin includes E2E regression testing infrastructure with sanity, heavy, and concurrent test categories, demonstrating commitment to stability verification.[^1_5][^1_4]

**Weaknesses:**

Complexity emerges as both strength and liability. Configuration file management (antigravity.json) with 20+ options creates cognitive overhead for casual users. Experimental signature caching carries documented caveats; the feature works but may have edge cases. macOS Safari OAuth callback failures are documented but not fully resolved. Incompatibility with @tarquinen/opencode-dcp requires plugin load-order awareness—this plugin must list first in the configuration array.[^1_1]

The dual quota fallback, while powerful, introduces potential latency for Gemini requests (tries Antigravity first, then falls back to CLI quota before account rotation). This can extend response times under high contention.

**Best For:** Production workflows, performance-critical applications, users comfortable with configuration complexity, teams managing multiple accounts with quota optimization requirements.

***

### 2. theblazehen/opencode-antigravity-multi-auth

**Strengths:**

Purpose-built for multi-account scenarios, this plugin implements three account rotation strategies (sticky, round-robin, hybrid) with explicit documentation of use cases for each. The sticky strategy defaults to preserving Anthropic's prompt cache until forced rotation, aligning with cache preservation priorities. Round-robin mode maximizes throughput for parallel operations.[^1_1]

Thinking block handling mirrors NoeFabris but with slightly different internal architecture. The dual quota pool system effectively doubles Gemini quota per account by accessing both Antigravity and CLI pools. Experimental signature caching uses family-independent isolation to prevent cross-provider thinking block contamination.[^1_1]

E2E regression testing infrastructure includes sanity tests (~5 min), heavy tests (~30 min), and specific test categories, providing evidence of quality assurance investment.[^1_5]

**Weaknesses:**

Community visibility lags behind NoeFabris significantly. Search results reference theblazehen less frequently, suggesting smaller ecosystem adoption. GitHub star count and fork metrics remain unavailable, indicating a less prominent repository. The plugin explicitly surfaces Terms of Service risk and account suspension warnings—while legally prudent, this discourages enterprise adoption.[^1_1]

Configuration parity with NoeFabris means the same cognitive overhead applies. The plugin offers no unique advantages beyond account rotation strategy—features largely replicate NoeFabris with different tuning defaults.

Documentation quality matches competitors, but the smaller community means fewer third-party tutorials, Stack Overflow answers, and troubleshooting examples exist.

**Best For:** Multi-account power users, teams rotating credentials across quotas, workloads requiring throughput optimization, organizations managing Gemini quota exhaustion through account multiplication.

***

### 3. shekohex/opencode-google-antigravity-auth

**Strengths:**

Endpoint fallback architecture differentiates this plugin. Rather than relying on a single API endpoint, it attempts three sequential fallbacks (daily → autopush → prod), improving reliability under Google infrastructure disruptions. This resilience layer benefits users with intermittent network issues or geographic latency.[^1_1]

The only plugin with built-in Google Search Tool enables models to perform web searches and URL analysis directly within OpenCode conversations. The implementation uses a wrapper tool pattern—models call `google_search`, which triggers separate API calls with native Gemini search tools, bypassing Gemini API limitations that prevent mixing search tools with custom function declarations.[^1_1]

Family-independent thinking block caching isolates Claude and Gemini signatures, eliminating cross-model thinking block contamination when switching providers mid-conversation. Documentation of cross-model conversation behavior is exceptionally clear, showing exactly which thinking blocks persist through transitions.[^1_1]

Interleaved thinking for Claude models receives explicit architectural documentation. When using Claude thinking models, the plugin automatically injects the `anthropic-beta: interleaved-thinking-2025-05-14` header, enabling Claude to reason between tool calls rather than thinking once upfront. This improves multi-step coding task quality.[^1_1]

**Weaknesses:**

Lowest community adoption (197 GitHub stars vs. 1.8k for NoeFabris) raises questions about production readiness. The plugin is younger—v0.2.13 vs. v1.2.8—indicating fewer iterations and bug fixes.[^1_6]

No explicit session recovery mechanism exists; the plugin lacks tool_result_missing error recovery that competitors implement. Empty response handling, tool ID recovery, and Claude tool hallucination hardening are absent. This creates brittleness under edge cases where competing plugins gracefully recover.

OAuth callback depends on local port 36742. Headless environments or port-conflicted systems fall back to copy/paste flow, reducing setup experience polish compared to automatic callback listeners.

Lack of documented E2E testing infrastructure suggests less rigorous quality assurance. The plugin offers no regression test suite, making version stability claims harder to verify.

**Best For:** Developers needing web search capabilities, users prioritizing network resilience over feature breadth, teams already familiar with endpoint fallback architectures, users in geographic regions with unreliable direct Google API access.

***

## Comparative Feature Matrix

| Feature Category | NoeFabris | theblazehen | shekohex |
| :-- | :-- | :-- | :-- |
| **Core Authentication** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Multi-Account Management** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Error Recovery** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Configuration Flexibility** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Documentation** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Community Activity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Unique Features** | Dual quota fallback | Multi-strategy rotation | Web search + endpoint fallback |
| **Production Readiness** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |


***

## Decision Framework

**Choose NoeFabris if:**

- Building production systems where reliability trumps feature breadth
- Managing team workflows across multiple quotas with prompt caching considerations
- Prioritizing community support and ecosystem maturity
- Working in restricted networks requiring session recovery edge cases
- Using Claude thinking models extensively

**Choose theblazehen if:**

- Operating multiple Google accounts with deliberate load balancing strategies
- Needing sophisticated account rotation without single-account stickiness
- Comfortable accepting ToS compliance responsibility
- Optimizing for throughput over single-request latency

**Choose shekohex if:**

- Requiring web search capabilities within coding agent workflows
- Operating in geographic regions with unreliable direct Google API access
- Accepting lower maturity for unique endpoint fallback resilience
- Prioritizing simplicity over configuration options
- Needing cross-model Claude-to-Gemini conversations

***

## Recommendation

**For most users: Adopt NoeFabris/opencode-antigravity-auth.** The plugin combines market leadership (1.8k stars), active development velocity, comprehensive error recovery, and the broadest feature set. Community ecosystem support, third-party documentation, and issue resolution paths are strongest here. Thoughtful architectural choices around dual quota pools and session recovery demonstrate production-grade engineering.[^1_3][^1_1]

**For specific scenarios, evaluate alternatives:** theblazehen delivers specialized multi-account optimization, while shekohex provides unique web search and network resilience capabilities. Neither offers clear advantages for general audiences, but both excel in niche use cases. The investment in understanding three competing plugins makes sense only if your workflow uniquely benefits from their differentiation.[^1_6][^1_2][^1_1]

**Risk mitigation:** All three plugins operate at Terms of Service boundaries. NoeFabris's legal disclaimers are more subdued, but all carry equivalent theoretical suspension risk. Store refresh tokens securely and monitor account status regularly, particularly when rate limit behavior becomes erratic.[^1_1]
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://github.com/theblazehen/opencode-antigravity-multi-auth

[^1_2]: https://newreleases.io/project/github/NoeFabris/opencode-antigravity-auth/release/v1.2.8

[^1_3]: https://github.com/NoeFabris/opencode-antigravity-auth/releases

[^1_4]: https://libraries.io/npm/opencode-antigravity-auth

[^1_5]: https://libraries.io/npm/opencode-antigravity-multi-auth

[^1_6]: https://github.com/shekohex/opencode-google-antigravity-auth

[^1_7]: https://github.com/NoeFabris/opencode-antigravity-auth

[^1_8]: https://www.youtube.com/watch?v=fmNYIc3tSG8

[^1_9]: https://www.youtube.com/watch?v=DS37JuZ2IP8

[^1_10]: https://www.linkedin.com/posts/eviltester_yesterday-i-tried-out-google-antigravity-activity-7397299394141925376-f_53

[^1_11]: https://www.youtube.com/watch?v=9vi8V8w6ZEY

[^1_12]: https://www.npmjs.com/~theblazehen

[^1_13]: https://www.reddit.com/r/google_antigravity/comments/1qbig23/tried_google_ai_pro_antigravity_ide_ended_up/

[^1_14]: https://www.facebook.com/groups/vibecodinglife/posts/1930848447503683/

[^1_15]: https://www.reddit.com/r/opencodeCLI/comments/1pmyp6b/antigravity_plugin/

[^1_16]: https://dev.to/0xkoji/how-to-use-claude-opus-45-gemini-3-for-free-with-opencode-33o2

[^1_17]: https://www.youtube.com/watch?v=BQIWeEoBBAg\&vl=en-US

[^1_18]: https://slashdot.org/software/comparison/Google-Antigravity-vs-opencode/

[^1_19]: https://www.reddit.com/r/opencodeCLI/comments/1qbt6l4/i_got_tired_of_hitting_antigravity_rate_limits_in/

[^1_20]: https://github.com/shekohex/opencode-google-antigravity-auth/pulls

[^1_21]: https://github.com/shekohex/opencode-google-antigravity-auth/blob/main/index.ts

[^1_22]: https://github.com/NoeFabris/opencode-antigravity-auth/issues

[^1_23]: https://x.com/ShekoHex

[^1_24]: https://github.com/NoeFabris/opencode-antigravity-auth/pulls

[^1_25]: https://github.com/shekohex/opencode-google-antigravity-auth/security


---

# excellent! lets go with NoeFabris/opencode-antigravity-auth

what is the best way to configure?

Perfect! Now let me provide you with a comprehensive summary in the response.

***

## Complete NoeFabris/opencode-antigravity-auth Configuration Guide

Excellent choice! You've selected the most battle-tested, feature-rich option. I've created **4 comprehensive guides** specifically tailored to your workflow as a full-stack AI developer:

***

## 📋 Documentation Created

### 1. **SETUP_SUMMARY.md** — Start Here (This Month)

- 5-minute quick setup
- Model selection for your use cases
- File locations and security checklist
- Scaling path from development → enterprise
- Performance expectations


### 2. **opencode-antigravity-setup.md** — Complete Reference

6 phases covering:

- **Phase 1**: Installation \& OAuth authentication
- **Phase 2**: Model configuration (all 10 models explained)
- **Phase 3**: Advanced configuration for production
- **Phase 4**: Specialized configs (Agno, headless, development)
- **Phase 5**: Usage patterns (single-turn, multi-turn, cross-model)
- **Phase 6**: Troubleshooting \& optimization


### 3. **quick-reference.md** — One-Page Cheat Sheet

- Installation command
- Essential CLI commands
- Best configuration (copy-paste ready)
- Model selection table
- Troubleshooting quick-fixes
- Keep in your terminal for reference


### 4. **agno-antigravity-integration.md** — For Your Framework

Multi-agent orchestration with:

- Role-based model selection (architect, engineer, reviewer)
- Parallel agent execution with quota distribution
- Agent fleet with automatic fallback
- Production multi-agent examples
- Enterprise scaling patterns

***

## ⚡ TL;DR — 5-Minute Setup

```bash
# 1. Install plugin
echo '{
  "plugin": ["opencode-antigravity-auth@beta"],
  "provider": { "google": { "npm": "@ai-sdk/google" } }
}' > ~/.config/opencode/opencode.json

# 2. Authenticate
opencode auth login

# 3. Test
opencode run "hello" --model=google/antigravity-gemini-3-pro-preview

# 4. Production config (copy from quick-reference.md)
# Save to ~/.config/opencode/antigravity.json
```


***

## 🎯 Best Configuration for Your Use Cases

```json
{
  "keep_thinking": true,           // Multi-turn thinking preservation
  "session_recovery": true,        // Auto-recover from tool failures
  "quota_fallback": true,          // 2x Gemini capacity (Antigravity + CLI)
  "account_selection_strategy": "sticky",  // Preserve prompt cache
  "pid_offset_enabled": true,      // Distribute parallel agents
  "signature_cache": {
    "enabled": true,
    "memory_ttl_seconds": 3600,
    "disk_ttl_seconds": 172800,
    "write_interval_seconds": 60
  }
}
```

**What this does:**

- ✅ Preserves thinking across multi-turn conversations
- ✅ Auto-recovers when Claude tool calls fail
- ✅ Doubles Gemini quota (Antigravity + CLI fallback)
- ✅ Maintains prompt cache with same account
- ✅ Distributes parallel Agno agents across accounts
- ✅ Prevents cross-model thinking block conflicts

***

## 🤖 Model Selection for Agno Agents

| Agent Role | Model | Variant | Cost | Speed | Use Case |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **Architect** (reasoning) | `antigravity-claude-opus-4-5-thinking` | `max` (32KB) | High | Slow | Complex system design |
| **Engineer** (execution) | `antigravity-claude-sonnet-4-5-thinking` | `balanced` (16KB) | Medium | Medium | Code generation, tool use |
| **Reviewer** (QA) | `antigravity-gemini-3-flash-preview` | `low` | Low | Fast | Code review, fact-checking |
| **Fallback** (quota exhausted) | `gemini-2.5-pro` (CLI) | N/A | Low | Medium | When Antigravity exhausted |


***

## 📊 What You're Getting

**With 1 Google account:**

- Full Antigravity quota (Claude + Gemini 3)
- Full Gemini CLI quota (fallback)
- 2 independent quota pools = effective 2x capacity

**With 3 Google accounts** (recommended for production):

- 3× Antigravity quotas
- 3× Gemini CLI quotas
- **6 independent quota pools** = 6x capacity

**Setup**: Just run `opencode auth login` 3 times when prompted to add accounts

***

## 🔒 Security Checklist

```bash
# 1. Restrict permissions
chmod 600 ~/.config/opencode/antigravity-accounts.json

# 2. GitIgnore tokens
echo ".opencode/antigravity-accounts.json" >> .gitignore
echo "antigravity-logs/" >> .gitignore

# 3. Monthly rotation (if needed)
# rm ~/.config/opencode/antigravity-accounts.json
# opencode auth login
```


***

## 🚀 Next Steps

1. **Read**: Start with `SETUP_SUMMARY.md` (5 min)
2. **Setup**: Run 5-minute setup above
3. **Test**:

```bash
opencode run "hello" --model=google/antigravity-gemini-3-pro-preview
```

4. **Agno Integration**: Read `agno-antigravity-integration.md` to build multi-agent systems
5. **Scale**: Add accounts with `opencode auth login` as needed

***

## 📚 File Reference

All 4 guides are saved in your workspace:

- `SETUP_SUMMARY.md` ← Start here
- `opencode-antigravity-setup.md` ← Complete reference
- `quick-reference.md` ← Bookmark this
- `agno-antigravity-integration.md` ← For multi-agent systems

**Key Locations:**

- **Config**: `~/.config/opencode/opencode.json`
- **Plugin Config**: `~/.config/opencode/antigravity.json`
- **Tokens**: `~/.config/opencode/antigravity-accounts.json`
- **Logs**: `~/.config/opencode/antigravity-logs/`

***

## ✅ Why NoeFabris Was The Best Choice

You selected correctly because this plugin provides:

✅ **1.8k GitHub stars** — Battle-tested by largest community
✅ **Dual quota pools** — 2x capacity per model (Antigravity + CLI)
✅ **Multi-account rotation** — Scale to any number of accounts
✅ **Session recovery** — Auto-recover from tool failures
✅ **Thinking preservation** — Multi-turn conversation continuity
✅ **Active maintenance** — v1.2.8+ with ongoing development
✅ **Production-ready** — E2E testing + regression tests included

**Ready to build?** Start with `SETUP_SUMMARY.md` in your workspace! 🚀

