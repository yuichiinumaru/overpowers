# Audience Distinction: AGENTS.md vs .agents/rules/

## Rule

- **`AGENTS.md`** (root of the repo) is the **Root Constitution** and is read by **ALL agents** that interact with this repository, including:
  - Jules (Google's async coding agent)
  - Antigravity (Gemini CLI coding agent)
  - OpenCode agents
  - Any other AI agent that reads the repo

- **`.agents/rules/`** contains rules that apply **only to Antigravity** (and the local developer's AI setup). These rules are NOT seen by Jules or other external agents. This is the right place for:
  - Jujutsu VCS rules (Jules uses Git, not Jujutsu)
  - OpenCode-specific formatting rules (tools/color schema)
  - Jules-specific operational rules (branch naming, report saving — Jules reads these because `.agents/` is in the repo, but these are orchestration rules, not constitution rules)

## Why This Matters

Jules operates remotely and only reads files committed to the repository. It will always read `AGENTS.md` because it is the root constitution. It will also read `.agents/rules/` if instructed to, but the rules there are designed for the local AI coding environment.

Do NOT put Antigravity-specific conventions (like Jujutsu VCS usage) in `AGENTS.md` — it will confuse Jules, which uses standard Git.
