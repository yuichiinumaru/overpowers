#!/bin/bash
PROJECT_DIR=${PROJECT_DIR:-$HOME/agentic_paper_digest}
cd "$PROJECT_DIR" && python3 main.py "$@"
