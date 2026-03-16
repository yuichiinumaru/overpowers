#!/bin/bash
# eval_all_models.sh
# Script to evaluate multiple models on specific tasks using lm_eval

TASKS="mmlu,gsm8k,hellaswag,truthfulqa"
MODELS_FILE="models.txt"

if [ ! -f "$MODELS_FILE" ]; then
    echo "Error: $MODELS_FILE not found."
    # Use return instead of exit to prevent bash session closing
    return 1 2>/dev/null || exit 1
fi

while read model; do
    echo "Evaluating $model"
    # Extract model name for output file
    model_name=$(echo $model | sed 's/\//-/g')

    lm_eval --model hf \
      --model_args pretrained=$model,dtype=bfloat16 \
      --tasks $TASKS \
      --num_fewshot 5 \
      --batch_size auto \
      --output_path results/$model_name.json
done < "$MODELS_FILE"
