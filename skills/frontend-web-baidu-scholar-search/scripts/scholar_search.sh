#!/bin/bash
# Baidu Scholar Search Skill Implementation

set -e

# Check if required environment variable is set
if [ -z "$BAIDU_API_KEY" ]; then
    echo '{"error": "BAIDU_API_KEY environment variable not set"}'
    exit 1
fi

WD="$1"
if [ -z "$WD" ]; then
    echo '{"error": "Missing wd parameter"}'
    exit 1
fi
pageNum="$2"
if [ -z "$pageNum" ]; then
    pageNum=0
fi
enable_abstract="$3"
if [ -z "$enable_abstract" ]; then
    enable_abstract=false
fi

curl -s -XGET "https://qianfan.baidubce.com/v2/tools/baidu_scholar/search?wd=$WD&pageNum=$pageNum&enable_abstract=$enable_abstract" \
     -H "Authorization: Bearer $BAIDU_API_KEY" 
