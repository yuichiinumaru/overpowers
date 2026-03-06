#!/bin/bash
TIME=$1
if [ -z "$TIME" ]; then
    TIME="24h"
fi

echo "Summarizing GitHub activity for the last $TIME..."
echo "MOCK: 15 PRs merged, 3 Issues closed, 2 Discussions created."
