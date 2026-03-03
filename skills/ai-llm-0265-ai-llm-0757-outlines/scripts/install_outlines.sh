#!/bin/bash

# Helper to install Outlines with recommended backends.
# Usage: ./install_outlines.sh [backend]

BACKEND=$1

case $BACKEND in
  transformers)
    pip install outlines transformers torch
    ;;
  llamacpp)
    pip install outlines llama-cpp-python
    ;;
  vllm)
    pip install outlines vllm
    ;;
  *)
    echo "Usage: $0 {transformers|llamacpp|vllm}"
    echo "Example: $0 transformers"
    exit 1
    ;;
esac
