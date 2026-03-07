import { MemoryIndexManager, ChunkMetadata } from './memory-index-manager.js';
import * as path from 'path';
import * as fs from 'fs';

const DB_PATH = path.join(process.cwd(), '.agents', 'moltbot_memory.db');

// Ensure clean start
if (fs.existsSync(DB_PATH)) fs.unlinkSync(DB_PATH);

async function main() {
  const manager = new MemoryIndexManager(DB_PATH);

  // 1. Store File
  manager.storeFile('src/index.ts', 'console.log("hello world");', 'hash123', Date.now());

  // 2. Store Chunk
  const metadata: ChunkMetadata = { type: 'code', startLine: 1, endLine: 1 };
  const chunkId = manager.storeChunk('src/index.ts', 'console.log("hello world");', metadata);
  console.log(`Stored chunk ID: ${chunkId}`);

  // 3. Store FTS automatically via trigger, test Keyword Search
  const keywordResults = manager.searchKeyword('hello');
  console.log('Keyword Search Results:', keywordResults);

  // 4. Store Embedding
  const dummyEmbedding = new Float32Array(1536);
  dummyEmbedding[0] = 0.5; // Dummy value
  manager.storeEmbedding(chunkId, dummyEmbedding);

  // 5. Search Vector
  const vectorResults = manager.searchVector(dummyEmbedding, 1);
  console.log('Vector Search Results:', vectorResults);

  manager.close();

  console.log('Memory test complete. Verifying persistence...');

  // Verify persistence across sessions
  const manager2 = new MemoryIndexManager(DB_PATH);
  const persistentResults = manager2.searchKeyword('world');
  console.log('Persistent Keyword Search Results:', persistentResults);

  const persistentFile = manager2.getFile('src/index.ts');
  console.log('Persistent File retrieval:', persistentFile);

  manager2.close();
}

main().catch(console.error);
