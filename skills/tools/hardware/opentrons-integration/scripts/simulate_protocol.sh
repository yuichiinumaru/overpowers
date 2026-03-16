#!/bin/bash
# Script to simulate an Opentrons protocol using the opentrons_simulate CLI

PROTOCOL_FILE=$1

if [ -z "$PROTOCOL_FILE" ]; then
    echo "Usage: $0 <protocol_file.py>"
    return 1 2>/dev/null || exit 1
fi

if ! command -v opentrons_simulate &> /dev/null; then
    echo "Error: opentrons_simulate command not found."
    echo "Please install the Opentrons Python package: pip install opentrons"
    return 1 2>/dev/null || exit 1
fi

echo "Simulating protocol: $PROTOCOL_FILE"
opentrons_simulate "$PROTOCOL_FILE"
