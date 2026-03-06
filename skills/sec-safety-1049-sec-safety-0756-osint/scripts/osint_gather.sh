#!/bin/bash
# Helper script for basic OSINT data gathering
target=$1

if [ -z "$target" ]; then
    echo "Usage: $0 <domain_or_ip>"
    return 1 2>/dev/null || true
fi

echo "Gathering OSINT for $target..."
echo "Running whois..."
whois "$target" > "${target}_whois.txt" || echo "whois failed"
echo "Running nslookup..."
nslookup "$target" > "${target}_nslookup.txt" || echo "nslookup failed"
echo "OSINT gathering complete. Check *_whois.txt and *_nslookup.txt"
