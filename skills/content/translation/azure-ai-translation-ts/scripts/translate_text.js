// translate_text.js - Azure AI Translation CLI (Node.js)
import TextTranslationClient from "@azure-rest/ai-translation-text";
import { parseArgs } from "node:util";

const API_KEY = process.env.TRANSLATOR_SUBSCRIPTION_KEY;
const REGION = process.env.TRANSLATOR_REGION;
const ENDPOINT = process.env.TRANSLATOR_ENDPOINT || "https://api.cognitive.microsofttranslator.com";

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      to: { type: 'string', short: 't', default: 'es' },
      from: { type: 'string', short: 'f' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: node translate_text.js "text to translate" [options]

Options:
  -t, --to <lang>    Target language code (default: es)
  -f, --from <lang>  Source language code (optional, auto-detect)
  -h, --help         Show help
    `);
    return;
  }

  if (!API_KEY || !REGION) {
    console.error('Error: TRANSLATOR_SUBSCRIPTION_KEY and TRANSLATOR_REGION are required.');
    process.exit(1);
  }

  const text = positionals[0];
  const targetLanguage = values.to;
  const sourceLanguage = values.from;

  const credential = { key: API_KEY, region: REGION };
  const client = TextTranslationClient(ENDPOINT, credential);

  console.log(`Translating to ${targetLanguage}...`);

  try {
    const response = await client.path("/translate").post({
      body: {
        inputs: [{ text, language: sourceLanguage, targets: [{ language: targetLanguage }] }],
      },
    });

    if (response.status !== "200") {
      console.error('Translation failed:', response.body.error);
      return;
    }

    for (const result of response.body.value) {
      for (const translation of result.translations) {
        console.log(`--- Result (${translation.language}) ---`);
        console.log(translation.text);
      }
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main().catch(console.error);
