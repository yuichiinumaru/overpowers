/**
 * ValidateTemplate.ts
 * 
 * Validates a Handlebars template for syntax errors and missing variables.
 */

import Handlebars from "https://esm.sh/handlebars";
import { parse as parseArgs } from "https://deno.land/std/flags/mod.ts";

async function main() {
    const args = parseArgs(Deno.args);
    const templatePath = args.template;

    if (!templatePath) {
        console.error("Usage: deno run ValidateTemplate.ts --template <path>");
        Deno.exit(1);
    }

    try {
        const templateSource = await Deno.readTextFile(templatePath);
        
        // 1. Check syntax
        try {
            Handlebars.precompile(templateSource);
            console.log(`✅ Template syntax is valid: ${templatePath}`);
        } catch (syntaxError) {
            console.error(`❌ Syntax error in template: ${syntaxError.message}`);
            Deno.exit(1);
        }

        // 2. Extract and list variables (basic extraction)
        const variables = new Set<string>();
        const regex = /\{\{\s*([a-zA-Z0-9_.]+)\s*\}\}/g;
        let match;
        while ((match = regex.exec(templateSource)) !== null) {
            variables.add(match[1]);
        }

        if (variables.size > 0) {
            console.log("\nDetected variables:");
            Array.from(variables).sort().forEach(v => console.log(`  - ${v}`));
        } else {
            console.log("\nNo variables detected in template.");
        }

    } catch (error) {
        console.error("Error validating template:", error.message);
        Deno.exit(1);
    }
}

if (import.meta.main) {
    main();
}
