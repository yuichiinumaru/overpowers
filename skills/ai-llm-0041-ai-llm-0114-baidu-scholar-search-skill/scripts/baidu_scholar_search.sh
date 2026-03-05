#!/bin/bash
# baidu_scholar_search.sh - Baidu Scholar Search CLI

KEYWORD=$1
PAGE=${2:-0}
INCLUDE_ABSTRACT=${3:-false}

if [ -z "$KEYWORD" ]; then
  echo "Usage: bash baidu_scholar_search.sh \"keyword\" [page_number] [include_abstract]"
  exit 1
fi

if [ -z "$BAIDU_API_KEY" ]; then
  echo "Error: BAIDU_API_KEY environment variable is not set."
  exit 1
fi

echo "Searching Baidu Scholar for: \"$KEYWORD\" (Page: $PAGE, Abstract: $INCLUDE_ABSTRACT)..."

curl -s -G "https://qianfan.baidubce.com/v2/tools/baidu_scholar/search" \
  --data-urlencode "wd=$KEYWORD" \
  --data "pageNum=$PAGE" \
  --data "enable_abstract=$INCLUDE_ABSTRACT" \
  -H "Authorization: Bearer $BAIDU_API_KEY" | jq .
