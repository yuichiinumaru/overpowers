---
name: jules-dispatch-login
description: Manages Jules account rotation and authentication limits. Handles the 14-task / 100-daily quota per Google Account for Jules.
tags:
- ai
- llm
---
# Jules Dispatch Login

This skill manages the Google Cloud authentication flow for the Jules CLI. Jules Pro accounts are strictly limited by Google to 15 concurrent tasks and 100 tasks per day.

## Using `jules-launcher.sh`

The `jules-launcher.sh` script (inside scripts folder of this skill) automatically tracks task dispatches. Because it launches 2 identical sessions for every 1 task defined (for redundancy and quality assurance), processing 7 user tasks results in 14 actual jobs. 

This approaches the 15-job concurrent limit. Therefore, the launcher is designed to gracefully pause after every 7 tasks (14 jobs) and prompt for account rotation.

## Account Rotation Process

When the script pauses or when you hit concurrent task limits, you must rotate to a different Google account:

1. **Invoke Login**: Run `jules login` in the terminal.
2. **Authenticate**: Follow the browser link provided by the CLI.
3. **Select Account**: Choose a fresh Google account that hasn't reached its quota.
4. **Resume**: Once authenticated, the launcher will continue dispatching the remaining tasks.

## Managing Quotas

- **Concurrent Limit**: 15 tasks per account.
- **Daily Limit**: 100 tasks per account.
- **Redundancy Factor**: Remember that 1 specified task = 2 actual Jules jobs.

*Important:* Do not attempt to bypass these limits without rotating accounts, as it will result in 429 Too Many Requests errors from the Jules backend, leading to failed dispatches.

## Empty Diffs Fallback

If you notice that Jules completed a task but the resulting native Pull Request is empty (+0 -0) because Jules committed the changes internally, use the fallback mechanism:

1. Locate the session ID in `.agents/sessions.json`.
2. Save your current work: `jj commit -m "backup: pre-jules-pull"`
3. Pull the code directly into your local codebase: `jules remote pull --session <SESSION_ID> --apply`
4. Use Jujutsu bookmarks if you need to merge multiple session diffs cautiously.
