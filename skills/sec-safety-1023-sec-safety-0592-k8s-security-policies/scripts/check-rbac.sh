#!/bin/bash
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: check-rbac.sh <verb> <resource> [namespace] [serviceaccount]"
  # exit 1
fi
VERB=$1
RESOURCE=$2
NS=${3:-default}
SA=${4:-default}

echo "Checking if $SA in $NS can $VERB $RESOURCE..."
kubectl auth can-i "$VERB" "$RESOURCE" -n "$NS" --as "system:serviceaccount:$NS:$SA"
