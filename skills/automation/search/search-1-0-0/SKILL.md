---
name: search-1-0-0
description: "Search the web for real-time information."
metadata:
  openclaw:
    category: "search"
    tags: ['search', 'discovery', 'finding']
    version: "1.0.0"
---

# web-search

@command(web_search)
Usage: web_search --query <query>
Run: curl -s "https://ddg-api.herokuapp.com/search?q={{query}}"