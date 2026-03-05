#!/bin/bash

# AI Tool Decision Helper based on the Architectural Decision Matrix.
# Usage: ./decision-helper.sh "Requirement description"

REQ=$1

if [ -z "$REQ" ]; then
  echo "Usage: $0 \"Requirement description\""
  exit 1
fi

echo "Requirement: $REQ"
echo "--------------------------------"

# Simple keyword-based mapping
if [[ "$REQ" =~ (poem|summarize|translate|write) ]]; then
  echo "Recommended Tool: Pure LLM"
  echo "Why: The task relies entirely on the model's internal knowledge or provided context."
elif [[ "$REQ" =~ (questions|handbook|knowledge|docs) ]]; then
  echo "Recommended Tool: LLM + RAG"
  echo "Why: The model needs external knowledge but only needs to read it once."
elif [[ "$REQ" =~ (book|cancel|email|api|csv|graph|save|modify) ]]; then
  echo "Recommended Tool: AI Agent"
  echo "Why: The task requires interacting with the outside world, modifying state, or iterative reasoning."
else
  echo "Recommended Tool: Pure LLM (Start Simple)"
  echo "Why: Attempt to solve with a well-crafted prompt first. Upgrade only if multi-step reasoning or tool usage is required."
fi
