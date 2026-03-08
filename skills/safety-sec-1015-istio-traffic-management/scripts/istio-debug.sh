#!/bin/bash
# Script to run common Istio debugging commands

if [ -z "$1" ]; then
    echo "Usage: $0 <deployment-name> [namespace]"
    exit 1
fi

DEPLOYMENT=$1
NAMESPACE=${2:-default}

echo "Analyzing Istio configuration..."
istioctl analyze -n "$NAMESPACE"

echo -e "\n--- Proxy Config Routes ---"
istioctl proxy-config routes "deploy/$DEPLOYMENT" -n "$NAMESPACE" -o json | head -n 20

echo -e "\n--- Proxy Config Endpoints ---"
istioctl proxy-config endpoints "deploy/$DEPLOYMENT" -n "$NAMESPACE" | head -n 20

echo -e "\n--- Cluster Health (istioctl proxy-status) ---"
istioctl proxy-status
