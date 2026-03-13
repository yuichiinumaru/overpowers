#!/usr/bin/env python3
import json
import sys

def generate_base_tokens():
    tokens = {
        "color": {
            "primitive": {
                "blue": {
                    "500": "#3b82f6",
                    "600": "#2563eb"
                },
                "gray": {
                    "900": "#111827",
                    "600": "#4b5563"
                }
            },
            "semantic": {
                "brand": {
                    "primary": "{color.primitive.blue.600}"
                },
                "text": {
                    "primary": "{color.primitive.gray.900}"
                }
            }
        },
        "spacing": {
            "base": "0.25rem",
            "1": "0.25rem",
            "2": "0.5rem",
            "4": "1rem"
        }
    }
    print(json.dumps(tokens, indent=2))

if __name__ == "__main__":
    generate_base_tokens()
