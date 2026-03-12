import { GraphNode, OverpowersGraph } from './build-graph';

export class GraphEngine {
  private graph: OverpowersGraph;

  constructor(graphData: OverpowersGraph) {
    this.graph = graphData;
  }

  /**
   * Search nodes using simple token matching on description and name
   */
  search(query: string, maxResults: number = 3): GraphNode[] {
    const tokens = query.toLowerCase().split(/\s+/).filter(Boolean);
    
    const scoredNodes = Object.values(this.graph.nodes).map(node => {
      const text = `${node.id} ${node.description} ${node.domain}`.toLowerCase();
      let score = 0;
      for (const token of tokens) {
        if (text.includes(token)) score++;
      }
      return { node, score };
    });

    return scoredNodes
      .filter(n => n.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, maxResults)
      .map(n => n.node);
  }

  /**
   * Resolve a node and traverse its 'requires' and 'related_to' dependencies
   * using a BFS approach up to a certain depth.
   */
  resolveDependencies(startNodeId: string, depth: number = 1): { target: GraphNode, contextNodes: GraphNode[] } | null {
    const target = this.graph.nodes[startNodeId];
    if (!target) return null;

    const contextNodes = new Map<string, GraphNode>();
    let queue: { id: string, currentDepth: number }[] = [
      ...target.requires.map(id => ({ id, currentDepth: 1 })),
      ...target.related_to.map(id => ({ id, currentDepth: 1 }))
    ];

    while (queue.length > 0) {
      const { id, currentDepth } = queue.shift()!;
      
      if (contextNodes.has(id)) continue; // avoid cycles
      
      const node = this.graph.nodes[id];
      if (node) {
        contextNodes.set(id, node);
        
        if (currentDepth < depth) {
          node.requires.forEach(req => queue.push({ id: req, currentDepth: currentDepth + 1 }));
          node.related_to.forEach(rel => queue.push({ id: rel, currentDepth: currentDepth + 1 }));
        }
      }
    }

    return {
      target,
      contextNodes: Array.from(contextNodes.values())
    };
  }
}
