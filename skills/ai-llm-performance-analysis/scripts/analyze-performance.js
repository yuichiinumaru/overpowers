#!/usr/bin/env node
/**
 * Analyze performance using claude-flow analysis capabilities.
 * Wraps bottleneck detection and performance report generation.
 */

const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

function runCommand(cmd) {
  return new Promise((resolve, reject) => {
    exec(cmd, (error, stdout, stderr) => {
      if (error) {
        reject(error);
      } else {
        resolve(stdout);
      }
    });
  });
}

async function analyzePerformance() {
  const outputDir = path.join(process.cwd(), 'analysis');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  console.log('Running bottleneck detection...');
  let bottlenecks;
  try {
    bottlenecks = await runCommand('npx claude-flow bottleneck detect --format json');
  } catch (err) {
    console.warn('Failed to detect bottlenecks. Is claude-flow installed?', err.message);
    bottlenecks = "{}";
  }

  console.log('Generating performance report...');
  let report;
  try {
    report = await runCommand('npx claude-flow analysis performance-report --format json');
  } catch (err) {
    console.warn('Failed to generate performance report.', err.message);
    report = "{}";
  }

  const analysis = {
    bottlenecks: JSON.parse(bottlenecks),
    performance: JSON.parse(report),
    timestamp: new Date().toISOString()
  };

  const outputFile = path.join(outputDir, 'combined-report.json');
  fs.writeFileSync(outputFile, JSON.stringify(analysis, null, 2));
  console.log(`Analysis complete. Report saved to ${outputFile}`);

  if (analysis.bottlenecks?.critical?.length > 0) {
    console.error('\nCRITICAL: Performance bottlenecks detected!');
    process.exit(1);
  }
}

analyzePerformance().catch(err => {
  console.error('Performance analysis failed:', err);
  process.exit(1);
});
