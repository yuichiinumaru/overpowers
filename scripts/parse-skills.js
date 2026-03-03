const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');
const OUTPUT_FILE_1 = path.join(__dirname, '..', 'docs', 'architecture', 'codemaps', '003-arch-skills-map.json');
const OUTPUT_FILE_2 = path.join(__dirname, '..', '.agents', 'knowledge', 'kb_skills_mapping.json');

function ensureDirectoryExistence(filePath) {
    const dirname = path.dirname(filePath);
    if (fs.existsSync(dirname)) {
        return true;
    }
    ensureDirectoryExistence(dirname);
    fs.mkdirSync(dirname, { recursive: true });
}

function parseSkill(skillDirName) {
    const skillMdPath = path.join(SKILLS_DIR, skillDirName, 'SKILL.md');
    if (!fs.existsSync(skillMdPath)) {
        return null;
    }

    const content = fs.readFileSync(skillMdPath, 'utf8');

    // Extract frontmatter if it exists
    const frontmatterRegex = /^---\s*\n([\s\S]*?)\n---\s*\n/;
    const match = content.match(frontmatterRegex);

    let name = skillDirName;
    let description = '';

    if (match) {
        const frontmatter = match[1];

        // Attempt to extract name
        const nameMatch = frontmatter.match(/^name:\s*(.+)$/m);
        if (nameMatch) name = nameMatch[1].trim();

        // Attempt to extract description
        const descMatchString = frontmatter.match(/^description:\s*(['"]?)([\s\S]*?)\1(?=\n[a-z_]+:|\s*$)/mi);
        if (descMatchString) {
            description = descMatchString[2].trim();
        }

        // Fallback description search if not in frontmatter
        if (!description) {
            const rest = content.slice(match[0].length).trim();
            const firstLine = rest.split('\n').map(l => l.trim()).filter(l => l.length > 0 && !l.startsWith('#'))[0];
            if (firstLine) description = firstLine;
        }
    } else {
        // No frontmatter, extract first text
        const lines = content.split('\n');
        for (let l of lines) {
            l = l.trim();
            if (l && !l.startsWith('#')) {
                description = l;
                break;
            }
        }
    }

    // Also look for name in `# title` if no frontmatter name
    if (name === skillDirName) {
        const h1Match = content.match(/^#\s+(.+)$/m);
        if (h1Match) {
            name = h1Match[1].trim();
        }
    }

    return {
        id: skillDirName,
        name: name,
        description: description.substring(0, 1000), // truncate long descriptions to 1000 chars
        path: `skills/${skillDirName}/SKILL.md`,
        url: `file://${path.resolve(skillMdPath)}`
    };
}

function generateSkillMap() {
    console.log(`Reading skills from ${SKILLS_DIR}`);
    if (!fs.existsSync(SKILLS_DIR)) {
        console.error('Skills directory not found.');
        process.exit(1);
    }

    const entries = fs.readdirSync(SKILLS_DIR, { withFileTypes: true });
    const skills = [];

    for (const entry of entries) {
        if (entry.isDirectory()) {
            const skill = parseSkill(entry.name);
            if (skill) {
                skills.push(skill);
            }
        }
    }

    console.log(`Found ${skills.length} skills. Writing to outputs...`);

    const resultJson = JSON.stringify(skills, null, 2);

    ensureDirectoryExistence(OUTPUT_FILE_1);
    fs.writeFileSync(OUTPUT_FILE_1, resultJson);
    console.log(`Saved: ${OUTPUT_FILE_1}`);

    ensureDirectoryExistence(OUTPUT_FILE_2);
    fs.writeFileSync(OUTPUT_FILE_2, resultJson);
    console.log(`Saved: ${OUTPUT_FILE_2}`);

    console.log('Success! Skill knowledge base mapping generated.');
}

generateSkillMap();
