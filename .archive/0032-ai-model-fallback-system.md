# Task 0032: Model Fallback System

**Status**: [ ]
**Priority**: HIGH
**Type**: feature

## Objective
Implement automatic fallback and load balancing across model providers to ensure reliable execution when hit by rate limits.

## Sub-tasks
- [ ] **Script Fallback**: Update `run-subagent.sh` with a fallback chain (Opus -> Sonnet -> Flash -> GLM).
- [ ] **Health Monitor**: Implement `model_selector.py` to track rate limits and cooldowns.
- [ ] **CEO Intelligence**: Train CEO agent to select models based on task complexity.
