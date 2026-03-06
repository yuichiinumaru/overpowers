#!/bin/bash
# Script to scaffold Istio traffic management YAML files from templates

TEMPLATE_DIR="$(dirname "$0")/../"
SKILL_MD="$TEMPLATE_DIR/SKILL.md"

if [ -z "$1" ]; then
    echo "Usage: $0 <output-file> [template-type]"
    echo "Templates: routing, canary, circuit-breaker, retry, mirror, fault, gateway"
    exit 1
fi

OUTPUT_FILE=$1
TYPE=${2:-routing}

echo "Scaffolding Istio $TYPE template to $OUTPUT_FILE..."

case $TYPE in
    routing)
        sed -n '/### Template 1: Basic Routing/,/###/p' "$SKILL_MD" | sed '1d;$d' | sed '/^```yaml/d;/^```$/d' > "$OUTPUT_FILE"
        ;;
    canary)
        sed -n '/### Template 2: Canary Deployment/,/###/p' "$SKILL_MD" | sed '1d;$d' | sed '/^```yaml/d;/^```$/d' > "$OUTPUT_FILE"
        ;;
    circuit-breaker)
        sed -n '/### Template 3: Circuit Breaker/,/###/p' "$SKILL_MD" | sed '1d;$d' | sed '/^```yaml/d;/^```$/d' > "$OUTPUT_FILE"
        ;;
    retry)
        sed -n '/### Template 4: Retry and Timeout/,/###/p' "$SKILL_MD" | sed '1d;$d' | sed '/^```yaml/d;/^```$/d' > "$OUTPUT_FILE"
        ;;
    mirror)
        sed -n '/### Template 5: Traffic Mirroring/,/###/p' "$SKILL_MD" | sed '1d;$d' | sed '/^```yaml/d;/^```$/d' > "$OUTPUT_FILE"
        ;;
    fault)
        sed -n '/### Template 6: Fault Injection/,/###/p' "$SKILL_MD" | sed '1d;$d' | sed '/^```yaml/d;/^```$/d' > "$OUTPUT_FILE"
        ;;
    gateway)
        sed -n '/### Template 7: Ingress Gateway/,/##/p' "$SKILL_MD" | sed '1d;$d' | sed '/^```yaml/d;/^```$/d' > "$OUTPUT_FILE"
        ;;
    *)
        echo "Error: Unknown template type $TYPE"
        exit 1
        ;;
esac

echo "Done. Please customize $OUTPUT_FILE for your environment."
