#!/bin/bash

# Execute specific mode
npx claude-flow sparc run <mode> "task description"

# Use alpha features
npx claude-flow@alpha sparc run <mode> "task description"

# List all available modes
npx claude-flow sparc modes

# Get help for specific mode
npx claude-flow sparc help <mode>

# Run with options
npx claude-flow sparc run <mode> "task" --parallel --monitor

# Execute TDD workflow
npx claude-flow sparc tdd "feature description"

# Batch execution
npx claude-flow sparc batch <mode1,mode2,mode3> "task"

# Pipeline execution
npx claude-flow sparc pipeline "task description"
