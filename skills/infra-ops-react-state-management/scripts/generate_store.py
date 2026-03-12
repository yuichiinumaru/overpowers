#!/usr/bin/env python3
import argparse
import sys

def generate_zustand_store(name):
    template = f"""import {{ create }} from 'zustand'

interface {name.capitalize()}State {{
  // Define state properties here
  value: string;
  setValue: (value: string) => void;
}}

export const use{name.capitalize()}Store = create<{name.capitalize()}State>((set) => ({{
  value: '',
  setValue: (value) => set({{ value }}),
}}))
"""
    print(f"Generated Zustand store '{name}':")
    print("-" * 40)
    print(template)
    print("-" * 40)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a simple Zustand store.")
    parser.add_argument("name", help="Name of the store (e.g. user, app)")
    args = parser.parse_args()
    generate_zustand_store(args.name)
