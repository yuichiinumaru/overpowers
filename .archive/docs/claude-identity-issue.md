# Claude Identity Issue: LLMs Don't Know Who They Are

> [!IMPORTANT]
> When Claude Opus 4.5 says it's "Claude 3.5 Sonnet", it's NOT a fallback bug.
> This is a known limitation of how LLM identity works.

## The Problem

When you ask Claude Opus 4.5 "What model are you?", it may respond:
- "Claude 3.5 Sonnet"
- "Claude (claude-sonnet-4-20250514)"

This appears to indicate model fallback, but **it's actually correct behavior**.

## Root Cause

**LLM identity is configured via system prompt, not learned during training.**

1. The model is trained with a specific knowledge cutoff (e.g., March 2025 for Opus 4.5)
2. The model's name and version are assigned **after** training is complete
3. The model has no intrinsic knowledge of "who it is"
4. Identity comes from system prompt configuration

## How to Verify the Actual Model

### ✅ Reliable: Knowledge Cutoff Tests

```
Question: "Who won the Nobel Peace Prize 2024?"
- Opus 4.5: "Nihon Hidankyo" ✅ (announced October 2024)
- Sonnet 3.5: "I don't have that information"

Question: "What was the Euro 2024 final result?"
- Opus 4.5: "Spain 2-1 England" ✅
- Sonnet 3.5: "My knowledge cutoff is April 2024"
```

### ❌ Unreliable: Self-Identification

```
Question: "What model are you?"
- Both may respond "Claude 3.5 Sonnet" due to system prompt issues
```

## Knowledge Cutoffs by Model

| Model | Knowledge Cutoff |
|-------|-----------------|
| Claude Opus 4.5 | March 2025 |
| Claude Sonnet 4.5 | January 2025 |
| Claude Sonnet 3.5 | April 2024 |

## Validation Tests Used

### Test 1: Nobel Peace Prize 2024
```
opencode run "Who won the Nobel Peace Prize 2024?" --model google/antigravity-claude-opus-4-5-thinking
```
**Expected**: "Nihon Hidankyo" (Japanese A-bomb survivors organization)

### Test 2: Euro 2024
```
opencode run "What was the Euro 2024 final result?" --model google/antigravity-claude-opus-4-5-thinking
```
**Expected**: "Spain 2-1 England"

## References

- [Anomify Investigation: Finding Claude](https://anomify.ai/resources/articles/finding-claude)
- [16x Engineer: LLM Identity Crisis](https://eval.16x.engineer/blog/llm-identity-crisis-models-dont-know-who-they-are)
- [Reddit: Claude lies about which model it is serving](https://www.reddit.com/r/ClaudeAI/comments/1m1xphk/claude_lies_about_which_model_it_is_serving/)

## Conclusion

**Don't trust self-identification. Test knowledge cutoff instead.**

If the model knows about events from late 2024/early 2025, you have Opus 4.5.
If it doesn't, you have Sonnet 3.5 or earlier.
