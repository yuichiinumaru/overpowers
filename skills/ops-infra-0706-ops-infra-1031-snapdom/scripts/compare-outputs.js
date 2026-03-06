#!/usr/bin/env node
const file1 = process.argv[2] || "output.svg";
const file2 = process.argv[3] || "output.png";
console.log(`[SnapDOM] Comparing SVG vs PNG quality for: ${file1} vs ${file2}`);
console.log(`Mock: SSIM Score = 0.98. The SVG preserves vector crispness.`);
