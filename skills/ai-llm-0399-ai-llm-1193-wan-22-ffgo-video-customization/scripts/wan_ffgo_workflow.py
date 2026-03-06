#!/usr/bin/env python3
"""
Helper script to generate a basic ComfyUI workflow JSON for Wan 2.2 + FFGO LoRA
"""
import json
import sys

def generate_workflow():
    workflow = {
        "1": {
            "inputs": {"image": "subject1.png"},
            "class_type": "LoadImage",
            "_meta": {"title": "Load Subject 1"}
        },
        "2": {
            "inputs": {"image": "background.png"},
            "class_type": "LoadImage",
            "_meta": {"title": "Load Background"}
        },
        "3": {
            "inputs": {
                "images": ["1", 0, "2", 0],
                "stitch_mode": "horizontal"
            },
            "class_type": "ImageStitch",
            "_meta": {"title": "Stitch Images"}
        },
        "4": {
            "inputs": {
                "lora_name": "ffgo_v1.safetensors",
                "strength_model": 1.0,
                "strength_clip": 1.0
            },
            "class_type": "LoraLoader",
            "_meta": {"title": "Load FFGO LoRA"}
        },
        "5": {
            "inputs": {
                "model": ["4", 0],
                "image": ["3", 0],
                "prompt": "A subject moving in front of the background."
            },
            "class_type": "WanVideoSampler",
            "_meta": {"title": "Wan 2.2 Video Sampler"}
        },
        "6": {
            "inputs": {
                "video": ["5", 0],
                "start_frame": 4,
                "end_frame": -1
            },
            "class_type": "ImageFrameBatchTrim",
            "_meta": {"title": "Trim First 4 Frames (FFGO Post-Process)"}
        }
    }

    with open("wan_ffgo_workflow.json", "w") as f:
        json.dump(workflow, f, indent=4)
    print("Generated wan_ffgo_workflow.json")

if __name__ == "__main__":
    generate_workflow()
