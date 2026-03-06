#!/bin/bash
set -e

# Checks basic labarchive configuration via env vars
# Requires LABARCHIVE_API_TOKEN, LABARCHIVE_REGION

if [ -z "$LABARCHIVE_API_TOKEN" ]; then
    echo "Error: LABARCHIVE_API_TOKEN environment variable is not set."
    exit 1
fi

if [ -z "$LABARCHIVE_REGION" ]; then
    echo "Warning: LABARCHIVE_REGION environment variable is not set, defaulting to 'US'."
    LABARCHIVE_REGION="US"
fi

if [ "$LABARCHIVE_REGION" == "US" ]; then
    BASE_URL="https://api.labarchives.com/api"
elif [ "$LABARCHIVE_REGION" == "EU" ]; then
    BASE_URL="https://api.eu.labarchives.com/api"
elif [ "$LABARCHIVE_REGION" == "AU" ]; then
    BASE_URL="https://api.au.labarchives.com/api"
else
    echo "Error: Invalid LABARCHIVE_REGION. Valid options are: US, EU, AU."
    exit 1
fi

echo "Checking LabArchives connection for region $LABARCHIVE_REGION ($BASE_URL)..."

# Test API connectivity using a generic test endpoint if available,
# or simply getting notebooks.
# Here we try to get a list of notebooks.
response=$(curl -s -w "%{http_code}" -X GET "${BASE_URL}/notebooks" \
    -H "Authorization: Bearer $LABARCHIVE_API_TOKEN" \
    -H "Accept: application/json")

http_status="${response:${#response}-3}"

if [ "$http_status" == "200" ]; then
    echo "Connection successful. Token is valid."
elif [ "$http_status" == "401" ] || [ "$http_status" == "403" ]; then
    echo "Error: Authentication failed ($http_status). Check your LABARCHIVE_API_TOKEN."
    exit 1
else
    echo "Warning: Unexpected response ($http_status). Check connection and configuration."
    exit 1
fi
