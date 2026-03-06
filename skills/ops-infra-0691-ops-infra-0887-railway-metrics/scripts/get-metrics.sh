#!/bin/bash
ENV_ID="$1"
SERVICE_ID="$2"

if [ -z "$ENV_ID" ]; then
    echo "Usage: $0 <environment-id> [service-id]"
else
    START_DATE=$(date -u -v-1H +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || date -u -d "1 hour ago" +"%Y-%m-%dT%H:%M:%SZ")

    if [ -z "$SERVICE_ID" ]; then
        VARS=$(jq -n \
          --arg env "$ENV_ID" \
          --arg start "$START_DATE" \
          '{environmentId: $env, startDate: $start, measurements: ["CPU_USAGE", "MEMORY_USAGE_GB"], groupBy: ["SERVICE_ID"]}')
    else
        VARS=$(jq -n \
          --arg env "$ENV_ID" \
          --arg svc "$SERVICE_ID" \
          --arg start "$START_DATE" \
          '{environmentId: $env, serviceId: $svc, startDate: $start, measurements: ["CPU_USAGE", "MEMORY_USAGE_GB"]}')
    fi

    SCRIPT_DIR="${CLAUDE_PLUGIN_ROOT:-.}/skills/lib/railway-api.sh"

    if [ -f "$SCRIPT_DIR" ]; then
        if [ -z "$SERVICE_ID" ]; then
            bash "$SCRIPT_DIR" \
              'query metrics($environmentId: String!, $startDate: DateTime!, $measurements: [MetricMeasurement!]!, $groupBy: [MetricTag!]) {
                metrics(environmentId: $environmentId, startDate: $startDate, measurements: $measurements, groupBy: $groupBy) {
                  measurement
                  tags { serviceId region }
                  values { ts value }
                }
              }' \
              "$VARS"
        else
            bash "$SCRIPT_DIR" \
              'query metrics($environmentId: String!, $serviceId: String, $startDate: DateTime!, $measurements: [MetricMeasurement!]!) {
                metrics(environmentId: $environmentId, serviceId: $serviceId, startDate: $startDate, measurements: $measurements) {
                  measurement
                  tags { deploymentId region serviceId }
                  values { ts value }
                }
              }' \
              "$VARS"
        fi
    else
        echo "Railway API helper script not found at $SCRIPT_DIR"
        echo "Variables payload would be: $VARS"
    fi
fi
