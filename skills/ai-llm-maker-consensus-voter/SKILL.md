---
name: ai-llm-maker-consensus-voter
description: This skill implements the first-to-ahead-by-k voting mechanism for the MAKER framework. Given a pool of valid, red-flag free micro-delegate outputs, it determines if a consensus answer has been reached or if the orchestrator is UNDECIDED and needs to sample more.
tags:
- ai
- llm
- maker-framework
- consensus
license: Complete terms in LICENSE.txt
version: 1.0.0
category: orchestration
---
# MAKER Consensus Voter

## Overview
This skill executes the core statistical decision mechanism of the MAKER architecture: the **first-to-ahead-by-k** voting rule.
In a deeply decomposed process, one error breaks the chain. To guarantee high accuracy, multiple agents output candidate actions. This skill tallies them up.

## The Rule
A candidate action wins **if and only if** its vote count is $k$ votes strictly greater than the runner-up candidate's vote count, AND a minimum number of votes ($k_{min}$) have been cast. 

If no candidate satisfies this condition, the skill returns an `UNDECIDED` state, which signals the MAKER Orchestrator workflow that it needs to sample more outputs (i.e. spin up more micro-delegates) to break the tie or overcome statistical noise.

## Input
- `k`: Integer (e.g., 3).
- `k_min`: Integer (usually equal to `k`).
- `responses`: Array of validated action objects/strings representing the votes.

## Output
- `status`: String (`"DECIDED"` or `"UNDECIDED"`).
- `winner`: The winning action object (if `DECIDED`).
- `tally`: Distribution of current votes.
