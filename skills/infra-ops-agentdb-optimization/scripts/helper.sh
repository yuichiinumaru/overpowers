#!/bin/bash

# Comprehensive performance benchmarking
npx agentdb@latest benchmark

# Results show:
# ✅ Pattern Search: 150x faster (100µs vs 15ms)
# ✅ Batch Insert: 500x faster (2ms vs 1s for 100 vectors)
# ✅ Large-scale Query: 12,500x faster (8ms vs 100s at 1M vectors)
# ✅ Memory Efficiency: 4-32x reduction with quantization

# Get comprehensive stats
npx agentdb@latest stats .agentdb/vectors.db

# Output:
# Total Patterns: 125,430
# Database Size: 47.2 MB (with binary quantization)
# Avg Confidence: 0.87
# Domains: 15
# Cache Hit Rate: 84%
# Index Type: HNSW

# Check database size
npx agentdb@latest stats .agentdb/vectors.db

# Enable quantization
# Use 'binary' for 32x reduction
