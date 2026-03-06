# 1. Create research article
uv run scripts/paper_manager.py create \
  --template "modern" \
  --title "Novel Fine-Tuning Approach" \
  --output "paper.md"

# 2. Edit paper.md with your content

# 3. Submit to arXiv (external process)
# Upload to arxiv.org, get arXiv ID

# 4. Index on Hugging Face
uv run scripts/paper_manager.py index --arxiv-id "2301.12345"

# 5. Link to your model
uv run scripts/paper_manager.py link \
  --repo-id "your-username/your-model" \
  --repo-type "model" \
  --arxiv-id "2301.12345"

# 6. Claim authorship
uv run scripts/paper_manager.py claim \
  --arxiv-id "2301.12345" \
  --email "your.email@edu"
