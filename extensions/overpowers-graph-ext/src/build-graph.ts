import fs from 'node:fs/promises';
import path from 'node:path';
import YAML from 'yaml';

export interface GraphNode {
  id: string; // The filename/name
  type: string; // agent, skill, workflow
  domain: string;
  description: string;
  requires: string[];
  related_to: string[];
  filePath: string;
}

export interface OverpowersGraph {
  nodes: Record<string, GraphNode>;
}

async function getMarkdownFiles(dir: string): Promise<string[]> {
  let results: string[] = [];
  try {
    const list = await fs.readdir(dir, { withFileTypes: true });
    for (const file of list) {
      const fullPath = path.join(dir, file.name);
      if (file.isDirectory()) {
        results = results.concat(await getMarkdownFiles(fullPath));
      } else if (file.name.endsWith('.md')) {
        results.push(fullPath);
      }
    }
  } catch (e) {
    // Ignore if directory doesn't exist
  }
  return results;
}

export async function buildGraph(sourceDirs: string[], outputPath: string) {
  const graph: OverpowersGraph = { nodes: {} };

  for (const dir of sourceDirs) {
    const files = await getMarkdownFiles(dir);
    for (const filePath of files) {
      // Only include continuity-*.md files if we are in the .agents directory
      if (dir.endsWith('.agents') && !path.basename(filePath).startsWith('continuity')) continue;

      const content = await fs.readFile(filePath, 'utf-8');
      
      // Simple regex to extract YAML frontmatter
      const match = content.match(/^---\n([\s\S]+?)\n---/);
      if (!match) continue;

      try {
        const metadata = YAML.parse(match[1]);
        const id = metadata.name || path.basename(filePath, '.md');
        
        graph.nodes[id] = {
          id,
          type: metadata.type || 'unknown',
          domain: metadata.domain || 'General',
          description: metadata.description || '',
          requires: metadata.requires || [],
          related_to: metadata.related_to || [],
          filePath
        };
      } catch (e) {
        console.error(`Failed to parse YAML in ${filePath}`);
      }
    }
  }

  await fs.writeFile(outputPath, JSON.stringify(graph, null, 2), 'utf-8');
  console.log(`Graph built successfully with ${Object.keys(graph.nodes).length} nodes.`);
  console.log(`Saved to: ${outputPath}`);
}

// Allow running directly from CLI
if (require.main === module) {
  const dataDir = path.join(__dirname, '..', '..', '..');
  const outPath = path.join(__dirname, '..', 'overpowers-graph.json');
  buildGraph([
    path.join(dataDir, '.agents'), // New location for continuity files
    path.join(dataDir, 'skills'), 
    path.join(dataDir, 'agents'), 
    path.join(dataDir, 'workflows')
  ], outPath);
}
