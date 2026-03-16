#!/bin/bash

curl -s -X POST http://localhost:8888/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Checking security updates from sources"}' \
  > /dev/null 2>&1 &
