#!/bin/bash

# eightctl helper script
# Usage: ./eight_helper.sh status
#        ./eight_helper.sh temp 20

case "$1" in
    status)
        eightctl status
        ;;
    on|off)
        eightctl "$1"
        ;;
    temp)
        eightctl temp "$2"
        ;;
    alarm)
        eightctl alarm "$2" "$3"
        ;;
    *)
        echo "Usage: $0 {status|on|off|temp|alarm} args..."
        exit 1
        ;;
esac
