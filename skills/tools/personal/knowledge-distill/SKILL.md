---
name: knowledge-distill
version: 1.0.0
description: Knowledge distillation and archiving tool. Categorizes discussion results into five specific knowledge documents (Command Memory, Professional Work, General Knowledge, Research Logs, and Thought Distillation).
tags: [knowledge-management, archiving, documentation, distillation, research-logs]
category: knowledge
---

# Knowledge Distillation Skill

Classify discussion outcomes and write them into corresponding knowledge documents, supporting convenient recording of commands, knowledge conclusions, and thinking frameworks.

## Initialization

When using for the first time, check if `~/knowledge-base/` exists:
- If it does not exist, automatically create the directory and 5 empty documents.
- Users can customize the path by setting the `KNOWLEDGE_BASE_PATH` environment variable.

```
~/knowledge-base/
├── Command Memory Bank.md     ← OpenClaw/CLI Command Quick Reference
├── Professional Knowledge Distillation.md         ← Professional domain technical conclusions
├── Interest Knowledge Distillation.md         ← Learning content outside of work
├── Learning and Research Log.md         ← Process records for each discussion
└── Thinking Distillation.md             ← Methodologies, cognitive models, thinking frameworks
```

## Five Document Classifications (Document Classification)

| Target Document | Writing Condition | Content Type |
|----------|---------|---------|
| Command Memory Bank.md | User says "Record a command" | Command format, parameter description, usage scenarios |
| Professional Knowledge Distillation.md | Technical conclusions in professional domains | Technical parameters, operation steps, best practices |
| Interest Knowledge Distillation.md | Knowledge in interest areas outside of work | Same format as professional knowledge |
| Learning and Research Log.md | Process records for each discussion | Problem background, conclusions, evolution trajectory |
| Thinking Distillation.md | Crystallization of thought that is not specific content | Ways of thinking, methodologies, decision frameworks |

## Workflow

1. **Determine Classification**: Judge which document to write to based on the content and trigger phrase.
2. **Organize Content**: Extract core conclusions, removing trial-and-error processes.
3. **Show Preview**: Display the organized content and the planned writing location in the chat window.
4. **Wait for Confirmation**: Write only after user confirmation.
5. **Write to Log**: Synchronously record the process of this discussion in the Learning and Research Log.

## Constraints

- Do not write to any document without user confirmation.
- Distillation retains only the final correct conclusions, not the trial-and-error process.
- Content should be concise; each conclusion should be an independent block for easy retrieval.
