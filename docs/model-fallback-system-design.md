# Model Fallback System Design

> **Status:** Draft / Future Implementation
> **Date:** 2026-01-19
> **Author:** Antigravity + Yuichi Inumaru

## Problem Statement

When using Antigravity with multiple model providers:

1. **Rate Limiting:** All accounts may hit quota simultaneously, causing subagent failures
2. **Not Graceful:** Failures stop mid-task with no recovery
3. **Manual Intervention:** User must manually switch models

## Goals

1. **Automatic Fallback:** When primary model fails, try secondary
2. **Load Distribution:** Spread requests across models to avoid quota exhaustion
3. **Priority-Based:** Use best models for complex tasks, cheaper for simple
4. **Smart Selection:** CEO agent decides based on task + available quota

---

## Architecture Options

### Option A: Script-Level Fallback (Simple)

Add fallback logic directly to `run-subagent.sh`:

```bash
#!/bin/bash
# run-subagent-with-fallback.sh

MODELS=(
    "google/antigravity-claude-opus-4-5-thinking"
    "google/antigravity-gemini-3-flash"
    "windsurf/glm-4.7"        # GLM fallback
    "google/opencode-gemini-pro"          # Gemini fallback
)

for MODEL in "${MODELS[@]}"; do
    echo "Trying $MODEL..."
    
    OPENCODE_PERMISSION='"allow"' timeout 300 opencode run "$PROMPT" --model "$MODEL" > "$OUTPUT" 2>&1
    
    if [ $? -eq 0 ]; then
        echo "✅ Success with $MODEL"
        exit 0
    fi
    
    # Check if rate limited
    if grep -q "rate_limit\|quota\|429" "$OUTPUT"; then
        echo "⚠️ Rate limited, trying next model..."
        continue
    fi
    
    # Other error, report and stop
    echo "❌ Failed with $MODEL: $(head -5 $OUTPUT)"
    exit 1
done

echo "❌ All models exhausted"
exit 1
```

**Pros:** Simple, no infrastructure needed
**Cons:** Sequential (slow), no global coordination

---

### Option B: Round-Robin Distribution

Distribute tasks across models to avoid quota exhaustion:

```bash
#!/bin/bash
# round-robin-subagent.sh

STATE_FILE="/tmp/model_rotation_state"

MODELS=(
    "google/antigravity-claude-opus-4-5-thinking"
    "google/antigravity-gemini-3-flash"
    "windsurf/glm-4.7"
)

# Get current index
INDEX=$(cat "$STATE_FILE" 2>/dev/null || echo 0)
MODEL="${MODELS[$((INDEX % ${#MODELS[@]}))]}"

# Increment for next call
echo $((INDEX + 1)) > "$STATE_FILE"

echo "Using model: $MODEL"
OPENCODE_PERMISSION='"allow"' opencode run "$1" --model "$MODEL"
```

**Pros:** Spreads load evenly
**Cons:** May use weaker model for complex tasks

---

### Option C: Task-Based Model Selection

CEO agent analyzes task complexity and selects model:

```markdown
## CEO Task Analysis

Before delegating, classify the task:

| Complexity | Indicators | Model |
|------------|------------|-------|
| **Simple** | File reads, grep, status checks | GLM 4.7 (preserve Claude quota) |
| **Medium** | Code analysis, refactoring | Sonnet 4.5 |
| **Complex** | Architecture design, security audit | Opus 4.5 |

### Decision Matrix

| Task Type | Default Model | Fallback 1 | Fallback 2 |
|-----------|---------------|------------|------------|
| Analysis | Sonnet 4.5 | GLM 4.7 | Gemini Pro |
| Generation | Opus 4.5 | Sonnet 4.5 | GLM 4.7 |
| Research | Sonnet 4.5 | Gemini Pro | GLM 4.7 |
| Simple ops | GLM 4.7 | Gemini Pro | Sonnet 4.5 |
```

**Pros:** Optimal model usage
**Cons:** Requires CEO agent intelligence

---

### Option D: Priority Queue with Health Checks

Advanced system with model health monitoring:

```python
# model_selector.py

import json
from pathlib import Path
from datetime import datetime, timedelta

MODEL_STATUS_FILE = Path.home() / ".config/opencode/model_status.json"

# Model priorities (higher = better)
MODEL_PRIORITIES = {
    "google/antigravity-claude-opus-4-5-thinking": 100,
    "google/antigravity-gemini-3-flash": 80,
    "windsurf/glm-4.7": 50,
    "google/opencode-gemini-pro": 40,
}

def get_model_status():
    """Load model status from file."""
    if MODEL_STATUS_FILE.exists():
        return json.loads(MODEL_STATUS_FILE.read_text())
    return {}

def update_model_status(model: str, success: bool, error_type: str = None):
    """Update model status after a call."""
    status = get_model_status()
    
    now = datetime.now().isoformat()
    
    if model not in status:
        status[model] = {"failures": 0, "last_success": None, "cooldown_until": None}
    
    if success:
        status[model]["failures"] = 0
        status[model]["last_success"] = now
        status[model]["cooldown_until"] = None
    else:
        status[model]["failures"] += 1
        
        # If rate limited, put on cooldown
        if error_type == "rate_limit":
            cooldown_minutes = min(60, 5 * status[model]["failures"])
            status[model]["cooldown_until"] = (
                datetime.now() + timedelta(minutes=cooldown_minutes)
            ).isoformat()
    
    MODEL_STATUS_FILE.write_text(json.dumps(status, indent=2))

def select_best_model(task_complexity: str = "medium") -> str:
    """Select the best available model based on status and task."""
    status = get_model_status()
    now = datetime.now()
    
    # Filter out models on cooldown
    available = []
    for model, priority in MODEL_PRIORITIES.items():
        model_status = status.get(model, {})
        cooldown = model_status.get("cooldown_until")
        
        if cooldown and datetime.fromisoformat(cooldown) > now:
            continue  # Skip, still on cooldown
        
        available.append((model, priority))
    
    if not available:
        # All on cooldown, return the one with shortest remaining cooldown
        return min(MODEL_PRIORITIES.keys(), 
                   key=lambda m: status.get(m, {}).get("cooldown_until", "9999"))
    
    # Task-based filtering
    if task_complexity == "simple":
        # Prefer cheaper models for simple tasks
        available = [(m, p * 0.5 if p > 60 else p) for m, p in available]
    elif task_complexity == "complex":
        # Require high-tier models
        available = [(m, p) for m, p in available if p >= 80] or available
    
    # Return highest priority available
    return max(available, key=lambda x: x[1])[0]
```

**Pros:** Smart, adaptive, persistent state
**Cons:** Requires maintaining Python script, more complex

---

## Recommended Implementation Path

### Phase 1: Script Fallback (Immediate)

Update `run-subagent.sh` with simple fallback chain including GLM 4.7:

```bash
# Add to skills/subagent_orchestration/scripts/run-subagent.sh
FALLBACK_MODELS=(
    "$MODEL"
    "windsurf/glm-4.7"
)
```

### Phase 2: CEO Intelligence (Short-term)

Train CEO agent to:
1. Classify task complexity
2. Select appropriate model tier
3. Reserve Claude quota for complex tasks

### Phase 3: Health Monitoring (Medium-term)

Implement model status tracking:
1. Log success/failure per model
2. Auto-cooldown on rate limits
3. Dashboard for quota visibility

### Phase 4: Dynamic Load Balancing (Long-term)

Full system with:
1. Real-time quota monitoring
2. Predictive model selection
3. Cross-account load distribution

---

## Quick Win: GLM 4.7 Fallback

Add to ALL agent configs as last fallback:

```json
{
  "models": {
    "primary": "google/antigravity-gemini-3-flash",
    "fallback": [
      "google/antigravity-claude-opus-4-5-thinking",
      "windsurf/glm-4.7"
    ]
  }
}
```

Update personas to include fallback configuration in `mcp.json`.

---

## Environment Variables

```bash
# Default and fallback models
export SUBAGENT_MODEL="google/antigravity-gemini-3-flash"
export SUBAGENT_FALLBACK="windsurf/glm-4.7"

# Quota preservation
export PRESERVE_OPUS_QUOTA=true  # Use Opus only for complex tasks
```

---

## Related Files

- `/home/sephiroth/.config/opencode/Overpowers/skills/subagent_orchestration/`
- `/home/sephiroth/.config/opencode/Overpowers/agents/000_ceo_orchestrator.md`
- `/home/sephiroth/.config/opencode/Overpowers/configure-persona.sh`

---

## Open Questions

1. How to detect rate limit vs other failures?
2. Should we expose quota status to users?
3. Per-model timeout configuration?
4. Session-level vs global model state?

---

**Next Steps:**
- [ ] Implement Phase 1 (script fallback)
- [ ] Update CEO agent with model selection guidelines
- [ ] Test GLM 4.7 compatibility with existing prompts
