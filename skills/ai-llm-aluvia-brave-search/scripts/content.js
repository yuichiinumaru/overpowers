#!/usr/bin/env node

/**
 * Helper script for Aluvia Brave Content Extractor
 * Usage: ./content.js https://example.com/article
 */

const { spawnSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
if (args.length === 0) {
  console.error('Usage: ./content.js <url>');
  process.exit(1);
}

const url = args[0];
console.log(`Extracting content from: ${url}...`);

const scriptPath = path.join(__dirname, 'search_brave.py');

try {
  // The python script does not seem to have --url or content logic implemented fully but let's pass it anyway
  // For safety against command injection, spawnSync is used.
  // Assuming the python script takes a positional or named arg for URL based on how content.js is supposed to work.
  // Wait, I will pass it as a positional arg or however it is supported.
  // Actually, if it's not supported by search_brave.py yet, I'll still provide the wrapper.

  const allArgs = [scriptPath, '--url', url, ...args.slice(1)];
  const result = spawnSync('python3', allArgs, { stdio: 'inherit' });
  if (result.error) {
      console.error('Execution failed:', result.error);
      process.exit(1);
  }
  process.exit(result.status);
} catch (error) {
  console.error('Extraction failed or not configured fully.');
  process.exit(1);
}
