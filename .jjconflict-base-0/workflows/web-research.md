# Workflow: Web Research

**Purpose**: Conduct deep research on a topic using browser automation to bypass limitations of simple text search.

## Phase 1: Reconnaissance
1.  **Search**: Use `web_search` to identify high-value targets (documentation, forums, GitHub repos).
2.  **Filter**: Select the top 3-5 most relevant URLs.

## Phase 2: Deep Dive
*For each URL:*
1.  **Navigate**: Open the page.
2.  **Extract**: Read the main content. Use `read_page` or `extract_content`.
3.  **Synthesize**: Summarize key findings relative to the research goal.

## Phase 3: Synthesis
1.  **Compile**: Aggregate findings into a structured report.
2.  **Cite**: Ensure every claim has a source URL.
3.  **Verify**: If conflicting info exists, perform a tie-breaker search.

## Output
A markdown report containing:
- Executive Summary
- Key Findings
- Code Examples (if applicable)
- Source Links
