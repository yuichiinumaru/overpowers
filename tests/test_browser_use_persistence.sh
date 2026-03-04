#!/bin/bash
set -e

# Activate virtual environment
source .venv/bin/activate

echo "Starting browser-use persistence test..."

# 1. Open a session and set a variable
echo "Step 1: Open session and set variable"
browser-use open https://example.com
browser-use python "x = 42"

# 2. Access the variable in a separate command
echo "Step 2: Access variable"
OUTPUT=$(browser-use python "print(f'Value of x is {x}')")

echo "Output received: $OUTPUT"

# 3. Verify
if [[ "$OUTPUT" == *"Value of x is 42"* ]]; then
    echo "SUCCESS: Persistence verified."
    exit 0
else
    echo "FAILURE: Persistence check failed."
    exit 1
fi
