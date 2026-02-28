---
name: vibe-coding-best-practices
description: Diretrizes e práticas recomendadas para "Vibe Coding" - a arte de desenvolver software orquestrando múltiplos agentes de IA especializados através de linguagem natural, com foco em arquitetura, design de sistemas e refinamento iterativo.
category: engineering
color: "#FF8C00"
tools:
  read: true
  write: true
---

# Vibe Coding Best Practices

## Description
This skill encapsulates the principles and best practices of "Vibe Coding," a paradigm shift in software development where engineers orchestrate specialized AI agents using natural language instead of writing code line by line. The focus shifts from syntax to system design, architecture, and ensuring the overall "vibe" (functionality, UX, and security) of the application is correct.

## Context
Extracted from: [IBM Technology - What Is Vibe Coding? Building Software with Agentic AI](https://www.youtube.com/watch?v=Y68FF_nUSWE)

## Core Principles of Vibe Coding

1.  **Shift Left to Architecture:**
    -   Spend significantly more time designing the system architecture, data models, and API contracts *before* engaging the AI agents.
    -   The agents are fast typists, but they need a clear blueprint. Without it, the "vibe" will be incoherent.

2.  **Prompt Engineering as Coding:**
    -   Treat your prompts as the source code. They should be version-controlled, modular, and precise.
    -   Provide clear context: What is the goal? What are the constraints (language, framework, performance)? What are the expected inputs and outputs?

3.  **Iterative Refinement (Fixing the Vibe):**
    -   Don't expect perfect code on the first try. Vibe coding is an iterative process.
    -   If the generated code has a bug or doesn't feel right, don't fix the code directly (unless it's a trivial typo). Instead, *fix the prompt* that generated the code. Explain *why* the output is wrong to the agent.

4.  **Multi-Agent Orchestration:**
    -   Use specialized agents for different tasks. Don't ask one generalist model to build the entire app.
    -   *Example:* Have an `Architect Agent` design the database schema, a `Backend Agent` write the API endpoints, a `Frontend Agent` build the UI components, and a `Testing Agent` write the unit tests.

5.  **Rigorous Review and Testing:**
    -   The human engineer is now the ultimate Code Reviewer. You are responsible for the quality, security, and performance of the generated code.
    -   Always mandate that the agents generate comprehensive test suites alongside the application code.

## Workflow Example: Building a Microservice

1.  **System Prompt (Human):** Define the microservice's purpose, REST API endpoints, and database schema in a Markdown file.
2.  **Generation Phase (Agent 1 - Architect):** Review the Markdown file and generate OpenAPI/Swagger specifications.
3.  **Generation Phase (Agent 2 - Backend):** Ingest the OpenAPI specs and generate the Python/FastAPI code for the endpoints.
4.  **Review Phase (Human):** Inspect the generated code for security vulnerabilities (e.g., SQL injection, improper auth).
5.  **Iteration Phase (Human to Agent):** "The `/users` endpoint does not handle pagination. Please update the code to support offset and limit parameters."
6.  **Testing Phase (Agent 3 - QA):** Generate Pytest unit tests for all endpoints, including edge cases.
7.  **Final Polish (Human):** Ensure the code adheres to company style guides and runs successfully in the CI/CD pipeline.

## Required Mindset
- You are a **Director**, not just a typist.
- Focus on the **"What"** and **"Why"**, let the AI figure out the **"How"**.
- Always verify the output; **Trust, but Verify**.
