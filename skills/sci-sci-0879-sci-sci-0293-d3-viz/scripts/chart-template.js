// Starter template for basic chart
function createChart(data, containerSelector, options = {}) {
  const width = options.width || 800;
  const height = options.height || 600;
  const margin = options.margin || {top: 20, right: 20, bottom: 30, left: 40};

  const svg = d3.select(containerSelector)
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  // Add chart logic here
}
