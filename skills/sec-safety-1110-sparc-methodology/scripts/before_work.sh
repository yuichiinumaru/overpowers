#!/bin/bash

# Before work
npx claude-flow@alpha hooks pre-task --description "implement auth"

# During work
npx claude-flow@alpha hooks post-edit --file "auth.js"

# After work
npx claude-flow@alpha hooks post-task --task-id "task-123"
