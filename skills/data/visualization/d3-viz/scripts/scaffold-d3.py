#!/usr/bin/env python3
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Scaffold a D3.js visualization project.")
    parser.add_argument("name", help="Name of the visualization")
    parser.add_argument("--type", choices=["bar", "line", "scatter", "pie"], default="bar", help="Type of chart to scaffold")
    args = parser.parse_args()

    project_name = args.name.lower().replace(" ", "-")
    os.makedirs(project_name, exist_ok=True)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{args.name}</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {{ font-family: sans-serif; }}
        .chart-container {{ width: 800px; height: 400px; margin: 20px auto; border: 1px solid #ddd; }}
        .bar {{ fill: steelblue; }}
        .bar:hover {{ fill: orange; }}
        .line {{ fill: none; stroke: steelblue; stroke-width: 2; }}
        .dot {{ fill: steelblue; stroke: #fff; }}
    </style>
</head>
<body>
    <h1>{args.name}</h1>
    <div id="chart" class="chart-container"></div>
    <script src="script.js"></script>
</body>
</html>
"""

    if args.type == "bar":
        script_content = """const data = [
    { category: 'A', value: 30 },
    { category: 'B', value: 80 },
    { category: 'C', value: 45 },
    { category: 'D', value: 60 },
    { category: 'E', value: 20 },
    { category: 'F', value: 90 },
    { category: 'G', value: 55 }
];

const drawBarChart = (data) => {
    const margin = { top: 20, right: 30, bottom: 40, left: 50 };
    const width = 800 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;

    const svg = d3.select('#chart')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

    const x = d3.scaleBand()
        .domain(data.map(d => d.category))
        .range([0, width])
        .padding(0.1);

    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.value)])
        .nice()
        .range([height, 0]);

    svg.append('g')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x));

    svg.append('g')
        .call(d3.axisLeft(y));

    svg.selectAll('.bar')
        .data(data)
        .join('rect')
        .attr('class', 'bar')
        .attr('x', d => x(d.category))
        .attr('y', d => y(d.value))
        .attr('width', x.bandwidth())
        .attr('height', d => height - y(d.value));
};

drawBarChart(data);
"""
    elif args.type == "line":
        script_content = """const data = [
    { x: 0, y: 30 },
    { x: 1, y: 80 },
    { x: 2, y: 45 },
    { x: 3, y: 60 },
    { x: 4, y: 20 },
    { x: 5, y: 90 },
    { x: 6, y: 55 }
];

const drawLineChart = (data) => {
    const margin = { top: 20, right: 30, bottom: 40, left: 50 };
    const width = 800 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;

    const svg = d3.select('#chart')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

    const x = d3.scaleLinear()
        .domain(d3.extent(data, d => d.x))
        .range([0, width]);

    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.y)])
        .nice()
        .range([height, 0]);

    const line = d3.line()
        .x(d => x(d.x))
        .y(d => y(d.y));

    svg.append('g')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x));

    svg.append('g')
        .call(d3.axisLeft(y));

    svg.append('path')
        .datum(data)
        .attr('class', 'line')
        .attr('d', line);
};

drawLineChart(data);
"""
    # ... more types can be added here ...
    else:
        script_content = "// Placeholder for " + args.type + " chart"

    with open(os.path.join(project_name, "index.html"), "w") as f:
        f.write(html_content)
    
    with open(os.path.join(project_name, "script.js"), "w") as f:
        f.write(script_content)

    print(f"Scaffolded {args.type} chart project in '{project_name}/'")

if __name__ == "__main__":
    main()
