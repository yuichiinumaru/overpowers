#!/bin/bash
# Expected usage: ./monitor-experiment.sh <experiment-id>
if [ -z "$1" ]; then echo 'Missing experiment ID'; exit 1; fi
while true; do
  STATUS=$(beaker experiment get $1 --format json | jq -r '.status.exited')
  if [ "$STATUS" = "true" ]; then echo 'Experiment complete'; beaker experiment logs $1; break; fi
  echo 'Still running...'
  sleep 30
done
