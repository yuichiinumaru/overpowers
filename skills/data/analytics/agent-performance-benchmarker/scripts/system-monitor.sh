#!/bin/bash
echo "Timestamp: $(date +%s)"
echo "CPU Usage: $(top -bn1 | grep \"Cpu(s)\" | awk '{print $2 + $4}')%"
echo "Memory Usage: $(free -m | awk 'NR==2{printf \"%.2f%%\", $3*100/$2 }')"
echo "Disk I/O: $(iostat -dx 1 1 | tail -n +4)"
