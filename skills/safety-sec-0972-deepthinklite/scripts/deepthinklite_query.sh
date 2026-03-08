#!/bin/bash
# Wrapper for deepthinklite query

QUERY=$1
MODE=${2:-raw} # default to raw, can be summary-only
OUTDIR=${3:-./deepthinklite}

if [ -z "$QUERY" ]; then
    echo "Usage: \$0 \"<query>\" [raw|summary-only] [output_dir]"
else
    echo "Running deepthinklite query with mode: $MODE, out: $OUTDIR"
    deepthinklite query "$QUERY" --out "$OUTDIR" --source-mode "$MODE"
fi
