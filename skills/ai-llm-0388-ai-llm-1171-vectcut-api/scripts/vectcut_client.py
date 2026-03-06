#!/usr/bin/env python3
"""
VectCutAPI Client Wrapper Script.
Provides a simple CLI interface to interact with VectCutAPI.
"""
import sys
import argparse

def create_draft(width=1080, height=1920):
    print(f"Mock: Creating draft project ({width}x{height})")
    print("Draft ID: draft_12345")
    return "draft_12345"

def add_video(draft_id, video_url):
    print(f"Mock: Adding video {video_url} to draft {draft_id}")

def save_draft(draft_id):
    print(f"Mock: Saving draft {draft_id}")
    print("Draft saved at: https://example.com/draft/12345")

def main():
    parser = argparse.ArgumentParser(description="VectCutAPI Helper")
    parser.add_argument("--create", action="store_true", help="Create a new draft")
    parser.add_argument("--add-video", metavar=('DRAFT_ID', 'URL'), nargs=2, help="Add video to draft")
    parser.add_argument("--save", metavar='DRAFT_ID', help="Save draft")

    args = parser.parse_args()

    if args.create:
        create_draft()
    elif args.add_video:
        add_video(args.add_video[0], args.add_video[1])
    elif args.save:
        save_draft(args.save)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
