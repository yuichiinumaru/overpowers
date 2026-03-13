# Feature Plan: Advanced Hooks Implementation

## 1. Goal
Enhance the autonomy and reliability of Overpowers agents by introducing system-level hooks that enforce task completion and provide automated error correction.

## 2. Vertical Slices
- **Milestone 1**: Todo Enforcer (Basic logic + prompt injection).
- **Milestone 2**: Directory Injector (Auto-context based on path).
- **Milestone 3**: Edit Tool Middleware (Self-correction feedback loop).

## 3. Exit Conditions
- [ ] Agent continues working automatically if todos are pending after an idle event.
- [ ] System prompt includes local `README.md` content when CWD changes.
- [ ] Failed edits trigger a specific hint explaining the error instead of a generic failure message.

## 4. Jobs To Be Done (JTBD)
When I am working on a multi-file task, I want the system to ensure I don't stop until all sub-tasks are done, so that I maintain high productivity without manual re-prompting.
