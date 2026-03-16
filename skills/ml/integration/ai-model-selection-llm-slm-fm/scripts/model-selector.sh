#!/bin/bash

# AI Model Selector based on the Selection Matrix.
# Usage: ./model-selector.sh "Constraint/Goal"

GOAL=$1

if [ -z "$GOAL" ]; then
  echo "Usage: $0 \"Constraint or Goal\""
  exit 1
fi

echo "Goal/Constraint: $GOAL"
echo "--------------------------------"

if [[ "$GOAL" =~ (reasoning|planning|complex|generation) ]]; then
  echo "Recommended Model: Large Language Model (LLM)"
  echo "Examples: GPT-4o, Claude 3.5 Sonnet"
  echo "Why: High parameter count is needed for deep logical deduction and complex instructions."
elif [[ "$GOAL" =~ (privacy|premises|sensitive) ]]; then
  echo "Recommended Model: Local LLMs / Fine-Tuned SLMs"
  echo "Examples: Llama 3 70B (Local), Fine-tuned Phi-3"
  echo "Why: Data cannot be sent to public cloud APIs."
elif [[ "$GOAL" =~ (edge|offline|iot|mobile) ]]; then
  echo "Recommended Model: Small Language Model (SLM)"
  echo "Examples: Phi-3, Llama 3 8B, Gemma 2B"
  echo "Why: Fits in limited VRAM and runs without internet."
elif [[ "$GOAL" =~ (throughput|latency|simple|sentiment) ]]; then
  echo "Recommended Model: Small Language Model (SLM)"
  echo "Examples: Claude 3 Haiku, Gemini 1.5 Flash"
  echo "Why: Economically viable and fast for high-volume simple tasks."
else
  echo "Recommended Workflow: Start Big (LLM) -> Build Evals -> Scale Down (SLM)"
fi
