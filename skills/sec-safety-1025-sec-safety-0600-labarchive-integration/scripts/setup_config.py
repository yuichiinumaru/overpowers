#!/usr/bin/env python3
import sys
import yaml

def main():
    print("Setting up LabArchives configuration...")
    # Basic boilerplate
    config = {
        "api_url": "https://api.labarchives.com/api",
        "access_key_id": "YOUR_ACCESS_KEY_ID",
        "access_password": "YOUR_ACCESS_PASSWORD"
    }
    with open("config.yaml", "w") as f:
        yaml.dump(config, f)
    print("Created config.yaml template.")

if __name__ == "__main__":
    main()
