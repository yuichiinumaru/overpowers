#!/bin/bash
REPO_URL="https://github.com/matanle51/agentic_paper_digest"
PROJECT_DIR=${PROJECT_DIR:-$HOME/agentic_paper_digest}
echo "Bootstrapping Agentic Paper Digest to $PROJECT_DIR..."
if [ ! -d "$PROJECT_DIR" ]; then
  git clone "$REPO_URL" "$PROJECT_DIR" || (echo "Git clone failed, attempting zip download..." && curl -L "$REPO_URL/archive/refs/heads/main.zip" -o digest.zip && unzip main.zip && mv agentic_paper_digest-main "$PROJECT_DIR" && rm main.zip)
fi
cd "$PROJECT_DIR" && pip install -r requirements.txt
