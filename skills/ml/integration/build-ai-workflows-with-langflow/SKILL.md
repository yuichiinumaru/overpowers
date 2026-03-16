---
name: build-ai-workflows-with-langflow
description: Guia de aceleração de desenvolvimento de IA Generativa. Utiliza o Langflow
  (uma interface visual open-source para o LangChain) para projetar, prototipar e
  exportar pipelines de RAG e Agentes Autônomos sem escrever o boilerplate inicial
  de conexão de LLMs, Vector Stores e Prompts, integrando também ferramentas MCP.
tags:
- ai
- llm
category: engineering
color: null
tools:
  read: true
  write: true
  bash: true
version: 1.0.0
---
# Build AI Workflows with Langflow

## Description
This skill accelerates the GenAI development cycle by leveraging **Langflow**, a visual, drag-and-drop IDE for building LLM applications based on the LangChain framework. It eliminates the repetitive boilerplate code associated with connecting Document Loaders, Text Splitters, Embeddings, Vector Databases, and LLMs. Engineers can visually construct complex RAG pipelines or Agent architectures, test them in the built-in UI, and then export them as production-ready Python code or expose them via a REST API.

## Context
Extracted from: [IBM Technology - What is Langflow? Build AI Workflows with Python, Gen AI, & MCP Tools](https://www.youtube.com/watch?v=xz00BbW1z6M)

## Installation and Startup

To start prototyping, install Langflow locally via pip:

```bash
pip install langflow
# Run the local server (usually available at http://127.0.0.1:7860)
python -m langflow run
```

## The Langflow Prototyping Cycle

1.  **Visual Design (The Canvas):**
    -   Drag nodes from the sidebar (e.g., `OpenAI`, `Prompt Template`, `Chroma DB`, `Web Search Tool`).
    -   Connect the edges. The UI enforces type safety (e.g., an Embedding node's output must connect to a Vector Store's embedding input).

2.  **Configuration (The Properties Panel):**
    -   Input your API keys (store them as environment variables or securely within Langflow).
    -   Set hyperparameters (temperature, chunk size for text splitters, top_k for retrievers).

3.  **Interactive Testing (The Chat Interface):**
    -   Click the "Play" or "Chat" button directly within the Langflow UI.
    -   Interact with your newly built RAG pipeline or Agent in real-time to validate the logic, prompt instructions, and tool usage before writing a single line of backend code.

4.  **Deployment (Exporting to Production):**
    -   Once the flow behaves correctly, click "Export".
    -   **Option A (Code Integration):** Export the flow as a JSON file and load it using the `langflow` Python package in your backend application:
        ```python
        from langflow.load import run_flow_from_json
        TWEAKS = {"PromptTemplate-1234": {"template": "You are a helpful assistant..."}}
        result = run_flow_from_json(flow="my_rag_flow.json",
                                    input_value="What is the company policy?",
                                    tweaks=TWEAKS)
        print(result[0].outputs[0].results["text"])
        ```
    -   **Option B (API Endpoint):** Langflow automatically exposes your flow as a REST endpoint that you can call via `curl` or any HTTP client from a frontend application.

## Advanced: MCP Integration
Langflow allows the integration of **Model Context Protocol (MCP)** tools. By adding an MCP node, your visual agent can securely access data and systems (like a local database, a GitHub repository, or enterprise APIs) by connecting to a running MCP Server, bridging the gap between the LLM and real-world execution environments.
