import fs from 'node:fs/promises';
import path from 'node:path';
import { GraphEngine } from './graph-engine';

/**
 * OVERPOWERS GRAPH RAG EXTENSION
 * This is the entrypoint designed to be plugged into the Gemini CLI.
 */

// Dummy types mirroring the @google/gemini-cli-core Extension API
interface ExtensionContext {
  registerTool(tool: any): void;
  logger: { info(msg: string): void, error(msg: string): void };
}

let graphEngine: GraphEngine | null = null;

export async function activate(context: ExtensionContext) {
  context.logger.info('Initializing Overpowers Graph RAG Extension...');
  
  try {
    const graphPath = path.join(__dirname, '..', 'overpowers-graph.json');
    const graphData = JSON.parse(await fs.readFile(graphPath, 'utf-8'));
    graphEngine = new GraphEngine(graphData);
    context.logger.info(`Successfully loaded Graph DB with ${Object.keys(graphData.nodes).length} nodes.`);
  } catch (e) {
    context.logger.error(`Failed to load graph data. Make sure to run the indexer first.`);
    return;
  }

  // Register the intelligent traversal tool
  context.registerTool({
    name: 'overpowers_resolve_intent',
    description: 'Resolve a user intent into a complete dependency graph of required skills, agents, and workflows from the Overpowers repository.',
    parameters: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'The natural language task or intent (e.g. "Security audit for API")'
        }
      },
      required: ['query']
    },
    async execute(params: { query: string }) {
      if (!graphEngine) throw new Error('Graph Engine not initialized.');
      
      const searchResults = graphEngine.search(params.query, 1);
      if (searchResults.length === 0) {
        return { llmContent: `No Overpowers capabilities found for "${params.query}".` };
      }

      const rootNode = searchResults[0];
      const resolution = graphEngine.resolveDependencies(rootNode.id, 2);

      if (!resolution) return { llmContent: 'Failed to resolve graph traversal.' };

      let contextStr = `🎯 TARGET CAPABILITY: ${resolution.target.id} (${resolution.target.type.toUpperCase()})\n`;
      contextStr += `Description: ${resolution.target.description}\n\n`;
      contextStr += `🔗 REQUIRED DEPENDENCIES TO LOAD IN CONTEXT:\n`;
      
      resolution.contextNodes.forEach(node => {
        contextStr += `- [${node.type.toUpperCase()}] ${node.id}:\n  Location: ${node.filePath}\n  Desc: ${node.description}\n\n`;
      });

      contextStr += `\nINSTRUCTION: Please read the files listed above using the 'read_file' tool to acquire the necessary context before proceeding with the user's request.`;

      return {
        llmContent: contextStr,
        returnDisplay: `Graph Resolved: ${rootNode.id} + ${resolution.contextNodes.length} dependencies.`
      };
    }
  });
}
