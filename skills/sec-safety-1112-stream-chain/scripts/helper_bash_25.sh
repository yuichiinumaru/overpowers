#!/bin/bash

claude-flow stream_chain run \
  "Generate initial implementation" \
  "Review and identify issues" \
  "Refine based on issues found" \
  "Final quality check"
