# Auto-generated example usage from SKILL.md

# results = EuropePMC_search_articles(
#     query="bacterial antibiotic resistance evolution",
#     limit=10,
#     extract_terms_from_fulltext=["ciprofloxacin", "meropenem", "A. baumannii", "MIC"]
# )
#
# # Check which articles have full-text snippets
# for article in results:
#     if "fulltext_snippets" in article:
#         # Snippets automatically extracted from OA full text
#         for snippet in article["fulltext_snippets"]:
#             # Use snippet["term"] and snippet["snippet"] for verification
#             pass

# # Step 1: Search
# papers = SemanticScholar_search_papers(
#     query="machine learning interpretability",
#     limit=10
# )
#
# # Step 2: Extract from specific OA papers
# for paper in papers:
#     if paper.get("open_access_pdf_url"):
#         snippets = SemanticScholar_get_pdf_snippets(
#             open_access_pdf_url=paper["open_access_pdf_url"],
#             terms=["SHAP", "gradient attribution", "layer-wise relevance"],
#             window_chars=300
#         )
#         if snippets["status"] == "success":
#             # Process snippets["snippets"]
#             pass

# # All arXiv papers are freely available
# snippets = ArXiv_get_pdf_snippets(
#     arxiv_id="2301.12345",
#     terms=["attention mechanism", "self-attention", "layer normalization"],
#     max_snippets_per_term=5
# )

# # For paywalled PDFs accessible via institution
# webpage_text = get_webpage_text_from_url(
#     url="https://doi.org/10.1016/...",
#     # Requires institutional proxy or VPN
# )
#
# # Extract relevant sections manually
# if "Methods" in webpage_text:
#     # Parse methods section
#     pass

# if article.get("open_access") and article.get("fulltext_xml_url"):
#     # Proceed with extraction
#     pass

# if "fulltext_snippets" not in article:
#     # Fallback: use abstract or skip
#     print(f"No full text available: {article['title']}")
