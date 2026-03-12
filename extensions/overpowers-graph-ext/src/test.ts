import fs from 'node:fs/promises';
import path from 'node:path';
import { GraphEngine } from './graph-engine';

async function main() {
  const graphPath = path.join(__dirname, '..', 'overpowers-graph.json');
  
  console.log('--- 1. Loading Precomputed Graph ---');
  const graphData = JSON.parse(await fs.readFile(graphPath, 'utf-8'));
  const engine = new GraphEngine(graphData);
  
  console.log('Graph loaded into memory (0ms latency in production)\n');

  console.log('--- 2. Semantic Search ---');
  const query = "penetration test pipeline";
  console.log(`Query: "${query}"`);
  const searchResults = engine.search(query);
  console.log(`Found best match: ${searchResults[0]?.id} (${searchResults[0]?.type})\n`);

  console.log('--- 3. Graph RAG Traversal ---');
  console.log(`Resolving dependencies for: ${searchResults[0]?.id}...`);
  const resolution = engine.resolveDependencies(searchResults[0]?.id, 2);
  
  if (resolution) {
    console.log(`\n🎯 TARGET INTENT: ${resolution.target.id} [${resolution.target.domain} Domain]`);
    console.log(`   Description: ${resolution.target.description}`);
    
    console.log(`\n🔗 AUTO-INJECTED CONTEXT (Dependencies):`);
    resolution.contextNodes.forEach(node => {
      console.log(`   -> [${node.type.toUpperCase()}] ${node.id}: ${node.description}`);
    });
  }
}

main().catch(console.error);