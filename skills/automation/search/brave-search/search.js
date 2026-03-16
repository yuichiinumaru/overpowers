#!/usr/bin/env node
// search.js
import axios from 'axios';
import { parseArgs } from 'node:util';

const API_KEY = process.env.BRAVE_API_KEY;

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      n: { type: 'string', short: 'n', default: '5' },
      content: { type: 'boolean', default: false },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: ./search.js "query" [options]

Options:
  -n <number>       Number of results (default: 5)
  --content         Include page content as markdown
  -h, --help        Show help
    `);
    return;
  }

  if (!API_KEY) {
    console.error('Error: BRAVE_API_KEY environment variable is not set.');
    process.exit(1);
  }

  const query = positionals[0];
  const count = parseInt(values.n, 10);

  console.log(`Searching Brave for: "${query}"...`);
  // API Call implementation
}

main().catch(console.error);
