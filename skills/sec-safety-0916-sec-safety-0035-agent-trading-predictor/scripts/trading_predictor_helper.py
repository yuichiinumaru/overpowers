#!/usr/bin/env python3
import json
import argparse
import sys
import math

# Speed of light in fiber optic cable is roughly 200,000 km/s
SPEED_OF_LIGHT_FIBER_KM_S = 200000

def calculate_light_travel_payload(distance_km, matrix_size=1000):
    """Generate payload to calculate temporal advantage."""
    # Rough estimation for demonstration
    light_travel_ms = (distance_km / SPEED_OF_LIGHT_FIBER_KM_S) * 1000

    payload = {
        "distanceKm": distance_km,
        "matrixSize": matrix_size,
        "estimated_light_travel_ms": round(light_travel_ms, 3)
    }
    return json.dumps(payload, indent=2)

def predict_temporal_advantage_payload(distance_km, matrix_size=1000):
    """Generate payload for predictive execution."""
    payload = {
        "matrix": {
            "rows": matrix_size,
            "cols": matrix_size,
            "format": "dense"
        },
        "vector": {
            "size": matrix_size,
            "type": "market_signal"
        },
        "distanceKm": distance_km
    }
    return json.dumps(payload, indent=2)

def demonstrate_temporal_lead_payload(scenario_type):
    """Generate payload for demonstrating temporal lead."""
    valid_scenarios = {
        "satellite": 35786,  # GEO
        "transatlantic": 6000, # NY to London
        "transpacific": 10000, # NY to Tokyo
        "chicago_ny": 1145   # Chicago to NY
    }

    if scenario_type not in valid_scenarios:
        print(f"Error: Invalid scenario '{scenario_type}'. Must be one of {list(valid_scenarios.keys())}", file=sys.stderr)
        sys.exit(1)

    payload = {
        "scenario": scenario_type,
        "customDistance": valid_scenarios[scenario_type]
    }
    return json.dumps(payload, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trading Predictor Payload Generator")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Calculate travel
    calc_parser = subparsers.add_parser("calc-travel", help="Calculate light travel time payload")
    calc_parser.add_argument("--distance", required=True, type=float, help="Distance in km")
    calc_parser.add_argument("--size", type=int, default=1000, help="Matrix size for computation")

    # Predict advantage
    predict_parser = subparsers.add_parser("predict", help="Predict with temporal advantage payload")
    predict_parser.add_argument("--distance", required=True, type=float, help="Distance in km")
    predict_parser.add_argument("--size", type=int, default=1000, help="Matrix size for portfolio")

    # Demonstrate lead
    demo_parser = subparsers.add_parser("demo-lead", help="Demonstrate temporal lead payload")
    demo_parser.add_argument("--scenario", required=True,
                             choices=["satellite", "transatlantic", "transpacific", "chicago_ny"],
                             help="Trading scenario")

    args = parser.parse_args()

    if args.command == "calc-travel":
        print(calculate_light_travel_payload(args.distance, args.size))
    elif args.command == "predict":
        print(predict_temporal_advantage_payload(args.distance, args.size))
    elif args.command == "demo-lead":
        print(demonstrate_temporal_lead_payload(args.scenario))
    else:
        parser.print_help()
        sys.exit(1)
