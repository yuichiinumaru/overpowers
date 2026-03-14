# Technical Design: Moltbot Memory Hybrid Search

## 1. Architecture Overview
The hybrid search feature will be implemented as a new method within the `MemoryIndexManager` class in `services/memory-index/memory-index-manager.ts`. This class already manages a SQLite database with `FTS5` for keyword search and `sqlite-vec` for vector search. The hybrid search will orchestrate these two methods and combine their results.

## 2. API Signatures & Data Contracts

### MemoryIndexManager Changes
```typescript
public async hybridSearch(query: string, embedding: Float32Array, limit: number = 10): Promise<SearchResult[]>
```

### Data Structures
```typescript
interface SearchResult {
  id: number;
  file_path: string;
  content: string;
  metadata: string;
  score: number; // Combined hybrid score
}
```

## 3. Database & Schema Changes
- No new tables are required.
- The existing `chunks_vec` and `chunks_fts` tables will be used.
- The `chunks_vec` table uses `vec0` from `sqlite-vec`.

## 4. System Dependencies
- `sqlite-vec`: Already present in `package.json`.
- `better-sqlite3`: Already present.

## 5. Security & Performance Considerations
- **Security Implications:** No new security risks as it uses existing data access patterns.
- **Performance Impact:** Running two searches instead of one will increase latency. However, since they are local SQLite queries, the impact should be minimal. We will limit the individual search results before combining them to keep performance high.
- **Error Handling:** The system should fall back to either keyword search or vector search if one of them fails (e.g., if embeddings are not available).

## 6. Testing Strategy
- **Unit Tests:** Test the `hybridSearch` method with mock results from `searchKeyword` and `searchVector` to verify the RRF calculation.
- **Integration Tests:** Use the `services/memory-index/test-memory.ts` script (or a new one) to index sample data and perform hybrid searches.
- **E2E/Manual Verification:** Compare search results for specific queries to ensure hybrid search provides more relevant results than either method alone.
