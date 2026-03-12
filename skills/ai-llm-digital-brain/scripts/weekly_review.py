#!/usr/bin/env python3
"""
Generate a weekly review summary from Digital Brain logs.
"""
import os
import json
from datetime import datetime, timedelta

def load_jsonl(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as f:
        return [json.loads(line) for line in f]

def main():
    one_week_ago = (datetime.now() - timedelta(days=7)).isoformat()
    
    print(f"Weekly Review: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 40)

    # 1. Content Ideas
    ideas = load_jsonl("content/ideas.jsonl")
    recent_ideas = [i for i in ideas if i.get("timestamp", "") > one_week_ago]
    print(f"\nNew Ideas ({len(recent_ideas)}):")
    for idea in recent_ideas:
        print(f"- {idea.get('idea', 'Unnamed idea')}")

    # 2. Network Interactions
    interactions = load_jsonl("network/interactions.jsonl")
    recent_interactions = [i for i in interactions if i.get("timestamp", "") > one_week_ago]
    print(f"\nRecent Interactions ({len(recent_interactions)}):")
    for interaction in recent_interactions:
        print(f"- {interaction.get('contact', 'Someone')}: {interaction.get('summary', 'No summary')}")

    # 3. Published Posts
    posts = load_jsonl("content/posts.jsonl")
    recent_posts = [p for p in posts if p.get("timestamp", "") > one_week_ago]
    print(f"\nPublished Posts ({len(recent_posts)}):")
    for post in recent_posts:
        print(f"- {post.get('platform', 'Platform')}: {post.get('title', 'Post title')}")

    print("\nNext Steps:")
    print("1. Review metrics in operations/metrics.jsonl")
    print("2. Update goals in operations/goals.yaml")
    print("3. Plan next week in content/calendar.md")

if __name__ == "__main__":
    main()
