/**
 * Helper script for batch screenshots using snapDOM and Playwright
 * This is a template for capturing multiple elements from a page.
 */

const { chromium } = require('playwright');
const path = require('path');

async function captureElements(url, selectors, outputDir = './screenshots') {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  await page.goto(url, { waitUntil: 'networkidle' });

  // Inject snapDOM
  await page.addScriptTag({ url: 'https://unpkg.com/@zumer/snapdom/dist/snapdom.umd.js' });

  for (const selector of selectors) {
    const fileName = selector.replace(/[^a-z0-9]/gi, '_').toLowerCase() + '.png';
    const outputPath = path.join(outputDir, fileName);

    await page.evaluate(async (sel, out) => {
      const element = document.querySelector(sel);
      if (element) {
        // snapdom is available globally from UMD
        await snapdom.download(element, out);
      }
    }, selector, fileName);
    
    console.log(`Captured ${selector} to ${fileName}`);
  }

  await browser.close();
}

// Example usage
// captureElements('https://example.com', ['.header', '.main-content', '.footer']);
