---
name: ai-llm-maker-micro-delegate
description: The execution engine of the MAKER framework. Instantiates an extremely lightweight, contextless LLM call isolated to a single reasoning step (m=1).
tags:
- ai
- llm
- maker-framework
- execution
license: Complete terms in LICENSE.txt
version: 1.0.0
category: execution
---
# MAKER Micro Delegate

## Overview
This skill is the muscle of the MAKER framework. Instead of relying on a large agent with huge context to plan and execute everything, the orchestrator invokes the **Micro Delegate**. 
The delegate only knows the current state $S_i$ and the requested micro-step action $A_i$. It processes it with its LLM and returns the string output.

## Philosophy
In accordance with Maximal Agentic Decomposition ($m=1$), the micro-delegate should have **zero memory**. It does not know what happened 10 steps ago. It does not know the final goal of the project. It only solves the immediate logic puzzle it is handed, eliminating context confusion and hallucination creep.

## Inputs
- `state_context`: The strictly necessary context for the current step.
- `step_instruction`: The explicit instructions of what needs to be answered/solved.
- `temperature`: Usually > 0.0 (e.g., 0.1 to 0.7) to allow sampling diversity for the consensus voter.

## Output
Returns the raw string output of the LLM. It is expected that the Orchestrator will call this skill $N$ times in parallel and feed the collective outputs to the `maker-red-flag-validator`.
