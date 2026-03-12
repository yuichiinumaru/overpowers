#!/bin/bash
# Helper script to simulate IOC enrichment via OpenClaw
ioc=$1

if [ -z "$ioc" ]; then
    echo "Usage: $0 <ip_or_domain>"
    return 1 2>/dev/null || true
fi

echo "Enriching IOC: $ioc"
# Simulated output
echo "Fetching Threat Intelligence for $ioc..."
echo "Result: Clean / No known malicious activity found."
