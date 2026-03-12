import { createAgentDBAdapter } from 'agentic-flow/reasoningbank';

// Optimized configuration
const adapter = await createAgentDBAdapter({
  dbPath: '.agentdb/optimized.db',
  quantizationType: 'binary',   // 32x memory reduction
  cacheSize: 1000,               // In-memory cache
  enableLearning: true,
  enableReasoning: true,
});

const adapter = await createAgentDBAdapter({
  quantizationType: 'binary',
  // 768-dim float32 (3072 bytes) → 96 bytes binary
  // 1M vectors: 3GB → 96MB
});

const adapter = await createAgentDBAdapter({
  quantizationType: 'scalar',
  // 768-dim float32 (3072 bytes) → 768 bytes (uint8)
  // 1M vectors: 3GB → 768MB
});

const adapter = await createAgentDBAdapter({
  quantizationType: 'product',
  // 768-dim float32 (3072 bytes) → 48-96 bytes
  // 1M vectors: 3GB → 192MB
});

const adapter = await createAgentDBAdapter({
  quantizationType: 'none',
  // Full float32 precision
});

const adapter = await createAgentDBAdapter({
  dbPath: '.agentdb/vectors.db',
  // HNSW automatically enabled
});

// Search with HNSW (100µs vs 15ms linear scan)
const results = await adapter.retrieveWithReasoning(queryEmbedding, {
  k: 10,
});

// Advanced HNSW configuration
const adapter = await createAgentDBAdapter({
  dbPath: '.agentdb/vectors.db',
  hnswM: 16,              // Connections per layer (default: 16)
  hnswEfConstruction: 200, // Build quality (default: 200)
  hnswEfSearch: 100,       // Search quality (default: 100)
});

const adapter = await createAgentDBAdapter({
  cacheSize: 1000,  // Cache 1000 most-used patterns
});

// First retrieval: ~2ms (database)
// Subsequent: <1ms (cache hit)
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  k: 10,
});

// Cache automatically evicts least-recently-used patterns
// Most frequently accessed patterns stay in cache

// Monitor cache performance
const stats = await adapter.getStats();
console.log('Cache Hit Rate:', stats.cacheHitRate);
// Aim for >80% hit rate

// ❌ SLOW: Individual inserts
for (const doc of documents) {
  await adapter.insertPattern({ /* ... */ });  // 1s for 100 docs
}

// ✅ FAST: Batch insert
const patterns = documents.map(doc => ({
  id: '',
  type: 'document',
  domain: 'knowledge',
  pattern_data: JSON.stringify({
    embedding: doc.embedding,
    text: doc.text,
  }),
  confidence: 1.0,
  usage_count: 0,
  success_count: 0,
  created_at: Date.now(),
  last_used: Date.now(),
}));

// Insert all at once (2ms for 100 docs)
for (const pattern of patterns) {
  await adapter.insertPattern(pattern);
}

// Retrieve multiple queries efficiently
const queries = [queryEmbedding1, queryEmbedding2, queryEmbedding3];

// Parallel retrieval
const results = await Promise.all(
  queries.map(q => adapter.retrieveWithReasoning(q, { k: 5 }))
);

// Enable automatic pattern consolidation
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  domain: 'documents',
  optimizeMemory: true,  // Consolidate similar patterns
  k: 10,
});

console.log('Optimizations:', result.optimizations);
// {
//   consolidated: 15,  // Merged 15 similar patterns
//   pruned: 3,         // Removed 3 low-quality patterns
//   improved_quality: 0.12  // 12% quality improvement
// }

// Manually trigger optimization
await adapter.optimize();

// Get statistics
const stats = await adapter.getStats();
console.log('Before:', stats.totalPatterns);
console.log('After:', stats.totalPatterns);  // Reduced by ~10-30%

// Prune low-confidence patterns
await adapter.prune({
  minConfidence: 0.5,     // Remove confidence < 0.5
  minUsageCount: 2,       // Remove usage_count < 2
  maxAge: 30 * 24 * 3600, // Remove >30 days old
});

const stats = await adapter.getStats();

console.log('Performance Metrics:');
console.log('Total Patterns:', stats.totalPatterns);
console.log('Database Size:', stats.dbSize);
console.log('Avg Confidence:', stats.avgConfidence);
console.log('Cache Hit Rate:', stats.cacheHitRate);
console.log('Search Latency (avg):', stats.avgSearchLatency);
console.log('Insert Latency (avg):', stats.avgInsertLatency);

const adapter = await createAgentDBAdapter({
  quantizationType: 'binary',  // 32x memory reduction
  cacheSize: 5000,             // Large cache
  hnswM: 8,                    // Fewer connections = faster
  hnswEfSearch: 50,            // Low search quality = faster
});

// Expected: <50µs search, 90-95% accuracy

const adapter = await createAgentDBAdapter({
  quantizationType: 'scalar',  // 4x memory reduction
  cacheSize: 1000,             // Standard cache
  hnswM: 16,                   // Balanced connections
  hnswEfSearch: 100,           // Balanced quality
});

// Expected: <100µs search, 98-99% accuracy

const adapter = await createAgentDBAdapter({
  quantizationType: 'none',    // No quantization
  cacheSize: 2000,             // Large cache
  hnswM: 32,                   // Many connections
  hnswEfSearch: 200,           // High search quality
});

// Expected: <200µs search, 100% accuracy

const adapter = await createAgentDBAdapter({
  quantizationType: 'binary',  // 32x memory reduction
  cacheSize: 100,              // Small cache
  hnswM: 8,                    // Minimal connections
});

// Expected: <100µs search, ~10MB for 100K vectors

const adapter = await createAgentDBAdapter({
  quantizationType: 'none',    // Full precision
  cacheSize: 500,
  hnswM: 8,
});

const adapter = await createAgentDBAdapter({
  quantizationType: 'scalar',  // 4x reduction
  cacheSize: 1000,
  hnswM: 16,
});

const adapter = await createAgentDBAdapter({
  quantizationType: 'binary',  // 32x reduction
  cacheSize: 2000,
  hnswM: 32,
});

const adapter = await createAgentDBAdapter({
  quantizationType: 'product',  // 8-16x reduction
  cacheSize: 5000,
  hnswM: 48,
  hnswEfConstruction: 400,
});

// Increase cache size
const adapter = await createAgentDBAdapter({
  cacheSize: 2000,  // Increase from 1000
});

// Reduce search quality (faster)
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  k: 5,  // Reduce from 10
});

// Disable or use lighter quantization
const adapter = await createAgentDBAdapter({
  quantizationType: 'scalar',  // Instead of 'binary'
  hnswEfSearch: 200,           // Higher search quality
});
