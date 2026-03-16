#!/bin/bash

# Execute chain with memory
claude-flow stream_chain run \
  "Analyze requirements" \
  "Design architecture" \
  --verbose

# Results stored in .claude-flow/memory/stream_chain/
