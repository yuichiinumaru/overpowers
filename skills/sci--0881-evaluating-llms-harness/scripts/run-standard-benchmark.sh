#!/bin/bash
# Run a standard suite of benchmarks on a model
# Usage: ./run-standard-benchmark.sh <model_name> [output_path]

MODEL=$1
OUTPUT=${2:-results/$(echo $MODEL | sed 's/\//-/g').json}

if [ -z "$MODEL" ]; then
    echo "Usage: ./run-standard-benchmark.sh <model_name> [output_path]"
    exit 1
fi

mkdir -p $(dirname $OUTPUT)

echo "Evaluating $MODEL on standard suite: mmlu, gsm8k, hellaswag, truthfulqa, arc_challenge"

lm_eval --model hf \
  --model_args pretrained=$MODEL \
  --tasks mmlu,gsm8k,hellaswag,truthfulqa,arc_challenge \
  --num_fewshot 5 \
  --batch_size auto \
  --output_path $OUTPUT

echo "Results saved to $OUTPUT"
