#!/usr/bin/env python3
"""
Helper script to generate a basic ComfyUI workflow JSON for UniLumos Character Relighting.
"""
import json
import sys

def generate_workflow():
    workflow = {
        "1": {
            "inputs": {
                "image": "foreground.png"
            },
            "class_type": "LoadImage",
            "_meta": {
                "title": "Load Foreground Image"
            }
        },
        "2": {
            "inputs": {
                "image": "background.png"
            },
            "class_type": "LoadImage",
            "_meta": {
                "title": "Load Background Image"
            }
        },
        "3": {
            "inputs": {
                "foreground": ["1", 0],
                "background": ["2", 0],
                "strength": 0.8
            },
            "class_type": "UniLumosRelighting",
            "_meta": {
                "title": "UniLumos Relighting"
            }
        },
        "4": {
            "inputs": {
                "filename_prefix": "unilumos_output",
                "images": ["3", 0]
            },
            "class_type": "SaveImage",
            "_meta": {
                "title": "Save Image"
            }
        }
    }

    with open("unilumos_workflow.json", "w") as f:
        json.dump(workflow, f, indent=4)
    print("Generated unilumos_workflow.json")

if __name__ == "__main__":
    generate_workflow()
