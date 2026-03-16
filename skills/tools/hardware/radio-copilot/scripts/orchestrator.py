import time
import json
import os
import sys

def run_orchestrator():
    """Predict satellite passes and log output."""
    print("Radio-Copilot Orchestrator started...")

    config_path = os.path.expanduser("~/.clawdbot/radio-copilot/config.json")
    if not os.path.exists(config_path):
        print(f"Warning: Configuration file not found at {config_path}. Using mock defaults.")
        config = {"latitude": 0, "longitude": 0, "satellites": ["NOAA 15", "ISS"]}
    else:
        try:
            with open(config_path, "r") as f:
                config = json.load(f)
        except Exception as e:
            print(f"Error reading config: {e}")
            config = {}

    print(f"Configuration loaded for {config.get('satellites', ['Unknown'])}...")
    time.sleep(1)

    # Mock output
    print("Passes calculated:")
    print("- NOAA 15: AOS 10:00 UTC (Az 30°, El 15°) -> LOS 10:15 UTC (Az 150°, El 10°)")
    print("- ISS: AOS 11:30 UTC (Az 270°, El 45°) -> LOS 11:40 UTC (Az 90°, El 20°)")

    print("Orchestrator finished. Sending alerts...")

if __name__ == "__main__":
    run_orchestrator()