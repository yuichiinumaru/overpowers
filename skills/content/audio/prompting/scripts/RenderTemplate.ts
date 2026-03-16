/**
 * RenderTemplate.ts
 * 
 * Renders a Handlebars template with YAML data.
 */

import { parse } from "https://deno.land/std/yaml/mod.ts";
import Handlebars from "https://esm.sh/handlebars";
import { parse as parseArgs } from "https://deno.land/std/flags/mod.ts";

async function main() {
    const args = parseArgs(Deno.args);
    const templatePath = args.template;
    const dataPath = args.data;
    const outputPath = args.output;

    if (!templatePath || !dataPath) {
        console.error("Usage: deno run RenderTemplate.ts --template <path> --data <path> [--output <path>]");
        Deno.exit(1);
    }

    try {
        const templateSource = await Deno.readTextFile(templatePath);
        const yamlSource = await Deno.readTextFile(dataPath);
        const data = parse(yamlSource);

        const template = Handlebars.compile(templateSource);
        const result = template(data);

        if (outputPath) {
            await Deno.writeTextFile(outputPath, result);
            console.log(`Rendered template to ${outputPath}`);
        } else {
            console.log(result);
        }
    } catch (error) {
        console.error("Error rendering template:", error.message);
        Deno.exit(1);
    }
}

if (import.meta.main) {
    main();
}
