---
name: ai-llm-minimax-plan-checker
description: Retrieve MiniMax platform plan information, including plan name, quota, and current usage. Use this skill when users ask about MiniMax plans, quota usage, API call volume, or billing information.
tags: [minimax, plan, quota, billing]
version: 1.0.0
---

# MiniMax Plan Information Inquiry

Retrieve the plan name, quota, and current usage from the MiniMax platform.

## Usage

### Method 1: Automatic Retrieval via Browser (Recommended)

```bash
python scripts/get_plan.py
```

### Method 2: Direct Use in Conversation

Inform the user that a browser needs to be opened and ask if they want to automatically open the MiniMax platform page to retrieve plan information.

## Output Format

The script will output the following information:
- **Plan Name**: e.g., "Chat API" / "MoE API", etc.
- **Quota Information**: Total quota, used quota, remaining quota.
- **Usage Statistics**: API call count, Token usage, etc.

## Notes

- Requires the user to be logged into their MiniMax account.
- If not logged in, the browser will open the login page; the user should run the script again after logging in.
- Page URL: https://platform.minimaxi.com/user-center/payment/coding-plan
