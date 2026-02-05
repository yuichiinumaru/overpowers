#!/bin/bash

# Copyright (C) 2025 David Dallet
# Under permissive open source license known as "BSD 3-Clause License", see LICENSE file

# Configuration
PROCESS_NAME="language_server_linux"
ENDPOINT="/exa.language_server_pb.LanguageServerService/GetUserStatus"
BODY='{"metadata": {"ideName": "antigravity", "extensionName": "antigravity", "locale": "en"}}'

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

log() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

debug() {
    echo -e "${YELLOW}[DEBUG]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

# 1. Find Process ID and CSRF Token
log "Searching for Antigravity process..."
# Get PID and args, filter by name, exclude grep itself
PROCESS_INFO=$(ps -eo pid,args | grep "$PROCESS_NAME" | grep -v grep | head -n 1)

if [ -z "$PROCESS_INFO" ]; then
    error "Could not find running '$PROCESS_NAME' process. Is VS Code open?"
fi

PID=$(echo "$PROCESS_INFO" | awk '{print $1}')
# Extract token using grep with PCRE (-P) if available, or sed
CSRF_TOKEN=$(echo "$PROCESS_INFO" | grep -oP '(?<=--csrf_token )[a-f0-9-]+' || echo "$PROCESS_INFO" | sed -n 's/.*--csrf_token \([a-f0-9-]*\).*/\1/p')

if [ -z "$PID" ] || [ -z "$CSRF_TOKEN" ]; then
    error "Found process but failed to extract PID or CSRF token."
fi

log "Found PID: $PID"

# 2. Find Listening Ports
log "Scanning ports for PID $PID..."
if ! command -v lsof &> /dev/null; then
    error "lsof command not found. Please install lsof."
fi

# Get listening TCP ports, parse out the port number
# Redirect stderr to /dev/null to suppress warnings
PORTS=$(lsof -a -P -n -p "$PID" -iTCP -sTCP:LISTEN 2>/dev/null | awk 'NR>1 {print $9}' | awk -F: '{print $NF}' | sort -u)

if [ -z "$PORTS" ]; then
    error "No listening ports found for PID $PID."
fi

# 3. Try Ports
log "Candidate ports: $(echo $PORTS | tr '\n' ' ')"

for PORT in $PORTS; do
    # Construct the curl command string for display
    CURL_CMD="curl -s -k -X POST -H \"Content-Type: application/json\" -H \"Connect-Protocol-Version: 1\" -H \"X-Codeium-Csrf-Token: $CSRF_TOKEN\" -d '$BODY' \"https://127.0.0.1:$PORT$ENDPOINT\""

    debug "Trying command:\n$CURL_CMD"

    # Perform Request
    RESPONSE=$(eval "$CURL_CMD")

    # Check if response looks like JSON and not an HTML error page or empty
    if [[ $RESPONSE == *"userStatus"* ]]; then
        log "Success on port $PORT!"
        echo "----------------------------------------"
        echo "$RESPONSE"
        echo "----------------------------------------"
        exit 0
    fi
done

error "Could not connect to any port. The API might have changed or is unreachable."
