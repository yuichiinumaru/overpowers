import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

/**
 * Extract YAML frontmatter from a skill file.
 * Current format:
 * ---
 * name: skill-name
 * description: Use when [condition] - [what it does]
 * ---
 *
 * @param {string} filePath - Path to SKILL.md file
 * @returns {{name: string, description: string}}
 */
function extractFrontmatter(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        const lines = content.split('\n');

        let inFrontmatter = false;
        let name = '';
        let description = '';

        for (const line of lines) {
            if (line.trim() === '---') {
                if (inFrontmatter) break;
                inFrontmatter = true;
                continue;
            }

            if (inFrontmatter) {
                const match = line.match(/^(\w+):\s*(.*)$/);
                if (match) {
                    const [, key, value] = match;
                    switch (key) {
                        case 'name':
                            name = value.trim();
                            break;
                        case 'description':
                            description = value.trim();
                            break;
                    }
                }
            }
        }

        return { name, description };
    } catch (error) {
        return { name: '', description: '' };
    }
}

/**
 * Find all SKILL.md files in a directory recursively.
 *
 * @param {string} dir - Directory to search
 * @param {string} sourceType - 'personal' or 'overpowers' for namespacing
 * @param {number} maxDepth - Maximum recursion depth (default: 3)
 * @returns {Array<{path: string, name: string, description: string, sourceType: string}>}
 */
function findSkillsInDir(dir, sourceType, maxDepth = 3) {
    const skills = [];

    if (!fs.existsSync(dir)) return skills;

    function recurse(currentDir, depth) {
        if (depth > maxDepth) return;

        const entries = fs.readdirSync(currentDir, { withFileTypes: true });

        for (const entry of entries) {
            const fullPath = path.join(currentDir, entry.name);

            if (entry.isDirectory()) {
                // Check for SKILL.md in this directory
                const skillFile = path.join(fullPath, 'SKILL.md');
                if (fs.existsSync(skillFile)) {
                    const { name, description } = extractFrontmatter(skillFile);
                    skills.push({
                        path: fullPath,
                        skillFile: skillFile,
                        name: name || entry.name,
                        description: description || '',
                        sourceType: sourceType
                    });
                }

                // Recurse into subdirectories
                recurse(fullPath, depth + 1);
            }
        }
    }

    recurse(dir, 0);
    return skills;
}

/**
 * Resolve a skill name to its file path, handling shadowing
 * (personal skills override overpowers skills).
 *
 * @param {string} skillName - Name like "overpowers:brainstorming" or "my-skill"
 * @param {string} OverpowersDir - Path to overpowers skills directory
 * @param {string} personalDir - Path to personal skills directory
 * @returns {{skillFile: string, sourceType: string, skillPath: string} | null}
 */
function resolveSkillPath(skillName, OverpowersDir, personalDir) {
    // Strip overpowers: prefix if present
    const forceOverpowers = skillName.startsWith('overpowers:');
    const actualSkillName = forceOverpowers ? skillName.replace(/^overpowers:/, '') : skillName;

    // Try personal skills first (unless explicitly overpowers:)
    if (!forceOverpowers && personalDir) {
        const personalPath = path.join(personalDir, actualSkillName);
        const personalSkillFile = path.join(personalPath, 'SKILL.md');
        if (fs.existsSync(personalSkillFile)) {
            return {
                skillFile: personalSkillFile,
                sourceType: 'personal',
                skillPath: actualSkillName
            };
        }
    }

    // Try overpowers skills
    if (OverpowersDir) {
        const OverpowersPath = path.join(OverpowersDir, actualSkillName);
        const OverpowersSkillFile = path.join(OverpowersPath, 'SKILL.md');
        if (fs.existsSync(OverpowersSkillFile)) {
            return {
                skillFile: OverpowersSkillFile,
                sourceType: 'overpowers',
                skillPath: actualSkillName
            };
        }
    }

    return null;
}

/**
 * Check if a git repository has updates available.
 *
 * @param {string} repoDir - Path to git repository
 * @returns {boolean} - True if updates are available
 */
function checkForUpdates(repoDir) {
    try {
        // Quick check with 3 second timeout to avoid delays if network is down
        const output = execSync('git fetch origin && git status --porcelain=v1 --branch', {
            cwd: repoDir,
            timeout: 3000,
            encoding: 'utf8',
            stdio: 'pipe'
        });

        // Parse git status output to see if we're behind
        const statusLines = output.split('\n');
        for (const line of statusLines) {
            if (line.startsWith('## ') && line.includes('[behind ')) {
                return true; // We're behind remote
            }
        }
        return false; // Up to date
    } catch (error) {
        // Network down, git error, timeout, etc. - don't block bootstrap
        return false;
    }
}

/**
 * Strip YAML frontmatter from skill content, returning just the content.
 *
 * @param {string} content - Full content including frontmatter
 * @returns {string} - Content without frontmatter
 */
function stripFrontmatter(content) {
    const lines = content.split('\n');
    let inFrontmatter = false;
    let frontmatterEnded = false;
    const contentLines = [];

    for (const line of lines) {
        if (line.trim() === '---') {
            if (inFrontmatter) {
                frontmatterEnded = true;
                continue;
            }
            inFrontmatter = true;
            continue;
        }

        if (frontmatterEnded || !inFrontmatter) {
            contentLines.push(line);
        }
    }

    return contentLines.join('\n').trim();
}

/**
 * Find all markdown files in a directory that look like agents.
 *
 * @param {string} dir - Directory to search
 * @param {number} maxDepth - Maximum recursion depth (default: 1)
 * @returns {Array<{path: string, fileName: string}>}
 */
function findAgentsInDir(dir, maxDepth = 1) {
    const agents = [];

    if (!fs.existsSync(dir)) return agents;

    function recurse(currentDir, depth) {
        if (depth > maxDepth) return;

        const entries = fs.readdirSync(currentDir, { withFileTypes: true });

        for (const entry of entries) {
            const fullPath = path.join(currentDir, entry.name);

            if (entry.isDirectory()) {
                recurse(fullPath, depth + 1);
            } else if (entry.isFile() && entry.name.endsWith('.md')) {
                // Heuristic: agent files are usually small and have a specific name
                // To be precise, we'll extract metadata later
                agents.push({
                    path: fullPath,
                    fileName: entry.name.replace(/\.md$/, '')
                });
            }
        }
    }

    recurse(dir, 0);
    return agents;
}

/**
 * Extract agent metadata and instructions.
 *
 * @param {string} filePath - Path to agent markdown file
 * @returns {{name: string, description: string, prompt: string} | null}
 */
function extractAgentData(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        const { name, description } = extractFrontmatter(filePath);
        const prompt = stripFrontmatter(content);

        return {
            name: name || path.basename(filePath, '.md'),
            description: description || '',
            prompt: prompt
        };
    } catch (error) {
        return null;
    }
}

export {
    extractFrontmatter,
    findSkillsInDir,
    resolveSkillPath,
    checkForUpdates,
    stripFrontmatter,
    findAgentsInDir,
    extractAgentData
};

