// Example script demonstrating html2pptx usage based on the SKILL.md rules
const html2pptx = require('html2pptx');
const PptxGenJS = require('pptxgenjs');
const fs = require('fs');

async function createPresentation(htmlFilePath, outputFilename) {
    console.log(`Reading ${htmlFilePath}...`);

    // Create new PPTX instance
    const pptx = new PptxGenJS();

    // Configure standard settings
    pptx.layout = 'LAYOUT_16x9';
    pptx.author = 'HTML to PPTX Generator';

    try {
        // Convert HTML to slides
        // Ensure your HTML follows the specific structure expected by html2pptx
        // The HTML file should have <section> elements containing <h1> and <div class="content">
        const { slide, placeholders } = await html2pptx(htmlFilePath, pptx);

        console.log(`Generated slides. Adding charts and custom elements...`);

        // Example: Add a simple chart to the last generated slide using placeholders
        // Important Rule: Use colors WITHOUT the # prefix
        if (slide && placeholders && placeholders.length > 0) {
            slide.addChart(pptx.charts.BAR, [{
                name: "Example Data",
                labels: ["Q1", "Q2", "Q3", "Q4"],
                values: [4500, 5500, 6200, 7100]
            }], {
                ...placeholders[0],  // Use placeholder position from HTML
                barDir: 'col',
                showTitle: true,
                title: 'Quarterly Sales',
                showLegend: false,
                showCatAxisTitle: true,
                catAxisTitle: 'Quarter',
                showValAxisTitle: true,
                valAxisTitle: 'Sales ($000s)',
                chartColors: ["4472C4"] // NO # PREFIX!
            });
            console.log("Added example chart.");
        }

        // Save presentation
        await pptx.writeFile({ fileName: outputFilename });
        console.log(`Presentation saved successfully to ${outputFilename}`);

    } catch (error) {
        console.error("Error creating presentation:", error);
    }
}

// Check for command line arguments
if (process.argv.length < 4) {
    console.log("Usage: node generate_pptx.js <input.html> <output.pptx>");
    process.exit(1);
}

const htmlFile = process.argv[2];
const pptxFile = process.argv[3];

if (!fs.existsSync(htmlFile)) {
    console.error(`Input file not found: ${htmlFile}`);
    process.exit(1);
}

createPresentation(htmlFile, pptxFile);
