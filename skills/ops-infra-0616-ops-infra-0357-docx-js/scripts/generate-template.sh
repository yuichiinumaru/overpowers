#!/bin/bash
# Docx generation template
OUTPUT_FILE="${1:-doc.js}"

cat << 'JS_EOF' > "$OUTPUT_FILE"
const { Document, Packer, Paragraph, TextRun } = require('docx');
const fs = require('fs');

const doc = new Document({
    sections: [{
        children: [
            new Paragraph({
                children: [
                    new TextRun("Hello World"),
                ],
            }),
        ],
    }],
});

Packer.toBuffer(doc).then((buffer) => {
    fs.writeFileSync("output.docx", buffer);
    console.log("Document created successfully");
});
JS_EOF

echo "Docx generation template created at $OUTPUT_FILE"
