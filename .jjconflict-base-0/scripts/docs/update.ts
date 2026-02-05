/**
 * Update documentation from code
 * Usage: tsx scripts/docs/update.ts
 */

import * as fs from 'fs'
import * as path from 'path'

async function updateDocs() {
    console.log("📝 Updating documentation...");

    // 1. Read Codemaps
    const codemapsDir = path.join(process.cwd(), 'docs', 'CODEMAPS');
    if (!fs.existsSync(codemapsDir)) {
        console.error("❌ Codemaps not found. Run scripts/codemaps/generate.ts first.");
        return;
    }

    const indexContent = fs.readFileSync(path.join(codemapsDir, 'INDEX.md'), 'utf-8');

    // 2. Update README.md Architecture Section
    const readmePath = path.join(process.cwd(), 'README.md');
    if (fs.existsSync(readmePath)) {
        let readme = fs.readFileSync(readmePath, 'utf-8');

        // Simple replace logic for now - look for ## Architecture
        const architectureSection = `## Architecture\n\nSee [docs/CODEMAPS/INDEX.md](docs/CODEMAPS/INDEX.md) for detailed architecture.\n\n### Key Components\n- **Agents**: See [docs/CODEMAPS/agents.md](docs/CODEMAPS/agents.md)\n- **Source**: See [docs/CODEMAPS/source.md](docs/CODEMAPS/source.md)\n`;

        if (readme.includes('## Architecture')) {
            // Replace existing section (rough regex)
            readme = readme.replace(/## Architecture[\s\S]*?(?=##|$)/, architectureSection + '\n');
        } else {
            // Append if not found
            readme += '\n' + architectureSection;
        }

        fs.writeFileSync(readmePath, readme);
        console.log("✅ Updated README.md");
    }

    // 3. Update AGENTS.md registry count
    const agentsPath = path.join(process.cwd(), 'AGENTS.md');
    if (fs.existsSync(agentsPath)) {
        let agentsDoc = fs.readFileSync(agentsPath, 'utf-8');
        // Count markdown files in agents/
        const agentCount = countFiles(path.join(process.cwd(), 'agents'), '.md');

        agentsDoc = agentsDoc.replace(/\| Agents \| \d+\+ \|/, `| Agents | ${agentCount}+ |`);
        fs.writeFileSync(agentsPath, agentsDoc);
        console.log(`✅ Updated AGENTS.md count to ${agentCount}`);
    }
}

function countFiles(dir: string, ext: string): number {
    let count = 0;
    if (!fs.existsSync(dir)) return 0;
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            count += countFiles(fullPath, ext);
        } else if (file.endsWith(ext)) {
            count++;
        }
    }
    return count;
}

updateDocs().catch(console.error);
