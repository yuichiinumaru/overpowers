#!/bin/bash
# Quick start for metasploit framework shell
echo "Starting Metasploit Framework..."
if command -v msfconsole &> /dev/null; then
    msfconsole -q
else
    echo "Error: msfconsole not found in PATH."
    return 1 2>/dev/null || true
fi
