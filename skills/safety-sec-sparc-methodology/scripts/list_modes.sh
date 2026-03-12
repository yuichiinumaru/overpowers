#!/bin/bash

# List modes
npx claude-flow sparc modes

# Run specific mode
npx claude-flow sparc run <mode> "task"

# TDD workflow
npx claude-flow sparc tdd "feature"

# Full pipeline
npx claude-flow sparc pipeline "task"

# Batch execution
npx claude-flow sparc batch <modes> "task"
