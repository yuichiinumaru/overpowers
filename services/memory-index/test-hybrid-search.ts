import { MemoryIndexManager, ChunkMetadata } from './memory-index-manager.js';
import * as path from 'path';
import * as fs from 'fs';

const DB_PATH = path.join(process.cwd(), '.agents', 'moltbot_memory_hybrid_test.db');

// Ensure clean start
if (fs.existsSync(DB_PATH)) fs.unlinkSync(DB_PATH);

async function main() {
  const manager = new MemoryIndexManager(DB_PATH);
  
  console.log('--- Hybrid Search Test ---');
  
  // 1. Setup sample data
  const data = [
    { path: 'file1.ts', content: 'typescript is a typed superset of javascript', type: 'code' as const },
    { path: 'file2.ts', content: 'rust is a systems programming language', type: 'code' as const },
    { path: 'file3.md', content: 'coding agents are the future of software development', type: 'docs' as const },
    { path: 'file4.md', content: 'hybrid search combines fts and vector search', type: 'docs' as const },
  ];
  
  const chunkIds: number[] = [];
  for (const item of data) {
    manager.storeFile(item.path, item.content, 'hash', Date.now());
    const id = manager.storeChunk(item.path, item.content, { type: item.type });
    chunkIds.push(Number(id));
    
    // Create a unique embedding for each
    const embedding = new Float32Array(1536);
    // Use the index to make embeddings unique
    embedding[chunkIds.length - 1] = 1.0; 
    manager.storeEmbedding(id, embedding);
  }
  
  console.log(`Stored ${chunkIds.length} chunks with embeddings.`);
  
  // 2. Test Hybrid Search
  console.log('\nQuery: "programming agents"');
  // Dummy embedding matching "file3.md" (agents)
  const queryEmbedding = new Float32Array(1536);
  queryEmbedding[2] = 0.9; // Matches file3.md
  
  const results = await manager.hybridSearch('programming', queryEmbedding, 5);
  
  console.log('Hybrid Search Results:');
  results.forEach((res, i) => {
    console.log(`${i+1}. [Score: ${res.score?.toFixed(4)}] ${res.file_path}: ${res.content.substring(0, 50)}...`);
  });
  
  // 3. Verify RRF Logic
  // file2.ts matches "programming" via keyword (FTS rank 1)
  // file3.md matches queryEmbedding (Vector rank 1)
  // Both should be at the top.
  
  if (results.length > 0 && (results[0].file_path === 'file2.ts' || results[0].file_path === 'file3.md')) {
    console.log('\n✅ PASS: Top results matched expected files.');
  } else {
    console.log('\n❌ FAIL: Top results did not match expectations.');
  }

  manager.close();
}

main().catch(console.error);
