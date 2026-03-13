#!/usr/bin/env python3
import json
import sys

def generate_circuit_json():
    circuit = {
        "board": {
            "width": 1000,
            "height": 600,
            "gridSize": 20
        },
        "components": [
            {
                "type": "W65C02S",
                "x": 400,
                "y": 200,
                "rotation": 0,
                "properties": { "label": "CPU" }
            },
            {
                "type": "LED",
                "x": 100,
                "y": 100,
                "rotation": 0,
                "properties": { "color": "red" }
            }
        ],
        "wires": [
            {
                "start": { "x": 100, "y": 100 },
                "end": { "x": 400, "y": 200 },
                "color": "#ff0000"
            }
        ]
    }
    print(json.dumps(circuit, indent=2))

if __name__ == "__main__":
    generate_circuit_json()
