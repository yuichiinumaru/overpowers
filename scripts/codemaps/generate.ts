/**
 * Generate codemaps from repository structure
 * Usage: tsx scripts/codemaps/generate.ts
 */

import { Project, SyntaxKind } from 'ts-morph'
import * as fs from 'fs'
import * as path from 'path'

// Define the output directory
const OUTPUT_DIR = path.join(process.cwd(), 'docs', 'CODEMAPS');

// Ensure output directory exists
if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

async function generateCodemaps() {
    console.log('🔍 Analyzing codebase...');

    // Initialize project
    const project = new Project({
        tsConfigFilePath: fs.existsSync('tsconfig.json') ? 'tsconfig.json' : undefined,
        skipAddingFilesFromTsConfig: false,
    });

    // If no tsconfig, add source files manually
    if (!fs.existsSync('tsconfig.json')) {
        project.addSourceFilesAtPaths(['src/**/*.{ts,tsx}', 'agents/**/*.{md,ts}', 'commands/**/*.{md,ts}']);
    }

    const sourceFiles = project.getSourceFiles();
    console.log(`📂 Found ${sourceFiles.length} source files.`);

    // 1. Generate Index
    const indexContent = `# Project Codemap Index

**Last Updated:** ${new Date().toISOString().split('T')[0]}
**Total Files:** ${sourceFiles.length}

## Modules

- [Agents](./agents.md) - AI Agents definitions
- [Commands](./commands.md) - Custom commands
- [Scripts](./scripts.md) - Automation scripts
- [Source](./source.md) - Core source code (if applicable)

`;
    fs.writeFileSync(path.join(OUTPUT_DIR, 'INDEX.md'), indexContent);
    console.log('✅ Generated INDEX.md');

    // 2. Generate Agents Map
    const agentFiles = project.getSourceFiles().filter(f => f.getFilePath().includes('/agents/'));
    let agentsContent = `# Agents Codemap\n\n**Total Agents:** ${agentFiles.length}\n\n| Agent | Path |\n|-------|------|\n`;

    // Also scan .md files in agents/ manually since ts-morph focuses on TS
    const agentsDir = path.join(process.cwd(), 'agents');
    if (fs.existsSync(agentsDir)) {
        const scanDir = (dir: string) => {
            const files = fs.readdirSync(dir);
            for (const file of files) {
                const fullPath = path.join(dir, file);
                if (fs.statSync(fullPath).isDirectory()) {
                    scanDir(fullPath);
                } else if (file.endsWith('.md')) {
                    const relPath = path.relative(process.cwd(), fullPath);
                    agentsContent += `| ${path.basename(file, '.md')} | \`${relPath}\` |\n`;
                }
            }
        };
        scanDir(agentsDir);
    }
    fs.writeFileSync(path.join(OUTPUT_DIR, 'agents.md'), agentsContent);
    console.log('✅ Generated agents.md');

    // 3. Generate Source Map (TS/JS)
    let sourceContent = `# Source Code Map\n\n`;

    // Group by directory
    const filesByDir: Record<string, string[]> = {};

    for (const sourceFile of sourceFiles) {
        const filePath = path.relative(process.cwd(), sourceFile.getFilePath());
        if (filePath.startsWith('node_modules')) continue;

        const dir = path.dirname(filePath);
        if (!filesByDir[dir]) filesByDir[dir] = [];
        filesByDir[dir].push(path.basename(filePath));
    }

    for (const [dir, files] of Object.entries(filesByDir)) {
        sourceContent += `## ${dir}\n`;
        for (const file of files) {
            sourceContent += `- ${file}\n`;
        }
        sourceContent += '\n';
    }

    fs.writeFileSync(path.join(OUTPUT_DIR, 'source.md'), sourceContent);
    console.log('✅ Generated source.md');
}

generateCodemaps().catch(console.error);
