# Checkpoint Protocol

> **Context:** When operating autonomously, agents (like Jules or Antigravity) may hit boundaries they cannot or should not cross alone (e.g., authentication, ambiguous architecture choices). This protocol defines how to "pause" execution and yield to the user elegantly.

## Checkpoint Return Format

Whenever a Checkpoint is triggered, you must output the following structured format to the user (either in the UI, or saved to your `task.md` output).

```markdown
## CHECKPOINT REACHED

**Type:** [human-verify | decision | human-action]
**Task:** [What you are currently trying to do]

### Checkpoint Details
[Describe exactly what is happening, what you discovered, or what you built]

### Options / Action Required
[State clearly what the user needs to do to unblock you]
```

## Types of Checkpoints

### 1. `checkpoint:human-verify`
*   **When to use:** When you have completed a complex UI feature or workflow and an automated test isn't sufficient to prove it "looks good".
*   **Description:** Human confirms the automated work works correctly. 
*   **What you ask the user:** "Please visit `http://localhost:3000/xyz`, log in, and verify the modal animations look correct. Reply 'approved' to continue."

### 2. `checkpoint:decision`
*   **When to use:** When you hit **Deviation Rule 4**. You need to make a foundational architectural choice (e.g., which database ORM to use, how to structure a new table).
*   **Description:** Human makes an implementation choice affecting the direction.
*   **What you ask the user:** Present a clear A/B options table with pros and cons. Ask them to select an option so you can resume.

### 3. `checkpoint:human-action`
*   **When to use:** When there is an unavoidable manual step that you, the agent, physically cannot do.
*   **Description:** The agent is gated by an external system.
*   **Examples:** Fetching a 2FA code sent via SMS, clicking an email verification link, approving an OAuth prompt in a browser, grabbing an API Key from a dashboard.
*   **What you ask the user:** Provide exact instructions on what they need to click or copy-paste back to you.

## The Rule of Automation First
Do not use `checkpoint:human-action` if the action can be automated via CLI.
*   *Bad:* "Please go to Vercel and deploy this project."
*   *Good:* Execute `npx vercel --prod` yourself.
