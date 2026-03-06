#!/usr/bin/env node

// find-missing-translations.js
const fs = require('fs');
const path = require('path');

const localesDir = path.join(process.cwd(), 'locales');
const baseLocale = 'en';

if (!fs.existsSync(localesDir)) {
  console.error(`Error: 'locales' directory not found in ${process.cwd()}`);
  process.exit(1);
}

const getKeys = (obj, prefix = '') => {
  return Object.keys(obj).reduce((acc, key) => {
    const p = prefix ? `${prefix}.${key}` : key;
    if (typeof obj[key] === 'object' && obj[key] !== null && !Array.isArray(obj[key])) {
      acc.push(...getKeys(obj[key], p));
    } else {
      acc.push(p);
    }
    return acc;
  }, []);
};

const baseFilePath = path.join(localesDir, `${baseLocale}.json`);
if (!fs.existsSync(baseFilePath)) {
  console.error(`Error: Base locale file not found: ${baseFilePath}`);
  process.exit(1);
}

const baseContent = JSON.parse(fs.readFileSync(baseFilePath, 'utf8'));
const baseKeys = getKeys(baseContent);

console.log(`Checking translations against base locale '${baseLocale}'...`);

fs.readdirSync(localesDir).forEach(file => {
  if (file === `${baseLocale}.json` || !file.endsWith('.json')) return;

  const localePath = path.join(localesDir, file);
  const localeContent = JSON.parse(fs.readFileSync(localePath, 'utf8'));
  const localeKeys = getKeys(localeContent);
  const localeName = file.replace('.json', '');

  const missingKeys = baseKeys.filter(key => !localeKeys.includes(key));

  if (missingKeys.length > 0) {
    console.log(`\nLocale '${localeName}' is missing ${missingKeys.length} translations:`);
    missingKeys.forEach(k => console.log(`  - ${k}`));
  } else {
    console.log(`Locale '${localeName}' is fully translated.`);
  }
});
