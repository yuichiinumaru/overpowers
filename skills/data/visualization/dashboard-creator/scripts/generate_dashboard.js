#!/usr/bin/env node

/**
 * Dashboard Creator Script
 * Generates an HTML dashboard with KPI cards and an SVG chart.
 *
 * Usage:
 *   node generate_dashboard.js --name "Sales" --kpis '[{"label":"Revenue","val":"$100K","trend":"up"}]'
 */

const fs = require('fs');
const args = process.argv.slice(2);

let name = "Default";
let kpis = [];

for (let i = 0; i < args.length; i++) {
    if (args[i] === '--name' && i + 1 < args.length) {
        name = args[++i];
    }
    if (args[i] === '--kpis' && i + 1 < args.length) {
        try {
            kpis = JSON.parse(args[++i]);
        } catch (e) {
            console.error("Invalid JSON for --kpis", e.message);
            process.exit(1);
        }
    }
}

let kpiHtml = kpis.map(k => `
      <div class="kpi-card">
        <div class="kpi-label">${k.label}</div>
        <div class="kpi-value">${k.val}</div>
        <div class="trend-${k.trend}">${k.trend === 'up' ? '↑' : '↓'}</div>
      </div>
`).join('');

const html = `<!DOCTYPE html>
<html>
<head>
  <title>${name} Dashboard</title>
  <style>
    body { font-family: system-ui; background: #f7fafc; margin: 2rem; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem; }
    .kpi-card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .kpi-value { font-size: 36px; font-weight: bold; margin: 0.5rem 0; }
    .trend-up { color: #48bb78; }
    .trend-down { color: #e53e3e; }
    .chart { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
  </style>
</head>
<body>
  <h1>${name} Dashboard</h1>
  <div class="grid">
${kpiHtml}
  </div>
  <div class="chart">
    <h3>Overview Chart</h3>
    <svg viewBox="0 0 400 300" style="width:100%; max-width:600px; height:auto;">
      <rect x="50" y="100" width="40" height="150" fill="#4299e1"/>
      <rect x="120" y="80" width="40" height="170" fill="#48bb78"/>
      <rect x="190" y="140" width="40" height="110" fill="#ecc94b"/>
      <text x="70" y="270" text-anchor="middle" font-size="12">Jan</text>
      <text x="140" y="270" text-anchor="middle" font-size="12">Feb</text>
      <text x="210" y="270" text-anchor="middle" font-size="12">Mar</text>
    </svg>
  </div>
</body>
</html>`;

const filename = `${name.toLowerCase().replace(/[^a-z0-9]/g, '-')}-dashboard.html`;
fs.writeFileSync(filename, html);
console.log(`Generated ${filename}`);
