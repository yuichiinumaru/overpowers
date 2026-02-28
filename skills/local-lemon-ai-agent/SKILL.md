---
name: local-lemon-ai-agent
description: Install and run the open-source Lemon AI agent locally as a general-purpose AI assistant for complex task execution.
category: ai-agents
color: "#1ABC9C"
tools:
  read: true
  write: true
  bash: true
---

# Run Lemon AI Agent Locally

## Overview
Install and run the open-source Lemon AI agent locally as a general-purpose AI assistant for complex task execution.

## Procedure
### 1. Installation & Environment Setup
- Clone the **Lemon AI** repository from GitHub.
- Create an isolated Python virtual environment (`python -m venv venv`).
- Install dependencies: `pip install -r requirements.txt`.
- Configure your local LLM backend (e.g., Ollama running Llama 3 or Qwen) or provide necessary API keys in the `.env` file if using cloud models.

### 2. Agent Configuration
- Review the `config.yaml` file to define the agent's tool access (e.g., web browsing, file system read/write, terminal execution).
- Set the system prompt to define the agent's persona and safety boundaries.

### 3. Execution
- Launch the agent via the terminal: `python main.py` or through its provided local web UI.
- Provide a complex, multi-step prompt (e.g., "Research the latest news on AI video models, summarize the top 3, and save them to a markdown file").
- Monitor the agent's execution chain as it reasons, calls tools, and compiles the final output.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=W6R8Ux0sDsU
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
