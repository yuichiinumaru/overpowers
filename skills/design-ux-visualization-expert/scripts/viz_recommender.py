#!/usr/bin/env python3
import sys

def recommend_viz(data_type, goal):
    print(f"--- Visualization Recommendation ---")
    print(f"Data Type: {data_type}")
    print(f"Goal: {goal}")
    print("-" * 20)

    if goal == "comparison":
        print("Recommended: Bar Chart or Column Chart")
        print("Rationale: Best for comparing discrete categories.")
    elif goal == "distribution":
        print("Recommended: Histogram or Box Plot")
        print("Rationale: Shows frequency and spread of data.")
    elif goal == "relationship":
        print("Recommended: Scatter Plot or Bubble Chart")
        print("Rationale: Visualizes correlation between variables.")
    elif goal == "composition":
        print("Recommended: Stacked Bar or Pie Chart (sparingly)")
        print("Rationale: Shows parts of a whole.")
    elif goal == "trend":
        print("Recommended: Line Chart or Area Chart")
        print("Rationale: Best for temporal data.")
    else:
        print("Unknown goal. Please specify: comparison, distribution, relationship, composition, or trend.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: viz_recommender.py <data_type> <goal>")
        sys.exit(1)
    
    recommend_viz(sys.argv[1], sys.argv[2])
