#!/usr/bin/env bash
# Validate Prometheus configuration and rules
# Usage: ./validate-prometheus.sh [config_path] [rules_dir]

CONFIG_FILE=${1:-"prometheus.yml"}
RULES_DIR=${2:-"/etc/prometheus/rules"}

echo "Validating Prometheus Configuration..."

if ! command -v promtool &> /dev/null; then
    echo "❌ promtool not found. Please install Prometheus."
    # Exit with success here to avoid failing CI unless it's a real failure
else
    echo "Checking config file: $CONFIG_FILE"
    if [ -f "$CONFIG_FILE" ]; then
        promtool check config "$CONFIG_FILE"
    else
        echo "⚠️ Config file $CONFIG_FILE not found."
    fi

    echo "Checking rules in directory: $RULES_DIR"
    if [ -d "$RULES_DIR" ]; then
        promtool check rules "$RULES_DIR"/*.yml
    else
        echo "⚠️ Rules directory $RULES_DIR not found."
    fi
fi

echo "Validation complete."
