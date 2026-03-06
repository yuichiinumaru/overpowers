#!/bin/bash

# feishu_doc helper script
# Usage: ./feishu_helper.sh read ABC123def
#        ./feishu_helper.sh write ABC123def "content"

ACTION=$1
TOKEN=$2
CONTENT=$3

case "$ACTION" in
    read)
        # Assuming feishu_doc is a tool that can be called via a CLI or MCP wrapper
        mcporter call feishu.feishu_doc action=read doc_token="$TOKEN"
        ;;
    write|append)
        mcporter call feishu.feishu_doc action="$ACTION" doc_token="$TOKEN" content="$CONTENT"
        ;;
    create)
        mcporter call feishu.feishu_doc action=create title="$TOKEN"
        ;;
    *)
        echo "Usage: $0 {read|write|append|create} token [content]"
        exit 1
        ;;
esac
