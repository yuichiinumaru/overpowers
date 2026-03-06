#!/usr/bin/env node

const { parseArgs } = require('node:util');

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: ./content.js <url> [options]

Options:
  -h, --help        Show this help message
    `);
    return;
  }

  console.log(`Brave Search content extraction placeholder for url: ${positionals[0]}`);
}

main().catch(console.error);
