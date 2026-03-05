import sys
import requests
import json

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def get_stories(feed_type, limit=10):
    url = f"{BASE_URL}/{feed_type}stories.json"
    response = requests.get(url)
    ids = response.json()[:limit]
    
    for story_id in ids:
        item_url = f"{BASE_URL}/item/{story_id}.json"
        item = requests.get(item_url).json()
        print(f"{item.get('title')} - {item.get('url', 'N/A')} (ID: {story_id})")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        feed = sys.argv[1]
        n = 10
        if "-n" in sys.argv:
            n_idx = sys.argv.index("-n") + 1
            n = int(sys.argv[n_idx])
        get_stories(feed, n)
    else:
        print("Usage: python hn.py [top|new|best|ask|show|jobs] [-n limit]")
