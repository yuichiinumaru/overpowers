# NoeFabris/opencode-antigravity-auth — Complete Setup Guide for AI Developers

**Last Updated**: January 17, 2026  
**Plugin Version**: v1.2.8+ (beta)  
**Target**: Full-stack AI developers, Agno framework users, multi-agent system builders

---

## Phase 1: Installation & Authentication

### Step 1.1: Install the Plugin

Edit your OpenCode configuration file:

**Linux/macOS:**
```bash
~/.config/opencode/opencode.json
```

**Windows:**
```
%APPDATA%\opencode\opencode.json
```

Add the plugin to your configuration:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-antigravity-auth@beta"],
  "provider": {
    "google": {
      "npm": "@ai-sdk/google"
    }
  }
}
```

### Step 1.2: Authenticate with Google OAuth

```bash
opencode auth login
```

This launches a browser window. Sign in with your Google account. The plugin automatically:
- Generates OAuth refresh tokens
- Stores them securely in `~/.config/opencode/antigravity-accounts.json`
- Sets up proactive token refresh (30 minutes before expiry)

**Troubleshooting macOS Safari:**
If Safari shows "Safari can't open the page," use Chrome or Firefox instead. Copy the auth URL from terminal output and paste into the other browser.

### Step 1.3: Verify Installation

```bash
opencode run "test" --model=google/antigravity-gemini-3-pro-preview
```

Expected output shows Gemini 3 Pro response with your Google account email in debug logs.

---

## Phase 2: Model Configuration

### Step 2.1: Add All Models to opencode.json

This gives you access to both Antigravity quota (Claude, Gemini 3) and Gemini CLI quota:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-antigravity-auth@beta"],
  "provider": {
    "google": {
      "npm": "@ai-sdk/google",
      "models": {
        "antigravity-gemini-3-pro-preview": {
          "name": "Gemini 3 Pro (Antigravity)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingLevel": "low" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-gemini-3-flash-preview": {
          "name": "Gemini 3 Flash (Antigravity)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "minimal": { "thinkingLevel": "minimal" },
            "low": { "thinkingLevel": "low" },
            "medium": { "thinkingLevel": "medium" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-claude-sonnet-4-5": {
          "name": "Claude Sonnet 4.5 (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "antigravity-claude-sonnet-4-5-thinking": {
          "name": "Claude Sonnet 4.5 Thinking (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingConfig": { "thinkingBudget": 8192 } },
            "medium": { "thinkingConfig": { "thinkingBudget": 16384 } },
            "max": { "thinkingConfig": { "thinkingBudget": 32768 } }
          }
        },
        "antigravity-claude-opus-4-5-thinking": {
          "name": "Claude Opus 4.5 Thinking (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingConfig": { "thinkingBudget": 8192 } },
            "medium": { "thinkingConfig": { "thinkingBudget": 16384 } },
            "max": { "thinkingConfig": { "thinkingBudget": 32768 } }
          }
        },
        "gemini-2.5-flash": {
          "name": "Gemini 2.5 Flash (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-2.5-pro": {
          "name": "Gemini 2.5 Pro (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3-flash-preview": {
          "name": "Gemini 3 Flash Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3-pro-preview": {
          "name": "Gemini 3 Pro Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        }
      }
    }
  }
}
```

### Step 2.2: Model Selection Guide

| Use Case | Model | Variant | Why |
|----------|-------|---------|-----|
| **Complex reasoning, code generation** | `antigravity-claude-opus-4-5-thinking` | `max` | Opus thinking provides deepest reasoning for complex tasks |
| **Balanced reasoning + speed** | `antigravity-claude-sonnet-4-5-thinking` | `medium` or `max` | Great for multi-step agent workflows |
| **Fast inference, quick iterations** | `antigravity-gemini-3-flash-preview` | `low` or `medium` | Lower latency for rapid prototyping |
| **High-quality long-context processing** | `antigravity-gemini-3-pro-preview` | `high` | 1M token context ideal for large codebases |
| **Free quota overflow (when Antigravity rate-limited)** | `gemini-2.5-pro` or `gemini-3-pro-preview` | N/A | Dual quota pools extend your capacity |

---

## Phase 3: Advanced Configuration

### Step 3.1: Create antigravity.json for Production Workflows

**Location**: `~/.config/opencode/antigravity.json` (global) or `.opencode/antigravity.json` (project-specific)

**Production-Optimized Configuration:**

```json
{
  "$schema": "https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/assets/antigravity.schema.json",
  "quiet_mode": false,
  "debug": false,
  "auto_update": true,
  "keep_thinking": true,
  
  "session_recovery": true,
  "auto_resume": true,
  "resume_text": "continue",
  
  "empty_response_max_attempts": 4,
  "empty_response_retry_delay_ms": 2000,
  "tool_id_recovery": true,
  "claude_tool_hardening": true,
  
  "proactive_token_refresh": true,
  "proactive_refresh_buffer_seconds": 1800,
  "proactive_refresh_check_interval_seconds": 300,
  
  "max_rate_limit_wait_seconds": 300,
  "quota_fallback": true,
  "switch_on_first_rate_limit": true,
  
  "account_selection_strategy": "sticky",
  "pid_offset_enabled": false,
  
  "signature_cache": {
    "enabled": true,
    "memory_ttl_seconds": 3600,
    "disk_ttl_seconds": 172800,
    "write_interval_seconds": 60
  }
}
```

### Step 3.2: Configuration Deep Dive

**Session Recovery Settings** — Critical for multi-step agent workflows:

```json
"session_recovery": true,        // Auto-recover from tool_result_missing errors
"auto_resume": true,             // Auto-send "continue" prompt after recovery
"resume_text": "continue"        // Customize resume text if needed
```

When a Claude tool call fails mid-execution, the plugin automatically:
1. Detects the error
2. Recovers the session state
3. Sends "continue" to resume from where it left off
4. Continues task execution

**Thinking Block Preservation** — For conversation continuity:

```json
"keep_thinking": true,           // MUST be true for multi-turn thinking model conversations
"signature_cache": {
  "enabled": true,
  "memory_ttl_seconds": 3600,    // Cache thinking signatures in RAM for 1 hour
  "disk_ttl_seconds": 172800,    // Persist to disk for 48 hours
  "write_interval_seconds": 60   // Flush to disk every 60 seconds
}
```

When enabled:
- Claude thinking blocks are cached by family (Claude vs Gemini isolated)
- Prevents "thinking block not found" errors when switching between models
- Enables seamless cross-model conversations

**Rate Limit Management** — For multi-account scenarios:

```json
"quota_fallback": true,          // Try Gemini CLI quota before switching accounts
"max_rate_limit_wait_seconds": 300,  // Wait max 5 minutes for quota reset
"account_selection_strategy": "sticky" // Preserve prompt cache
```

With `quota_fallback: true`, when Antigravity quota exhausts:
1. Plugin retries on Gemini CLI quota (same account)
2. Only switches to next account if CLI quota also exhausted
3. **Effectively doubles your Gemini quota**

### Step 3.3: Multi-Account Setup (For Team Workflows)

Add multiple Google accounts to scale quota:

```bash
opencode auth login
```

When prompted with existing accounts:
```
2 account(s) saved:
  1. your-primary@gmail.com
  2. your-secondary@gmail.com

(a)dd new account(s) or (f)resh start? [a/f]:
```

Choose `(a)` to add another account. This account storage is secure:

**File**: `~/.config/opencode/antigravity-accounts.json`
```json
{
  "version": 3,
  "accounts": [
    {
      "email": "primary@gmail.com",
      "refreshToken": "...encrypted...",
      "projectId": "your-gcp-project-id"
    },
    {
      "email": "secondary@gmail.com",
      "refreshToken": "...encrypted...",
      "projectId": "another-gcp-project-id"
    }
  ],
  "activeIndex": 0,
  "activeIndexByFamily": {
    "claude": 0,
    "gemini": 1
  }
}
```

**Account Selection Strategies:**

- **`sticky`** (default): Uses same account until rate-limited. **Best for prompt cache preservation.**
- **`round-robin`**: Rotates accounts on every request. **Best for maximum throughput.**
- **`hybrid`**: Touches all fresh accounts first, then sticky. **Best for sync reset timers.**

---

## Phase 4: Specialized Configurations

### For Agno Framework Integration

If using Agno for multi-agent systems:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-antigravity-auth@beta"],
  "provider": {
    "google": {
      "models": {
        "antigravity-claude-opus-4-5-thinking": {
          "name": "Claude Opus (Agent Primary)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "reasoning": { "thinkingConfig": { "thinkingBudget": 32768 } },
            "fast": { "thinkingConfig": { "thinkingBudget": 8192 } }
          }
        },
        "antigravity-gemini-3-pro-preview": {
          "name": "Gemini Pro (Agent Secondary)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingLevel": "low" },
            "high": { "thinkingLevel": "high" }
          }
        }
      }
    }
  }
}
```

Then in your Agno config:
```python
agents = [
    Agent(
        name="reasoning_agent",
        model="google/antigravity-claude-opus-4-5-thinking",
        variant="reasoning",  # Uses 32KB thinking budget
        tools=[...]
    ),
    Agent(
        name="analysis_agent",
        model="google/antigravity-gemini-3-pro-preview",
        variant="high",  # Uses high thinking level
        tools=[...]
    )
]
```

### For Development (Debug Mode)

**During development, enable comprehensive logging:**

```json
{
  "debug": true,
  "log_dir": "~/.config/opencode/antigravity-logs",
  "quiet_mode": false,
  "keep_thinking": true,
  "session_recovery": true,
  "tool_id_recovery": true,
  "claude_tool_hardening": true
}
```

Also enable verbose environment debugging:

```bash
OPENCODE_ANTIGRAVITY_DEBUG=2 opencode run "complex task" --model=google/antigravity-claude-opus-4-5-thinking
```

This writes detailed logs to `~/.config/opencode/antigravity-logs/` including:
- Full request/response bodies
- Token refresh events
- Rate limit transitions
- Account rotation decisions
- Thinking block cache hits/misses

### For Headless/Server Environments

If running OpenCode on a server without browser:

```json
{
  "quiet_mode": true,
  "debug": false,
  "session_recovery": true,
  "auto_resume": true,
  "pid_offset_enabled": true
}
```

Set `pid_offset_enabled: true` when running multiple parallel OpenCode processes. This distributes sessions across accounts using PID-based offsets, preventing thundering herd on single account.

---

## Phase 5: Usage Patterns

### Pattern 1: Single-Turn Complex Reasoning

```bash
opencode run "Analyze this architecture and suggest optimizations" \
  --model=google/antigravity-claude-opus-4-5-thinking \
  --variant=max
```

Claude spends full 32KB thinking budget analyzing your request before responding.

### Pattern 2: Multi-Turn Conversation with Thinking Preservation

```bash
# Turn 1: Initial thinking
opencode run "Design a multi-agent system for X" \
  --model=google/antigravity-claude-sonnet-4-5-thinking \
  --variant=max

# Turn 2 (same session): Follow-up benefits from previous thinking signatures
opencode run "Now add these additional requirements" \
  --model=google/antigravity-claude-sonnet-4-5-thinking \
  --variant=max
```

With `keep_thinking: true`, the plugin preserves thinking block signatures across turns, preventing "thinking block not found" errors.

### Pattern 3: Fast Iteration with Automatic Account Fallback

```bash
# When Antigravity quota exhausted, automatically tries Gemini CLI quota
opencode run "Generate test cases" \
  --model=google/antigravity-gemini-3-flash-preview \
  --variant=low
```

With `quota_fallback: true`, no rate limit wait—instantly uses fallback quota pool.

### Pattern 4: Cross-Model Conversation (Claude→Gemini→Claude)

```bash
# Start with Claude thinking
opencode run "Plan the algorithm" \
  --model=google/antigravity-claude-sonnet-4-5-thinking

# Switch to Gemini for analysis (uses different quota pool)
opencode run "Now analyze using Gemini" \
  --model=google/antigravity-gemini-3-pro-preview

# Back to Claude (thinking cache isolated by family)
opencode run "Refine based on Gemini analysis" \
  --model=google/antigravity-claude-sonnet-4-5-thinking
```

Family-independent caching ensures clean separation of Claude vs Gemini thinking blocks.

---

## Phase 6: Troubleshooting & Optimization

### Common Issues

**Issue: "Empty response" errors**

**Solution:** Increase retry attempts
```json
"empty_response_max_attempts": 6,
"empty_response_retry_delay_ms": 3000
```

**Issue: "tool_result_missing" during Claude tool use**

**Solution:** Already handled by default, but ensure:
```json
"session_recovery": true,
"tool_id_recovery": true,
"claude_tool_hardening": true
```

**Issue: Rate limits too aggressive**

**Solution:** Add more accounts or enable quota fallback
```json
"quota_fallback": true,
"max_rate_limit_wait_seconds": 600  // Wait up to 10 minutes
```

Then add account: `opencode auth login`

**Issue: Models not found**

**Solution:** Ensure `npm` field in provider:
```json
"provider": {
  "google": {
    "npm": "@ai-sdk/google"
  }
}
```

### Optimization Checklist

- [ ] Set `account_selection_strategy: "sticky"` to preserve prompt cache
- [ ] Enable `quota_fallback: true` for Gemini workloads (doubles capacity)
- [ ] Set `keep_thinking: true` for multi-turn conversations
- [ ] Use `antigravity-claude-opus-4-5-thinking` with `variant: max` for complex reasoning
- [ ] Use `antigravity-gemini-3-flash-preview` with `variant: low` for fast iteration
- [ ] Monitor logs with `debug: true` during first week
- [ ] Add 2-3 Google accounts for sustained high-volume workflows

---

## Security Best Practices

1. **Token File Permissions:**
   ```bash
   chmod 600 ~/.config/opencode/antigravity-accounts.json
   ```

2. **Git Ignore OAuth Tokens:**
   ```bash
   echo ".opencode/antigravity-accounts.json" >> .gitignore
   ```

3. **Rotate Accounts Regularly:**
   If a token is compromised:
   ```bash
   rm ~/.config/opencode/antigravity-accounts.json
   opencode auth login  # Re-authenticate
   ```

4. **Never Commit antigravity.json if it contains projectId secrets:**
   Use `.opencode/antigravity.json` in project root for shared config, but exclude from git if it has sensitive data.

---

## Next Steps

1. **Verify Setup:**
   ```bash
   opencode run "Hello" --model=google/antigravity-claude-sonnet-4-5
   ```

2. **Test Multi-Account (Optional):**
   ```bash
   opencode auth login
   # Add 2nd account when prompted
   ```

3. **Enable Debug Logging:**
   ```bash
   OPENCODE_ANTIGRAVITY_DEBUG=1 opencode run "test" --model=google/antigravity-gemini-3-pro-preview
   ```

4. **Integrate with Agno/Multi-Agent Framework:**
   - Reference Phase 4 configuration
   - Test with your first agent

5. **Monitor Rate Limits:**
   - Watch logs for quota exhaustion patterns
   - Add accounts if hitting limits consistently

---

## Support & Resources

- **GitHub Issues:** https://github.com/NoeFabris/opencode-antigravity-auth/issues
- **Documentation:** https://github.com/NoeFabris/opencode-antigravity-auth
- **Schema Reference:** https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/assets/antigravity.schema.json
- **Sponsor:** ko-fi.com/noefabris
