#!/usr/bin/env node

/**
 * Form Field JSON Validator
 * Validates the structure of the fields.json file for non-fillable forms
 * as defined in the Forms skill documentation.
 *
 * Usage:
 *   node form_validator.js fields.json
 */

const fs = require('fs');

const file = process.argv[2];

if (!file) {
    console.error("Usage: node form_validator.js <fields.json>");
    process.exit(1);
}

try {
    const data = JSON.parse(fs.readFileSync(file, 'utf8'));
    let errors = 0;

    if (!data.pages || !Array.isArray(data.pages)) {
        console.error("❌ Missing or invalid 'pages' array");
        errors++;
    }

    if (!data.form_fields || !Array.isArray(data.form_fields)) {
        console.error("❌ Missing or invalid 'form_fields' array");
        errors++;
    } else {
        data.form_fields.forEach((field, i) => {
            if (!field.page_number) { console.error(`❌ Field ${i} missing page_number`); errors++; }
            if (!field.field_label) { console.error(`❌ Field ${i} missing field_label`); errors++; }
            if (!field.label_bounding_box || field.label_bounding_box.length !== 4) {
                console.error(`❌ Field ${i} missing or invalid label_bounding_box [left, top, right, bottom]`);
                errors++;
            }
            if (!field.entry_bounding_box || field.entry_bounding_box.length !== 4) {
                console.error(`❌ Field ${i} missing or invalid entry_bounding_box [left, top, right, bottom]`);
                errors++;
            }
            if (!field.entry_text || typeof field.entry_text.text === 'undefined') {
                console.error(`❌ Field ${i} missing entry_text.text`);
                errors++;
            }

            // Basic intersection check
            if (field.label_bounding_box && field.entry_bounding_box) {
                const [l1, t1, r1, b1] = field.label_bounding_box;
                const [l2, t2, r2, b2] = field.entry_bounding_box;

                const intersect = !(r1 < l2 || l1 > r2 || b1 < t2 || t1 > b2);
                if (intersect) {
                    console.error(`❌ Field ${i} ('${field.field_label}') has intersecting label and entry bounding boxes.`);
                    errors++;
                }
            }
        });
    }

    if (errors === 0) {
        console.log("✅ fields.json format is valid.");
    } else {
        console.log(`\nFound ${errors} errors.`);
        process.exit(1);
    }

} catch (e) {
    console.error("Error reading or parsing JSON file:", e.message);
    process.exit(1);
}
