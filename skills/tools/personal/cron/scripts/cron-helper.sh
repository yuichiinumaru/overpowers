#!/bin/bash
# Helper script to simulate cron syntax validation or list cron expressions

if [ "$1" == "--help" ]; then
    echo "Usage: $0 [cron_expression]"
    echo "If provided, validates cron expression syntax. Otherwise prints a reference."
    exit 0
fi

if [ -n "$1" ]; then
    # Very basic validation just counting fields
    FIELDS=$(echo "$1" | awk '{print NF}')
    if [ "$FIELDS" -ne 5 ]; then
        echo "Invalid cron expression: expected 5 fields, got $FIELDS."
        exit 1
    else
        echo "Cron expression format seems valid (5 fields)."
    fi
else
    echo "Cron Expression Reference:"
    echo "0 9 * * *       | Every day at 9:00 AM"
    echo "0 9 * * MON     | Every Monday at 9:00 AM"
    echo "0 9 * * MON-FRI | Weekdays at 9:00 AM"
    echo "*/30 * * * *    | Every 30 minutes"
    echo "0 */2 * * *     | Every 2 hours"
    echo "0 0 1 * *       | 1st of every month at midnight"
    echo "0 18 * * FRI    | Every Friday at 6:00 PM"
    echo "0 9,18 * * *    | Every day at 9:00 AM and 6:00 PM"
fi
