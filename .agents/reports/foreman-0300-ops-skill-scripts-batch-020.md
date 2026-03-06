# Report for Task 0300: Skill Scripts Batch 020

This report tracks the completion of adding helper scripts for the 20th batch of skills.

### `ai-llm-0618-ops-infra-0370-email-composer`
- Checked skill directory. It's a pure guideline/text skill for email composition.
- No helper scripts are needed.
### `ai-llm-0682-ops-infra-0838-professional-communication`
- Checked skill directory. Like the previous, it provides communication guidelines.
- No helper scripts are needed.
### `ai-llm-0695-ops-infra-0915-requesting-code-review`
- Added `scripts/request-review.sh` to fetch base/head SHAs and output a template payload for requesting a review.
### `ai-llm-0733-reasoning`
- Checked skill directory. This is a framework for reasoning templates.
- No helper scripts needed.
### `ai-llm-0906-scientific`
- Checked skill directory. Guidelines for rigorous scientific investigation.
- No helper scripts needed.
### `ai-llm-1165-ux-design-0448-frontend-design`
- Checked skill directory. This provides frontend aesthetic guidelines.
- No helper scripts needed.
### `ai-llm-1172-ux-design-0517-haskell-pro`
- Checked skill directory. Guidelines for Haskell expert development.
- No helper scripts needed.
### `ai-llm-1203-web-frontend-0281-create-justification`
- Checked skill directory. SKILL.md mentions a script to create a justification at `scripts/create-justification.ts`.
- Creating `scripts/create-justification.ts` in the skill's directory since it's the standard for skills to own their helper scripts.
### `ai-llm-1234-build-review-interface`
- Checked skill directory. Guidelines for building an annotation interface.
- Mentions functional testing via Playwright. I will add a stub shell script or testing guideline.
### `ai-llm-1236-claude-ai`
- This directory contains `vercel-deploy-claimable` which acts as a skill but is nested. I will place a wrapper script inside `scripts/`.
- The `vercel-deploy-claimable` skill references `bash /mnt/skills/user/vercel-deploy/scripts/deploy.sh [path]`. Since that path is internal to another environment, I'll add a placeholder `deploy.sh` script under its own scripts directory to make it actionable within the repository.
### `ai-llm-1237-claude-api`
- Checked skill directory. This provides API documentation and language-specific snippets for using Claude API.
- No generic helper scripts are needed since they provide code blocks and reference documents.
### `ai-llm-1238-error-analysis`
- Checked skill directory. This outlines a conceptual process for analyzing LLM errors.
- No helper scripts needed.
### `ai-llm-1239-eval-audit`
- Checked skill directory. This outlines an audit process.
- No helper scripts needed.
### `ai-llm-1240-evaluate-rag`
- Checked skill directory. This provides guidelines for evaluating RAG pipelines.
- No helper scripts needed.
### `ai-llm-1241-generate-synthetic-data`
- Checked skill directory. Guidelines for generating synthetic data using tuples and LLMs.
- No helper scripts needed.
### `ai-llm-1242-notion-knowledge-capture`
- Checked skill directory. This is a framework for using Notion via an MCP server.
- No helper scripts needed since the interaction depends on the MCP connection.
### `ai-llm-1243-openai-docs`
- Checked skill directory. This is a skill for interacting with an OpenAI MCP server.
- The SKILL.md mentions a command `codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp`.
- I will create a setup script `scripts/setup-openai-docs-mcp.sh` to help users install the MCP.
### `ai-llm-1244-stitch-loop`
- Checked skill directory. This describes an autonomous baton-passing loop pattern for building websites.
- Since it relies heavily on reading/writing a `next-prompt.md` file, I will add a small helper script to bootstrap this loop by creating the initial files if they don't exist.
### `ai-llm-1245-validate-evaluator`
- Checked skill directory. This outlines the process for calibrating an LLM judge.
- Includes Python code snippets for metrics and bootstrap CI.
- I will create a python helper script `scripts/validate-evaluator.py` containing the logic for computing TPR/TNR and bootstrap CI.
### `ai-llm-1246-write-judge-prompt`
- Checked skill directory. Guidelines for writing LLM-as-judge prompts.
- No helper scripts needed.
- Wait, I accidentally overwrote `vercel-deploy-claimable/scripts/deploy.sh`. Reverted the file to its original state.
