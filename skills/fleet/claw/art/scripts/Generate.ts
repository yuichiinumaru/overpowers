#!/usr/bin/env bun
/**
 * Helper script for Art Generation
 * Maps ~/.claude/skills/Art/Tools/Generate.ts to local runner
 */
console.log("Art Generation Tool started");
console.log("Executing Python backend...");
const { spawnSync } = require("child_process");

const args = process.argv.slice(2);
const pythonArgs = ["generate_art.py", ...args];

const result = spawnSync("python3", pythonArgs, { stdio: "inherit", cwd: __dirname });
if (result.error) {
    console.error("Execution failed:", result.error);
    process.exit(1);
}
process.exit(result.status);
