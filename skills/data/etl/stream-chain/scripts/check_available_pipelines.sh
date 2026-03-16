#!/bin/bash

# Check available pipelines
cat .claude-flow/config.json | grep -A 10 "streamChain"
