#!/bin/bash
PROJECT_DIR=${PROJECT_DIR:-$HOME/agentic_paper_digest}
if [ -f "$PROJECT_DIR/api.pid" ]; then
  kill $(cat "$PROJECT_DIR/api.pid") && rm "$PROJECT_DIR/api.pid"
fi
