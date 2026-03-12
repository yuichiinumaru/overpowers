#!/bin/bash
# Helper script to generate Prometheus SLO recording and alerting rules based on a template.

# Default values
SERVICE_NAME="http_api"
SLO_TARGET="0.999"
WINDOW="28d"
OUTPUT_FILE="slo_rules.yml"

show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "Generates Prometheus SLO recording and alerting rules."
    echo ""
    echo "Options:"
    echo "  -s, --service    Service name (default: http_api)"
    echo "  -t, --target     SLO target e.g. 0.999 for 99.9% (default: 0.999)"
    echo "  -w, --window     Time window (default: 28d)"
    echo "  -o, --output     Output file (default: slo_rules.yml)"
    echo "  -h, --help       Show this help message"
}

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -s|--service) SERVICE_NAME="$2"; shift ;;
        -t|--target) SLO_TARGET="$2"; shift ;;
        -w|--window) WINDOW="$2"; shift ;;
        -o|--output) OUTPUT_FILE="$2"; shift ;;
        -h|--help) show_help; return 0 ;;
        *) echo "Unknown parameter passed: $1"; show_help; return 1 ;;
    esac
    shift
done

echo "Generating SLO rules for $SERVICE_NAME with target $SLO_TARGET over $WINDOW..."

cat << 'YML' > "$OUTPUT_FILE"
groups:
  - name: REPLACEME_SERVICE_NAME_sli_rules
    interval: 30s
    rules:
      # Availability SLI (Example: successful requests / total requests)
      - record: sli:REPLACEME_SERVICE_NAME_availability:ratio
        expr: |
          sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME", status!~"5.."}[REPLACEME_WINDOW]))
          /
          sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME"}[REPLACEME_WINDOW]))

      # Latency SLI (Example: requests < 500ms)
      - record: sli:REPLACEME_SERVICE_NAME_latency:ratio
        expr: |
          sum(rate(http_request_duration_seconds_bucket{job="REPLACEME_SERVICE_NAME", le="0.5"}[REPLACEME_WINDOW]))
          /
          sum(rate(http_request_duration_seconds_count{job="REPLACEME_SERVICE_NAME"}[REPLACEME_WINDOW]))

  - name: REPLACEME_SERVICE_NAME_slo_rules
    interval: 5m
    rules:
      # SLO compliance
      - record: slo:REPLACEME_SERVICE_NAME_availability:compliance
        expr: sli:REPLACEME_SERVICE_NAME_availability:ratio >= bool REPLACEME_SLO_TARGET

      # Error budget remaining (percentage)
      - record: slo:REPLACEME_SERVICE_NAME_availability:error_budget_remaining
        expr: |
          (sli:REPLACEME_SERVICE_NAME_availability:ratio - REPLACEME_SLO_TARGET) / (1 - REPLACEME_SLO_TARGET) * 100

      # Error budget burn rate (5m)
      - record: slo:REPLACEME_SERVICE_NAME_availability:burn_rate_5m
        expr: |
          (1 - (
            sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME", status!~"5.."}[5m]))
            /
            sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME"}[5m]))
          )) / (1 - REPLACEME_SLO_TARGET)

      # Error budget burn rate (1h)
      - record: slo:REPLACEME_SERVICE_NAME_availability:burn_rate_1h
        expr: |
          (1 - (
            sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME", status!~"5.."}[1h]))
            /
            sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME"}[1h]))
          )) / (1 - REPLACEME_SLO_TARGET)

      # Error budget burn rate (6h)
      - record: slo:REPLACEME_SERVICE_NAME_availability:burn_rate_6h
        expr: |
          (1 - (
            sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME", status!~"5.."}[6h]))
            /
            sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME"}[6h]))
          )) / (1 - REPLACEME_SLO_TARGET)

      # Error budget burn rate (30m)
      - record: slo:REPLACEME_SERVICE_NAME_availability:burn_rate_30m
        expr: |
          (1 - (
            sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME", status!~"5.."}[30m]))
            /
            sum(rate(http_requests_total{job="REPLACEME_SERVICE_NAME"}[30m]))
          )) / (1 - REPLACEME_SLO_TARGET)

  - name: REPLACEME_SERVICE_NAME_slo_alerts
    interval: 1m
    rules:
      # Fast burn: 14.4x rate, 1 hour window
      - alert: REPLACEME_SERVICE_NAMESLOErrorBudgetBurnFast
        expr: |
          slo:REPLACEME_SERVICE_NAME_availability:burn_rate_1h > 14.4
          and
          slo:REPLACEME_SERVICE_NAME_availability:burn_rate_5m > 14.4
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Fast error budget burn detected for REPLACEME_SERVICE_NAME"
          description: "Error budget burning at {{ $value }}x rate"

      # Slow burn: 6x rate, 6 hour window
      - alert: REPLACEME_SERVICE_NAMESLOErrorBudgetBurnSlow
        expr: |
          slo:REPLACEME_SERVICE_NAME_availability:burn_rate_6h > 6
          and
          slo:REPLACEME_SERVICE_NAME_availability:burn_rate_30m > 6
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Slow error budget burn detected for REPLACEME_SERVICE_NAME"
          description: "Error budget burning at {{ $value }}x rate"

      # Error budget exhausted
      - alert: REPLACEME_SERVICE_NAMESLOErrorBudgetExhausted
        expr: slo:REPLACEME_SERVICE_NAME_availability:error_budget_remaining < 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "SLO error budget exhausted for REPLACEME_SERVICE_NAME"
          description: "Error budget remaining: {{ $value }}%"
YML

sed -i "s/REPLACEME_SERVICE_NAME/$SERVICE_NAME/g" "$OUTPUT_FILE"
sed -i "s/REPLACEME_SLO_TARGET/$SLO_TARGET/g" "$OUTPUT_FILE"
sed -i "s/REPLACEME_WINDOW/$WINDOW/g" "$OUTPUT_FILE"

echo "Successfully generated $OUTPUT_FILE"
