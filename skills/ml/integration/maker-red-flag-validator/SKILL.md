---
name: ai-llm-maker-red-flag-validator
description: This skill implements the MAKER framework's Red Flag Validation concept. It parses outputs from micro-delegate LLM instances and filters out ("red-flags") responses that are malformed, exceedingly long, or show signs of cognitive loops, thus destroying correlated errors before they reach the voting phase.
tags:
- ai
- llm
- maker-framework
- validation
license: Complete terms in LICENSE.txt
version: 1.0.0
category: orchestration
---
# MAKER Red Flag Validator

## Overview
Based on the paper *Solving a Million-Step LLM Task with Zero Errors*, this skill acts as the first line of defense in the MAKER (Massively Decomposed Agentic Processes) architecture. It receives an array of parallel sampled outputs for a single micro-task and silently discards any output that presents signs of "uncorrelated/correlated errors" (e.g., parsing failures, extreme verbosity indicative of confusing loops, or schema breaks).

## When to Use This Skill
- Orchestrating a MAKER multi-agent process where $N$ independent micro-agents have returned answers for step $i$.
- Establishing consensus pipelines where untidy LLM outputs must be pruned.
- When you need to increase the true success rate ($p$) by artificially inflating the quality of the sample pool via pruning.

## Red Flag Triggers
1. **Schema Non-compliance:** The expected JSON or exact format was not provided.
2. **Verbosity Threshold Execedeed:** The output token count or length is unusually large for a micro-task, indicating the LLM was confabulating "too heavily" instead of giving a direct answer.
3. **Empty/Null Output:** The agent failed to produce a valid sequence.

## Output
Returns a filtered array of strictly valid, well-formatted actions that can be safely forwarded to the `maker-consensus-voter` skill.
