# Context Degradation Protocol

> **Context:** LLMs (Large Language Models) suffer from 'amnesia' or 'hallucination' when their context window becomes saturated during long sessions. This protocol instructs all agents operating in the Overpowers ecosystem on how to prevent catastrophic data loss due to overextended context.

## The Triggers

Because an agent cannot inherently 'feel' how full its context window is, users or CI runners must provide context percentages (usually via injection in the prompt). If an agent suspects its context is becoming dangerously large, or it receives a context metric from a wrapper, it must obey these thresholds:

### 1. WARNING: Context < 35% Remaining
When the context goes below 35% remaining capacity, the agent must:
1.  **Stop initiating new sub-tasks.**
2.  Rapidly finalize the current immediate action (e.g. finish the function it is currently writing).
3.  Pre-emptively prepare a state summary (see `STATE.md`).

### 2. CRITICAL: Context < 25% Remaining
When the context threshold hits critical mass, the agent must execute the **Law of Thought Offloading**:
1.  **Drop all work immediately.** DO NOT attempt to write "just one more file".
2.  Synthesize everything learned, blocked, and decided during the session.
3.  Save this payload inside `.agents/thoughts/<session_id>.md`.
4.  Issue a `/gsd:pause-work` or equivalent command to yield control back to the orchestrator or user.

## Why this matters?
Continuing to operate below 20% context drastically increases the likelihood that the agent will corrupt files, generate phantom code, or forget overarching instructions laid out in `AGENTS.md`. The most responsible action is to die gracefully and let a fresh agent context pick up the synthesized thought file.
