#!/bin/bash
# Start a pair programming session
role=$1

if [ -z "$role" ]; then
    role="driver"
fi

echo "Starting pair programming session in role: $role"
echo "Initializing shared session... (simulated)"
echo "Ready."
