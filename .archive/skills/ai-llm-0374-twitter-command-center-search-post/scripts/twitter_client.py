#!/usr/bin/env python3
# twitter_client.py

import argparse
import sys
import os
import json
import urllib.request
import urllib.error

def fetch(endpoint, method="GET", data=None):
    api_key = os.getenv("AISA_API_KEY")
    if not api_key:
        print("Error: AISA_API_KEY environment variable is missing.")
        sys.exit(1)

    url = f"https://api.aisa.one/apis/v1/twitter/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    req = urllib.request.Request(url, headers=headers, method=method)
    if data:
        req.data = json.dumps(data).encode("utf-8")

    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode("utf-8")
            res_data = json.loads(res_body)
            print(json.dumps(res_data, indent=2))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Twitter Command Center Client")
    subparsers = parser.add_subparsers(dest="command")

    # Read Operations
    info_parser = subparsers.add_parser("user-info", help="Get user info")
    info_parser.add_argument("--username", required=True)

    tweets_parser = subparsers.add_parser("tweets", help="Get user's latest tweets")
    tweets_parser.add_argument("--username", required=True)

    followers_parser = subparsers.add_parser("followers", help="Get user followers")
    followers_parser.add_argument("--username", required=True)

    followings_parser = subparsers.add_parser("followings", help="Get user followings")
    followings_parser.add_argument("--username", required=True)

    # Search & Discovery
    search_parser = subparsers.add_parser("search", help="Advanced tweet search")
    search_parser.add_argument("--query", required=True)
    search_parser.add_argument("--queryType", default="Latest", choices=["Latest", "Top"])

    user_search_parser = subparsers.add_parser("user-search", help="Search users by keyword")
    user_search_parser.add_argument("--keyword", required=True)

    trends_parser = subparsers.add_parser("trends", help="Get trending topics")
    trends_parser.add_argument("--woeid", type=int, default=1)

    # Write Operations
    login_parser = subparsers.add_parser("login", help="Login to account")
    login_parser.add_argument("--username", required=True)
    login_parser.add_argument("--email", required=True)
    login_parser.add_argument("--password", required=True)
    login_parser.add_argument("--proxy")

    post_parser = subparsers.add_parser("post", help="Send a tweet")
    post_parser.add_argument("--username", required=True)
    post_parser.add_argument("--text", required=True)

    like_parser = subparsers.add_parser("like", help="Like a tweet")
    like_parser.add_argument("--username", required=True)
    like_parser.add_argument("--tweet-id", required=True)

    retweet_parser = subparsers.add_parser("retweet", help="Retweet")
    retweet_parser.add_argument("--username", required=True)
    retweet_parser.add_argument("--tweet-id", required=True)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "user-info":
        fetch(f"user/info?userName={args.username}")
    elif args.command == "tweets":
        fetch(f"user/user_last_tweet?userName={args.username}")
    elif args.command == "followers":
        fetch(f"user/user_followers?userName={args.username}")
    elif args.command == "followings":
        fetch(f"user/user_followings?userName={args.username}")
    elif args.command == "search":
        encoded_query = urllib.parse.quote(args.query)
        fetch(f"tweet/advanced_search?query={encoded_query}&queryType={args.queryType}")
    elif args.command == "user-search":
        encoded_keyword = urllib.parse.quote(args.keyword)
        fetch(f"user/search_user?keyword={encoded_keyword}")
    elif args.command == "trends":
        fetch(f"trends?woeid={args.woeid}")
    elif args.command == "login":
        data = {
            "user_name": args.username,
            "email": args.email,
            "password": args.password
        }
        if args.proxy:
            data["proxy"] = args.proxy
        fetch("user_login_v3", method="POST", data=data)
    elif args.command == "post":
        data = {
            "user_name": args.username,
            "text": args.text
        }
        fetch("send_tweet_v3", method="POST", data=data)
    elif args.command == "like":
        data = {
            "user_name": args.username,
            "tweet_id": args.tweet_id
        }
        fetch("like_tweet_v3", method="POST", data=data)
    elif args.command == "retweet":
        data = {
            "user_name": args.username,
            "tweet_id": args.tweet_id
        }
        fetch("retweet_v3", method="POST", data=data)

if __name__ == "__main__":
    main()
