// Template with tooltips, zoom, and interactions
function createInteractiveChart(data, containerSelector, options = {}) {
  // Chart initialization
  const svg = d3.select(containerSelector).append("svg");

  // Tooltip
  const tooltip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("position", "absolute")
    .style("visibility", "hidden")
    .style("background-color", "white")
    .style("border", "1px solid #ddd")
    .style("padding", "10px");

  // Zoom
  const zoom = d3.zoom()
    .scaleExtent([0.5, 10])
    .on("zoom", (event) => {
      svg.select("g").attr("transform", event.transform);
    });

  svg.call(zoom);
}
