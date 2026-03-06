# Link multiple papers to one repository
for arxiv_id in "2301.12345" "2302.67890" "2303.11111"; do
  uv run scripts/paper_manager.py link \
    --repo-id "username/model-name" \
    --repo-type "model" \
    --arxiv-id "$arxiv_id"
done
