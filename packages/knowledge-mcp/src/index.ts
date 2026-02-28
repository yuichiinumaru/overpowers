import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import * as fs from "fs/promises";
import * as path from "path";
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Define the absolute path to the docs directory relative to the repository root
const REPO_ROOT = path.resolve(__dirname, "../../..");
const DOCS_DIR = path.join(REPO_ROOT, "docs");

const server = new McpServer({
  name: "knowledge-mcp",
  version: "1.0.0",
});

// Tool to read a specific file in the docs/ folder
server.tool(
  "read_knowledge_file",
  "Read the content of a specific file in the docs/ folder",
  {
    filePath: z.string().describe("The path of the file to read, relative to docs/"),
  },
  async ({ filePath }) => {
    try {
      const fullPath = path.join(DOCS_DIR, filePath);
      
      // Security check: ensure the file is within the docs directory
      if (!fullPath.startsWith(DOCS_DIR + path.sep)) {
        return {
          content: [{ type: "text", text: "Error: Cannot access files outside the docs/ directory." }],
        };
      }

      const content = await fs.readFile(fullPath, "utf-8");
      return {
        content: [{ type: "text", text: content }],
      };
    } catch (error: any) {
      return {
        content: [{ type: "text", text: `Error reading file: ${error.message}` }],
      };
    }
  }
);

// Helper function to recursively list files
async function getFiles(dir: string): Promise<string[]> {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  const files = await Promise.all(
    entries.map((entry) => {
      const res = path.resolve(dir, entry.name);
      return entry.isDirectory() ? getFiles(res) : [res];
    })
  );
  return files.flat();
}

// Tool to list files in the knowledge base
server.tool(
  "list_knowledge_files",
  "List available files in a specific knowledge category or the root docs/ folder",
  {
    category: z.string().optional().describe("Optional subdirectory within docs/ to list files from"),
  },
  async ({ category }) => {
    try {
      const targetDir = category ? path.join(DOCS_DIR, category) : DOCS_DIR;

      // Security check
      if (!targetDir.startsWith(DOCS_DIR) || (category && !targetDir.startsWith(DOCS_DIR + path.sep))) {
        return {
          content: [{ type: "text", text: "Error: Cannot access directories outside docs/." }],
        };
      }

      const allFiles = await getFiles(targetDir);
      const relativeFiles = allFiles.map((file) => path.relative(DOCS_DIR, file));

      return {
        content: [{ type: "text", text: JSON.stringify(relativeFiles, null, 2) }],
      };
    } catch (error: any) {
      return {
        content: [{ type: "text", text: `Error listing files: ${error.message}` }],
      };
    }
  }
);

// Tool to search the knowledge base
server.tool(
  "search_knowledge",
  "Search for a specific string or pattern in the knowledge base",
  {
    query: z.string().describe("The string to search for"),
    directory: z.string().optional().describe("Optional subdirectory within docs/ to search in"),
  },
  async ({ query, directory }) => {
    try {
      const targetDir = directory ? path.join(DOCS_DIR, directory) : DOCS_DIR;

      // Security check
      if (!targetDir.startsWith(DOCS_DIR) || (directory && !targetDir.startsWith(DOCS_DIR + path.sep))) {
         return {
          content: [{ type: "text", text: "Error: Cannot search outside docs/ directory." }],
        };
      }

      const allFiles = await getFiles(targetDir);
      const results: { file: string; match: string }[] = [];

      for (const file of allFiles) {
        // Skip non-text files based on extension for simplicity
        if (!file.endsWith(".md") && !file.endsWith(".txt") && !file.endsWith(".json")) continue;

        try {
            const content = await fs.readFile(file, "utf-8");
            const lines = content.split('\n');
            
            for (let i = 0; i < lines.length; i++) {
                if (lines[i].toLowerCase().includes(query.toLowerCase())) {
                    results.push({
                        file: path.relative(DOCS_DIR, file),
                        match: `Line ${i + 1}: ${lines[i].trim()}`
                    });
                }
            }
        } catch(e) {
            // Ignore read errors for individual files during search
        }
      }

      if (results.length === 0) {
        return {
          content: [{ type: "text", text: `No matches found for query: "${query}"` }],
        };
      }

      // Group results by file
      const groupedResults = results.reduce((acc, curr) => {
        if (!acc[curr.file]) {
            acc[curr.file] = [];
        }
        acc[curr.file].push(curr.match);
        return acc;
      }, {} as Record<string, string[]>);

      let responseText = "Search Results:\n\n";
      for (const [file, matches] of Object.entries(groupedResults)) {
          responseText += `File: ${file}\n`;
          matches.forEach(match => {
              responseText += `  - ${match}\n`;
          });
          responseText += "\n";
      }

      return {
        content: [{ type: "text", text: responseText }],
      };
    } catch (error: any) {
      return {
        content: [{ type: "text", text: `Error searching knowledge base: ${error.message}` }],
      };
    }
  }
);

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Knowledge MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Fatal error:", error);
  process.exit(1);
});
