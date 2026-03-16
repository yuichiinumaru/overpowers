#!/bin/bash
set -euo pipefail

# Check AWS VPN connections
echo "[*] Checking AWS VPN connections..."
if command -v aws &> /dev/null; then
    aws ec2 describe-vpn-connections --query 'VpnConnections[*].{ID:VpnConnectionId,State:State,Type:Type}' --output table || echo "Failed to fetch AWS VPNs or no access"
else
    echo "[-] AWS CLI not installed"
fi

# Check Azure VPN connections
echo -e "\n[*] Checking Azure VPN connections..."
if command -v az &> /dev/null; then
    az network vpn-connection list -o table || echo "Failed to fetch Azure VPNs or no access"
else
    echo "[-] Azure CLI not installed"
fi

echo -e "\n[*] VPN connection check complete."
