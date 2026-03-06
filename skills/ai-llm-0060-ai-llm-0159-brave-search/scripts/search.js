#!/usr/bin/env node

const { parseArgs } = require('node:util');

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      content: { type: 'boolean' },
      n: { type: 'string', short: 'n' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: ./search.js "query" [options]

Options:
  -n <number>       Number of results
  --content         Include page content as markdown
  -h, --help        Show this help message
    `);
    return;
  }

  console.log(`Brave Search placeholder for query: ${positionals[0]}`);
}

main().catch(console.error);
