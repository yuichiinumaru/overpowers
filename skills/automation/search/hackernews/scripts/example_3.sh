# Basic search
scripts/hn.sh search "rust programming"

# With filters
scripts/hn.sh search "LLM" --type story --sort date --period week --limit 5
scripts/hn.sh search "hiring remote" --type comment --period month
