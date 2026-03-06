#!/bin/bash

# Gathers host security context for the healthcheck skill (read-only)

echo "🔍 Gathering host context..."

echo "--- OS Information ---"
uname -a
if [ -f /etc/os-release ]; then
    cat /etc/os-release
elif command -v sw_vers &> /dev/null; then
    sw_vers
fi

echo -e "\n--- Listening Ports ---"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    ss -ltnp 2>/dev/null || netstat -ltnp 2>/dev/null
elif [[ "$OSTYPE" == "darwin"* ]]; then
    lsof -nP -iTCP -sTCP:LISTEN
fi

echo -e "\n--- Firewall Status ---"
if command -v ufw &> /dev/null; then
    ufw status
elif command -v firewall-cmd &> /dev/null; then
    firewall-cmd --state
elif [[ "$OSTYPE" == "darwin"* ]]; then
    /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
fi

echo -e "\n--- OpenClaw Security Audit ---"
if command -v openclaw &> /dev/null; then
    openclaw security audit --deep
else
    echo "openclaw command not found"
fi

echo -e "\n--- OpenClaw Update Status ---"
if command -v openclaw &> /dev/null; then
    openclaw update status
fi
