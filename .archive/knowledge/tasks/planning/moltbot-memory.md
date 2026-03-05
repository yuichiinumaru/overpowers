# Moltbot Memory Architecture Research

**Source**: `references/moltbot/src/memory/`

## Overview
Moltbot uses a hybrid memory system combining **Vector Search** (via `sqlite-vec`) and **Keyword Search** (via SQLite FTS5) to index codebase files and chat session transcripts.

## Key Components

### 1. Storage (`sqlite-vec`)
*   **Database**: SQLite file.
*   **Tables**:
    *   `files`: Tracks indexed files (path, hash, mtime).
    *   `chunks`: Stores text chunks and metadata.
    *   `chunks_vec` (Virtual Table): Stores vector embeddings using `vec0` extension.
    *   `chunks_fts` (Virtual Table): Stores text for keyword search.
    *   `embedding_cache`: Caches embeddings to save tokens/cost.

### 2. Embedding Providers
*   **OpenAI**: Supports batch processing (`v1/embeddings` batch API).
*   **Gemini**: Supports batch processing (`RETRIEVAL_DOCUMENT` task type).
*   **Local**: Can fallback to local models (though `sqlite-vec` usually pairs with external APIs in this config).

### 3. Indexing Strategy
*   **Chunking**: Markdown-aware chunking (headers, paragraphs).
*   **File Watching**: Uses `chokidar` to watch `MEMORY.md` and configured paths.
*   **Session Indexing**: Indexes `sessions/*.jsonl` files to make past conversations searchable.
*   **Batching**: Heavily uses batch APIs for performance and cost reduction.

### 4. Search Algorithm (Hybrid)
*   **Vector Search**: Finds semantic matches.
*   **Keyword Search**: Finds exact term matches (BM25 ranking).
*   **Fusion**: Merges results using Reciprocal Rank Fusion (RRF) or weighted scoring (`vectorWeight`, `textWeight`).

## Implementation Notes for Overpowers
To adopt this, we would need:
1.  **Dependencies**: `sqlite-vec`, `better-sqlite3` (or `node:sqlite`), `chokidar`.
2.  **Infrastructure**: A persistent SQLite DB location.
3.  **Secrets**: API keys for embedding providers.

## Recommendation
This is a robust system but requires significant infrastructure setup. For now, we can rely on `explore-recon` (grep-based) and `librarian` (web/search-based) agents. If we need long-term memory, we should port the `MemoryIndexManager` class and its dependencies.
