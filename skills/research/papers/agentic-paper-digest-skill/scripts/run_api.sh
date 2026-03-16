#!/bin/bash
PROJECT_DIR=${PROJECT_DIR:-$HOME/agentic_paper_digest}
cd "$PROJECT_DIR" && uvicorn app.main:app --host 127.0.0.1 --port 8000 &
echo $! > "$PROJECT_DIR/api.pid"
