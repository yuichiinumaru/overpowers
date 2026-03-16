import json
import argparse
import sys

def create_payload(action, **kwargs):
    payload = {"action": action}
    for key, value in kwargs.items():
        if value is not None:
            payload[key] = value
    return payload

def main():
    parser = argparse.ArgumentParser(description="Helper script to generate JSON payloads for feishu_doc tool.")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    # Read action
    read_parser = subparsers.add_parser("read", help="Read Document")
    read_parser.add_argument("--doc-token", required=True, help="Document Token")

    # Write action
    write_parser = subparsers.add_parser("write", help="Write Document (Replace All)")
    write_parser.add_argument("--doc-token", required=True, help="Document Token")
    write_parser.add_argument("--content", required=True, help="Markdown content")

    # Append action
    append_parser = subparsers.add_parser("append", help="Append Content")
    append_parser.add_argument("--doc-token", required=True, help="Document Token")
    append_parser.add_argument("--content", required=True, help="Markdown content")

    # Create action
    create_parser = subparsers.add_parser("create", help="Create Document")
    create_parser.add_argument("--title", required=True, help="Document Title")
    create_parser.add_argument("--folder-token", help="Folder Token (optional)")

    # List blocks action
    list_blocks_parser = subparsers.add_parser("list_blocks", help="List Blocks")
    list_blocks_parser.add_argument("--doc-token", required=True, help="Document Token")

    # Get single block action
    get_block_parser = subparsers.add_parser("get_block", help="Get Single Block")
    get_block_parser.add_argument("--doc-token", required=True, help="Document Token")
    get_block_parser.add_argument("--block-id", required=True, help="Block ID")

    # Update block text action
    update_block_parser = subparsers.add_parser("update_block", help="Update Block Text")
    update_block_parser.add_argument("--doc-token", required=True, help="Document Token")
    update_block_parser.add_argument("--block-id", required=True, help="Block ID")
    update_block_parser.add_argument("--content", required=True, help="New text content")

    # Delete block action
    delete_block_parser = subparsers.add_parser("delete_block", help="Delete Block")
    delete_block_parser.add_argument("--doc-token", required=True, help="Document Token")
    delete_block_parser.add_argument("--block-id", required=True, help="Block ID")

    args = parser.parse_args()

    if not args.action:
        parser.print_help()
        sys.exit(1)

    payload = {}
    if args.action == "read":
        payload = create_payload(args.action, doc_token=args.doc_token)
    elif args.action == "write":
        payload = create_payload(args.action, doc_token=args.doc_token, content=args.content)
    elif args.action == "append":
        payload = create_payload(args.action, doc_token=args.doc_token, content=args.content)
    elif args.action == "create":
        payload = create_payload(args.action, title=args.title, folder_token=args.folder_token)
    elif args.action == "list_blocks":
        payload = create_payload(args.action, doc_token=args.doc_token)
    elif args.action == "get_block":
        payload = create_payload(args.action, doc_token=args.doc_token, block_id=args.block_id)
    elif args.action == "update_block":
        payload = create_payload(args.action, doc_token=args.doc_token, block_id=args.block_id, content=args.content)
    elif args.action == "delete_block":
        payload = create_payload(args.action, doc_token=args.doc_token, block_id=args.block_id)

    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
