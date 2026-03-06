#!/bin/bash
# Extract metrics from benchmark evaluation

if [ ! -f "tests/benchmark/prediction/opendataloader/evaluation.json" ]; then
    echo "Error: tests/benchmark/prediction/opendataloader/evaluation.json not found."
    return 1
fi

jq '{summary, metrics, table_detection, speed}' tests/benchmark/prediction/opendataloader/evaluation.json
