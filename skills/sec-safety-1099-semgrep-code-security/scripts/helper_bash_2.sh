#!/bin/bash

semgrep --config auto --sarif -o results.sarif .  # Output results in SARIF format
semgrep --config auto --json -o results.json .    # Output results in JSON format
semgrep --config auto --include="src/**" .        # Limit scan to specific directory
semgrep --config auto --exclude="tests/**" .      # Exclude specific directory
