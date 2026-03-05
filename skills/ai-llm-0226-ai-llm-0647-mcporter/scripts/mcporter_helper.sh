#!/bin/bash

# mcporter helper script
# Usage: ./mcporter_helper.sh list
#        ./mcporter_helper.sh call <server.tool> key=value

COMMAND=$1
shift

case $COMMAND in
    list)
        mcporter list "$@"
        ;;
    call)
        mcporter call "$@"
        ;;
    config)
        mcporter config "$@"
        ;;
    daemon)
        mcporter daemon "$@"
        ;;
    *)
        echo "Usage: $0 {list|call|config|daemon} [args]"
        exit 1
        ;;
esac
