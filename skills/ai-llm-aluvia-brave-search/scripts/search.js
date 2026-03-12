#!/usr/bin/env node

/**
 * Helper script for Aluvia Brave Search
 * Usage: ./search.js "query" [-n results] [--content]
 */

const { spawnSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
if (args.length === 0) {
  console.error('Usage: ./search.js "query" [-n results] [--content]');
  process.exit(1);
}

const scriptPath = path.join(__dirname, 'search_brave.py');

try {
  // Pass all arguments directly to the python script
  const allArgs = [scriptPath, ...args];

  const result = spawnSync('python3', allArgs, { stdio: 'inherit' });
  if (result.error) {
      console.error('Execution failed:', result.error);
      process.exit(1);
  }
  process.exit(result.status);
} catch (error) {
  console.error('Search failed or not configured fully.');
  process.exit(1);
}
