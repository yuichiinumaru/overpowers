---
name: dev-testing-claude-skills-framework
description: Architectural guide and development framework for building Claude Skills with Tool Use, focusing on high cohesion and low coupling.
tags: [claude, skills, framework, architecture, testing]
version: 1.0.0
---

# Claude Skills Development Framework Architectural Guidance Manual

## 1. Project Overview

This framework is built based on the Tool Use (Skills) feature of Anthropic Claude, aiming to provide a development scaffold for invoking various underlying tools through natural language chat.
The framework follows the principles of high cohesion and low coupling, allowing developers to focus on writing the "Skill" itself without worrying about the complex logic of LLM conversation context, tool discovery, and function execution.

## 2. Architecture Design

The entire system is divided into the following layered architectures:

- **Interaction Layer (CLI/API Interface)**: Responsible for receiving user input and displaying Agent replies or execution results. `main.py`
- **Agent Layer**: Responsible for maintaining conversation history, interacting with the Claude API, and parsing Tool Use requests returned by the model. `core/agent.py`
- **Registration and Dispatch Layer (Registry & Dispatcher)**: Maintains all available Skills (tools) in the system, declares the JSON Schema of these tools to the LLM, and finds the corresponding Python function executor based on the LLM's instructions. `core/registry.py`
- **Skills Layer**: Specific business code abstractions and implementations, inheriting from a unified BaseSkill. `core/skill_base.py`, `skills/*`

## 3. Core Module Description
... (rest of content)
