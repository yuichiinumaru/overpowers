#!/bin/bash
# cf_cache_purge.sh - Script to purge Cloudflare cache

ZONE_ID=${CLOUDFLARE_ZONE_ID}
TOKEN=${CLOUDFLARE_API_TOKEN}

if [ -z "$ZONE_ID" ] || [ -z "$TOKEN" ]; then
    echo "Error: CLOUDFLARE_ZONE_ID and CLOUDFLARE_API_TOKEN environment variables must be set."
    # removed exit
else
    echo "Purging all cache for zone $ZONE_ID..."

    curl -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" \
         -H "Authorization: Bearer $TOKEN" \
         -H "Content-Type: application/json" \
         --data '{"purge_everything":true}'

    echo -e "\nCache purge requested."
fi
