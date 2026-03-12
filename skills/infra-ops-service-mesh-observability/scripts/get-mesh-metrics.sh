#!/bin/bash

# Helper script to output common Service Mesh PromQL queries
# Usage: ./get-mesh-metrics.sh <metric_type> <service_name>

TYPE=$1
SERVICE=$2

if [[ -z "$TYPE" ]]; then
  echo "Usage: $0 <type> [service_name]"
  echo "Types: rps, error-rate, p99, connections"
  exit 1
fi

case $TYPE in
  rps)
    QUERY="sum(rate(istio_requests_total{reporter=\"destination\""
    [[ -n "$SERVICE" ]] && QUERY+=",destination_service_name=\"$SERVICE\""
    QUERY+="}[5m])) by (destination_service_name)"
    ;;
  error-rate)
    QUERY="sum(rate(istio_requests_total{reporter=\"destination\", response_code=~\"5..\""
    [[ -n "$SERVICE" ]] && QUERY+=",destination_service_name=\"$SERVICE\""
    QUERY+="}[5m])) / sum(rate(istio_requests_total{reporter=\"destination\""
    [[ -n "$SERVICE" ]] && QUERY+=",destination_service_name=\"$SERVICE\""
    QUERY+="}[5m])) * 100"
    ;;
  p99)
    QUERY="histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket{reporter=\"destination\""
    [[ -n "$SERVICE" ]] && QUERY+=",destination_service_name=\"$SERVICE\""
    QUERY+="}[5m])) by (le, destination_service_name))"
    ;;
  connections)
    QUERY="sum(istio_tcp_connections_opened_total{reporter=\"destination\""
    [[ -n "$SERVICE" ]] && QUERY+=",destination_service_name=\"$SERVICE\""
    QUERY+="}) by (destination_service_name)"
    ;;
  *)
    echo "Invalid type: $TYPE."
    exit 1
    ;;
esac

echo "PromQL Query:"
echo "$QUERY"
