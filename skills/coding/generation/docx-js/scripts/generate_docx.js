#!/usr/bin/env node

/**
 * Basic script to scaffold a docx file using the docx package.
 * Requires: npm install docx
 *
 * Usage:
 *   node generate_docx.js "Hello World.docx"
 */

const fs = require("fs");
// For a real project, uncomment and install docx
// const { Document, Packer, Paragraph, TextRun } = require("docx");

const filename = process.argv[2] || "Sample.docx";

console.log(`[Mock] Generating Word document using docx.js: ${filename}`);

const content = `const { Document, Packer, Paragraph, TextRun } = require("docx");
const fs = require("fs");

const doc = new Document({
  sections: [
    {
      children: [
        new Paragraph({
          children: [
            new TextRun("Hello World"),
            new TextRun({
              text: "Foo Bar",
              bold: true,
            }),
          ],
        }),
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("${filename}", buffer);
  console.log("Document created successfully");
});
`;

fs.writeFileSync(`${filename}.js`, content);
console.log(`Generated generation script at ${filename}.js. Run it with node ${filename}.js after installing 'docx'`);
