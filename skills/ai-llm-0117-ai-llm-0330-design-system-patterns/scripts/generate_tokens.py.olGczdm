#!/usr/bin/env python3
"""
Initialize a Design System token structure and Style Dictionary configuration.
"""
import os
import json
import sys

def main():
    base_dir = "tokens"
    os.makedirs(base_dir, exist_ok=True)
    os.makedirs(os.path.join(base_dir, "primitives"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "semantic"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "components"), exist_ok=True)

    # Primitive tokens example
    primitives = {
        "color": {
            "gray": {
                "50": { "value": "#fafafa" },
                "900": { "value": "#171717" }
            },
            "blue": {
                "500": { "value": "#3b82f6" }
            }
        }
    }
    with open(os.path.join(base_dir, "primitives", "colors.json"), 'w') as f:
        json.dump(primitives, f, indent=2)

    # Style Dictionary config
    config = {
        "source": ["tokens/**/*.json"],
        "platforms": {
            "css": {
                "transformGroup": "css",
                "buildPath": "dist/css/",
                "files": [{
                    "destination": "variables.css",
                    "format": "css/variables",
                    "options": { "outputReferences": True }
                }]
            }
        }
    }
    with open("style-dictionary.config.json", 'w') as f:
        json.dump(config, f, indent=2)

    print("Created token directory structure and style-dictionary.config.json")

if __name__ == "__main__":
    main()
