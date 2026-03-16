#!/bin/bash
# Create a Writing Plan
PLAN_NAME="${1:-my_plan.md}"
echo "Creating writing plan $PLAN_NAME"
echo "# Writing Plan" > "$PLAN_NAME"
echo "Plan saved to $PLAN_NAME"
