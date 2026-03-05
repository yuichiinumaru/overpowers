#!/bin/bash
# Helper script for Serper search
# Usage: ./search.sh <query> [type] [tbs] [page]

QUERY=$1
TYPE=${2:-search}
TBS=${3:-qdr:m}
PAGE=${4:-1}

if [ -z "$QUERY" ]; then
  echo "Usage: $0 <query> [type] [tbs] [page]"
  exit 1
fi

serperV search -q "$QUERY" -t "$TYPE" --tbs "$TBS" --page "$PAGE"
