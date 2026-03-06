#!/bin/bash
# YouTube Summarizer
URL="$1"
if [ -z "$URL" ]; then
    echo "Usage: $0 <youtube_url>"
    return 1 2>/dev/null || true
fi
echo "Fetching transcript and summarizing video: $URL"
