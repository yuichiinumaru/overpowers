import json
import os

def get_tags():
    # Mocking tag retrieval logic as described in SKILL.md
    # In a real scenario, this would call the WeKnora API
    tags = [
        {"name": "tesla", "description": "Gateway, routing, and networking"},
        {"name": "Dayu", "description": "Microservice governance"},
        {"name": "miline", "description": "CI/CD, pipeline, and deployment"},
        {"name": "moon", "description": "Task scheduling and cron"},
        {"name": "常见问题", "description": "General questions and FAQs"}
    ]
    
    print(json.dumps({"tags": tags}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    get_tags()
