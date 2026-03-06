#!/usr/bin/env node
/**
 * Helper script to scaffold a new CLI command for v3 modernization.
 */
const fs = require('fs');

const commandName = process.argv[2] || 'example';

const template = `
import { Command, SubCommand, Option, Arg } from '@core/cli';

@Command({
  name: '${commandName}',
  description: '${commandName} management',
  category: 'general'
})
export class ${commandName.charAt(0).toUpperCase() + commandName.slice(1)}Command {
  @SubCommand('init')
  async init(): Promise<any> {
    console.log('Initializing ${commandName}...');
    return { status: 'success' };
  }
}
`;

fs.writeFileSync(`${commandName}.command.ts`, template.trim() + '\n');
console.log(`Scaffolded ${commandName}.command.ts`);
