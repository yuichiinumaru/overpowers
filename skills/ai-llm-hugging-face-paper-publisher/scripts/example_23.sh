# 1. Check if paper exists
uv run scripts/paper_manager.py check --arxiv-id "2301.12345"

# 2. Index if needed
uv run scripts/paper_manager.py index --arxiv-id "2301.12345"

# 3. Link to multiple repositories
uv run scripts/paper_manager.py link \
  --repo-id "username/model-v1" \
  --repo-type "model" \
  --arxiv-id "2301.12345"

uv run scripts/paper_manager.py link \
  --repo-id "username/training-data" \
  --repo-type "dataset" \
  --arxiv-id "2301.12345"

uv run scripts/paper_manager.py link \
  --repo-id "username/demo-space" \
  --repo-type "space" \
  --arxiv-id "2301.12345"
